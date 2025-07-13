// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth} from "firebase/auth";
import { getDatabase } from "firebase/database";
const firebaseConfig = {
  apiKey: "AIzaSyC7lXGwEcdXBKSzLw3qNrJnJH7uvmEGhyM",
  authDomain: "water-prediction.firebaseapp.com",
  projectId: "water-prediction",
  storageBucket: "water-prediction.firebasestorage.app",
  messagingSenderId: "472172566420",
  appId: "1:472172566420:web:d07e20c5db98538383e181",
  measurementId: "G-03EQXK84XY",
  databaseURL: "https://water-prediction-default-rtdb.asia-southeast1.firebasedatabase.app"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getDatabase(app);

export { app, auth, db };