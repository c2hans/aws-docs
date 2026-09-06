---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution follows best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

 **Topics**
+  [Operational excellence](#operational-excellence)
+  [Security](#security)
+  [Reliability](#reliability)
+  [Performance efficiency](#performance-efficiency)
+  [Cost optimization](#cost-optimization)
+  [Sustainability](#sustainability)

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ All resources are defined as infrastructure as code using AWS CloudFormation templates generated from AWS CDK constructs.
+ The solution pushes metrics to Amazon CloudWatch at various stages to provide observability into AWS Lambda functions, Amazon SageMaker, AWS Step Functions, Amazon S3 buckets, and other solution components.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ Amazon Cognito authenticates and authorizes web console users and API requests.
+ All interservice communications use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles with least privilege access, containing only the minimum permissions required.
+ All data storage, including S3 buckets and DynamoDB tables, encrypts data at rest using AWS managed keys.
+ Logging, tracing, and versioning are enabled where applicable for audit and compliance purposes.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The solution uses AWS serverless services wherever possible (examples: Lambda, API Gateway, Amazon S3, AWS Step Functions and Amazon DynamoDB) to ensure high availability and recovery from service failure.
+ Data is stored in DynamoDB and Amazon S3, so it persists in multiple Availability Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution uses a serverless architecture with the ability to scale horizontally as needed.
+ The solution can be launched in any region that supports the AWS services in this solution, which include: AWS Lambda, Amazon API Gateway, Amazon S3, AWS Step Functions, Amazon DynamoDB, and Amazon Cognito.
+ The solution uses managed services throughout to reduce the operational burden of resource provisioning and management.
+ The solution is automatically tested and deployed daily to achieve consistency as AWS services change, as well as reviewed by solution architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The solution uses a serverless architecture; therefore, you are only charged for what you use.
+ Amazon DynamoDB scales capacity on demand, so you only pay for the capacity you use.
+ Amazon SageMaker allows you to pay only for the compute resources you use, with no upfront expenses.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution uses managed, serverless services to minimize the environmental impact of the backend services compared to continually operating on-premises services.
+ Serverless services allow you to scale up or down as needed.
