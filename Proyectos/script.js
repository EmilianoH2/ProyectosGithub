document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const contactsList = document.getElementById('contacts');
    let contacts = [];

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const name = event.target.name.value;
        const email = event.target.email.value;

        const contact = { id: Date.now(), name, email };
        contacts.push(contact);
        event.target.reset();
        renderContacts();
    });

    function renderContacts() {
        contactsList.innerHTML = '';
        contacts.forEach((contact) => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${contact.name} - ${contact.email}
                <button onclick="deleteContact(${contact.id})">Delete</button>
            `;
            contactsList.appendChild(li);
        });
    }

    window.deleteContact = function(id) {
        contacts = contacts.filter(contact => contact.id !== id);
        renderContacts();
    };
});
