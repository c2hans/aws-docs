---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/well-architected.html
---

# AWS Well-Architected design considerations
<a name="well-architected"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ The solution pushes metrics to CloudWatch to provide observability into the infrastructure, Lambda functions, [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/), Amazon S3 buckets, and the rest of the solution components.
+ We develop, test, and publish the solution through an AWS continuous integration and continuous delivery (CI/CD) pipeline. This helps developers achieve high quality results consistently.
+ You can install the solution with a CloudFormation template that provisions all the required resources in your account. To update or delete the solution, you only need to update or delete the template.

## Security
<a name="security-pillar"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ All inter-service communications use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles.
+ All roles used by the solution follow [least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) access. In other words, they only contain minimum permissions required so that the service can function properly.
+ All data storage, including Amazon S3 buckets and DynamoDB, have encryption at rest.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The solution uses AWS serverless services wherever possible (for example, Lambda, Firehose, Amazon S3, and Athena) to ensure high availability and recovery from service failure.
+ We perform automated tests on the solution to detect and fix errors quickly.
+ The solution uses Lambda functions for data processing. The solution stores data in Amazon S3 and DynamoDB, and it persists in multiple Avaialbility Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution uses a serverless architecture to ensure high scalability and availability at a reduced cost.
+ The solution enhances database performance by parititioning data and optimizing query to reduce the amount of data scanning and achieve faster results.
+ The solution is automatically tested and deployed every day. Our solution architects and subject matter experts review the solution for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The solution uses a serverless architecture, and customers pay only for what they use.
+ The solution’s compute layer defaults to Lambda, which uses a pay-per-use model.
+ The Athena database and queries are optimized to reduce the amount of data scanning, thereby reducing cost.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution uses managed and serverless services to minimize the environmental impact of the backend services.
+ The solution’s serverless design is aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.
