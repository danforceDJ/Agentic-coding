import express, { Application } from 'express';
import healthRouter from './routes/health';

const app: Application = express();

app.use(express.json());

// Routes
app.use('/health', healthRouter);

// TODO: Register task routes here (added by @backend-engineer in Module 7)

export default app;
