---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ All Lambda functions send logging output to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).
+ Alarms from AWS services included in this solution are stored in CloudWatch to provide observability into the infrastructure.
+ You can review past runtime outcomes for Amazon MWAA, AWS Batch, and EMR Serverless.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ All inter-service communications use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles.
+ All roles used by the solution follow least-privilege access. That is, they only contain the minimum permissions required so that the service can function properly.
+ All S3 buckets have default encryption at rest activated.
+ Access to data storage buckets is logged into a separate bucket.
+ Database metadata is encrypted using [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) keys.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The solution uses AWS serverless services wherever possible to ensure high availability and recovery from service failure.
+ All compute processing uses Lambda functions wherever possible.
+ Data is stored in S3 buckets and DynamoDB tables, so it persists in multiple Availability Zones by default.
+ The solution uses Amazon MWAA to orchestrate the workflow and provides the run history and ability to retry the failed process(es) and re-invoke the workflow.
+ All custom code uses [AWS Software Development Kit](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html) (AWS SDK) and benefits from automatic retries and back-off for API calls.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution uses serverless compute and data resources throughout the architecture.
+ You can launch the solution in any Region that supports AWS services used in this solution, such as Amazon MWAA, Lambda, Amazon S3, SageMaker AI, EMR Serverless.
+ The solution is automatically tested and deployed every day. The solution is also reviewed by solution architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ This solution uses Lambda functions, AWS Batch, EMR Serverless, and SageMaker AI processing jobs for most compute needs.
+ You can choose to run the solution on-demand or at an interval that you choose.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ This solution uses serverless resources for compute and data storage.
+ Most data storage is maintained in an S3 bucket or DynamoDB table that you can remove easily.
