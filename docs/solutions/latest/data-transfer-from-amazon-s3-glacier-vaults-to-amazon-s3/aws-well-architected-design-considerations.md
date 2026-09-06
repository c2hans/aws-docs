---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

 This Guidance uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

 This section describes how the design principles and best practices of the Well-Architected Framework benefit this Guidance.

## Operational excellence
<a name="operational-excellence"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+  This Guidance pushes metrics to CloudWatch at various stages to provide visibility into archive transfer progress.

## Security
<a name="security"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+  All interservice communications use applicable [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles.
+  All roles used by the Guidance follow least privilege access. They only contain the minimum permissions required to accomplish the transfer.
+  All data storage, including the S3 buckets, encrypts the data at rest.

## Reliability
<a name="reliability"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+  The Guidance uses a serverless architecture to achieve high availability and recovery from failure.
+  The Guidance protects against state machine definition errors through a suite of automated tests.
+  Data processing uses Lambda functions. Data is stored in DynamoDB and Amazon S3, which persist in multiple Availability Zones by default.

## Performance efficiency
<a name="performance-efficiency"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+  The Guidance uses a serverless architecture with the ability to scale horizontally as needed.
+  The Guidance is tested and deployed daily to achieve consistency as AWS services change.

## Cost optimization
<a name="cost-optimization"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+  The Guidance uses a serverless architecture that only charges customers for what they use.
+  DynamoDB global secondary indexes are selected to reduce the pricing for queries.

## Sustainability
<a name="sustainability"></a>

 This section describes how we architected this Guidance using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+  The Guidance uses managed serverless services to minimize the environmental impact of the backend services compared to continually operating on-premises services.
