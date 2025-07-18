import Home from './pages/Home';
import { Container, Typography } from '@mui/material';

function App() {
  return (
    <Container maxWidth="md" sx={{ py: 5 }}>
      <Typography variant="h4" gutterBottom>
        🧠 Blog Post Generator (LangGraph + React)
      </Typography>
      <Home />
    </Container>
  );
}

export default App;
