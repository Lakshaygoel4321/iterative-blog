import { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

export default function TopicInput({ onSubmit }) {
  const [topic, setTopic] = useState('');

  const handleSubmit = () => {
    if (topic.trim()) {
      onSubmit(topic);
      setTopic('');
    }
  };

  return (
    <Box sx={{ display: 'flex', gap: 2, mb: 4 }}>
      <TextField
        fullWidth
        label="Enter blog topic"
        variant="outlined"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <Button variant="contained" onClick={handleSubmit}>
        Generate
      </Button>
    </Box>
  );
}
