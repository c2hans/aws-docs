---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-4-amazon-elastic-kubernetes-service.html
---

# Deployment Pattern 4 - Amazon Elastic Kubernetes Service
<a name="deployment-pattern-4-amazon-elastic-kubernetes-service"></a>

Amazon Elastic Kubernetes Service (EKS) delivers managed Kubernetes control planes for running containerized MCP servers with advanced orchestration capabilities. EKS enables sophisticated traffic management, multi-tenant isolation through namespaces, and integration with the rich Kubernetes ecosystem. Organizations with existing Kubernetes expertise benefit most from this pattern despite its higher complexity and cost. The proposed architecture uses API Gateway with IAM (SigV4) authorization as the public entry point and integrates privately to an internal ALB via VPC Link v2. SigV4 is selected for AWS-native service-to-service access but is not an EKS requirement. OAuth can be used when broader client compatibility is required. Run the MCP streamable HTTP endpoint on EKS behind the internal ALB. This pattern keeps the MCP server private, leverages AWS-native authorization and is best for AWS-controlled clients.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks)

![Deployment Pattern of Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/1d40f98c-05de-4c82-9c26-ea9cde096f87.png)

**Architecture Characteristics**
+ Pros: The API Gateway \+ Private ALB \+ IAM SigV4 pattern provides security isolation for EKS workloads by keeping all Kubernetes infrastructure completely private—no public load balancers or endpoints. For EKS specifically, EKS supports multi-tenant isolation through Kubernetes namespaces, RBAC, network policies, service accounts, and resource quotas. API Gateway IAM policies can additionally restrict specific AWS accounts or principals to permit API paths and methods.
+ Limitations: SigV4 authentication creates friction for general internet clients lacking AWS credentials or SigV4 signing capability—most off-the-shelf MCP tools expect OAuth/bearer tokens Third-party MCP clients without native SigV4 support can connect through the [MCP Proxy](https://github.com/aws/mcp-proxy-for-aws) for AWS, which signs requests using AWS credentials.; API Gateway HTTP APIs impose hard limits (30s timeout, 10MB payload) that break long-running MCP tool calls.
