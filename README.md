# 📝 Notes App

A full-stack Notes Management application built using **MERN Stack** (MongoDB, Express.js, React.js, Node.js) and Docker for containerization. This application allows users to create, read, update, and delete notes via a simple and interactive user interface.

---

## 🚀 Features

* 📄 Create, update, and delete notes
* 🧠 Real-time syncing with MongoDB
* 🔌 RESTful API backend using Node.js and Express.js
* 🎨 Clean and responsive UI built with React.js
* 🐳 Containerized using Docker for easy deployment

---

## 📁 Project Structure

```
.
├── backend/            # Node.js + Express backend
│   └── ...             # API Routes, Models, Controllers
├── frontend/           # React frontend
│   └── ...             # Components, Pages, Services
├── docker-compose.yaml # Docker configuration for all services
```

---

## ⚙️ Technologies Used

* **Frontend**: React.js, HTML, CSS
* **Backend**: Node.js, Express.js
* **Database**: MongoDB
* **Containerization**: Docker, Docker Compose

---

## 🛠️ Getting Started

### Prerequisites

Ensure you have the following installed:

* [Docker](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/AdithiNgatty/Notes.git
cd Notes
```

2. **Start all services using Docker Compose**

```bash
docker-compose up --build
```

3. **Access the App**

* Frontend: [http://localhost:8080](http://localhost:8080)
* Backend API: [http://localhost:8000](http://localhost:8000)
* MongoDB: runs internally at port 27017

---

## 🧪 API Endpoints

Sample API endpoints (assuming running locally on port `8000`):

| Method | Endpoint     | Description       |
| ------ | ------------ | ----------------- |
| GET    | `/notes`     | Get all notes     |
| POST   | `/notes`     | Create a new note |
| PUT    | `/notes/:id` | Update a note     |
| DELETE | `/notes/:id` | Delete a note     |

---

## 👨‍💼 Contributing

Pull requests are welcome! Please fork the repository and submit your PR. If you find any bugs or issues, feel free to open an issue.

---

## 📄 License

This project is licensed under the **MIT License**.

[View full LICENSE here](./license)

---

## 👩‍💼 Author

* **Adithi Gatty** – [GitHub Profile](https://github.com/AdithiNgatty)
