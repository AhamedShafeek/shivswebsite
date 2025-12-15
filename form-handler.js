// form-handler.js

import { db } from './firebase-config.js';
import { collection, addDoc } from 'https://www.gstatic.com/firebasejs/12.3.0/firebase-firestore.js';

document.addEventListener('DOMContentLoaded', () => {
    const inquiryForm = document.getElementById('inquiry-form');
    // Updated footer form id after refactor
    const footerForm = document.getElementById('footerContactForm');

    if (inquiryForm) {
        inquiryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = {
                name: inquiryForm.querySelector('input[name="name"]').value,
                eventType: inquiryForm.querySelector('select[name="eventType"]').value,
                place: inquiryForm.querySelector('input[name="place"]').value,
                date: inquiryForm.querySelector('input[name="date"]').value,
                phone: inquiryForm.querySelector('input[name="phone"]').value,
                botim: inquiryForm.querySelector('input[name="botim"]').value,
                details: inquiryForm.querySelector('input[name="details"]').value,
                timestamp: new Date()
            };

            try {
                const docRef = await addDoc(collection(db, "inquiries"), formData);
                console.log("Document written with ID: ", docRef.id);
                alert('Thank you for your inquiry! We will get back to you soon.');
                inquiryForm.reset();
            } catch (error) {
                console.error("Error adding document: ", error);
                alert('There was an error submitting your inquiry. Please try again.');
            }
        });
    }

    if (footerForm) {
        footerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            try {
                const formData = {
                    name: footerForm.querySelector('input[name="name"]').value || '',
                    eventType: footerForm.querySelector('select[name="eventType"]').value || '',
                    phone: footerForm.querySelector('input[name="phone"]').value || '',
                    message: footerForm.querySelector('textarea[name="message"]').value || '',
                    timestamp: new Date()
                };

                const docRef = await addDoc(collection(db, "footer_contacts"), formData);
                console.log("Footer contact saved with ID: ", docRef.id);
                alert('Thank you for your message! We will get back to you soon.');
                footerForm.reset();
            } catch (error) {
                console.error("Error adding footer contact: ", error);
                alert('There was an error submitting your message. Please try again.');
            }
        });
    }
});
