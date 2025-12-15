import { db } from './firebase-config.js';
import { collection, addDoc, serverTimestamp } from 'https://www.gstatic.com/firebasejs/12.3.0/firebase-firestore.js';

function notify(btn, message, isError=false){
  if(!btn) return;
  const original = btn.textContent;
  btn.textContent = message;
  btn.disabled = true;
  btn.style.opacity = '0.6';
  setTimeout(()=>{ btn.textContent = original; btn.disabled=false; btn.style.opacity='1'; }, 2600);
  if(isError){ btn.style.borderColor = '#c00'; setTimeout(()=> btn.style.borderColor = 'black', 2600); }
}

// Inquiry Form (custom sentence style form)
const inquiryForm = document.getElementById('inquiryForm');
if(inquiryForm){
  inquiryForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('inq_submit');
    const data = {
      name: document.getElementById('inq_name')?.value.trim() || '',
      eventType: document.getElementById('inq_eventType')?.value || '',
      place: document.getElementById('inq_place')?.value.trim() || '',
      eventDate: document.getElementById('inq_date')?.value || '',
      phone: document.getElementById('inq_phone')?.value.trim() || '',
      botim: document.getElementById('inq_botim')?.value.trim() || '',
      details: document.getElementById('inq_details')?.value.trim() || '',
      createdAt: serverTimestamp(),
      source: 'heroInquiry'
    };
    if(!data.name || !data.phone){
      notify(submitBtn, 'Name & Phone needed', true);
      return;
    }
    try {
      await addDoc(collection(db, 'inquiries'), data);
      inquiryForm.reset();
      notify(submitBtn, 'Submitted ✅');
    } catch(err){
      console.error(err);
      notify(submitBtn, 'Error ❌', true);
    }
  });
}

// Footer Contact Form
const footerForm = document.getElementById('footerContactForm');
if(footerForm){
  footerForm.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const btn = footerForm.querySelector('button[type="submit"]');
    const formData = new FormData(footerForm);
    const payload = {
      name: formData.get('name')?.toString().trim() || '',
      email: formData.get('email')?.toString().trim() || '',
      phone: formData.get('phone')?.toString().trim() || '',
      message: formData.get('message')?.toString().trim() || '',
      createdAt: serverTimestamp(),
      source: 'footerContact'
    };
    if(!payload.name || !payload.email){
      notify(btn, 'Name & Email needed', true);
      return;
    }
    try {
      await addDoc(collection(db, 'contacts'), payload);
      footerForm.reset();
      notify(btn, 'Sent ✅');
    } catch(err){
      console.error(err);
      notify(btn, 'Error ❌', true);
    }
  });
}
