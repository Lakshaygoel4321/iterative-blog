import { Box, Typography, Paper } from '@mui/material';

export default function MessageStream({ messages }) {
  return (
    <Box>
      {messages.map((msg, index) => (
        <Paper key={index} sx={{ p: 2, my: 1, backgroundColor: '#f9f9f9' }}>
          <Typography variant="body2" fontWeight="bold">
            {msg.role.toUpperCase()}
          </Typography>
          <Typography variant="body1">{msg.content}</Typography>
        </Paper>
      ))}
    </Box>
  );
}
