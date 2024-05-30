<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Manager</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Contact Manager</h1>
    </header>
    <main>
        <section id="add-contact">
            <h2>Add New Contact</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Add Contact</button>
            </form>
        </section>
        <section id="contact-list">
            <h2>Contact List</h2>
            <ul id="contacts"></ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Contact Manager. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
