---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html
---

# Basic reasoning agents
<a name="basic-reasoning-agents"></a>

A basic reasoning agent is the simplest form of agentic AI that performs logical inference or decision-making in response to a query. It accepts input from a user or system and processes queries and generates responses using structured prompts.

This pattern is useful for tasks that require single-step reasoning, classification, or summarization based on a given context. It doesn't use memory, tools, or state management, which makes it stateless, lightweight, and highly composable across large workflows.

## Architecture
<a name="architecture.83efeae6-81f9-514e-b8e3-3adf48484f65"></a>

The flow of a basic reasoning agent is shown in the following diagram:

![Basic reasoning agent.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/6a28fb96-02f2-41e8-8b95-41880fe3e172.png)

## Description
<a name="description.33fcee2a-6bc8-5f74-9e92-6f6a2609b2cf"></a>

1. Receives an input
   + A user, system, or upstream agent submits a query or instruction.
   + The input is handed off to the agent shell or orchestration layer.
   + This step includes any preprocessing, prompt templating, and goals identification.

1. Invokes the LLM
   + The agent transforms the query into a structured prompt and sends it to an LLM (for example, through Amazon Bedrock).
   + The LLM generates a response based on the prompt using pretrained knowledge and context.
   + The generated output may include reasoning steps (chain-of-thought), final answers, or ranked options.

1. Returns a response
   + The generated output is relayed to the agent's interface.
   + This may include formatting, postprocessing, or an API response.

## Capabilities
<a name="capabilities.edbd9c27-0584-5a60-9a5d-5d9b137ab5e8"></a>
+ Supports natural language or structured input
+ Uses prompt engineering to guide behavior
+ Stateless and scalable
+ Can be embedded into UI, CLI, APIs, and pipelines

## Limitations
<a name="limitations.7624897b-3492-5a19-acd6-e225ec3f1d7c"></a>
+ No memory or historical awareness
+ No interaction with external tools or data sources
+ Limited to what the LLM knows at the time of inference

## Common use cases
<a name="common-use-cases.1d9d6d6f-2911-54dc-b23e-c0371d5e38d6"></a>
+ Conversational questions and answers
+ Policy explanations and summaries
+ Guidance for making decisions
+ Lightweight and automated chatbot flows
+ Classification, labeling, and scoring

## Implementation guidance
<a name="implementation-guidance.e04a50b9-a6f3-5e1a-9c57-a2cd76726c25"></a>

You can use the following tools and services to create a basic reasoning agent:
+ Amazon Bedrock for LLM invocation (Anthropic, AI21, Meta)
+ Amazon API Gateway or AWS Lambda to expose it as a stateless microservice
+ Prompt templates stored in Parameter Store, AWS Secrets Manager, or as code

## Summary
<a name="summary.2c92ddfc-289f-54c4-bb03-7796aac0960c"></a>

The basic reasoning agent is foundational because of its simple structure. It has core capabilities that turn goals into reasoning paths that lead to intelligent outputs. This pattern is often a starting point for advanced patterns, such as tool-based agents and agents that use retrieval-augmented generation (RAG). It's also a reliable and modular component of large workflows.

### Agent RAG
<a name="agent-rag.94e19a89-d027-5bc5-99d7-6ecffa666a31"></a>

Retrieval-augmented generation (RAG) is a technique that combines information retrieval with text generation to create accurate and contextual responses. RAG enables agents to retrieve relevant external information before engaging the LLM. It extends an agent's effective memory and reasoning accuracy by grounding its decisions in up-to-date, factual, or domain-specific information. In contrast to stateless LLMs that rely solely on pretrained weights, RAG has an external knowledge search layer that dynamically enhances prompts with context.

## Architecture
<a name="architecture.37306cba-6a23-5025-b363-91721743fb6a"></a>

The logic of the RAG pattern is illustrated in the following diagram:

![Agent RAG.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/6b0f8d0b-1755-407f-abb9-5bfc2c5447b1.png)

*Figure 3. Agent RAG*

## Description
<a name="description.7cc94e0f-6bce-5cdd-bcd0-c965dd58525a"></a>

1. Receives a query
   + A user or upstream system submits a query or goal to the agent.
   + The agent shell accepts the request and formats it as a prompt for reasoning.

1. Searches an external source
   + The agent identifies concepts and intent from the query.
   + It queries a knowledge source, such as a vector store, database, or document index using semantic search or keyword matching.
   + The most relevant passages, documents, or entities are retrieved for use in the next step.

1. Generates a contextual response
   + The agent augments the prompt with the retrieved information, forming a context-enhanced input for the LLM.
   + The LLM processes any inputs using generative reasoning (for example, chain-of-thought or reflection) to produce an accurate response.

1. Returns the final output
   + The agent prepares the output by wrapping it in any communication headers or required formatting and then returns it to the user or calling system.
   + (Optional) The retrieved documents and LLM output may be logged, scored, and stored in memory for future queries.

## Capabilities
<a name="capabilities.84fa5195-5c7a-5745-9083-d8b3c6b46693"></a>
+ Fact-grounded output even in long-tail or enterprise-specific domains
+ Memory extension without fine-tuning the model
+ Dynamic context based on each query and user state
+ Fully compatible with vector databases, semantic indexes, and metadata filtering

## Common use cases
<a name="common-use-cases.a6536db9-4db9-5109-8351-218df920e86e"></a>
+ Enterprise knowledge assistants
+ Regulatory compliance bots
+ Customer support copilots
+ Search-enhanced chatbots
+ Developer documentation agents

## Implementation guidance
<a name="implementation-guidance.ebd8ef0d-c888-5a04-bbb2-c6537cebb47d"></a>

Use the following tools and services to create an agent that uses RAG:
+ Amazon Bedrock for LLM invocation
+ Amazon Kendra, OpenSearch, or Amazon Aurora for documentation or a structured data search
+ Amazon Simple Storage Service (Amazon S3) for document storage
+ AWS Lambda to orchestrate search, prompt, and LLM inference
+ Knowledge-based integrations with agents (by using memory plugins, semantic retrievers, or Amazon Bedrock)

## Summary
<a name="summary.00f8d6e3-f141-50ed-ad09-dcfdf4a5a1a2"></a>

Agent RAG connects static model reasoning to dynamic, real-world intelligence. It equips agents with the ability to look up what they don't know, synthesize answers from retrieved knowledge, and produce high-confidence, auditable responses.

RAG patterns are a foundation for building intelligent agents that scale knowledge access without retraining. It is often a precursor to more complex orchestration patterns involving tool use, planning, and long-term memory.
