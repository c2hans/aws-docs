---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-4-amazon-elastic-kubernetes-service.html
---

# Deployment Pattern 4 - Amazon Elastic Kubernetes Service
<a name="deployment-pattern-4-amazon-elastic-kubernetes-service"></a>

Amazon Elastic Kubernetes Service (EKS) delivers managed Kubernetes control planes for running containerized MCP servers with advanced orchestration capabilities. EKS enables sophisticated traffic management, multi-tenant isolation through namespaces, and integration with the rich Kubernetes ecosystem. Organizations with existing Kubernetes expertise or complex microservices architectures benefit most from this pattern despite its higher complexity and cost. The proposed architecture uses API Gateway with IAM (SigV4) authorization as the public entry point and integrate privately to an internal ALB via VPC Link v2. Run the MCP streamable HTTP endpoint on EKS behind the internal ALB. This pattern keeps the MCP server private, leverages AWS-native authorization and is best for AWS-controlled clients.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks)

![Deployment Pattern of Amazon Elastic Kubernetes Service](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/1d40f98c-05de-4c82-9c26-ea9cde096f87.png)

**Architecture Characteristics**
+ Pros: The API Gateway \+ Private ALB \+ IAM SigV4 pattern provides great security isolation for EKS workloads by keeping all Kubernetes infrastructure completely private—no public load balancers or endpoints—while leveraging AWS-native IAM authentication that eliminates OAuth token services and credential proxies entirely. For EKS specifically, it delivers multi-tenancy isolation flexibility through fine-grained permissions scoped to paths/methods/accounts, enabling workload isolation across namespaces/teams without complex network policies or shared ALB rules.
+ Limitations: SigV4 authentication creates friction for general internet clients lacking AWS credentials or SigV4 signing capability—most off-the-shelf MCP tools expect OAuth/bearer tokens, requiring a SigV4 proxy layer for third-party compatibility; API Gateway HTTP APIs impose hard limits (30s timeout, 10MB payload) that break long-running MCP tool calls.
