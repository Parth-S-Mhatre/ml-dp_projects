import React from "react";
import WaterQualityDashboard from "./WaterQualityDashboard";
import { Routes, Route } from 'react-router-dom';
import Header from './Authcontext/Header';
import Login from './Authcontext/login';
import Register from './Authcontext/Register';
import './water_quality_styles.css';
//import './App.css'

import {
  BarChart3, Shield, Users, MapPin, TrendingUp,
  Droplet, CheckCircle, ArrowRight, Waves
} from 'lucide-react';

import LandingPage from './Landingpage';
import ProtectedRoute from './ProtectedRoute';

function App() {
  return (
    <>
      <Header />
      {/* add paddingTop to prevent overlap with fixed header */}
      <div style={{ paddingTop: '56px' }}>
        <div className="content-wrapper">
  <Routes>...</Routes>


        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/home"
            element={
              <ProtectedRoute>
                <WaterQualityDashboard />
              </ProtectedRoute>
            }
          />
        </Routes>
        </div>
      </div>
    </>
  );
}

export default App;
