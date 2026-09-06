---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/capabilities.html
---

# Capabilities
<a name="capabilities"></a>

In addition to the [general-purpose AWS knowledge and API tools](understanding-mcp-server-tools.md), AWS MCP Server provides capabilities. A capability groups a set of helper functions that work together to handle a specific kind of AWS task. This document describes the capabilities that AWS MCP Server provides and what they do.

**Note**
Your agent discovers the relevant capability for a task and invokes its helper functions automatically through AWS MCP Server with no manual setup required. As a best practice, describe the outcome you want (for example, "find out why this AWS Lambda function is failing"), and let your agent select the appropriate tools.

AWS MCP Server provides a serverless capability that helps you troubleshoot your running Lambda functions and their connected resources.

## Serverless capability
<a name="aws-serverless-capability"></a>

The serverless capability helps coding and operational agents debug AWS serverless applications. It answers questions such as "Why is this Lambda function failing?", "Did anything change before the outage?", and "Is the issue in code, config, or an AWS dependency?" It provides a set of serverless-aware helper functions that return structured data your agent can use to diagnose and resolve issues.

The capability is scoped to the caller's own account and is read-only. It inspects the Lambda function and its connected resources, and can diagnose the following connected resource types:
+ [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) (including per-index Global Secondary Indexes)
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) (REST and HTTP)
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

The serverless capability provides the following helper functions.
+ `diagnose` – Returns a combined health check and rule-based diagnosis for a Lambda function and its connected resources in a single call. This includes current health status, metrics compared against a 7-day baseline to surface anomalies, detection of Lambda triggers and destinations, and root cause analysis correlated across the connected resources to identify the likely source of failure (for example, "DynamoDB throttling is causing Lambda invocation errors"). This gives your agent a starting point for resolution without requiring separate log, trace, and configuration inspection for every investigation.
+ `search_logs` – Retrieves recent log evidence for a Lambda function from Amazon CloudWatch Logs. The response groups log messages into common exception types and representative error lines, producing a structured summary for agents to consume. This surfaces recurring exceptions and failure patterns without overwhelming the agent's context window.
+ `get_live_config` – Returns the deployed configuration of a Lambda function and its connected resources, using consistent structure and field names across resource types. This covers runtime, memory, timeout, concurrency, event source mappings, and connected-resource settings. Use it to catch configuration drift (for example, a timeout that is too low, exhausted reserved concurrency, an SQS visibility timeout mismatch, or a missing dead-letter queue) or to confirm that a deployment took effect.
+ `get_recent_changes` – Returns a timeline of recent deployments and configuration changes for a Lambda function and its connected resources, sourced from AWS CloudTrail, Lambda APIs, and AWS CloudFormation. Each entry shows who made the change, which settings changed, and their previous and new values. If the function was deployed as part of an AWS CloudFormation stack, the timeline also includes that stack's deployment events. Use it to answer "what changed before the Lambda function broke?"
+ `get_trace_summary` – Summarizes recent [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) traces to show where a Lambda function's latency and errors originate. X-Ray records the duration of each step in an invocation, including calls to downstream services. This helper function samples traces from a recent time window (the last 30 minutes by default) and identifies the downstream calls with the highest latency and error counts (for example, "DynamoDB Query is consuming 24 seconds of a 30-second Lambda invocation"). For this helper function to return results, X-Ray tracing must be enabled on the function.
