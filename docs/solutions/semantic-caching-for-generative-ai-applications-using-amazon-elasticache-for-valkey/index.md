---
source_url: https://docs.aws.amazon.com/solutions/semantic-caching-for-generative-ai-applications-using-amazon-elasticache-for-valkey/index.html
---

---
title: 'Guidance for Semantic Caching for GenerativeAI applications using Amazon ElastiCache for Valkey'
canonical_url: https://docs.aws.amazon.com/solutions/semantic-caching-for-generative-ai-applications-using-amazon-elasticache-for-valkey/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Semantic Caching for GenerativeAI applications using Amazon ElastiCache for Valkey

## Overview

This Guidance demonstrates how to implement semantic caching for generative AI applications to reduce response latency and costs by storing and retrieving similar query results using Amazon ElastiCache for Valkey's vector search capabilities. The implementation uses vector embeddings generated from popular AI providers like Amazon Bedrock, Amazon SageMaker, Anthropic, or OpenAI to create searchable representations of queries and responses. ElastiCache for Valkey enables microsecond-latency searches across billions of high-dimensional vectors with up to 99% recall accuracy, making it ideal for caching semantically similar requests in real-time applications. You can significantly reduce your generative AI application costs and improve user experience by avoiding redundant API calls for semantically similar queries while maintaining high-quality responses.

## Benefits

### Reduce AI response costs

Serve cached responses for semantically similar prompts with microsecond latency, eliminating redundant foundation model calls. This approach can significantly lower operational expenses by reusing previously generated responses for similar user queries.

### Accelerate user experiences

Deliver AI responses with microsecond latency for semantically similar queries using ElastiCache for Valkey's vector search capabilities. Users receive immediate responses to common questions without waiting for foundation model processing, creating a more responsive application experience.

### Enhance response relevance

Combine semantic caching with personalized memory storage to maintain context across user interactions. The solution stores user preferences and conversation history in ElastiCache, enabling more contextually appropriate responses tailored to individual users.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/semantic-caching-for-generative-ai-applications-using-amazon-elasticache-for-valkey.pdf)

![Architecture diagram](/images/solutions/semantic-caching-for-generative-ai-applications-using-amazon-elasticache-for-valkey/images/semantic-caching-for-generative-ai-applications-using-amazon-elasticache-for-valkey-1.png)

1. **Step 1**: End users submit prompts, and Amazon API Gateway serves as the entry point for user requests.
1. **Step 2**: AWS Lambda orchestrates the request flow and business logic. It takes the prompt and immediately sends the user's text prompt to an Embedding Model hosted on Amazon Bedrock.
1. **Step 3**: The embedding model (such as Amazon Titan Text Embeddings V2) transforms the user's natural language text into a high-dimensional vector embedding. Vector embeddings enable semantic similarity comparisons.
1. **Step 4**: The Lambda function takes the newly created vector embedding and queries the Semantic Cache (powered by Amazon ElastiCache for Valkey) to search for previously answered similar questions. This can have two possible outcomes: Cache Hit (Similar Prompt Found): If a semantically similar prompt exists in the cache within the configured threshold, the cached response is immediately retrieved from ElastiCache, and is returned to the user with microsecond latency, delivering massive cost & latency benefits. Cache Miss (No Similar Prompt Found): If no semantically similar prompt exists in the cache, the Lambda function queries the RAG (Retrieval-Augmented Generation) knowledge base stored in Amazon ElastiCache for Valkey to retrieve relevant contextual information. This produces an "enriched prompt" containing both the user's original question and relevant factual information from the knowledge base.
1. **Step 5**: Cache Miss (No Similar Prompt Found): If no semantically similar prompt exists in the cache, the Lambda function queries the RAG (Retrieval-Augmented Generation) knowledge base stored in Amazon ElastiCache for Valkey to retrieve relevant contextual information. This produces an "enriched prompt" containing both the user's original question and relevant factual information from the knowledge base.
1. **Step 6**: The enriched prompt from Step 5 is sent to a Foundation Model hosted on Amazon Bedrock (such as Anthropic Claude, Amazon Nova, or other Foundation Models), and generates a comprehensive, contextually-aware response.
1. **Step 7**: As the interaction occurs, the Lambda function extracts and stores user-specific information into the LLM Memory component using mem0 (an open-source memory layer) integrated with Amazon ElastiCache for Valkey. This includes aspects like: Communication style preferences ("prefers detailed technical explanations"), Role/occupation ("is a Python developer"), Conversation History ("Unresolved questions or follow-ups"), etc.
1. **Step 8**: Finally, the Lambda function stores both the original user prompt (as a vector embedding) and the LLM's generated response into the Semantic Cache (Amazon ElastiCache for Valkey).
1. **Step 9**: After all caching and memory operations are complete (Steps 7 and 8), the final response flows back through the Lambda function and Amazon API Gateway to the user.
1. **Step 10**: Amazon CloudWatch provides observability and cache performance metrics. AWS Identity and Access Management (AWS IAM). AWS Key Management Service or Amazon Cognito can be used for authentication depending on how the frontend integration is designed. AWS Key Management Service (AWS KMS) is used to encrypt secrets.
[Read usage guidelines](/solutions/guidance-disclaimers/)
