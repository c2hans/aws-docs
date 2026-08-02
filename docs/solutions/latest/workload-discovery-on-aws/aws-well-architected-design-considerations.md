---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

We architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) to benefit this solution.
+ Resources defined as infrastructure as code using CloudFormation.
+ The solution pushes metrics to Amazon CloudWatch to provide observability into the infrastructure, Lambda functions, Amazon ECS tasks, AWS S3 buckets, and the rest of the solution components.

## Security
<a name="security"></a>

We architected this solution using principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) to benefit this solution.
+ Amazon Cognito authenticates and authorizes web UI app users.
+ All roles used by the solution follow least-privilege access. In other words, they only contain minimum permissions required so that the service can function properly.
+ Data at rest and transit is encrypted using keys stored in [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS)--a dedicated key management store.
+ Credentials have a short expiration and follow a strong password policy.
+ AWS AppSync security GraphQL directives give fine-grained control over what operations can be invoked by the frontend and backend.
+ Logging, tracing, and versioning is turned on where applicable.
+ Automatic patching ([minor version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html)) and snapshot creation is turned on where applicable.
+ Network access is private by default with [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) endpoints being turned on where available.

## Reliability
<a name="reliability"></a>

We architected this solution using principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to benefit this solution.
+ The solution uses AWS serverless services wherever possible to ensure high availability and recovery from service failure.
+ All compute processing uses Lambda functions or Amazon ECS on AWS Fargate.
+ All custom code uses the AWS SDK and requests are throttled on the client side to prevent reaching API rate quotas.

## Performance efficiency
<a name="performance-efficiency"></a>

We architected this solution using principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) to benefit this solution.
+ The solution uses AWS serverless architecture where possible. This removes the operational burden of managing physical servers.
+ The solution can launch in [any Region that supports AWS services](plan-your-deployment.md#supported-aws-regions) used in this solution such as: AWS Lambda, Amazon Neptune, AWS AppSync, Amazon S3, and Amazon Cognito.
+ In supported Regions, [Amazon Neptune serverless](https://aws.amazon.com/neptune/serverless/) allows you to run and instantly scale graph workloads, without the need to manage and optimize database capacity.
+ The solution uses managed services throughout to reduce the operational burden of resource provisioning and management.

## Cost optimization
<a name="cost-optimization"></a>

We architected this solution using principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) to benefit this solution.
+ AWS ECS on AWS Fargate uses Lambda functions exclusively for compute and only charges based on use.
+ Amazon DynamoDB scales capacity on demand, so you only pay for the capacity you use.

## Sustainability
<a name="sustainability"></a>

We architected this solution using principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) to benefit this solution.
+ The solution uses managed and serverless services where possible to minimize the environmental impact of the backend services.
