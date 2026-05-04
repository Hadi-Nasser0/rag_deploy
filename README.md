# GenAI-rag-assistant

## Description
The application provides a GenAI based on Retrieval‑Augmented Generation (RAG) service. It
exposes an API that accepts a user query, retrieves relevant documents from a
vector store, and generates a response using a large language model. The
architecture consists of three main components:

1. **Ingestion pipeline** – loads raw text data, splits it into chunks and
   creates embeddings that are stored in a vector database.
2. **Retrieval layer** – performs similarity search against the vector store to
   fetch the most relevant document chunks for a given query.
3. **Generation layer** – feeds the retrieved context to a language model (e.g.
   OpenAI's GPT) to produce a coherent answer.

The project is containerised with Docker and orchestrated via Docker Compose.
Key technologies used include:

* Python 3.11
* FastAPI for the HTTP API
* LangChain for RAG utilities
* FAISS as the in‑memory vector store (can be swapped for Pinecone, etc.)
* OpenAI API for LLM inference
* Pytest for testing

This README template now includes a concise description of the app, its
architecture, and the technologies employed.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.

## Usage
Run the main application with: `python -m src.main` (replace with actual entry point).

## Configuration
Set required environment variables or edit the config file as needed.

## Testing
Execute the test suite: `pytest`.

## Contributing
Please follow the code style guidelines and submit pull requests for improvements.

## License
Specify the license under which the project is released.

## Contact
Provide contact information or links for support.

## Deployment
The application can be deployed to an AWS EC2 instance. A typical deployment
workflow is:

1. **Provision an EC2 instance** – choose an Amazon Linux 2 or Ubuntu AMI,
   allocate sufficient CPU/RAM for the LLM inference, and open the required
   ports (e.g., 80/443 for HTTP/HTTPS and 22 for SSH).
2. **Install Docker** – follow the official Docker installation guide for the
   chosen OS, then add your user to the `docker` group so Docker commands can be
   run without `sudo`.
3. **Clone the repository** on the instance and navigate to the `rag_deploy`
   directory.
4. **Set environment variables** – create a `.env` file (or use the EC2
   parameter store/Secrets Manager) with keys such as `OPENAI_API_KEY` and any
   vector‑store credentials.
5. **Build and run the containers** with Docker Compose:
   ```bash
   docker compose up -d --build
   ```
   This will start the FastAPI service, the vector store, and any auxiliary
   components defined in `docker-compose.yaml`.
6. **Verify the deployment** – send a request to the public IP address of the
   EC2 instance (e.g., `http://<ec2-ip>/docs`) to access the automatically
   generated OpenAPI documentation and test the API.

For production use, consider adding an Nginx reverse proxy, enabling TLS via
Let's Encrypt, and configuring an auto‑scaling group or load balancer if you
need to handle higher traffic.