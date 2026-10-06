---
source_url: https://docs.aws.amazon.com/solutions/agentic-live-ops-on-aws/index.html
---

---
title: 'Guidance for Agentic Live Ops on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-live-ops-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Agentic Live Ops on AWS

## Overview

This Guidance helps game operators gain real-time operational insights and automate incident analysis by using AI-powered agents that answer natural language questions with data-driven responses, charts, and citations. A multi-agent system routes queries to specialized agents that access structured data, pre-computed summaries, and live metrics to deliver answers streamed in real time. The monitoring pipeline continuously ingests game telemetry events, detects anomalies against configurable thresholds, and automatically triggers AI-powered root cause analysis when issues arise. You can integrate third-party data sources by providing schema definitions, allowing the system to adapt to your specific operational data landscape and deliver comprehensive analytics across all your game infrastructure.

## Benefits

### Query live ops with natural language

Enable your game operators to investigate player metrics, diagnose incidents, and explore telemetry data through conversational AI, eliminating the need for SQL expertise or engineering support.

### Detect and diagnose issues automatically

Reduce mean time to detection and resolution with automated anomaly detection and AI-powered root cause analysis that triggers the moment configurable thresholds are breached.

### Unify fragmented game data sources

Connect your existing data systems, including third-party platforms like Databricks and Snowflake, into a single AI-accessible layer with automated schema discovery and knowledge base indexing.

## How it works

### High Level Overview

Natural language queries routed through a multi-agent system to structured data, knowledge bases, and live metrics.

[Download the architecture diagram](downloads/agentic-live-ops-on-aws.pdf)Step 1Game operators use a React SPA. Game servers emit telemetry events into the monitoring pipeline.

Step 2Amazon CloudFront serves the app from Amazon Simple Storage Service with AWS WAF protection. Amazon Cognito authenticates users and provides SigV4 credentials. A regional AWS WAF ACL protects the Amazon Cognito endpoint.

Step 3Four AWS Lambda Function URLs handle Stream, Monitor, Conversations, and Config. Stream invokes Amazon Bedrock AgentCore in a private-isolated VPC. An orchestrator routes to eight sub-agents. Amazon Bedrock Guardrails filter prompt attacks. Amazon Bedrock AgentCore Memory tracks per-user context. Amazon DynamoDB stores all operational state.

Step 4Three Amazon Bedrock Knowledge Bases on Amazon Simple Storage Service Vectors serve analytics summaries, remediation playbooks, and schema docs. Amazon Athena queries tables via AWS Glue. Amazon Kinesis Data Streams ingests game events. A Pattern Detector Lambda evaluates threshold rules against sliding-window metrics in DynamoDB. Breaches trigger an Analysis Runner Lambda for AI root cause analysis. Amazon Data Firehose archives events to Amazon S3 for Athena queries.

Step 5Amazon Simple Storage Service holds schema definitions. AWS Lambda and Amazon EventBridge are triggered to summarize schema definitions which are hydrated into Amazon Neptune Serverless to assist with NL2SQL via Amazon Athena.

### Chat / AI Analytics

Natural language queries routed through a multi-agent system to structured data, knowledge bases, and live metrics.

[Download the architecture diagram](downloads/agentic-live-ops-on-aws.pdf)Step 1Users access the React app via Amazon CloudFront with AWS WAF protection. Static assets served from Amazon Simple Storage Service.

Step 2Amazon Cognito authenticates users and provides IAM credentials. Requests signed with AWS Signature V4.

Step 3AWS Lambda Function URLs serve as APIs: Chat (SSE streaming), Monitoring, and Conversations.

Step 4Amazon Bedrock AgentCore Runtime hosts the orchestrator, routing queries to dynamically loaded sub-agents via Agent Factory. Sub-agents query three Amazon Bedrock Knowledge Bases (Analytics, Remediations, Schema) backed by Amazon Simple Storage Service vector storage.

Step 5Amazon DynamoDB stores live metrics, reports, pattern rules, conversations, and agent config cache. Amazon Athena runs SQL queries against structured data in Amazon S3 via AWS Glue Data Catalog (15 tables). Amazon Neptune Serverless stores a schema graph of table/column relationships, queried by the orchestrator via Gremlin for join path discovery.

Step 6Third party data source integration is possible by providing schema definitions through the Schema Discovery Pipeline and new agents pertaining to each data source.

### Real-Time Monitoring Pipeline

Game events flow through Kinesis, are evaluated by pattern detection rules, trigger AI-powered analysis, and archive to S3 for historical queries.

[Download the architecture diagram](downloads/agentic-live-ops-on-aws.pdf)Step 1Game events flow into Amazon Kinesis Data Streams from game clients in real time.

Step 2A Pattern Detector AWS Lambda evaluates configurable threshold rules against sliding-window metrics in Amazon DynamoDB.

Step 3On threshold breach, an Analysis Runner AWS Lambda invokes Amazon Bedrock for AI-powered root cause analysis. Reports stored in DynamoDB.

Step 4Amazon Data Firehose archives raw events to Amazon S3 in 5-minute batches, queryable via Amazon Athena for historical analysis.

### Schema Discovery Pipeline

Schema uploads trigger AI-powered documentation generation, knowledge base indexing, and graph relationship syncing.

[Download the architecture diagram](downloads/agentic-live-ops-on-aws.pdf)Step 1Operators upload raw schema files (SQL, JSON, text) to Amazon Simple Storage Service. An S3 event notification triggers processing.

Step 2A Schema Agent Lambda uses Amazon Bedrock Claude to parse schemas and generate standardized markdown documentation, saved to Amazon S3.

Step 3A daily Amazon EventBridge rule triggers a Hydration AWS Lambda that re-indexes the Schema Amazon Bedrock Knowledge Base and syncs table/column relationships to Amazon Neptune.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-live-ops-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
