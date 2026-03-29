# Research: RAG MCP vs Direct Workspace for Robot Documentation

## Context
After converting 237 PDF tutorials to Markdown + image sidecars, we needed to decide how to make this documentation available to Claude Code during robot development sessions.

## Option Investigated: local-knowledge-rag-mcp
- Repository: https://github.com/patakuti/local-knowledge-rag-mcp
- MCP server providing semantic search via vector embeddings (pgvector + PostgreSQL)
- Supports Markdown, plain text, HTML, JSON ingestion
- Embedding providers: OpenAI API, Ollama (local), or any OpenAI-compatible endpoint
- Chunking: LangChain RecursiveCharacterTextSplitter (default 1000 chars, 200 overlap)
- Exposes 13 MCP tools (search, report generation, index management)
- Has web-based Index Manager UI for rebuilding indexes

### Limitations found
- **No image indexing** — images and image descriptions in sidecars would not be searchable unless embedded as text in the markdown (which they are, but it's still a limitation of the tool)
- Requires PostgreSQL + pgvector infrastructure
- Needs an embedding provider (API cost or local Ollama setup)
- Dimension mismatch when changing models requires full reindex

## Documentation Size Analysis (extrapolated from 46/237 converted PDFs)

| Metric | Value |
|--------|-------|
| Total markdown text | ~1.6 MB |
| Estimated tokens | ~411,000 |
| Context window usage | ~41% of 1M |
| PNG images | ~401 |
| Sidecar description files | ~401 |

## Decision: Skip RAG, use direct workspace folder

**Rationale:**
1. Claude Code doesn't load all files at once — it uses Grep/Glob/Read to search on demand, so 411K tokens never hit context simultaneously
2. 237 well-named markdown files in a clear numbered directory structure are easily searchable by keyword (Grep)
3. RAG MCP adds significant infrastructure overhead (PostgreSQL, pgvector, embedding model) for marginal benefit over Grep on structured markdown
4. RAG MCP doesn't index images — the sidecar descriptions are already searchable as text in the workspace
5. No ongoing maintenance needed — files are just files, no database to keep in sync

**How to use:** Point Claude Code at the converted documentation folder via `--add-dir ROSMASTER-M3PRO-DOCS-MD` or place it in the same repo as the robot development project. Claude Code will naturally search through it with Grep/Glob/Read when answering questions about the robot.

## Future reconsideration
RAG may become worthwhile if:
- Documentation grows significantly beyond current ~400K tokens
- Semantic search proves necessary (keyword search insufficient for finding relevant content)
- A simpler RAG solution emerges that doesn't require PostgreSQL infrastructure (e.g., SQLite-based vector store)
