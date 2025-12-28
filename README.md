
# Construction Marketplace Mini RAG System

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) based AI assistant built for a construction marketplace. It allows users to ask questions about internal construction documents such as policies, FAQs and specifications and receive answers strictly grounded in those documents.

The system uses semantic search over document embeddings and a local open-source Large Language Model to generate accurate and explainable answers.

## Tech Stack Used
- Streamlit for chatbot interface
- FAISS for local vector search
- Sentence-Transformers (all-MiniLM-L6-v2) for embeddings
- Ollama with Phi-3 (2.7B) local LLM for answer generation
- LangChain for pipeline orchestration

## Why These Models Were Chosen
Sentence-Transformers all-MiniLM-L6-v2 was chosen because it is lightweight, fast, open-source and produces high-quality semantic embeddings.
Phi-3 (2.7B) was chosen as a local LLM to meet the requirement of using an open-source model and to avoid any external API dependency.

## Document Chunking
The markdown documents are split using RecursiveCharacterTextSplitter with:
Chunk size: 500
Chunk overlap: 100
This preserves semantic continuity while enabling efficient retrieval.

## Vector Search
All document chunks are embedded and indexed in a local FAISS vector database.
For every user query, the top 3 most relevant chunks are retrieved using cosine similarity.

## Grounded Answer Generation
The LLM is strictly instructed to answer ONLY using the retrieved document chunks.
If information is missing, it responds with:
Not available in the documents.
This prevents hallucinations and unsupported claims.

## Transparency
The application displays:
- Retrieved document context
- Final generated answer
- Source document names

## Evaluation Questions Used
1. What happens if a construction project is delayed?
2. How does Indecimal ensure payment safety for customers?
3. What are the available construction packages and their prices per sqft?
4. Do you provide real-time construction progress tracking?
5. What is included in the zero-cost maintenance program?
6. How many quality checkpoints are used during construction?
7. What flooring wallet is offered in the Infinia package?
8. What makes Indecimal different from typical builders?
9. How are contractor payments released?
10. What steel brands are used in the Pinnacle package?

## Observations
- Retrieved chunks were always relevant.
- No hallucinations were observed.
- Answers were concise, grounded and explainable.

## How to Run
1. Create virtual environment
2. Install requirements using pip install -r requirements.txt
3. Install Ollama and run ollama pull phi3
4. Start application using streamlit run ui/streamlit_app.py

## Screenshots
All screenshots used for evaluation are placed inside the screenshots folder.

## Limitations

-   The system can only answer questions that are present in the provided documents.
    
-   It does not use internet data or external knowledge.
    
-   Answers are limited to the scope of the uploaded markdown documents.
    
-   Large documents may increase initial loading time due to embedding generation.


## Flowchart

```mermaid
flowchart TD
A[User] --> B[Streamlit Web Interface]
B --> C[User Question]
C --> D[FAISS Vector Database]
D --> E[Top-K Relevant Document Chunks]
E --> F[Retrieved Context]
F --> G[Local LLM Phi-3 via Ollama]
G --> H[Final Grounded Answer and Sources]
H --> I[Displayed to User]

