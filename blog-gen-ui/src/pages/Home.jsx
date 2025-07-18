import { useState } from 'react';
import TopicInput from '../components/TopicInput';
import MessageStream from '../components/MessageStream';
import FeedbackForm from '../components/FeedbackForm';

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [showFeedback, setShowFeedback] = useState(false);

  const handleStart = async (topic) => {
    setMessages([{ role: 'user', content: topic }]);
    const eventSource = new EventSource(`http://localhost:8000/stream?topic=${encodeURIComponent(topic)}`);

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);

      if (data.role === 'system' && data.content === 'awaiting_feedback') {
        setShowFeedback(true);
      }

      if (data.role === 'system' && data.content === 'done') {
        eventSource.close();
        setShowFeedback(false);
      }
    };
  };

  const handleFeedback = async (feedback) => {
    await fetch('http://localhost:8000/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ feedback }),
    });
  };

  return (
    <div>
      <TopicInput onSubmit={handleStart} />
      <MessageStream messages={messages} />
      {showFeedback && <FeedbackForm onFeedback={handleFeedback} />}
    </div>
  );
}
