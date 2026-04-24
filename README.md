# 🔗 Pixel Link Generator (Dockerized FastAPI)

A production-ready, containerized web application built with **FastAPI** and **Docker**. This project demonstrates a complete **CI/CD** pipeline from local development to cloud deployment using a "Triple Threat" workflow: GitHub → Docker Hub → Render.

**Live Link:** [https://pixel-link-generator.onrender.com/](https://pixel-link-generator.onrender.com/)

## 🐳 Docker Architecture & DevOps Workflow
This project was built with a "Container-First" mindset. By using Docker, we ensure that the application runs identically in development, testing, and production environments.

### ⚙️ Container Configuration (`Dockerfile`)
The project utilizes a `python:3.11-slim` base image to keep the footprint small and secure. Key features include:
* **Layer Optimization**: Dependency installation is separated from source code copying to leverage Docker's layer caching.
* **Dynamic Port Injection**: Uses a shell-form `CMD` to allow cloud providers (like Render) to inject dynamic `${PORT}` variables at runtime.
* **Production Tuning**: Uvicorn is configured with `--proxy-headers` and `--forwarded-allow-ips` to properly handle traffic behind cloud load balancers.

### 🚢 Deployment Pipeline
1. **GitHub**: Source code management and automatic trigger for Render builds.
2. **Docker Hub**: Container registry for image versioning and storage.
3. **Render**: Automatically pulls the Docker configuration and deploys the containerized service on a Free Tier instance.

## 🛠️ Tech Stack
* **Backend Framework**: FastAPI (Python)
* **Templating**: Jinja2 Templates
* **Styling**: CSS3 (Pixel-Art / Dark Academia Theme)
* **Containerization**: Docker
* **ASGI Server**: Uvicorn

## 🚦 Getting Started 

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

### Local Development
To spin up the project locally without needing a local Python environment:

1. **Build the image:**
   ```bash
   docker build -t link-generator:v1 .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name link-gen-app link-generator:v1
   ```
   Access the app at: `http://localhost:8000`

### Pushing to Docker Hub
To save this version to your public registry:
```bash
docker tag link-generator:v1 your-docker-username/link-generator:v1
docker push your-docker-username/link-generator:v1
```

---

## 📂 Project Structure
```text
.
├── Dockerfile           # Container build instructions
├── requirements.txt     # Python dependencies
├── main.py              # FastAPI application logic
├── static/              # CSS and aesthetic assets
└── templates/           # Jinja2 HTML templates
```

## 🚀 What's Next?
The project is currently a **Link Generator**, but the goal is to evolve it into a **Personal Identity Hub**.

*   **Custom Landing Page**: Move from a "one-by-one" generator to a full-page dashboard showing all social links at once.
*   **Data-Driven**: Store links in a JSON file so the entire site updates instantly without changing the HTML.
*   **Portable Deployment**: Keep the entire app within a single Docker image for 1-click hosting.
