# thespian  
**A Movie Database & Tracking Platform**

thespian is a full-stack movie database and tracking application that allows users to explore detailed information about movies, cast, and crew, backed by a robust relational database and served through a modern web stack.

The project focuses on **clean architecture, real-world data modeling, and production-style deployment**, rather than being a simple CRUD demo.

---

## Features

- **Extensive Movie Database**
  - Information on **9,000+ movies**
  - **63,000+ cast members**
  - **16,000+ crew members**
  - Data sourced from **TMDB (The Movie Database) API**

- **Rich Browsing Experience**
  - Explore movies with detailed metadata
  - View cast and crew credits
  - Clean, intuitive, and responsive UI

- **User Authentication**
  - Secure authentication handled by the backend
  - Personalized experience for logged-in users

- **Well-Structured Backend**
  - RESTful APIs for data access
  - Efficient database querying
  - Separation of concerns between services

- **Fully Dockerized**
  - Frontend, backend, and database run in isolated containers
  - Easy setup and reproducible environment

---

## Tech Stack

### Frontend
- **React**
- Modern component-based UI
- Clean and responsive design

### Backend
- **Flask (Python)**
- Authentication & authorization
- API layer connecting frontend and database
- Handles business logic and data retrieval

### Database
- **MariaDB**
- Relational schema designed for:
  - Movies
  - Genres
  - Cast 
  - Crew
  - Users
  - User Lists
  - Relationships between entities
- Populated using **TMDB API**

---

## Running the Project
- Install Docker as a prerequiste and then run:
```bash
git clone https://github.com/hardi-g/thespian.git
cd thespian
docker-compose up --build
```
- The project will be available at `http://127.0.0.1:3000`

---

## Project Goals
- Build a real-world, data-heavy application
- Practice backend-driven frontend architecture
- Design and query a large relational database
- Use Docker for production-like deployment
- Go beyond simple scripts or demos into a complete system

---

## Future Enhancements

- Advanced search and filtering
- User watchlists and ratings
- Performance optimizations and caching
- Pagination and lazy loading
- Recommendation features
