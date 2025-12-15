// form.js

import { db } from './firebase-config.js';
import { collection, addDoc } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

const inquiryForm = document.getElementById('inquiry-form');

inquiryForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = inquiryForm.name.value;
    const eventType = inquiryForm.eventType.value;
    const place = inquiryForm.place.value;
    const date = inquiryForm.date.value;
    const phone = inquiryForm.phone.value;
    const botim = inquiryForm.botim.value;
    const details = inquiryForm.details.value;

    addDoc(collection(db, "inquiries"), {
        name: name,
        eventType: eventType,
        place: place,
        date: date,
        phone: phone,
        botim: botim,
        details: details
    })
    .then(() => {
        alert("Your inquiry has been submitted!");
        inquiryForm.reset();
    })
    .catch((error) => {
        console.error("Error adding document: ", error);
        alert("There was an error submitting your inquiry. Please try again.");
    });
});