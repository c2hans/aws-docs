---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/cost.html
---

# Cost
<a name="cost"></a>

With this AWS Solution, you pay only for the resources you use and there are no minimum fees or setup charges. Users pay for the dashboard used to launch Generative AI use cases and, and for any use cases that are deployed. The cost of deployed use cases depends on the configurations. Example configurations:

1. A simple Deployment dashboard which costs approximately $20 USD per month.

1. A simple production-ready chatbot use case deployed with default settings running in US East (N. Virginia), powered by Amazon Bedrock without access to documents, which also costs around $200 USD per month.

1. A scaled system in an Amazon VPC use case that supports 8,000 queries per day over tens of thousands of documents, which costs around $1,500 USD per month. The cost of the use case will vary depending on the configuration, such as Text use cases with different model providers, with or without Retrieval Augmented Generation (RAG) enabled, and so on.

| Workload description | Estimated cost (USD/month) |
| --- | --- |
|  [Sample cost for Deployment dashboard](#sample-deployment-dashboard-cost)  | $20/month |
|  [Sample costs for a text-based proof of concept](#sample-costs-for-a-text-based-proof-of-concept) <br />(includes Deployment dashboard and 1 Text use case, \~100 interactions per day) | $40/month |
|  [Sample costs for a highly scalable generative AI query engine](#sample-costs-for-a-highly-scalable-generative-ai-query-engine) <br />(Includes Deployment dashboard, 1 Text use case, and an Amazon Kendra Index for RAG up to 100K documents with \~8K queries per day, with [VPC enabled](#incremental-cost-of-enabling-amazon-vpc-for-a-use-case)  | $1,500/month |
|  [Sample costs for an agent-based proof of concept](#sample-costs-for-an-agent-based-proof-of-concept) <br />(Includes Deployment dashboard, 1 Bedrock Agent use case with Amazon Bedrock Knowledge Bases and Amazon Bedrock Guardrails enabled, \~100 interactions per day) | $840/month |
|  [Sample costs for MCP Server](#sample-costs-for-mcp-server) <br />(Includes Deployment dashboard, 1 MCP Server use case with Gateway method for Lambda integration, \~100 tool invocations per day) | $22/month |
|  [Sample costs for Agent Builder](#sample-costs-for-agent-builder) <br />(Includes Deployment dashboard, 1 Agent Builder use case with MCP integration and long-term memory enabled, \~100 interactions per day) | $55/month |
|  [Sample costs for Workflow Builder](#sample-costs-for-workflow-builder) <br />(Includes Deployment dashboard, 1 Workflow with 3 Agent Builder agents, \~100 interactions per day) | $109/month |

**Important**
These examples are only intended to help you estimate the costs for your specific workloads. The use of different LLMs, configurations, or AWS services can change your costs (example, serverless/on-demand billing vs. provisioned/time-billed). To manage costs, we recommend [creating a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/). Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Sample costs for running the Deployment dashboard
<a name="sample-deployment-dashboard-cost"></a>

The following table provides the cost breakdown for a Deployment dashboard with default parameters and 100 active users in the US East (N. Virginia) Region for one month, which will cost about $20/month.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway, DynamoDB, CloudFront, Amazon S3, Lambda, Systems Manager Parameter Store | 5,000 512 KB REST API calls per month without caching enabled | $1.97 |
| Amazon Cognito | 100 active users per month with advanced security features enabled and no users signing in through SAML or OIDC federation | $5.55 |
| AWS WAF | 10,000 web requests across 1 web ACL and 7 defined rules without any rule groups | $12.60 |
| Total Deployment dashboard cost |  |  **$20.12**  |

## Sample costs for a text-based proof of concept
<a name="sample-costs-for-a-text-based-proof-of-concept"></a>

A Deployment dashboard can have many use cases deployed at a given time. The following table shows the cost breakdown of a use case deployed without RAG for 1 business user performing 100 queries per day with the LLM. Queries are sent as a text message on the WebSocket and the response is streamed back as tokens with the assumption that streaming is enabled. Using the Amazon Bedrock Nova Pro model, the cost of running this use case is about $20/month.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway (WebSocket), CloudFront, Lambda, Amazon S3, AWS Systems Manager Parameter Store | 100 chat interactions per day. Average message size 32 KB per message and 5 minutes per connection. | $0.61 |
| CloudWatch | 1.5 GB CloudWatch logs with verbose mode on for experimentation | $7.23 |
| Amazon DynamoDB | Conversation history table, 1 GB storage<br />LLM configuration table, 1 GB storage | $3.05 |
|  **Subtotal of the use case costs (not including LLMs)**  |  |  **$10.89**  |
| Amazon Bedrock (Nova Pro) | Assumptions for 100 interactions per day:<br />\* Monthly cost for 190K input tokens per day = $0.152 × 30 \* Monthly cost for 16K output tokens per day = $0.0512 × 30 | $6.10 |
|  **Total application cost with Amazon Bedrock (Nova Pro)**  |  **$10.89 (Use Case cost) \+ $6.10 (Amazon Bedrock cost)**  |  **$17.00**  |

**Note**
The costs of inference calls made to services outside the AWS network are not included in these estimates. Refer to the pricing guide of your LLM provider if you’re not using an AWS model provider.
Pricing guides for AWS services can be found at: [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) and [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/).

## Sample costs for a highly scalable generative AI query engine
<a name="sample-costs-for-a-highly-scalable-generative-ai-query-engine"></a>

The following table provides the cost breakdown of a RAG-enabled use case with Amazon Bedrock’s Nova Pro model as the LLM. When a Bedrock Knowledge Base is added, this use case costs about $1300/month

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway (WebSocket) | 8000 chat interactions per day. Average message size 32 KB per message and 5 minutes per connection. | $38.89 |
| CloudFront | 240,000 requests per month with 100 GB data transferred out to the internet and 1 GB data transferred out to the origin | $8.76 |
| Amazon Bedrock (Nova Pro) | Assumptions:<br />Input tokens = promptTemplate (400) \+ context (400)\+ chatHistory (1080) \+ query Input tokens (20)= 1,900<br />Output tokens = 160 (average)<br />With 8,000 transactions a day,<br />Daily Input Tokens cost (1,900 x 8,000 = 15,200,000 tokens x 0.0008/1000 price per token)<br />Daily Output Tokens cost (160 x 8,000 = 1,280,000 tokens x 0.0032/1000 price per token)<br />Monthly cost (($12.16 \+ $4.10) x 30) | $487.80 |
| CloudWatch | 24 metrics using 5 GB data ingested for logs and 1 dashboard | $9.72 |
| DynamoDB | DynamoDB table to keep track of conversation history with each record up to 1 KB data, 8,000 read and writes per day | $11.70 |
| Lambda | Container size - 128 MB, 512 MB ephemeral<br />storage, 2 Lambda functions used for authorization<br />Container size - 256 MB, 512 MB ephemeral storage, 5 requests per second with 20 seconds average compute time | $20.89 |
|  **Total use case cost**  |  |  **$577.76/month \+ knowledge base cost (see below)**  |

**Note**
The costs of API calls made to any services outside of the AWS network are not included in these estimates. See the pricing guide of your LLM provider if not using Amazon Bedrock.

## Costs for adding a knowledge base
<a name="cost-of-adding-a-knowledge-base"></a>

Knowledge base costs will vary based on the type of knowledge base used, and (in the case of Bedrock) the backing vector store used by the knowledge base. Provisioning and managing the knowledge bases is outside of the scope of the solution.

 **Amazon Bedrock Knowledge Bases**

The solution does not manage or provision any resources related to Amazon Bedrock Knowledge Bases. Amazon Bedrock does not incur cost for using the knowledge base feature itself, however you will be charged for the usage of the embedding model used by your use case on each query. Additionally, the backing vector store for your knowledge base (for example, an index in [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service), or a database inside Amazon Relational Database Service) will have an associated cost which cannot be provided or calculated here.

For the above highly scalable generative AI query engine scenario, the costs incurred by this service for calling the Amazon Bedrock embeddings model are as follows:

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon Bedrock (Amazon Titan Text Embeddings V2) | 8,000 queries a day with 1,900 input tokens per query = 15,200,000 tokens = $0.30 USD per day.<br />Daily cost x 30 days = $9.00 USD monthly cost | $9.00 |
| Amazon OpenSearch Service (Serverless) Sample Usage | Basic serverless configuration with 4 x OpenSearch Compute Unit (OCU) (billable minimum) = $23.04 USD per day<br />Daily cost x 30 days = $691.20 USD This provides a rough estimate, as some workloads will require more OCUs, while customers with existing provisioned OpenSearch resources will incur less cost here.  | $691.20 |
|  **Total additional cost**  |  | $ 700.20 |

 **Amazon Kendra**

The solution can provision a Kendra index for you, or you can bring your own. The cost for running a configuration suited to the above highly scalable generative AI query engine is as follows:

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon Kendra | 0-8,000 queries a day and up to 100,000 documents with Amazon Kendra Enterprise Edition with 0-50 data sources | $1,008.00 |

**Note**
You can share the Amazon Kendra index between use cases, but this can drive up the number of queries per index. If this falls outside the Amazon Kendra Enterprise edition, additional charges will apply.

## Incremental cost of enabling Amazon VPC for a use case
<a name="incremental-cost-of-enabling-amazon-vpc-for-a-use-case"></a>

The following table provides the cost breakdown of enabling Amazon VPC for a use case deployed in two AZs.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon NAT Gateway | Assumption: 2 AZ deployment, with a NAT Gateway in each AZ. 100 GB of data processed through NAT Gateway 730 hours, 100 GB data processed per month | $74.70 |
| AWS PrivateLink (VPC Endpoints) | Assumptions: 2 AZ deployment, with 1 private subnet in each AZ and 1 VPC Endpoint with 2 elastic network interfaces (ENIs).<br />6 VPC endpoints, 2 ENIs per VPC endpoint, 730 hours with 1,024 GB data processed in a month | $97.84 |
| Public IPv4 address | Assumption: 2 AZ deployment, 1 public subnet in each AZ with a NAT Gateway in each public subnet. Each NAT Gateway configured with 1 active public IPv4.<br />2 active public IPv4 address x 730 hours in a month x $0.005 hourly charge = $7.3 USD | $7.30 |
| Additional cost<br />(for Amazon VPC) |  |  **$179.93**  |

## Cost implications when using Provisioned Throughput
<a name="cost-implications-when-using-provisioned-throughput"></a>

Provisioned throughput costs will vary based on the type of model you’ve provisioned and your commitment period as well as Model Units selected for the commitment period. There is an additional cost associated with using Provisioned Throughput.

For more information and the most up-to-date pricing, you can refer to [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/).

## Cost for using cross-region inference
<a name="cost-for-using-cross-region-inference"></a>

There is no additional cost for routing or data transfer for using [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). You pay the same price per token for models as in your source or primary Region.

## Sample costs for an agent-based proof of concept
<a name="sample-costs-for-an-agent-based-proof-of-concept"></a>

When you use Amazon Bedrock Agents, you’re charged based on the components comprising the agent, such as the backing model and knowledge base (if RAG is enabled), along with additional capabilities that you add. The following table shows the cost breakdown of a Bedrock Agent use case configured with an on-demand Claude 3.5 Sonnet model, Amazon Bedrock Knowledge Bases, and Amazon Bedrock Guardrails.

Similar to the [cost for adding Amazon Bedrock Knowledge Bases](#cost-of-adding-a-knowledge-base), this solution doesn’t manage or provision resources related to Amazon Bedrock Agents. The solution also doesn’t incur cost for using Amazon Bedrock Knowledge Bases, but does incur cost for:
+ Using the embedding model for each query that is sent to it
+ The backing vector store for your knowledge base (for example, an index in Amazon OpenSearch Service, or a database inside Amazon RDS)

The following table assumes 100 interactions per day with 1,900 input tokens and 160 output tokens per query.

**Note**
For this sample Bedrock Agent use case, if there were an action group configured to use an external API, those costs would be additional. They are outside the scope of the calculations in this table.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway (WebSocket), CloudFront, Lambda, Amazon S3, Systems Manager Parameter Store | 100 chat interactions per day, average message size 32 KB per message, 5 minutes per connection | $0.61 |
| CloudWatch | 1.5 GB CloudWatch Logs with verbose mode on for experimentation | $7.23 |
| DynamoDB | LLM configuration table for 1KB record size and 1 GB storage | $0.25 |
|  **Subtotal of costs (not including LLMs)**  |  |  **$8.09**  |
| Anthropic Claude 3.5 Sonnet | \* Daily cost for 190K input tokens per day (0.003/1,000 tokens) = $0.57 \+<br />Daily cost × 30 days = $17.10 \* Daily cost for 16K output tokens per day (0.015/1,000 tokens) = $0.24 \+<br />Daily cost × 30 days = $7.20 | $24.30 |
| Amazon Bedrock (Amazon Titan Text Embeddings V2) for Amazon Bedrock Knowledge Bases | Daily cost for 190K input tokens per day (0.00002/1000 tokens) = 0.004<br />Daily cost × 30 days = $0.12 | $0.12 |
| Amazon OpenSearch Service (Serverless) sample usage | Basic serverless configuration with 4 × OpenSearch Compute Unit (OCU) (billable minimum) = $23.04 per day<br />Daily cost × 30 days = $691.20 | $691.20 |
| Amazon Bedrock Guardrails | 190K tokens is roughly equivalent of 760K (190,000 × 4) characters and 3,800 text units (760K characters / 200)<br />Consider a guardrail configured with content filters, personally identifiable information (PII) filter, sensitive information filter (regular expression) and word filters<br />Daily content filter cost (0.75/1000 text units) \+ PII filter cost ($0.1/1000 text units) \+ sensitive information filter (regex) \+ word filters = $2.85 \+ $0.38 \+ $0 \+ $0<br />Monthly cost = Daily cost × 30 days = $96.90 | $96.90 |
|  **Total application cost for an agent backed by Anthropic Claude 3.5 Sonnet**  |  *$8.09 (use case cost) \+* **$812.52 (other agent configurations)**  | $820.61 |

**Note**
Refer to the pricing guide of your LLM provider if you’re not using an AWS model provider. Pricing guides for AWS services can be found at: [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) and [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/).

## Sample costs for MCP Server
<a name="sample-costs-for-mcp-server"></a>

MCP Server use cases enable deployment and management of Model Context Protocol servers on Amazon Bedrock AgentCore. The following table shows the cost breakdown of an MCP Server use case using the Gateway method to wrap existing Lambda functions.

The solution manages the AgentCore Gateway deployment and configuration. You’re charged for:
+ Infrastructure costs (API Gateway, Lambda, DynamoDB, CloudWatch, S3)
+ AgentCore Gateway consumption (per tool invocation)
+ Lambda function execution costs (for Gateway method with Lambda targets)
+ External API costs (for Gateway method with API or MCP Server targets, if applicable)

| Item | Calculations | Cost |
| --- | --- | --- |
| Amazon API Gateway (REST API) | 100 tool invocations per day × 30 days = 3,000 requests per month | $0.05 |
| AWS Lambda (orchestration) | 100 invocations per day × 30 days × 1 second average × 512 MB = 3,000 GB-seconds per month | $0.05 |
| Amazon DynamoDB | 3,000 read/write requests per month \+ 1 GB storage | $0.15 |
| Amazon CloudWatch | Standard monitoring and logging for 3,000 invocations | $1.00 |
| Amazon S3 | Configuration storage and logs (minimal usage) | $0.25 |
| Amazon Bedrock AgentCore Gateway | 3,000 tool invocations per month | $0.05 |
| Target Lambda Function | 100 invocations per day × 30 days × 0.5 seconds × 128 MB = 1,500 GB-seconds per month | $0.25 |
|  **Total monthly cost**  |  *$1.75 (infrastructure) \+ $0.05 (AgentCore Gateway)*  | $1.80 |

**Note**
Costs vary based on deployment method (Gateway vs Runtime), target types, and usage patterns. Runtime method deployments incur AgentCore Runtime charges instead of Gateway charges. External API costs and custom container hosting costs are additional.

## Sample costs for Agent Builder
<a name="sample-costs-for-agent-builder"></a>

Agent Builder enables you to create and deploy custom agents on Amazon Bedrock AgentCore. The following table shows the cost breakdown of an Agent Builder use case configured with Claude 3.5 Sonnet, MCP server integration, and long-term memory enabled.

The solution manages the AgentCore Runtime deployment and configuration. You’re charged for:
+ Infrastructure costs (API Gateway, Lambda, DynamoDB, CloudWatch, S3)
+ AgentCore Runtime consumption (CPU and memory hours based on actual agent execution time)
+ Foundation model inference (input and output tokens)
+ AgentCore Memory (short-term events and long-term storage/retrieval)

The following table assumes 100 interactions per day with 1,900 input tokens and 160 output tokens per query, with an average agent execution time of 5 seconds per interaction.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway (WebSocket), CloudFront, Lambda, Amazon S3, Systems Manager Parameter Store | 100 chat interactions per day, average message size 32 KB per message, 5 minutes per connection | $0.61 |
| CloudWatch | 1.5 GB CloudWatch Logs with verbose mode on for experimentation | $7.23 |
| DynamoDB | LLM configuration table for 1KB record size and 1 GB storage | $0.25 |
|  **Subtotal of infrastructure costs**  |  |  **$8.09**  |
| Amazon Bedrock AgentCore Runtime | \* CPU: 1 vCPU × 5 seconds × 100 interactions = 125 vCPU-seconds/day = 0.140 vCPU-hours/day \+ Daily cost: 0.140 × $0.0895 = $0.013 \+ Monthly cost: $0.013 × 30 = $0.38<br />\* Memory: 512 MB (0.5 GB) × 5 seconds × 100 interactions = 250 GB-seconds/day = 0.069 GB-hours/day \+ Daily cost: 0.069 × $0.00945 = $0.0007 \+ Monthly cost: $0.0007 × 30 = $0.02 | $0.40 |
| Anthropic Claude 3.5 Sonnet | \* Daily cost for 190K input tokens per day (0.003/1,000 tokens) = $0.57 \+ Daily cost × 30 days = $17.10<br />\* Daily cost for 16K output tokens per day (0.015/1,000 tokens) = $0.24 \+ Daily cost × 30 days = $7.20 | $24.30 |
| Amazon Bedrock AgentCore Memory | \* Short-term memory: 100 new events/day × $0.25/1,000 events = $0.025/day \+ Monthly cost: $0.025 × 30 = $0.75<br />\* Long-term memory storage (built-in strategy): 100 records × $0.75/1,000 records/month = $0.075/month<br />\* Long-term memory retrieval: 100 retrievals/day × $0.50/1,000 retrievals = $0.05/day \+ Monthly cost: $0.05 × 30 = $1.50 | $2.33 |
|  **Total application cost for Agent Builder with Claude 3.5 Sonnet**  |  *$8.09 (infrastructure) \+ $0.40 (AgentCore Runtime) \+ $24.30 (model) \+ $2.33 (memory)*  |  **$35.12**  |

**Note**
AgentCore Runtime pricing is consumption-based. Actual costs depend on:
Agent execution time (CPU and memory usage during active processing)
Number of interactions and their complexity
MCP tool usage (additional CPU/memory for tool execution)
Memory configuration (short-term vs. long-term memory enabled)
For detailed AgentCore pricing, refer to [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

**Note**
If using MCP servers that invoke external APIs or services, those costs are additional and outside the scope of this calculation. Similarly, if using AgentCore Browser or Code Interpreter tools, consumption-based charges apply at $0.0895 per vCPU-hour and $0.00945 per GB-hour.

## Sample costs for Workflow Builder
<a name="sample-costs-for-workflow-builder"></a>

Workflow Builder creates a supervisor agent that orchestrates multiple Agent Builder agents. The following table shows the cost breakdown for a workflow with 1 supervisor agent and 3 specialized Agent Builder agents, all configured with Claude 3.5 Sonnet and long-term memory enabled.

Assumptions: 100 interactions per day, average 2 agent delegations per interaction, 5 seconds execution time per agent.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| API Gateway (WebSocket), CloudFront, Lambda, Amazon S3, Systems Manager Parameter Store | 100 chat interactions per day, average message size 32 KB per message, 5 minutes per connection | $0.61 |
| CloudWatch | 1.5 GB CloudWatch Logs with verbose mode on for experimentation | $7.23 |
| DynamoDB | LLM configuration table for 1KB record size and 1 GB storage | $0.25 |
|  **Subtotal of infrastructure costs**  |  |  **$8.09**  |
| Amazon Bedrock AgentCore Runtime (Supervisor Agent) | \* CPU: 1 vCPU × 5 seconds × 100 interactions = 0.140 vCPU-hours/day × 30 = $0.38 \* Memory: 0.5 GB × 5 seconds × 100 interactions = 0.069 GB-hours/day × 30 = $0.02 | $0.40 |
| Amazon Bedrock AgentCore Runtime (3 Specialized Agents) | \* Average 2 delegations per interaction = 200 agent executions/day \* CPU: 1 vCPU × 5 seconds × 200 = 0.278 vCPU-hours/day × 30 = $0.75 \* Memory: 0.5 GB × 5 seconds × 200 = 0.139 GB-hours/day × 30 = $0.04 | $0.79 |
| Anthropic Claude 3.5 Sonnet (Supervisor Agent) | \* Input: 190K tokens/day × $0.003/1K = $0.57/day × 30 = $17.10 \* Output: 16K tokens/day × $0.015/1K = $0.24/day × 30 = $7.20 | $24.30 |
| Anthropic Claude 3.5 Sonnet (Specialized Agents) | \* Average 2 delegations per interaction \* Input: 380K tokens/day × $0.003/1K = $1.14/day × 30 = $34.20 \* Output: 32K tokens/day × $0.015/1K = $0.48/day × 30 = $14.40 | $48.60 |
| Amazon Bedrock AgentCore Memory (Supervisor Agent) | \* Short-term: 100 events/day × $0.25/1K × 30 = $0.75 \* Long-term storage: 100 records × $0.75/1K = $0.08 \* Long-term retrieval: 100 retrievals/day × $0.50/1K × 30 = $1.50 | $2.33 |
| Amazon Bedrock AgentCore Memory (Specialized Agents) | \* Short-term: 200 events/day × $0.25/1K × 30 = $1.50 \* Long-term storage: 200 records × $0.75/1K = $0.15 \* Long-term retrieval: 200 retrievals/day × $0.50/1K × 30 = $3.00 | $4.65 |
|  **Total application cost for Workflow Builder with 3 agents**  |  *$8.09 (infrastructure) \+ $1.19 (AgentCore Runtime) \+ $72.90 (models) \+ $6.98 (memory)*  |  **$89.16**  |

**Note**
Higher delegation rates increase token consumption proportionally
For detailed AgentCore pricing, refer to [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
