---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

We designed this solution with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework were applied when building this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ The solution pushes metrics to Amazon CloudWatch to provide observability into its components (such as its infrastructure and Lambda functions).
+ AWS X-Ray traces Lambda functions.
+ Uses Amazon SNS for error reporting.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ All inter-service communications use IAM roles.
+ All multi-account communications use IAM roles.
+ All roles used by the solution follow least-privilege access. In other words, they only contain minimum permissions required so that the service can function properly.
+ All data storage including DynamoDB tables have encryption at rest.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The solution uses serverless AWS services wherever possible (such as Lambda and DynamoDB) to ensure high availability and recovery from service failure.
+ Data processing uses Lambda functions. The solution stores data in DynamoDB, so it persists in multiple Availability Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution uses serverless architecture.
+ You can launch the solution in any AWS Region that supports the AWS services used in this solution (such as Lambda and DynamoDB). For details, refer to [Supported AWS Regions](solution-overview.md#supported-aws-regions).
+ The solution is automatically tested and deployed every day. Our solution architects and subject matter experts review the solution for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The solution uses serverless architecture, and customers pay only for what they use.
+ The compute layer defaults to Lambda, which uses a pay-per-use model.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution uses managed and serverless services to minimize the environmental impact of the backend services.
+ The solution’s serverless design is aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.
