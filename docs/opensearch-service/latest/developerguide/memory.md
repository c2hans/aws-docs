---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/memory.html
---

# What is Amazon OpenSearch Memory?
<a name="memory"></a>

Amazon OpenSearch Memory is a fully managed memory service for AI agents. Your agent or application sends the conversations, data, and documents it works with to OpenSearch Memory as *events*. OpenSearch Memory extracts the facts, summaries, and other details worth keeping from those events and stores them as *memories*. Your agent then searches those memories to recall what it learned, across sessions and over time.

With OpenSearch Memory, you don't build or operate a memory system yourself. You don't run a vector database, write extraction prompts for common cases, or manage the pipeline that turns raw conversation into durable knowledge. You create a *space*, choose the kinds of memory you want, send events, and search.

**Topics**
+ [Characteristics of OpenSearch Memory](#memory-characteristics)
+ [OpenSearch Memory use cases](#memory-use-cases)
+ [Capabilities of OpenSearch Memory](#memory-capabilities)
+ [Security](#memory-overview-security)
+ [Resilience](#memory-overview-resilience)
+ [Accessing OpenSearch Memory](#memory-accessing)
+ [Getting started with OpenSearch Memory](#memory-overview-getting-started)
+ [How Amazon OpenSearch Memory works](memory-how-it-works.md)
+ [Getting started with Amazon OpenSearch Memory](memory-getting-started.md)
+ [Working with spaces in Amazon OpenSearch Memory](memory-spaces.md)
+ [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md)
+ [Working with events in Amazon OpenSearch Memory](memory-events.md)
+ [Working with memories in Amazon OpenSearch Memory](memory-memories.md)
+ [Searching memories and events in Amazon OpenSearch Memory](memory-search.md)
+ [Best practices for Amazon OpenSearch Memory](memory-best-practices.md)
+ [Security in Amazon OpenSearch Memory](memory-security.md)
+ [Logging Amazon OpenSearch Memory API calls with AWS CloudTrail](memory-monitoring.md)
+ [Endpoints and quotas for Amazon OpenSearch Memory](memory-quotas.md)
+ [Error handling in Amazon OpenSearch Memory](memory-errors.md)
+ [Troubleshooting Amazon OpenSearch Memory](memory-troubleshooting.md)

## Characteristics of OpenSearch Memory
<a name="memory-characteristics"></a>

### Fully managed
<a name="memory-characteristics-managed"></a>

OpenSearch Memory handles storage, indexing, extraction, and the model calls that extraction needs. There are no servers to provision, no software to patch, and no maintenance windows. You don't request access to any foundation model or grant any model permissions. OpenSearch Memory calls the extraction model on your behalf.

### Write now, remember later
<a name="memory-characteristics-async"></a>

Writing an event is fast and durable. [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) returns as soon as the event is stored. OpenSearch Memory extracts memories from the event afterward, in the background, so your agent's response time doesn't depend on how long extraction takes. For more information, see [How Amazon OpenSearch Memory works](memory-how-it-works.md).

### Memories that stay current
<a name="memory-characteristics-current"></a>

By default, OpenSearch Memory *consolidates* new memories with what it already knows. When a user who said "I live in Seattle" later says "I moved to Austin," the stored fact is updated rather than duplicated or contradicted. For more information, see [Consolidation](memory-strategies.md#memory-strategies-consolidation).

### Familiar search
<a name="memory-characteristics-search"></a>

You search memories with a subset of the OpenSearch Query DSL that you may already know, including `match`, `neural`, `hybrid`, and `bool` queries. Results come back ranked by relevance. For more information, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).

## OpenSearch Memory use cases
<a name="memory-use-cases"></a>
+ **Personal assistants** – Remember a user's preferences, constraints, and history so the assistant doesn't ask the same questions twice. For example, a travel assistant that recalls "prefers window seats" and "vegetarian" on every trip.
+ **Customer support agents** – Summarize each support session and extract case details, such as order IDs and their status, so an agent picking up a case later has the context without rereading the transcript.
+ **Operational and coding agents** – Record what an agent did and what happened, such as a deployment result, so later runs can recall outcomes and avoid repeating mistakes.
+ **Knowledge from documents** – Send PDFs and images that your agent should be able to recall, and search their content alongside conversation history.

## Capabilities of OpenSearch Memory
<a name="memory-capabilities"></a>

### Memory strategies
<a name="memory-capabilities-strategies"></a>

A *memory strategy* defines one kind of memory that a space extracts. OpenSearch Memory provides `SEMANTIC` strategies that extract facts, `SUMMARY` strategies that summarize each session, and `CUSTOM` strategies that extract whatever your own prompt describes. A space can use up to 10 strategies at once, each extracting from the same events. For more information, see [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md).

### Scoping by actor and session
<a name="memory-capabilities-scoping"></a>

Every event and memory belongs to an *actor* (the user it is about) and a *session* (one conversation). Searches are scoped to one actor, so one user's memories never surface for another. You can also enforce this in IAM with the `osm:actorId` condition key. For more information, see [Identity and Access Management for Amazon OpenSearch Memory](security-iam-memory.md).

### Retention you control
<a name="memory-capabilities-retention"></a>

You choose how long a space keeps events (1 to 365 days) and memories (from 1 day to 10 years, or indefinitely). Expired events and memories are removed for you. For more information, see [Configuring retention](memory-spaces.md#memory-spaces-retention).

### Direct writes
<a name="memory-capabilities-direct-writes"></a>

When your application already knows a fact, you can write it as a memory directly with [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) instead of sending a conversation and waiting for extraction. For more information, see [Working with memories in Amazon OpenSearch Memory](memory-memories.md).

## Security
<a name="memory-overview-security"></a>

OpenSearch Memory uses AWS Identity and Access Management (IAM) to control who can create spaces and who can read and write the events and memories in them. Every operation is an IAM action with the `osm` prefix, authorized on the space's Amazon Resource Name (ARN). Condition keys let you limit a principal to specific actors, sessions, or strategies within a space.

OpenSearch Memory encrypts all data at rest. By default it uses an AWS owned key. You can instead use a customer managed key in AWS Key Management Service (AWS KMS) that you create and control. All requests use TLS 1.2 or later. For more information, see [Security in Amazon OpenSearch Memory](memory-security.md).

## Resilience
<a name="memory-overview-resilience"></a>

OpenSearch Memory is a Regional service. It stores each space's events and memories redundantly across multiple Availability Zones in the AWS Region where you created the space. For more information, see [Resilience in Amazon OpenSearch Memory](memory-resilience.md).

## Accessing OpenSearch Memory
<a name="memory-accessing"></a>

You can work with OpenSearch Memory using the AWS Management Console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the OpenSearch Memory API directly.
+ **Console** – Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home) and choose **Memory** in the navigation pane. The console supports creating, viewing, editing, tagging, and deleting spaces.
+ **AWS CLI** – OpenSearch Memory commands are under `aws opensearchmemory`. Each command is the operation name in lowercase words separated by hyphens, for example `aws opensearchmemory create-space`.
+ **AWS SDKs** – The service is available in every AWS SDK under the service ID `OpenSearchMemory`. The SDKs choose the correct endpoint for each operation, sign requests, and retry transient errors for you.
+ **API** – If you call the API directly, sign requests with Signature Version 4 using the service name `osm`. Space and tagging operations use the Regional endpoint `https://osm.{{region}}.api.aws`. Event and memory operations use the space's own endpoint, `https://{{space-id}}.osm.{{region}}.on.aws`. OpenSearch Memory doesn't have FIPS endpoints.

OpenSearch Memory is available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Frankfurt). For the endpoints, see [Service endpoints](memory-quotas.md#memory-quotas-endpoints).

## Getting started with OpenSearch Memory
<a name="memory-overview-getting-started"></a>

If you're a first-time user, we recommend that you begin with the following topics:
+ [How Amazon OpenSearch Memory works](memory-how-it-works.md) – Describes spaces, events, memories, and strategies, and what happens between writing an event and finding a memory.
+ [Getting started with Amazon OpenSearch Memory](memory-getting-started.md) – Walks you through creating a space, sending a conversation, searching the memories extracted from it, and cleaning up.
+ [Best practices for Amazon OpenSearch Memory](memory-best-practices.md) – Recommendations for choosing strategies, scoping data, and keeping memories useful.
