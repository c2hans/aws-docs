---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/designing-agentic-workflows-on-aws.html
---

# Designing agentic workflows on AWS

Each pattern in this guide can be built using AWS services. Amazon Bedrock agents provide orchestration, data access, and interaction channels.

|
|
| Component | AWS service | Purpose |
| --- |--- |--- |
| LLM reasoning | Amazon Bedrock | Agent logic, planning, tool use |
| Tool execution | AWS Lambda, Amazon ECS, Amazon SageMaker | Host external tools for agents |
| Memory and RAG | Amazon Bedrock knowledge base, Amazon S3, OpenSearch | Persistent and semantic memory |
| Orchestration | AWS Step Functions | Multistep task and agent coordination |
| Event routing | Amazon EventBridge, Amazon SQS | Decoupled interagent messaging |
| User interface | Amazon API Gateway, AWS AppSync, SDK | Entry points for applications or systems |
| Monitoring | Amazon CloudWatch, AWS X-Ray, AWS Distro for OpenTelemetry | Observability and agent introspection |
