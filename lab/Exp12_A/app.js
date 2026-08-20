const express = require('express');
const app = express();
const PORT = 3000;
app.use(express.json());

// ============================================================
// PART A (basic route, keep if you already had this)
// ============================================================
app.get('/', (req, res) => {
    res.send('Welcome to the Node.js and Express Lab!');
});

// ============================================================
// PART B - Step 8: URL Parameters (Route Parameters)
// ============================================================

app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    res.json({
        message: 'User details',
        userId: userId
    });
});

// Multiple URL parameters: /product/electronics/101
app.get('/product/:category/:id', (req, res) => {
    const { category, id } = req.params;
    res.json({
        category: category,
        productId: id
    });
});

// ============================================================
// PART B - POST data example (query params + body)
// ============================================================

// Query parameters: /search?q=laptop&limit=5
app.get('/search', (req, res) => {
    const { q, limit } = req.query;
    res.json({
        query: q,
        limit: limit
    });
});

// POST route reading JSON body
app.post('/user', (req, res) => {
    const { name, email } = req.body;
    res.json({
        message: 'User created',
        name: name,
        email: email
    });
});

// ============================================================
// Start server
// ============================================================
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
