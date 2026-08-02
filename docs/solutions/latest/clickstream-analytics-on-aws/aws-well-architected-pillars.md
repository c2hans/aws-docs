---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/aws-well-architected-pillars.html
---

# AWS Well-Architected pillars
<a name="aws-well-architected-pillars"></a>

 This guidance was designed with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

 This section describes how the design principles and best practices of the Well-Architected Framework were applied when building this guidance.

## Operational excellence
<a name="operational-excellence"></a>

 This section describes how the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) were applied when designing this guidance.

 The Clickstream Analytics on AWS guidance pushes metrics, logs and traces to Amazon CloudWatch at various stages to provide observability into the infrastructure, Elastic load balancer, Amazon ECS cluster, Lambda functions, EMR serverless application, Step Function workflow and the rest of the guidance components. This guidance also creates the CloudWatch dashboard for each [data pipeline](pipeline-management.md).

## Security
<a name="security"></a>

 This section describes how the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) were applied when designing this guidance.
+  Clickstream Analytics on AWS web console users are authenticated and authorized with Amazon Cognito or OpenID Connect.
+  All inter-service communications use AWS IAM roles.
+  All roles used by the guidance follows least-privilege access. That is, it only contains minimum permissions required so the service can function properly.

## Reliability
<a name="reliability"></a>

 This section describes how the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) were applied when designing this guidance.
+  Using AWS serverless services wherever possible (for example, EMR Serverless, Redshift Serverless, Lambda, Step Functions, Amazon S3, and Amazon SQS) to ensure high availability and recovery from service failure.
+  Data ingested by [data pipeline](pipeline-management.md) is stored in Amazon S3 and Amazon Redshift, so it persists in multiple Availability Zones (AZs) by default.

## Performance efficiency
<a name="performance-efficiency"></a>

 This section describes how the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) were applied when designing this guidance.
+  The ability to launch this guidance in any Region that supports AWS services in this guidance such as: Amazon S3, Amazon ECS, and Elastic load balancer.
+  Using Analytics Serverless architectures removes the need for you to run and maintain physical servers for traditional compute activities.
+  Automatically testing and deploying this guidance daily. Reviewing this guidance by guidance architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

 This section describes how the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) were applied when designing this guidance.
+  The guidance uses Autoscaling Group so that the compute costs are only related to how much data is ingested and processed.
+  The guidance uses serverless services such as Amazon S3, Amazon Kinesis Data Streams, Amazon EMR Serverless and Amazon Redshift Serverless so that customers only get charged for what they use.

## Sustainability
<a name="sustainability"></a>

 This section describes how the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) were applied when designing this guidance.
+  The guidance's serverless design (using Amazon Kinesis Data Streams, Amazon EMR Serverless, Amazon Redshift Serverless and Quick) and the use of managed services (such as Amazon ECS, Amazon MSK) are aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.
