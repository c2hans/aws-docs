---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/tools-and-services.html
---

# Related AWS services
<a name="tools-and-services"></a>

|
|
| **AWS service** | **Role in this architecture** |
| --- |--- |
| [AWS Organizations](https://aws.amazon.com/organizations/) | Multi-account structure, OU hierarchy, and organizational policy management |
| [AWS Control Tower](https://aws.amazon.com/controltower/) | Account provisioning, guardrails, and landing zone governance |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/) | Foundation model access and inference |
| [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) | Managed agent runtime infrastructure including tool gateway, MCP hosting, memory, and identity |
| [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | Cross-account metrics, logs, and observability dashboards |
| [AWS X-Ray](https://aws.amazon.com/xray/) | Distributed tracing for agent execution paths across service boundaries |
| [Amazon Managed Grafana](https://aws.amazon.com/grafana/) | Unified operational dashboards aggregating data from all source accounts |
| [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) | Metrics aggregation for containerized agent workloads |
| [Amazon GuardDuty](https://aws.amazon.com/guardduty/) | Threat detection across all platform accounts |
| [AWS Security Hub](https://aws.amazon.com/security-hub/) | Centralized security findings and compliance posture management |
| [Amazon Macie](https://aws.amazon.com/macie/) | Sensitive data discovery in conversation logs and agent outputs |
| [Amazon S3](https://aws.amazon.com/s3/) | Data lake storage, RAG knowledge base documents, and conversation logs |
| [AWS Glue](https://aws.amazon.com/glue/) | Data pipeline orchestration between raw and processed data zones |
| [AWS Lake Formation](https://aws.amazon.com/lake-formation/) | Fine-grained access control for data lake datasets |
| [Amazon ECR](https://aws.amazon.com/ecr/) | Shared Docker registry for agent container images |
| [AWS CodePipeline](https://aws.amazon.com/codepipeline/) | CI/CD pipeline orchestration for agent promotion |
| [AWS CodeBuild](https://aws.amazon.com/codebuild/) | Build, test, and deployment execution within the pipeline |
| [AWS PrivateLink](https://aws.amazon.com/privatelink/) | Secure cross-account service connectivity without public internet traversal |
| [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) | Network connectivity for landing zone integration |
| [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) | Cost monitoring and alerting at account and OU level |
| [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) | Centralized human access management across all platform accounts |
| [Amazon Cognito](https://aws.amazon.com/cognito/) | Workload-level identity management for agent authentication |
| [AWS KMS](https://aws.amazon.com/kms/) | Encryption key management for data at rest and in transit |
