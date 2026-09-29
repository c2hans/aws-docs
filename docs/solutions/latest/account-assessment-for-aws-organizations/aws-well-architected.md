---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/aws-well-architected.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected"></a>

We designed this guidance with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how we applied the design principles and best practices of the Well-Architected Framework when building this guidance.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) were applied when designing this guidance.
+ The guidance pushes metrics to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to provide observability into the infrastructure, Lambda functions, Step Functions, API Gateway, Amazon S3 buckets, and the rest of the guidance components.
+  [AWS X-Ray](https://aws.amazon.com/xray/) traces Lambda functions, Step Functions, and API Gateway. This helps you visualize the components of the state machine and analyze user requests as they travel through your Amazon API Gateway APIs to the underlying services, identify performance bottlenecks, and troubleshoot requests that resulted in an error.

## Security
<a name="security-pillar"></a>

This section describes how the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) were applied when designing this guidance.
+ The Web UI app users are authenticated and authorized with Amazon Cognito.
+ All inter-service communications use IAM roles.
+ All multi-account communications use IAM roles.
+ All roles used by the guidance follow least-privilege access. In other words, they only contain minimum permissions required so that the service can function properly.
+ The access token obtained from Amazon Cognito is used to authorize API calls.
+ All data storage including Amazon S3 buckets and DynamoDB tables have encryption at rest.
+ AWS WAF protects the web application and APIs from attacks using AWS managed web ACLs rule groups.

## Reliability
<a name="reliability"></a>

This section describes how the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) were applied when designing this guidance.
+ The guidance uses serverless AWS services wherever possible (such as Lambda, API Gateway, Amazon S3, and Step Functions) to ensure high availability and recovery from service failure.
+ AWS protects the guidance against definition errors of state machines leveraged by AWS Step Functions by running automated tests on the guidance.
+ Data processing uses Lambda functions. The guidance stores data in DynamoDB and Amazon S3, so it persists in multiple Availability Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) were applied when designing this guidance.
+ The guidance uses serverless architecture. For additional details, refer to [Reliability](#reliability).
+ The guidance uses `Map` state in Step Functions to run concurrent iterations that scan resources in multiple AWS services across multiple AWS accounts.
+ You can launch the guidance in any AWS Region that supports the AWS services used in this guidance (such as Lambda, API Gateway, Amazon S3, Step Functions, Amazon Cognito, CloudFront, and AWS WAF). For details, refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions).
+ The guidance is automatically tested and deployed every day. Our solution architects and subject matter experts review the guidance for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) were applied when designing this guidance.
+ Most of the resources used by the guidance are serverless, so customers pay only for them while in use.
+ The compute layer defaults to Lambda, which uses a pay-per-use model.
+ DynamoDB indexes are selected to reduce throughput cost for queries.
+ The DynamoDB [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) feature deletes the item from your table without consuming any write throughput at a customer-defined interval.

**Ongoing costs**
AWS WAF is always in use, and the Step Functions state machine runs once per day. If you are not using the guidance, delete its stacks to avoid ongoing cost. For the required deletion order and the resources that are retained, see [Uninstall the guidance](uninstall-the-guidance.md).

## Sustainability
<a name="sustainability"></a>

This section describes how the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) were applied when designing this guidance.
+ The guidance uses managed and serverless services to minimize the environmental impact of the backend services.
+ The guidance’s serverless design is aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.
