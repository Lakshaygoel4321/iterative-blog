import { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

export default function FeedbackForm({ onFeedback }) {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = () => {
    if (feedback.trim()) {
      onFeedback(feedback);
      setFeedback('');
    }
  };

  return (
    <Box sx={{ display: 'flex', gap: 2, mt: 3 }}>
      <TextField
        fullWidth
        label="Enter feedback or type 'done'"
        variant="outlined"
        value={feedback}
        onChange={(e) => setFeedback(e.target.value)}
      />
      <Button variant="contained" onClick={handleSubmit}>
        Send
      </Button>
    </Box>
  );
}
