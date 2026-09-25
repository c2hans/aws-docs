---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This Guidance uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework apply to this Guidance.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how this Guidance applies the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ This Guidance pushes metrics to CloudWatch to provide observability into the infrastructure, including Lambda functions, Step Functions, [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets, and the rest of the deployed components.
+ AWS X-Ray traces are enabled for Step Functions and AWS AppSync. This helps you visualize the components of the state machine and analyze user requests as they travel through your AWS AppSync APIs to the underlying services, identify performance bottlenecks, and troubleshoot requests that resulted in an error.

## Security
<a name="security-pillar"></a>

This section describes how this Guidance applies the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ The web UI users are authenticated and authorized with [Amazon Cognito](https://aws.amazon.com/cognito/).
+ All inter-service communications use [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) roles.
+ All multi-account communications use IAM roles.
+ All IAM roles used by this Guidance follow least-privilege access. In other words, they only contain minimum permissions required so that the service can function properly.
+ The access token obtained from Amazon Cognito is used to authorize application programming interface (API) calls.
+ All data storage, such as S3 buckets and DynamoDB tables, have encryption at rest.
+ AWS WAF protects the web UI and APIs from attacks using configured web access control lists (ACLs).

The deployment creates a CloudFront distribution with the [Default CloudFront SSL Certificate](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesSSLCertificate), which allows TLS 1.1 and TLS 1.0. We recommend using Custom SSL Certificate with [TLSv1.2\_2021 security policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html) to disallow insecure protocols and cipher suites.

## Reliability
<a name="reliability"></a>

This section describes how this Guidance applies the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ This Guidance uses serverless AWS services wherever possible (such as Lambda, [AWS AppSync](https://aws.amazon.com/appsync/), Amazon S3, and Step Functions) to ensure high availability and recovery from service failure.
+ AWS protects against definition errors of state machines leveraged by Step Functions by running automated tests.
+ Data processing uses Lambda functions. Data is stored in DynamoDB and Amazon S3, so it persists in multiple Availability Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how this Guidance applies the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ This Guidance uses serverless architecture. For additional details, refer to [Reliability](#reliability).
+ This Guidance uses `error handling` in Step Functions to run concurrent state machine executions that add or remove multiple subnets in the `VPC-TGW` attachment. This allows you to create VPC and related resources in parallel using CloudFormation stack.
+ You can launch this Guidance in any AWS Region that supports the AWS services used (such as Lambda, API Gateway, Amazon S3, Step Functions, Amazon Cognito, [Amazon CloudFront](https://aws.amazon.com/cloudfront/), and [AWS WAF](https://aws.amazon.com/waf/)). You can also choose not to deploy the web UI if CloudFront and Amazon Cognito aren’t supported in the Region. Refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions).

## Cost optimization
<a name="cost-optimization"></a>

This section describes how this Guidance applies the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ This Guidance uses serverless architecture (for example, Step Functions and DynamoDB) to minimize the cost of unused compute infrastructure, and customers pay only for what they use.
+ The compute layer defaults to Lambda, which uses a pay-per-use model.

## Sustainability
<a name="sustainability"></a>

This section describes how this Guidance applies the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ This Guidance uses managed and serverless services to minimize the environmental impact of the backend services.
+ Its serverless design reduces carbon footprint compared to continually operating on-premises servers.
+ The web UI allows users to select scan parameters to perform selective scans in specific AWS accounts, Regions, and services.
