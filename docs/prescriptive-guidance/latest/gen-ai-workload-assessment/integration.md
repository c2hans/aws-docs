---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-workload-assessment/integration.html
---

# Integration
<a name="integration"></a>

|
|
| Questions | Example response |
| --- |--- |
| What are the requirements for integrating the generative AI solution with existing systems or data sources? | REST APIs, message queues, database connectors, and so on. |
| How will data be ingested and preprocessed for the generative AI solution? | By using batch processing, streaming data, data transformations, and feature engineering. |
| How will the output of the generative AI solution be consumed or integrated with downstream systems? | Through API endpoints, message queues, database updates, and so on. |
| Which event-driven integration patterns can be used for the generative AI solution? | Message queues (such as Amazon SQS , Apache Kafka, RabbitMQ), pub/sub systems, webhooks, event streaming platforms. |
| Which API-based integration approaches can be used to connect the generative AI solution with other systems? | RESTful APIs, GraphQL APIs, SOAP APIs (for legacy systems). |
| Which microservices architecture components can be used for the generative AI solution integration? | Service mesh for inter-service communication, API gateways, container orchestration (for example, Kubernetes). |
| How can hybrid integration be implemented for the generative AI solution? | By combining event-driven patterns for real-time updates, batch processing for historical data, and APIs for external system integration. |
| How can the generative AI solution output be integrated with downstream systems? | Through API endpoints, message queues, database updates, webhooks, and file exports. |
| Which security measures should be considered for integrating the generative AI solution? | Authentication mechanisms (such as OAuth or JWT), encryption (in transit and at rest), API rate limiting, and access control lists (ACLs). |
| How do you plan to integrate open source frameworks such as LlamaIndex or LangChain into your existing data pipeline and generative AI workflow? | We're planning to use LangChain to build complex generative AI applications, particularly for its agent and memory management capabilities. We aim to have 60% of our generative AI projects using LangChain within the next 6 months. |
| How will you ensure compatibility between your chosen open source frameworks and your existing data infrastructure? | We're creating a dedicated integration team to ensure smooth compatibility. By the third quarter, our goal is to have a fully integrated pipeline that uses LlamaIndex for efficient data indexing and retrieval within our current data lake structure. |
| How do you plan to leverage the modular components of frameworks such as LangChain for rapid prototyping and experimentation? | We're setting up a sandbox environment where developers can quickly prototype by using LangChain's components. |
| What is your strategy for keeping up with updates and new features in these rapidly evolving open source frameworks? | We've assigned a team to monitor GitHub repositories and community forums for LangChain and LlamaIndex. We plan to evaluate and integrate major updates quarterly, with a focus on performance improvements and new capabilities. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
