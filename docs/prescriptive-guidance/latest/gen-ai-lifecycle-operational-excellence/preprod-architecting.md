---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod-architecting.html
---

# Architecting generative AI applications for production
<a name="preprod-architecting"></a>

Architecting generative AI applications for production environments requires a sophisticated approach that goes beyond experimental implementations in a PoC. As organizations scale their AI initiatives, they face complex challenges in creating robust, maintainable, and cost-effective systems. This section examines key architectural patterns and best practices that are essential for successfully deploying generative AI in real-world scenarios. With a focus on using a microservices architecture, implementing AI gateways, and optimizing cost and performance, the following sections provide practical strategies to build resilient generative AI systems. By adopting these principles, teams can create flexible, scalable infrastructures that are capable of meeting current demands while accommodating future growth and technological advancements.

**This section contains the following topics:**
+ [Decomposing generative AI monoliths into modular and reusable microservices](#preprod-architecting-monoliths)
+ [Data and prompt flow from PoC to preproduction](#preprod-architecting-flows)
+ [Centralizing control and observability with AI gateways](#preprod-architecting-gateway)
+ [Designing generative AI applications for performance and cost](#preprod-architecting-performance-cost)

## Decomposing generative AI monoliths into modular and reusable microservices
<a name="preprod-architecting-monoliths"></a>

Moving the generative AI PoC to a preproduction environment typically involves deploying its components into cloud-based resources. A common architectural anti-pattern in early generative AI development is the creation of a single, monolithic application that attempts to handle all aspects of a complex task in one application component. This approach is brittle and difficult to test. It's also extremely risky to update because a small change intended to improve one part of the output can have unforeseen and detrimental side effects on all other parts. A good practice is to move away from this monolithic approach and decompose the application's logic into a compound AI system, also known as a *chain*. For more information about compound AI systems, see [The Shift from Models to Compound AI Systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) (Berkley AI Research blog post). This architectural pattern involves breaking down a single large task into a sequence of smaller, discrete, and loosely coupled steps. Each step is handled by a more focused prompt or a dedicated tool.

The concept of a compound AI system aligns well with the principles of [cloud-native](https://aws.amazon.com/what-is/cloud-native/) architecture. *Cloud-native* refers to how a system is built and deployed. It emphasizes breaking down large applications into discrete, reusable, and independently deployable components that are known as *microservices*. Microservices are typically packaged in lightweight, portable containers. Adopting this approach for a generative AI application means that each component in the compound AI system (such as the RAG retriever, the summarization step, the data ingestion pipeline, and the user-facing frontend) can be developed, deployed, and scaled as a separate microservice. This architecture enables superior resilience because the failure of one non-critical component does not necessarily bring down the entire system. It also enhances manageability and observability because each service can be monitored and updated independently.

In a modular generative AI architecture, each microservice is designed to perform a specific, reusable function within the overall system. This helps organizations to build a library of standard components that can be quickly assembled to create new and complex generative AI applications.

The following are common microservices that you can reuse for multiple generative AI applications:
+ **Data ingestion and processing service** – This service is the data transformation hub for all knowledge. It is responsible for connecting to various data sources (such as databases or document repositories), cleaning the data, transforming it into a consistent format, strategically chunking it into smaller segments, and generating vector embeddings. By encapsulating this logic into a dedicated service, you create a reusable data pipeline that can feed multiple generative AI applications.
+ **Model abstraction service (*AI gateway*)** – This service acts as a unified interface to various foundation models. It abstracts the specific API details of different providers and services, such as Amazon Bedrock or Amazon SageMaker AI. This decoupling is immensely powerful because it helps the organization switch between LLMs with a simple configuration change, without altering the core application logic. This service facilitates A/B testing of different models and supports granular controls. For more information, see the [Centralizing control and observability with AI gateways](#preprod-architecting-gateway) section in this guide.
+ **Orchestration service** – This service acts as the conductor, defining the workflow and the sequence of calls to the various task-specific agents and services. It manages the flow of data between components to fulfill a complex user request. You can use frameworks such as [Strands Agents](https://strandsagents.com/) or [LangChain](https://www.langchain.com/) to build this layer, or you can build a custom service for more control.
+ **Memory as a service (MaaS)** – For sophisticated agentic systems, treat memory as a dedicated, decoupled service. A MaaS component provides a centralized and governable way to manage both short-term (*session*) and long-term memory. This approach breaks down the memory silos that form when each agent manages its own state. This allows memory to be shared and reused across different agents and interactions, which enables more coherent and personalized experiences. For more information, see [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) in the Amazon Bedrock documentation.
+ **Gateway service** – This service serves as a central hub for securely connecting, deploying, and managing tools for AI applications and agents. It simplifies tool development by transforming enterprise resources into agent-ready tools. The gateway service provides unified access through a single secure endpoint, features intelligent tool discovery with built-in semantic search capabilities, and offers comprehensive authentication for both inbound and outbound connections. For more information, see [Amazon Bedrock AgentCore Gateway: Securely connect tools and other resources to your Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html).
+ **Feedback and logging service** – This service centralizes the collection of all user feedback (both explicit and implicit) and operational logs. By creating a single, reusable service for this function, you drive consistent data collection and monitoring across all generative AI applications in the enterprise.

The true power of a microservices architecture lies in decoupling and reducing the dependencies between components so they can operate and evolve independently. A key enabler of decoupling is the choice of communication protocols between services. The following are considerations when choosing protocols:
+ Protocol independence
  + Asynchronous messaging, such as message queues and event streams, allows services to communicate without waiting for immediate responses. This reduces temporal coupling.
  + RESTful APIs provide standardized, stateless communication that doesn't require services to maintain connection state.
  + Event-driven architectures enable services to react to events without direct knowledge of event producers.
+ Technology stack freedom
  + Well-defined communication protocols allow each microservice to be built using the most appropriate technology stack.
  + Services can be written in different programming languages if they adhere to the agreed communication contract.
  + Teams can choose databases, frameworks, and tools that best fit their specific service requirements.
+ Evolutionary architecture
  + Proper protocol design allows services to evolve independently through versioning strategies.
  + New service versions can be deployed without breaking existing consumers.
  + Services can be replaced entirely if they maintain the communication contract.
+ Scalability and resilience
  + Load balancing becomes possible when services communicate through well-defined protocols.
  + You can implement circuit breaker patterns to handle service failures gracefully.
  + Services can be scaled independently based on their specific performance requirements.

## Managing asset promotion and environment transitions
<a name="preprod-architecting-flows"></a>

One of the most critical aspects of generative AI development is the structured transition of validated artifacts between lifecycle stages. Unlike traditional software development, generative AI applications involve multiple interdependent components, such as prompts, model configurations, evaluation datasets, and application code. These components  must be carefully coordinated and promoted together. Organizations that struggle with this transition can experience the following:
+ Loss of experimental insights when moving from PoC to production environments
+ Inconsistent configurations across different stages of development
+ Quality regression when untested or unstable artifacts are promoted
+ Broken feedback loops that prevent continuous improvement

The GLOE framework emphasizes continuous improvement and feedback loops and iterative and evidence-backed development. This asset promotion process is where these principles are operationalized. You must make sure that only validated, stable configurations advance and maintain channels for learning and refinement. The transition from the PoC stage to preproduction involves a structured governance process for promoting validated artifacts across environments:
+ **Prompts and LLM versions** – Approved prompt versions, along with their associated LLM versions and hyperparameters (temperature, top\_p, top\_k), are promoted from the prompt store management solution in the PoC environment to the preproduction environment. This promotion follows version control principles that are similar to code deployment. The goal is to make sure that only stable, validated configurations advance to the next stage. The process emphasizes that prompt tuning and LLM selection should be primarily completed during the PoC stage, and preproduction should focus on infrastructure optimization and deployment tuning. Significant prompt or model alterations should occur in the PoC stage. This shift in focus prevents the common anti-pattern of continuing experimentation in environments designed for stability testing.
+ **Application code deployment and integration **– The core application code orchestrates LLM calls, integrates with other services (such as vector databases for RAG), and handles user interactions. It should undergo structured deployment to the preproduction cloud environment. This code represents the culmination of initial unit and integration testing conducted during the development phase, and it serves as the foundation for more comprehensive system-level testing in preproduction. The deployment process should make sure that all dependencies, service integrations, and orchestration logic are properly configured for the target environment. The application code also needs to maintain compatibility with the promoted prompt and model assets.
+ **Evaluation datasets** **enhancement **– Evaluation datasets, including human-labeled ground truth data developed during the PoC stage, are systematically carried forward to preproduction environments. These datasets serve as the foundation for continued quality assessment. You can strategically extend them with real-world data that you collect from internal user interactions or controlled beta testing programs. This creates an enhanced evaluation dataset that provides more comprehensive coverage of actual usage patterns and edge cases. Importantly, this process includes bidirectional flow capability. The enhanced evaluation datasets can be returned to the PoC environment if performance requirements aren't met during preproduction testing. This supports iterative refinement without losing valuable insights.
+ **Environment configuration and infrastructure setup** – Deployment configurations encompass the complete infrastructure specification required for preproduction operations. This includes cloud resource allocations, security configurations, and operational parameters. This also includes the secure management of API keys, environment variables, and service endpoints that enable proper integration with external systems and services. Infrastructure as code (IaC) templates support consistent environment provisioning and enable repeatable deployments while maintaining security and compliance requirements. The configuration management process establishes the foundation for scalable operations and provides groundwork for the production deployment.

## Centralizing control and observability with AI gateways
<a name="preprod-architecting-gateway"></a>

As generative AI proliferates within an enterprise, leaving individual applications unmanaged can create a chaotic, unsecure, and expensive problem. Each team might use different models, manage API keys insecurely in their code, and have no visibility into costs or security risks. An *AI gateway* is a unified API gateway that streamlines access to multiple LLMs. The role of an AI gateway is to provide governance and security while improving agility, making it easier and faster for your teams to build AI applications.

The following are the key features and benefits of an AI gateway:
+ **Unified authentication and security** – The gateway acts as a single, hardened entry point. It offloads the burden of authentication from individual applications, allowing the enforcement of a uniform, enterprise-wide security mechanism, such as OAuth. It securely manages all backend API keys and prevents them from being scattered across dozens of codebases.
+ **Dynamic load balancing and routing** – A gateway can intelligently distribute requests across multiple model deployments. This can increase overall throughput by load balancing across different AWS Regions because requests per minute (RPM) and tokens per minute (TPM) limits are often Regional. It can also build resilience by routing traffic between different model providers. For example, it can fail over from Amazon Bedrock to self-hosted LLMs.
+ **Centralized quota and cost management** – The gateway can manage complex rate limits (TPM and RPM) for different consumer groups. This prevents any single application from monopolizing resources. It becomes the central point for logging token consumption, which enables accurate cost tracking and departmental chargebacks.
+ **Resilience and fallback strategies** – The gateway can implement sophisticated resilience patterns. A common strategy is called *spillover*, where traffic is primarily routed to a cost-effective, prepurchased provisioned throughput unit (PTU). If that PTU reaches its capacity, the gateway automatically redirects the overflow traffic to a more expensive but elastic pay-as-you-go endpoint. This promotes service continuity during demand spikes.
+ **Centralized observability and logging** – The gateway is the ideal location to log all prompts, responses, latencies, and other performance metrics in a standardized format. You can feed this data directly into the central observability platform.

For more information about generative AI gateways and a solution to deploy an AI gateway on AWS, see [Guidance for Multi-Provider Generative AI Gateway on AWS](https://aws.amazon.com/solutions/guidance/multi-provider-generative-ai-gateway-on-aws/).

### Considerations for AI gateways
<a name="considerations-for-ai-gateways.ecb3c2d0-d523-55f1-817f-fabeb0ff2e6d"></a>

When considering an AI gateway, to assess the needs for your AI eco-system, assess the following security, privacy, compliance, performance, reliability, and monitoring considerations.

#### Authentication
<a name="authentication.0e471a4e-aea0-52ba-a48f-676d0418bba9"></a>

In general, the generative AI application access models through an API and authenticates through an API key. Your AI gateway should support authentication through the API key and securely store those keys. It should also provide a seamless way to integrate with your existing identity provider by using single sign-on (SSO) so that access is integrated with the larger ecosystem. Consider an AI gateway that also supports multiple protocols that are required by foundation models (stateless), MCP servers , and other components of your application. Provide a means to consistently apply the authentication policies for such protocols.

#### MCP and data providers
<a name="mcp-and-data-providers.95d02877-9837-5eaf-a7bd-1fe103dca060"></a>

Modern AI systems have more components than just an LLM. Data enrichment from existing systems makes the model provide more relevant results. As a result, organizations are exposing their data to the model in multiple ways, such as through RAG or MCP. The model might be hosted outside of your organization; therefore, adherence to the principle of least privilege becomes more critical. Your AI gateway should secure components and other data systems that the model accesses, and it must also secure the agentic applications and the associated access logs.

#### Fine-grained access control
<a name="fine-grained-access-control.02997f78-f5c2-5ee3-a04e-807432859645"></a>

Because the AI gateway is a central access point, it should separate authentication and tracking mechanisms based on association with groups or teams. This helps you manage multiple access policies that are suitable for different teams. Your gateway shall provide a way to manage different access policies to different set of users.

#### Guardrails
<a name="guardrails.5077a7a3-500e-596d-8807-5c8400a53c1a"></a>

LLMs hallucinate, and you need control of the output they generate based on your business rules. Your gateway should provide a central point to capture outputs from LLMs and apply your guardrails in order to adhere to your organization's policies. Consider a gateway that allows data teams to write guardrails with ease, such as with a Python function, for easy integration and fast adoption of new business rules.

#### Auditing
<a name="auditing.7fbd5749-2dc2-50d0-b4e3-9c515b282d87"></a>

For compliance and security, organizations might need to maintain a record of AI interactions. An AI gateway can act as a single point of entry for all LLMs and MCP traffic. It creates a log for every request, and it captures who made the request, which model was used, the full prompt and response, and any guardrails that were triggered. It can also track the cost.

#### Model choice
<a name="model-choice.bd6e3220-e9ea-5b64-a487-19f1eb239082"></a>

As the investment in foundation models grows, more models are becoming available for use in your applications. Open-source models or models from various providers might have their own protocol and formats to access the models. If your applications and teams are accessing multiple models, the time cost of switching between model protocols can become steep. Consider an AI gateway that provides the capability to translate from an open standard, such as OpenAI API, to any other protocol. This can simplify applications and help your team test and experiment with new models.

#### Cost control and chargebacks
<a name="cost-control-and-chargebacks.3dfbc4df-2878-5abc-8f0d-70588e8eac31"></a>

The financial governance of AI is fundamentally different from traditional APIs. Consider an AI gateway that provides cost controls based on AI-native metrics. Examples include token-based rate limiting and budget enforcement based on model price and token usage.

#### Dynamic routing
<a name="dynamic-routing.cb66d14e-1516-527b-b2f5-0239f44c207d"></a>

An AI gateway can serve as a control plane for model orchestration. It can address key challenges, such as resource availability and performance. Through intelligent routing strategies, the AI gateway can analyze incoming requests and route them to more appropriate models. There are different approaches to implementing a routing strategy. For example, you can use rule-based routing (such as time-based routing to use off-peak capacity) and more sophisticated semantic routing. Semantic routing might include *content-type intelligent routing* (where the AI gateway analyzes the content and intent of queries to determine the most appropriate model for each task) or *complexity-based smart routing* (where the gateway evaluates the complexity and sophistication required for each request before selecting the appropriate model).

#### Monitoring and alerting
<a name="monitoring-and-alerting.29c6010d-7936-5ab1-ad48-70daf5dc351e"></a>

A primary challenge in operating AI systems is the need for specialized monitoring to validate performance and reliability. Consider an AI gateway that captures LLM-specific interactions and sends alerts if things have gone wrong, such as slow responses. For seamless integration into an existing customer environment, the gateway must be able to export these metrics to the organization's established observability and incident management tools.

## Designing generative AI applications for performance and cost
<a name="preprod-architecting-performance-cost"></a>

During the PoC stage, performance and cost are often secondary concerns. They are overshadowed by the drive to simply make the technology work. In preproduction, they become primary architectural drivers that influence every design decision. An application that is too slow or too expensive fails in production, regardless of how impressive its outputs are.

### Latency reduction
<a name="latency-reduction.93673eef-83ed-5f80-b55a-176f1dba6dbb"></a>

Latency reduction in generative AI applications is crucial because users expect natural, real-time interactions. Additionally, lower latency often means more efficient resource usage, reducing costs for both providers and users. The following are latency reduction strategies:
+ **Use streaming** – For applications with long-form text generation, waiting for the entire response can lead to a poor user experience. *Streaming*, where partial responses are sent to the UI as they are generated, dramatically improves the perceived speed of the application.
+ **Smart caching** – Many user queries are repetitive. You can implement a caching layer in the AI gateway that stores and serves results for identical or semantically similar queries. This can significantly reduce both latency and cost.
+ **Right-sized models** – A common mistake is to use the most powerful model, which is often the most expensive and slowest, for every task. A more sophisticated approach is to use a chain of models. A simple, fast, and cheap model can handle most requests. If it fails or lacks confidence in its answer, the request is escalated to a more powerful and expensive model. This tiered approach optimizes the trade-off between performance, cost, and quality.

### Cost modelling
<a name="cost-modelling.1b1a0162-152d-559f-bf18-759dd0ea9334"></a>

The preproduction stage must begin with the creation of a detailed cost model. This is not a rough estimate. It is a living document that is continuously updated and validated as the application is tested. The model should break down costs by the following categories:
+ Estimated query volume and patterns, such as daily peaks
+ For each type of query, the average token usage for both the prompt and completion
+ The cost per token for the selected LLMs
+ The cost of the underlying cloud infrastructure, such as compute for hosting, vector database storage and queries, and guardrails

Every architectural decision—from the choice of vector database to the selection of a foundation model—must be evaluated against this cost model. This practice forces the team to make conscious, data-driven trade-offs and provides the business with a predictable cost forecast for the production deployment.
