---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/aws-well-architected-pillars.html
---

# AWS Well-Architected pillars
<a name="aws-well-architected-pillars"></a>

 This Guidance was designed with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

## Operational excellence
<a name="operational-excellence"></a>

 This section describes how the principles and best practices of the [*operational excellence pillar*](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) were applied when designing this Guidance.

 The Data Transfer Hub Guidance pushes metrics to Amazon CloudWatch at various stages to provide observability into the infrastructure, Lambda functions, Amazon EC2 transfer workers, Step Function workflow, and the rest of the Guidance components. Data transferring errors are added to the Amazon SQS queue for retries and alerts.

## Security
<a name="security"></a>

 This section describes how the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) were applied when designing this Guidance.
+  Data Transfer Hub web console users are authenticated and authorized with Amazon Cognito.
+  All inter-service communications use AWS IAM roles.
+  All roles used by the Guidance follows least-privilege access. That is, it only contains minimum permissions required so the service can function properly.

## Reliability
<a name="reliability"></a>

 This section describes how the principles and best practices of the [*reliability pillar*](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) were applied when designing this Guidance.
+  Using AWS serverless services wherever possible (for example, Lambda, Step Functions, Amazon S3, and Amazon SQS) to ensure high availability and recovery from service failure.
+  Data is stored in DynamoDB and Amazon S3, so it persists in multiple Availability Zones (AZs) by default.

## Performance efficiency
<a name="performance-efficiency"></a>

 This section describes how the principles and best practices of the [*performance efficiency pillar*](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) were applied when designing this Guidance.
+  The ability to launch this Guidance in any Region that supports AWS services in this Guidance such as: AWS Lambda, AWS S3, Amazon SQS, Amazon DynamoDB, and Amazon EC2.
+  Automatically testing and deploying this GUidance daily. Reviewing this Guidance by solution architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

 This section describes how the principles and best practices of the [*cost optimization*](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) pillar were applied when designing this Guidance.
+  Use Autoscaling Group so that the compute costs are only related to how much data is transferred.
+  Using serverless services such as Amazon SQS and DynamoDB so that customers only get charged for what they use.

## Sustainability
<a name="sustainability"></a>

 This section describes how the principles and best practices of the [*sustainability pillar*](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) were applied when designing this Guidance.
+  The Guidance's serverless design (using Lambda, Amazon SQS and DynamoDB) and the use of managed services (such as Amazon EC2) are aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.
