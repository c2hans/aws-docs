---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution was designed with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework were applied when building this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ We built the solution as infrastructure-as-code using Amazon CloudFormation.
+ Lambda functions push custom metrics to CloudWatch and a custom CloudWatch dashboard to monitor the health of the solution.
+ The solution components are highly modularized, providing the flexibility to choose which components to deploy.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ The Deployment dashboard and all use cases are authenticated and authorized with Amazon Cognito.
+ All inter-service communications use AWS IAM roles.
+ All solution roles follows least-privilege access; meaning, only the minimum permissions required are granted.
+ All data storage including S3 buckets, DynamoDB, and Amazon Kendra have encryption at rest.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ Architecture based on serverless paradigm.
+ We built the architecture for on-demand, horizontal scalability, and automatic recovery from failure of underlying infrastructure.
+ The architecture includes buffering and throttling requests to not overwhelm underlying endpoints.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution uses DynamoDB, a fully managed serverless NoSQL database with on-demand scaling.
+ The solution uses Amazon S3 for object storage and to host a website (through CloudFront) to provide low cost, scalable, with 11 9s durability.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ Where possible, we built the solution to use serverless architecture; so you only pay for what you use.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution’s modular, componentized architecture provides the flexibility to customize resources to be provisioned for individual use cases.
+ The architecture uses serverless compute and storage, which optimizes resource utilization.
+ As a cloud-based solution, this solution benefits from shared resources, networking, power cooling, and physical facilities.
