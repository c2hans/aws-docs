---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/mfg-overview.html
---

# Overview
<a name="mfg-overview"></a>

The overview diagram shows how manufacturing workloads connect through a central data lake on AWS.

![Overview diagram showing how manufacturing workloads connect through a central data lake on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/images/manufacturing-on-aws-ra-1.png)

1. Central to the architecture is a manufacturing data lake for analytics and machine learning (ML). Use [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) or [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) to structure your data lake.

1. Establish smart factories by connecting Industrial Internet of Things (IIoT) devices to the cloud with hybrid infrastructure.

1. Host enterprise applications with cost-effective, resilient AWS architecture.

1. Use Amazon EC2 Spot Instances and GPU instances for computer-aided design (CAD) and computer-aided engineering (CAE) workloads.

1. Build smart products for connected products and machines that send telemetry to the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
