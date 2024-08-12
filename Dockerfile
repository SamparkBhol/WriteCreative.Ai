version: '3'
services:
  backend:
    build:
      context: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend/src:/app/src
    environment:
      - FLASK_ENV=development

  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
