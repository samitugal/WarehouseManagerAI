
# Warehouse Management ChatBot Project

This project is designed to assist with warehouse management through a ChatBot application. It leverages support from OpenAI and Amazon LLM models to respond to various user queries related to warehouse management.

## Features

- **LLM Models:** Supports both OpenAI and Amazon LLM models.
- **Database:** Utilizes PostgreSQL for relational database management.
- **Embeddings:** Pinecone is used for embedding operations.
- **Langchain Agents and Tools:** Creates an agent to query both relational and unstructured datasets based on user queries.
- **Frontend:** A Streamlit application provides the user interface.
- **History Mechanism:** Keeps track of user interactions and query history.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samitugal/WarehouseManagerAI.git
   cd warehouse-management-chatbot
   ```

2. **Set up the Python environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL using Docker:**
   - Ensure Docker is installed and running on your system.
   - Use the provided `docker-compose.yaml` file to set up the PostgreSQL database with a sample Northwind database.
   - Run the following command to start the services:
     ```bash
     docker-compose up -d
     ```
   - The database connection settings in the project configuration file should be updated to match those specified in the `docker-compose.yaml` file.

5. **Set up Pinecone:**
   - Sign up for Pinecone and obtain the API key.
   - Update the Pinecone API settings in the project configuration file.

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run ui/streamlit_ui.py
   ```

2. **Interacting with the ChatBot:**
   - Open the Streamlit application in your browser.
   - Use the ChatBot interface to query the warehouse management system.
   - The ChatBot will respond based on the combined power of OpenAI and Amazon LLM models, querying the PostgreSQL database and Pinecone embeddings as needed.

## Project Structure

- `ui/streamlit_ui.py`: The main Streamlit application file.
- `requirements.txt`: List of required Python packages.
- `configs/`: Directory for configuration definitions.
   - `Database/`: Directory for database configration definitons.
   - `Embeddings/`: Directory for embeddings configration definitons.
   - `LLM/`: Directory for large language model configration definitons.
- `data/`: Directory for data-related files.
- `src/`: Source code directory.
  - `agents/`: Agents used for querying data.
  - `database/`: Database-related modules.
  - `embedding_providers/`: Modules for embedding operations.
  - `llm/`: Large Language Model-related modules.
  - `prompts/`: Directory for prompt templates.
  - `tools/`: Tools used by the agents.
  - `utils/`: Utility functions and modules.
  - `ui/`: Streamlit UI components.

## Contributing

We welcome contributions to improve the project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## Screenshots

![image](https://github.com/user-attachments/assets/4cdf354a-37ad-4bfc-ad74-e1a3150f6559)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/)
- [Amazon LLM](https://aws.amazon.com/machine-learning/large-language-models/)
- [Langchain](https://langchain.com/)
- [Pinecone](https://www.pinecone.io/)
- [Streamlit](https://streamlit.io/)
