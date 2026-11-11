---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-4-amazon-elastic-kubernetes-service.html
---

# Deployment Pattern 4 - Amazon Elastic Kubernetes Service
<a name="deployment-pattern-4-amazon-elastic-kubernetes-service"></a>

Amazon Elastic Kubernetes Service (EKS) provides managed Kubernetes control planes for running containerized MCP servers with advanced orchestration capabilities. EKS enables advanced traffic management, multi-tenant isolation through namespaces, and integration with Kubernetes tools and add-ons. Organizations with existing Kubernetes expertise can benefit from this pattern despite its higher complexity and cost. The proposed architecture uses API Gateway with IAM (SigV4) authorization as the public entry point and integrates privately with an internal Application Load Balancer (ALB) through VPC Link v2. This pattern uses SigV4 for AWS-native service-to-service access, but EKS doesn't require it. You can use OAuth when you need broader client compatibility. Run the MCP streamable HTTP endpoint on EKS behind the internal ALB. This pattern keeps the MCP server private, uses AWS-native authorization, and is designed for AWS-controlled clients.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-eks)

![Deployment Pattern of Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/1d40f98c-05de-4c82-9c26-ea9cde096f87.png)

**Architecture Characteristics**
+ Pros: The API Gateway \+ Private ALB \+ IAM SigV4 pattern provides security isolation for EKS workloads by keeping Kubernetes infrastructure private, with no public load balancers or endpoints. EKS supports multi-tenant isolation through Kubernetes namespaces, RBAC, network policies, service accounts, and resource quotas. API Gateway IAM policies can additionally restrict specific AWS accounts or principals to permitted API paths and methods.
+ Limitations: SigV4 authentication is difficult for general internet clients that lack AWS credentials or SigV4 signing capability, because many MCP tools expect OAuth/bearer tokens. Third-party MCP clients without native SigV4 support can connect through the [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws), which signs requests using AWS credentials. API Gateway HTTP APIs impose quotas (30-second timeout, 10 MB payload) that can interrupt long-running MCP tool calls.
