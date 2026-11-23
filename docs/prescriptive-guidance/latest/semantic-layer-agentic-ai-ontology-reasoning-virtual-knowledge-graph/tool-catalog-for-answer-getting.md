---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/tool-catalog-for-answer-getting.html
---

# Tool Catalog for Question & Answer

## Tool Catalog for Question & Answer
<a name="tool-catalog-for-question-9999999999999999amp--answer.0fb915f1-7052-5f1e-aca4-be58bd4b27e0"></a>

### 1. ask — Natural Language Query with Clarification Support
<a name="1.-ask---natural-language-query-with-clarification-support.d6813b16-ecb0-5ae6-9df5-b6eec630f66f"></a>

**Purpose**: Primary entry point for natural language questions. Accepts a question and returns an answer grounded in the knowledge graph, with support for multi-turn clarification when additional information is needed.

**Input:**
+ `question: string` — Natural language question (required)
+ `ontology_iri?: IRI` — Optional ontology scope to limit query to specific domain ontologies
+ `conversation_id?: string` — Optional conversation context for multi-turn interactions

**Output:**
+ `status: "needs_clarification" | "complete" | "error"` — Response status
+ `answer: string` — Natural language answer
+ `clarification_request?: { message: string, options?: [], required_fields?: [] }` — Structured clarification request
+ `evidence: [{ subject, predicate, object, graph }]` — Supporting evidence triples
+ `confidence: float` — Overall confidence score (0.0-1.0)
+ `conversation_id: string` — Conversation ID for follow-up queries
+ `metrics_used: [{ metric_id, metric_name, version, expression, publish_date }]` — lists which Metric Store definitions were injected during query generation

**Example Input:**

```
{
  "question": "What is the average claim amount for diabetes patients in Q4 2025?",
  "ontology_iri": "urn:ontology:healthcare:claims:v2"
}
```

**Example Output:**

```
{
  "status": "complete",
  "answer": "The average claim amount for diabetes patients in Q4 2025 was $3,847.23, based on 1,247 claims across 892 unique patients.",
  "evidence": [
    {
      "subject": "urn:claim:12345",
      "predicate": "claimAmount",
      "object": "4200.00",
      "graph": "urn:graph:claims:2025-q4"
    }
  ],
  "confidence": 0.94,
  "conversation_id": "conv-12345"
}
```

### 2. search — Semantic Search
<a name="2.-search---semantic-search.654082d1-c863-5d51-ad89-b38356acdacf"></a>

**Purpose**: Explore ontology classes, properties, and individuals using keyword, semantic similarity, or hybrid search modes.

**Input:**
+ `query: string` — Search query (required)
+ `mode?: "keyword" | "semantic" | "hybrid"` — Search mode (default: "hybrid")
+ `ontology_iri?: IRI` — Optional ontology scope
+ `top_k?: int` — Maximum number of results to return

**Output:**
+ `results: [{ iri, label, type, score, rdfs_comment }]` — Ranked search results with similarity scores

**Example Input:**

```
{
  "query": "patient claims",
  "mode": "hybrid",
  "ontology_iri": "urn:ontology:healthcare:claims:v2",
  "top_k": 5
}
```

**Example Output:**

```
{
  "results": [
    {
      "iri": "urn:ontology:healthcare:claims:Claim",
      "label": "Claim",
      "type": "owl:Class",
      "score": 0.92,
      "rdfs_comment": "A request for payment submitted to an insurance provider for medical services rendered. Synonyms: insurance claim, medical claim, reimbursement request"
    },
    {
      "iri": "urn:ontology:healthcare:claims:Patient",
      "label": "Patient",
      "type": "owl:Class",
      "score": 0.88,
      "rdfs_comment": "An individual receiving or registered to receive medical care. Synonyms: healthcare recipient, medical patient"
    }
  ]
}
```

### 3. intent\_classification — Question Intent Classification
<a name="3.-intent-classification---question-intent-classification.0f992010-03b0-5c14-ba6f-5949d5110373"></a>

**Purpose**: Analyze question intent, extract entities, and determine processing requirements.

**Input:**
+ `question: string` — Natural language question (required)
+ `ontology_iri?: IRI` — Optional ontology scope
+ `conversation_id?: string` — Optional conversation context

**Output:**
+ `intent_category: string` — Intent type
+ `extracted_entities: [{ entity_iri, label, type, ontology_iri }]` — Entities grounded in ontology
+ `extracted_relationships: [{ subject, predicate, object }]` — Relationships identified
+ `suggested_strategy: string` — Recommended query strategy
+ `requires_graphrag: boolean` — Whether document retrieval is needed
+ `confidence: float` — Classification confidence score

**Example Input:**

```
{
  "question": "What is the average claim amount for diabetes patients in Q4 2025?",
  "ontology_iri": "urn:ontology:healthcare:claims:v2"
}
```

**Example Output:**

```
{
  "intent_category": "AGGREGATION",
  "extracted_entities": [
    {
      "entity_iri": "urn:ontology:healthcare:claims:Claim",
      "label": "Claim",
      "type": "owl:Class",
      "ontology_iri": "urn:ontology:healthcare:claims:v2"
    },
    {
      "entity_iri": "urn:ontology:healthcare:claims:Patient",
      "label": "Patient",
      "type": "owl:Class",
      "ontology_iri": "urn:ontology:healthcare:claims:v2"
    }
  ],
  "extracted_relationships": [
    {
      "subject": "Claim",
      "predicate": "submittedBy",
      "object": "Patient"
    }
  ],
  "suggested_strategy": "sparql",
  "requires_graphrag": false,
  "confidence": 0.91
}
```

### 4. generate\_queries — Query Generation & Optimization
<a name="4.-generate-queries---query-generation-9999999999999999amp--optimization.52c6c182-773c-5a5c-9ca6-24b191b244a2"></a>

**Purpose**: Generate optimized SPARQL queries and execution plans based on question intent.

**Input:**
+ `question: string` — Natural language question (required)
+ `ontology_iri?: IRI` — Optional ontology scope
+ `conversation_id?: string` — Optional conversation context
+ `intent_classification: object` — Output from `intent_classification` tool (required)

**Output:**
+ `queries: [{ query: string, named_graph?: IRI, description: string }]` — Generated SPARQL queries
+ `execution_plan: { strategy, estimated_cost, estimated_latency_ms }` — Execution strategy
+ `graphrag_plan?: { similarity_threshold, top_k, traversal_depth }` — GraphRAG parameters
+ `explanation: string` — Natural language explanation

**Example Input:**

```
{
  "question": "What is the average claim amount for diabetes patients in Q4 2025?",
  "ontology_iri": "urn:ontology:healthcare:claims:v2",
  "intent_classification": {
    "intent_category": "AGGREGATION",
    "extracted_entities": [...],
    "suggested_strategy": "sparql"
  }
}
```

**Example Output:**

```
{
  "queries": [
    {
      "query": "PREFIX : <urn:ontology:healthcare:claims:> SELECT (AVG(?amount) AS ?avgAmount) WHERE { ?claim a :Claim ; :claimAmount ?amount ; :submittedBy ?patient. ?patient :hasCondition :Diabetes. FILTER(?claimDate >= '2025-10-01' && ?claimDate <= '2025-12-31') }",
      "named_graph": "urn:graph:claims:2025-q4",
      "description": "Calculate average claim amount for diabetes patients in Q4 2025"
    }
  ],
  "execution_plan": {
    "strategy": "parallel",
    "estimated_cost": 0.15,
    "estimated_latency_ms": 250
  },
  "explanation": "This query filters claims by diabetes patients in Q4 2025 and calculates the average claim amount using SPARQL aggregation."
}
```

### 5. execute\_queries — Federated Query Execution
<a name="5.-execute-queries---federated-query-execution.e92c4be0-90fa-505c-a6ec-eeb2bbcbcdbf"></a>

**Purpose**: Execute SPARQL queries across federated knowledge graphs.

**Input:**
+ `queries: [{ query: string, named_graph?: IRI }]` — SPARQL queries to execute

**Output:**
+ `results: [{ query_index, bindings, graph?, boolean? }]` — Query results
+ `provenance: [{ source_type, source_id, confidence }]` — Source metadata
+ `execution_stats: { total_latency_ms, queries_executed, sources_queried }` — Performance metrics

**Example Input:**

```
{
  "queries": [
    {
      "query": "PREFIX : <urn:ontology:healthcare:claims:> SELECT (AVG(?amount) AS ?avgAmount) WHERE { ?claim a :Claim ; :claimAmount ?amount ; :submittedBy ?patient. ?patient :hasCondition :Diabetes. FILTER(?claimDate >= '2025-10-01' && ?claimDate <= '2025-12-31') }",
      "named_graph": "urn:graph:claims:2025-q4"
    }
  ]
}
```

**Example Output:**

```
{
  "results": [
    {
      "query_index": 0,
      "bindings": [
        {
          "avgAmount": "3847.23"
        }
      ]
    }
  ],
  "provenance": [
    {
      "source_type": "neptune_graph",
      "source_id": "urn:graph:claims:2025-q4",
      "confidence": 0.98
    }
  ],
  "execution_stats": {
    "total_latency_ms": 245,
    "queries_executed": 1,
    "sources_queried": ["neptune_graph"]
  }
}
```

### 6. graphrag\_search — GraphRAG Retrieval
<a name="6.-graphrag-search---graphrag-retrieval.5da49ec4-c98d-5422-b999-8a9039f12623"></a>

**Purpose**: Retrieve relevant document chunks and concepts using hybrid retrieval.

**Input:**
+ `question: string` — Natural language question (required)
+ `ontology_iri?: IRI` — Optional ontology scope
+ `conversation_id?: string` — Optional conversation context
+ `similarity_threshold?: float` — Minimum cosine similarity (default: 0.7)
+ `top_k?: int` — Maximum results (default: 10)
+ `traversal_depth?: int` — Graph traversal depth (default: 2)

**Output:**
+ `document_chunks: [{ chunk_id, document_id, text, page_number, similarity_score }]` — Retrieved chunks
+ `concepts: [{ concept_iri, label, definition, similarity_score, related_concepts }]` — Extracted concepts
+ `graph_context: [{ subject, predicate, object }]` — Graph relationships
+ `provenance: [{ document_id, chunk_id, s3_uri }]` — Source document links

**Example Input:**

```
{
  "question": "What are the common complications of diabetes?",
  "similarity_threshold": 0.75,
  "top_k": 5
}
```

**Example Output:**

```
{
  "document_chunks": [
    {
      "chunk_id": "chunk-42",
      "document_id": "diabetes-guidelines-2025",
      "text": "Common complications of diabetes include cardiovascular disease, neuropathy, nephropathy, and retinopathy...",
      "page_number": 15,
      "similarity_score": 0.89
    }
  ],
  "concepts": [
    {
      "concept_iri": "urn:concept:diabetes-complications",
      "label": "Diabetes Complications",
      "definition": "Medical conditions arising from diabetes",
      "similarity_score": 0.91,
      "related_concepts": ["cardiovascular-disease", "neuropathy"]
    }
  ],
  "graph_context": [
    {
      "subject": "urn:concept:diabetes",
      "predicate": "hasComplication",
      "object": "urn:concept:cardiovascular-disease"
    }
  ],
  "provenance": [
    {
      "document_id": "diabetes-guidelines-2025",
      "chunk_id": "chunk-42",
      "s3_uri": "s3://medical-docs/diabetes-guidelines-2025.pdf"
    }
  ]
}
```

### 7. reasoning — Semantic Reasoning & Validation
<a name="7.-reasoning---semantic-reasoning-9999999999999999amp--validation.e4de0a57-7c6e-5be3-9683-5b2a8164d3e7"></a>

**Purpose**: Perform inference, constraint validation, and consistency checking on query results.

**Input:**
+ `vkg_results?: object` — Output from `execute_queries` (optional)
+ `graphrag_results?: object` — Output from `graphrag_search` (optional)
+ `search_results?: object` — Output from `search` (optional)
+ `ontology_iri?: IRI` — Optional ontology scope for reasoning rules

**Output:**
+ `inferred_triples: [{ subject, predicate, object, rule, confidence }]` — New triples derived
+ `validation_results: { conforms, violations }` — SHACL validation results
+ `consistency_check: { is_consistent, conflicts }` — Consistency validation
+ `reasoning_steps: [{ step, axiom, rule }]` — Reasoning chain explanation
+ `provenance: [{ source_type, source_id, rule, confidence }]` — Links to axioms/rules

**Example Input:**

```
{
  "vkg_results": {
    "results": [
      {
        "bindings": [{ "avgAmount": "3847.23" }]
      }
    ]
  },
  "ontology_iri": "urn:ontology:healthcare:claims:v2"
}
```

**Example Output:**

```
{
  "inferred_triples": [
    {
      "subject": "urn:claim:12345",
      "predicate": "requiresReview",
      "object": "true",
      "rule": "HighValueClaimRule",
      "confidence": 0.87
    }
  ],
  "validation_results": {
    "conforms": true,
    "violations": []
  },
  "consistency_check": {
    "is_consistent": true,
    "conflicts": []
  },
  "reasoning_steps": [
    {
      "step": "Applied HighValueClaimRule",
      "axiom": "Claims > $5000 require review",
      "rule": "SWRL: Claim(?c) ^ claimAmount(?c, ?amt) ^ greaterThan(?amt, 5000) -> requiresReview(?c, true)"
    }
  ],
  "provenance": [
    {
      "source_type": "reasoning_rule",
      "source_id": "HighValueClaimRule",
      "rule": "SWRL",
      "confidence": 0.87
    }
  ]
}
```

## Tool Design Principles
<a name="tool-design-principles.4c4023a6-195b-55b1-a7a5-d3b12782485f"></a>
+ `ask` is the primary entry point for chatbots and non-technical users — it abstracts all complexity and orchestrates the other tools internally
+ `intent_classification`**, **`generate_queries`**, **`execute_queries`**, **`graphrag_search`**, **`reasoning` expose the Q&A Agent's internal orchestration steps as discrete tools, enabling power users and agents to compose custom workflows
+ `search` provides lightweight semantic search without full Q&A orchestration
+ All tools propagate OpenTelemetry trace context for end-to-end observability
+ All tools support `ontology_iri` for scoping to specific domain ontologies
+ All tools return provenance metadata to support trustworthy AI and explainability
