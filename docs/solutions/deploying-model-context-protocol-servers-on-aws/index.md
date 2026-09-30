---
source_url: https://docs.aws.amazon.com/solutions/deploying-model-context-protocol-servers-on-aws/index.html
---

---
title: 'Guidance for Deploying Model Context Protocol Servers on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-model-context-protocol-servers-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Deploying Model Context Protocol Servers on AWS

## Overview

This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. The Guidance shows how to effectively manage client sessions and tokens, monitor server behavior through centralized logging, and maintain high availability using container orchestration services. By following this Guidance, you can confidently deploy and operate secure, scalable MCP server implementations to reduce operational overhead and improve overall system reliability.

## How it works

### MCP servers with Cognito OAuth

This architecture diagrams illustrates how to effectively support the secure deployment of MCP servers on AWS. It shows the key components and their interactions, providing an overview of the architecture’s structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-model-context-protocol-servers-on-aws.pdf)Step 1The MCP client initiates the OAuth request. The request passes through the Amazon CloudFront distribution (protected by AWS WAF) and Application Load Balancer (ALB) to the MCP Auth Service (MAS).Step 2MAS runs in a secure virtual private cloud (VPC) on AWS Fargate using container images published to Amazon Elastic Container Registry (Amazon ECR). The server writes task logs to Amazon CloudWatch, retrieves configurations from Parameter Store (a capability of AWS Systems Manager), and retrieves sensitive variables from AWS Secrets Manager.Step 3The MAS redirects the user to Amazon Cognito for authentication. The server generates a unique session ID and stores the client information and OAuth parameters in Amazon DynamoDB with a 24-hour time-to-live (TTL).Step 4The user authenticates directly with Amazon Cognito in the browser. Amazon Cognito validates credentials and issues authorization codes for successful authentications.Step 5After successful authentication, Amazon Cognito redirects back to the MAS callback URL. The MAS retrieves the original session data from DynamoDB using the session ID passed as state parameter.Step 6MAS exchanges an authorization code for tokens from Amazon Cognito. MAS stores a mapping between the MAS authorization code and Amazon Cognito tokens in DynamoDB with a 10-minute TTL.Step 7MAS generates its own access token and sends to the MCP client. The response flows back through ALB and CloudFront. MAS generates refresh tokens stored in DynamoDB with a 30-day TTL for enabling token refresh without re-authentication.Step 8The MCP client uses the received access token when making API requests to MCP servers on Fargate and AWS Lambda, which validate the token's signature and verify its status with Amazon Cognito before processing the request and returning a response to the client.### ECS-hosted MCP with Cognito OAuth

This architecture diagrams illustrates how to effectively support the secure deployment of MCP servers on AWS. It shows the key components and their interactions, providing an overview of the architecture’s structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-model-context-protocol-servers-on-aws.pdf)Step 1MCP Server Service (MSS) runs in a secure Virtual Private Cloud (VPC) on Amazon ECS using container images published to Amazon Elastic Container Registry (ECR). The server writes task logs to Amazon CloudWatch and retrieves sensitive variables from AWS Secrets Manager.Step 2MCP Client initiates the OAuth request. The request passes through the Amazon CloudFront distribution (protected by AWS WAF) and Application Load Balancer (ALB) to the MSS.Step 3The MSS redirects the user to Amazon Cognito for authentication. The server generates a unique session ID and stores the client information and OAuth parameters in Amazon DynamoDB with a 24-hour time-to-live (TTL).Step 4The User authenticates directly with Amazon Cognito in the browser. Amazon Cognito validates credentials and issues authorization codes for successful authentications.Step 5After successful authentication, Amazon Cognito redirects back to MSS callback URL. The MSS retrieves the original session data from DynamoDB using the session ID passed as state parameter.Step 6MCP Server exchanges an authorization code for tokens from Amazon Cognito. MSS stores a mapping between the MSS authorization code and Amazon Cognito tokens in DynamoDB with a 10-minute TTL.Step 7MSS generates its own access token and sends to MCP Client. Response flows back through ALB and CloudFront. MSS generates refresh tokens stored in DynamoDB with a 30-day TTL for enabling token refresh without re-authentication.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch logs provide centralized logging for all MCP server containers with configurable retention periods, allowing operators to monitor and troubleshoot server behavior. The AWS Cloud Development Kit (AWS CDK) implementation enables infrastructure-as-code (IaC) practices for consistent, repeatable deployments. Amazon Elastic Container Service (Amazon ECS) health checks integrate with ALB to provide automated monitoring of service health. This creates a unified operational model with clear visibility into MCP server behavior. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito provides OAuth 2.0 authentication with the authorization code grant flow, enabling secure machine-to-machine communication with MCP servers. AWS WAF protects against common web exploits and includes rate limiting to prevent distributed denial of service (DDoS) attacks. The network architecture places MCP servers in private subnets without direct internet access, while security groups restrict traffic flow between components. CloudFront provides HTTPS encryption in transit with modern HTTP2 and HTTP3 protocols. This multi-layered security approach implements the principle of defense in depth, eliminating the need to build custom authentication systems and providing industry-standard OAuth flows. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon ECS services are configured to run across multiple Availability Zones with health checks that automatically replace unhealthy containers. ALB routes traffic only to healthy targets and provides connection draining during deployments. CloudFront improves availability by serving from edge locations and caching responses. Auto-scaling policies adjust capacity based on demand. This Guidance eliminates single points of failure, helping ensure that MCP servers remain available even if an entire AZ experiences an outage. Health checks with automatic recovery minimize downtime by replacing failed containers without human intervention. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront improves global performance by caching and serving content from edge locations closer to clients. ALB efficiently distributes traffic across healthy containers and supports modern HTTP/2 protocols for improved connection efficiency. This avoids overprovisioning by allowing precise specification of resource requirements per MCP server and dynamically adjusting capacity based on actual demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

CloudWatch log retention policies automatically delete older logs, preventing storage costs from growing unbounded. The Guidance enables multiple MCP servers to share common infrastructure components like NAT gateways, ALBs, and the VPC. The serverless container model eliminates costs associated with idle servers. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The shared infrastructure approach for multiple MCP servers increases utilization of networking components like NAT gateways and load balancers, improving the overall carbon efficiency of the deployment. This Guidance aligns with sustainability best practices by maximizing resource utilization through efficient container placement, dynamic scaling, and infrastructure sharing. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
