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
git clone https://github.com/imhrdk/thespian.git
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

---

## Screenshots
<img width="1470" height="2885" alt="Screenshot 2025-12-26 at 18-48-16 Movie Tracker" src="https://github.com/user-attachments/assets/6bd7fb6b-a64f-4285-8071-18a166acb471" />
<img width="1486" height="2060" alt="Screenshot 2025-12-26 at 18-57-49 Movie Tracker" src="https://github.com/user-attachments/assets/137f0b4f-47d6-49a6-8cea-ebc3ada11927" />
<img width="1470" height="804" alt="Screenshot 2025-12-26 at 18-53-25 Movie Tracker" src="https://github.com/user-attachments/assets/d3d8c4b0-3ed1-40b4-af5a-d176af01f0f5" />
<img width="1470" height="804" alt="Screenshot 2025-12-26 at 18-52-43 Movie Tracker" src="https://github.com/user-attachments/assets/52b8e7b7-0c8b-4b88-aa46-83c489302124" />
<img width="1470" height="935" alt="Screenshot 2025-12-26 at 18-56-44 Movie Tracker" src="https://github.com/user-attachments/assets/020bedbc-3790-4f96-a329-f65161116763" />
