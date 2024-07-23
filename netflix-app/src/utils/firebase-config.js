// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyBJ9ux3LFdJCuIhucQG7vxRbTFmRr-pAXY",
  authDomain: "react-netflix-clone-18255.firebaseapp.com",
  projectId: "react-netflix-clone-18255",
  storageBucket: "react-netflix-clone-18255.appspot.com",
  messagingSenderId: "513900022495",
  appId: "1:513900022495:web:c77f0e4672de332cbbf76a",
  measurementId: "G-3107WQ45Z9"
};

const app = initializeApp(firebaseConfig);

export const firebaseAuth = getAuth(app)