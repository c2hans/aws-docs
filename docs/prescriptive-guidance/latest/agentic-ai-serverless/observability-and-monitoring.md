---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.html
---

# Observability and monitoring
<a name="observability-and-monitoring"></a>

Observability is essential for operating event-driven, AI-powered systems at scale. Unlike monolithic applications, serverless and generative AI systems are distributed, stateless, and composed of ephemeral compute and integrated AI services (for example, Amazon Bedrock and Amazon SageMaker). These characteristics require new thinking around visibility, correlation, and accountability.

Without observability, teams face the following issues:
+ Blind spots in execution and agent behavior
+ Undetected cost anomalies or performance regressions
+ Limited insight into model outputs and large language model (LLM) quality
+ Difficulty in root-cause analysis across asynchronous workflows

Observability plays a critical role in the following areas of serverless AI:
+ **AI outputs** – LLMs are non–deterministic. Logging and inspecting their outputs is the only way to validate their correctness over time.
+ **Serverless execution** – AWS Lambda, AWS Step Functions, and Amazon EventBridge don't run on fixed hosts. Monitoring needs to be trace-based, not server-based.
+ **Costs and latency** – Amazon Bedrock usage is based on tokens. Lambda and Step Functions are charged per duration and execution.
+ **Security and governance** – Prompt logs, agent tool usage, and API calls must be audited and scoped to identity and role context.
+ **User experience** – Failures, delays, or hallucinations impact trust. Early detection of these issues is key to maintaining user confidence in AI systems.

## Key observability metrics to monitor
<a name="key-observability-metrics-to-monitor.114c1725-208a-55cb-a718-210d8e9d74a5"></a>

The following table describes the importance of key metrics related to observability and monitoring.

|
|
| Metrics category | Metric | Why the metric is important |
| --- |--- |--- |
| Agent behavior | + Tool selection rate<br />+ Invalid tool invocations | Reveals misalignment between intent and action. |
| Cost trends | Inference cost per user or session | Enables FinOps reporting and tiered model routing decisions. |
| Invocation metrics | + Lambda invocations<br />+ Error rate<br />+ Cold starts | Validates pipeline stability and error resilience. |
| Knowledge base retrieval | + Hit/miss ratio<br />+ Grounding relevance score | Measures how well the RAG pipeline is performing. |
| Latency | Inference latency per model | + Detects slowdowns in Amazon Bedrock or SageMaker.<br />+ Optimizes user response time. |
| Prompt and response quality | + Hallucination rate<br />+ Fallback rate | Ensures grounding is working and prompts are behaving as expected. |
| Security and access | Agent and tool usage by IAM role | Ensures principle of least privilege and traceability. |
| Token usage | Total input and output tokens (Amazon Bedrock) | + Controls cost.<br />+ Detects prompt bloat or model misuse. |
| Workflow health | Step Functions workflow failures, retries, and timeouts | Surfaces orchestration issues and retry loops. |

## AWS services for observing serverless and generative AI
<a name="9999999999999999aws-services--for-observing-serverless-and-generative-ai.57a8d9c8-96da-5071-ad01-efe509478bee"></a>

The following table describes AWS services and features that support observability for serverless and generative AI applications, including their ideal use cases.

|
|
| AWS service | Description | Ideal use case |
| --- |--- |--- |
| [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) | Captures logs from Lambda, Step Functions, Amazon Bedrock Agents, and Amazon API Gateway | + Debugging<br />+ Audit trails<br />+ User session tracing |
| [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) | Custom and service-generated key performance indicators (KPIs), such as invocation count, duration, and token count | + Dashboarding<br />+ Alerts <br />+ Trend analysis |
| [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) | Traces across serverless flows, including Lambda, API Gateway, and Step Functions | + Root-cause analysis<br />+ Latency tracking<br />+ Dependency mapping |
| [CloudWatch embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) | Structured logging for advanced metrics in log streams | Enable analytics without separate metrics calls |
| [Amazon Bedrock agent trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) and [model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) | Native Amazon Bedrock Agent execution trace, tool calls, and RAG insights | Monitor agent behavior and troubleshoot failures |
| [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) and [schema registries](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-registry.html) | Tracks and validates event formats flowing through your pipeline | + Prevent malformed events <br />+ Ensure contract consistency |
| [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) | Logs all API calls and identity context | + Compliance<br />+ Security audits<br />+ Agent and tool usage by role |
| [Amazon OpenSearch Service](https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/elasticsearch.html) | Indexes inference responses, structured logs, or audit records | + Semantic search of responses <br />+ Observability dashboards |
| [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) | Simulates traffic to test endpoints or workflows proactively | Ensure uptime and regression monitoring across versions |

## Example: Monitoring an agent-based support workflow
<a name="example--monitoring-an-agent-based-support-workflow.8011dc58-be7c-558c-995d-ca992f75c363"></a>

To effectively monitor an agent-based support workflow, consider using the following metrics at their associated workflow stage:

1. **User query to **API Gateway – Monitor response time and 5xx errors.

1. **Pre-processor Lambda function** – Monitor cold starts and parsing failures.

1. **Amazon Bedrock agent** – Monitor prompt, tool call traces, token cost, and latency.

1. **Tool Lambda function** (for example, `getOrderStatus`) – Monitor execution time and tool invocation count per user.

1. **RAG query through knowledge base** – Monitor relevance score and missing grounding.

1. **Post-processor Lambda function** – Monitor schema validation and fallback triggers.

1. **Logs CloudWatch and OpenSearch** – Monitor session logs, trace IDs, and model response quality.

1. **Alarms** – Monitor alerts for high failure rates, spikes in cost per session, and degraded latency.

## Best practices for observability
<a name="best-practices-for-observability.dbfa7e70-7ebd-5ed7-96e3-d5b7c66dfb5e"></a>

Consider the following best practices for observability in serverless and generative AI workflows:
+ Instrument AI flows with structured logs to enable correlation across components (for example, user session, trace ID, and model response).
+ Use consistent logging schema to support downstream parsing, alerting, and analytics pipelines.
+ Emit custom metrics per layer to help trace model-related errors compared to infrastructure issues.
+ Tag logs with environment and context to enable filtering by user role, region, version, or team.
+ Use anomaly detection alarms to detect token surges, latency spikes, or output drift.
+ Correlate LLM response logs with downstream impact to link agent outputs to decisions, escalations, or failures.
+ Automate report generation through weekly dashboards with prompt cost, model usage, and fallback rates to drive accountability and improvement cycles.

## Summary of observability and monitoring
<a name="summary-of-observability-and-monitoring.d2c2353f-2f98-59d1-a946-67f72643cb1b"></a>

In AI-driven serverless systems, you don't monitor hosts. Instead, you monitor behavior, cost, and correctness. Observability provides the foundation for operational resilience, cost control and forecasting, LLM performance evaluation, governance and compliance, and continuous prompt and agent improvement.

Native AWS services that support observability and monitoring, along with structured, event-aware telemetry provide the necessary capabilities. With these capabilities in place, teams can confidently operate AI workloads at scale, knowing what's happening, where, and why.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
