// firebase-config.js

// Firebase configuration and initialization
// Make sure to use the same version across all your Firebase imports
import { initializeApp } from 'https://www.gstatic.com/firebasejs/12.3.0/firebase-app.js';
import { getFirestore } from 'https://www.gstatic.com/firebasejs/12.3.0/firebase-firestore.js';
import { getAuth } from 'https://www.gstatic.com/firebasejs/12.3.0/firebase-auth.js';

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyCiXgKBN6wWm9d7QMf3vV5TkmMtZVzMBaI',
  authDomain: 'shivsform-2c155.firebaseapp.com',
  projectId: 'shivsform-2c155',
  storageBucket: 'shivsform-2c155.appspot.com',
  messagingSenderId: '502438164025',
  appId: '1:502438164025:web:cc7ce06af86c989bbf7fe8'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

// Export the instances you need in other files
export { app, db, auth };
