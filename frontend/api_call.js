const axios = require('axios');

async function placeBet(betAmount) {
    try {
        const response = await axios.post('http://localhost:5000/place-bet', {
            bet_amount: betAmount
        });
        console.log('Bet placed successfully:', response.data);
    } catch (error) {
        console.error('Failed to place bet:', error);
    }
}

placeBet(100);