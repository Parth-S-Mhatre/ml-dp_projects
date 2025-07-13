import React, { useState } from "react";
import {
  Container,
  Typography,
  Card,
  CardContent,
  Grid,
  TextField,
  Button,
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Alert,
  Divider
} from "@mui/material";
import OpacityIcon from '@mui/icons-material/Opacity';
import WaterDropIcon from '@mui/icons-material/WaterDrop';
import WavesIcon from '@mui/icons-material/Waves';
import { db } from "./firebase/firebase";
import { ref, push, set, onValue, remove, query, orderByChild } from "firebase/database";
import { useAuth } from "./Authcontext";
import { useEffect } from "react";

const initialState = {
  ph: "",
  Hardness: "",
  Solids: "",
  Chloramines: "",
  Sulfate: "",
  Conductivity: "",
  Organic_carbon: "",
  Trihalomethanes: "",
  Turbidity: "",
};

// Simple SVG wave animation component
function WaveAnimation() {
  return (
    <div style={{ width: '100%', overflow: 'hidden', lineHeight: 0, marginBottom: -8 }}>
      <svg viewBox="0 0 1200 120" preserveAspectRatio="none" style={{ width: '100%', height: 60, display: 'block' }}>
        <path d="M0,0 C300,100 900,0 1200,100 L1200,120 L0,120 Z" fill="#2196f3" fillOpacity="0.2">
          <animate attributeName="d" dur="6s" repeatCount="indefinite"
            values="M0,0 C300,100 900,0 1200,100 L1200,120 L0,120 Z;M0,0 C400,0 800,100 1200,0 L1200,120 L0,120 Z;M0,0 C300,100 900,0 1200,100 L1200,120 L0,120 Z" />
        </path>
      </svg>
    </div>
  );
}

// Function to save experiment history to Firebase Realtime Database for a user
async function saveExperimentHistoryToFirebase(userId, historyData) {
  if (!userId) return;
  try {
    const historyRef = ref(db, `experimentHistory/${userId}`);
    await push(historyRef, {
      ...historyData,
      timestamp: Date.now(),
    });
  } catch (err) {
    console.error("Failed to save experiment history to Firebase:", err);
  }
}

// Function to delete history older than a week for a user
async function deleteOldHistory(userId) {
  if (!userId) return;
  const oneWeekAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;
  const historyRef = ref(db, `experimentHistory/${userId}`);
  const q = query(historyRef, orderByChild("timestamp"));
  onValue(q, (snapshot) => {
    snapshot.forEach((child) => {
      const data = child.val();
      if (data.timestamp < oneWeekAgo) {
        remove(ref(db, `experimentHistory/${userId}/${child.key}`));
      }
    });
  }, { onlyOnce: true });
}

export default function WaterQualityDashboard() {
  const [form, setForm] = useState(initialState);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [history, setHistory] = useState([]); // For prediction history
  const { currentUser } = useAuth();

  // Fetch user history and delete old entries on mount and when user changes
  useEffect(() => {
    if (!currentUser) return;
    const userId = currentUser.uid;
    const historyRef = ref(db, `experimentHistory/${userId}`);
    const q = query(historyRef, orderByChild("timestamp"));
    const unsubscribe = onValue(q, (snapshot) => {
      const all = [];
      snapshot.forEach((child) => {
        const data = child.val();
        all.push(data);
      });
      // Sort by timestamp descending, filter out old entries
      const oneWeekAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;
      const recent = all.filter((item) => item.timestamp >= oneWeekAgo)
                        .sort((a, b) => b.timestamp - a.timestamp)
                        .slice(0, 5);
      setHistory(recent);
    });
    // Delete old entries
    deleteOldHistory(userId);
    return () => unsubscribe();
  }, [currentUser]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    // Convert all values to float
    const payload = {};
    for (let key in form) {
      payload[key] = parseFloat(form[key]);
    }

    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error("API error");
      const data = await response.json();
      const predResult = data.potability === 1 ? "Potable" : "Not Potable";
      setResult(predResult);
      // Save to Firebase under user
      if (currentUser) {
        await saveExperimentHistoryToFirebase(currentUser.uid, { ...form, result: predResult });
        // History will auto-update from onValue
      }
    } catch (err) {
      setError("Failed to get prediction. Please check your input and backend.");
    } finally {
      setLoading(false);
    }
  };

  // Water theme background
  const backgroundStyle = {
    minHeight: '100vh',
    background: 'linear-gradient(135deg, #e3f2fd 0%, #90caf9 100%)',
    padding: 0,
    margin: 0,
    position: 'relative',
    overflowX: 'hidden',
  };

  return (
    <div style={backgroundStyle}>
      <WaveAnimation />
      <Container maxWidth="md" sx={{ mt: 6, mb: 6 }}>
        {/* Dashboard Header */}
        <Box display="flex" alignItems="center" justifyContent="center" mb={2}>
          <WavesIcon sx={{ fontSize: 48, color: '#1976d2', mr: 1 }} />
          <Typography variant="h3" align="center" fontWeight={700} color="#1976d2">
            Water Quality Dashboard
          </Typography>
        </Box>
        <Grid container spacing={3} sx={{ mb: 4 }}>
          <Grid item xs={12} md={6}>
            <Card elevation={6} sx={{ borderRadius: 4, background: 'rgba(255,255,255,0.85)' }}>
              <CardContent>
                <Typography variant="h6" gutterBottom color="#1976d2">
                  <OpacityIcon sx={{ verticalAlign: 'middle', mr: 1 }} /> Instructions
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Enter the water sample features below and click <b>Predict</b> to check if the water is potable. The last 5 predictions will be shown in the dashboard below.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <Card elevation={6} sx={{ borderRadius: 4, background: 'rgba(255,255,255,0.85)' }}>
              <CardContent>
                <Typography variant="h6" gutterBottom color="#1976d2">
                  <WaterDropIcon sx={{ verticalAlign: 'middle', mr: 1 }} /> Model Info
                </Typography>
                <Typography variant="body2" color="text.secondary">
                 <b>Train Accuracy:</b> 100%<br />
                  <b>Test Accuracy:</b> 86%<br />
                  <b>F1-Score (Potable Class):</b> 0.81<br />
                  <b>Baseline Accuracy:</b> ~62% (predicting majority class)<br />
                  <b>Real-World Insight:</b> F1-score of 0.81 indicates strong balance between precision and recall, important for water safety assessments.<br />
                  <b>Features Used:</b> 9 water quality parameters — pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity

                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>

        {/* Animated Graph Placeholders */}
        <Grid container spacing={3} sx={{ mb: 4 }}>
          <Grid item xs={12} md={6}>
            <Card elevation={4} sx={{ borderRadius: 4, background: 'rgba(33,150,243,0.08)' }}>
              <CardContent>
                <Typography variant="subtitle1" color="#1976d2" gutterBottom>
                  Potability Pie Chart (Coming Soon)
                </Typography>
                <Box height={180} display="flex" alignItems="center" justifyContent="center">
                  {/* Pie chart will go here */}
                  <WavesIcon sx={{ fontSize: 60, color: '#90caf9', opacity: 0.5, animation: 'waveMove 2s infinite linear alternate' }} />
                </Box>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <Card elevation={4} sx={{ borderRadius: 4, background: 'rgba(33,150,243,0.08)' }}>
              <CardContent>
                <Typography variant="subtitle1" color="#1976d2" gutterBottom>
                  Prediction Trend (Coming Soon)
                </Typography>
                <Box height={180} display="flex" alignItems="center" justifyContent="center">
                  {/* Line chart will go here */}
                  <OpacityIcon sx={{ fontSize: 60, color: '#90caf9', opacity: 0.5, animation: 'floatDrop 2s infinite ease-in-out alternate' }} />
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>

        {/* Prediction Form */}
        <Card elevation={8} sx={{ mb: 4, borderRadius: 4, background: 'rgba(255,255,255,0.95)' }}>
          <CardContent>
            <Typography variant="h5" gutterBottom color="#1976d2">
              Enter Water Sample Features
            </Typography>
            <Divider sx={{ mb: 2 }} />
            <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
              <Grid container spacing={2}>
                {Object.keys(initialState).map((key) => {
                  // Set min/max for each parameter
                  let min = 0, max = 100000;
                  if (key === 'ph') { min = 0; max = 14; }
                  else if (key === 'Hardness') { min = 0; max = 500; }
                  else if (key === 'Solids') { min = 0; max = 50000; }
                  else if (key === 'Chloramines') { min = 0; max = 10; }
                  else if (key === 'Sulfate') { min = 0; max = 1000; }
                  else if (key === 'Conductivity') { min = 0; max = 1000; }
                  else if (key === 'Organic_carbon') { min = 0; max = 30; }
                  else if (key === 'Trihalomethanes') { min = 0; max = 200; }
                  else if (key === 'Turbidity') { min = 0; max = 10; }
                  return (
                    <Grid item xs={12} sm={6} md={4} key={key}>
                      <TextField
                        label={key.replace(/_/g, " ")}
                        name={key}
                        value={form[key]}
                        onChange={handleChange}
                        type="number"
                        step="any"
                        required
                        fullWidth
                        variant="outlined"
                        InputProps={{
                          style: { background: '#e3f2fd', borderRadius: 8 },
                          inputProps: { min, max }
                        }}
                      />
                    </Grid>
                  );
                })}
              </Grid>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                size="large"
                sx={{ mt: 3, width: "100%", borderRadius: 2, fontWeight: 600, fontSize: 18, boxShadow: 3, background: 'linear-gradient(90deg, #1976d2 60%, #64b5f6 100%)' }}
                disabled={loading}
              >
                {loading ? "Predicting..." : "Predict"}
              </Button>
            </Box>
            {result && (
              <Alert severity={result === "Potable" ? "success" : "warning"} sx={{ mt: 3, fontSize: 18, borderRadius: 2 }}>
                Result: <b>{result}</b>
              </Alert>
            )}
            {error && (
              <Alert severity="error" sx={{ mt: 3, borderRadius: 2 }}>
                {error}
              </Alert>
            )}
          </CardContent>
        </Card>

        {/* Prediction History Table */}
        <Card elevation={2} sx={{ borderRadius: 4, background: 'rgba(255,255,255,0.92)' }}>
          <CardContent>
            <Typography variant="h6" gutterBottom color="#1976d2">
              Last 5 Predictions
            </Typography>
            {history.length === 0 ? (
              <Typography color="text.secondary">No predictions yet.</Typography>
            ) : (
              <TableContainer component={Paper} sx={{ borderRadius: 2 }}>
                <Table size="small">
                  <TableHead>
                    <TableRow>
                      {Object.keys(initialState).map((key) => (
                        <TableCell key={key}>{key.replace(/_/g, " ")}</TableCell>
                      ))}
                      <TableCell>Result</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {history.map((row, idx) => (
                      <TableRow key={idx}>
                        {Object.keys(initialState).map((key) => (
                          <TableCell key={key}>{row[key]}</TableCell>
                        ))}
                        <TableCell style={{ color: row.result === "Potable" ? "#1976d2" : "#e53935", fontWeight: 600 }}>{row.result}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            )}
          </CardContent>
        </Card>
      </Container>
      {/* Water theme keyframes */}
      <style>{`
        @keyframes waveMove {
          0% { transform: translateX(0); }
          100% { transform: translateX(20px); }
        }
        @keyframes floatDrop {
          0% { transform: translateY(0); }
          100% { transform: translateY(12px); }
        }
      `}</style>
    </div>
  );
}
