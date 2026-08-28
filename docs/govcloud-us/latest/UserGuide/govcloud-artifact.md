---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-artifact.html
---

# AWS Artifact in AWS GovCloud (US)
<a name="govcloud-artifact"></a>

AWS Artifact provides on-demand downloads of AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and Service Organization Control (SOC) reports. You can submit the security and compliance documents (also known as audit artifacts) to your auditors or regulators to demonstrate the security and compliance of the AWS infrastructure and services that you use. You can also use AWS Artifact to review, accept, and track the status of AWS agreements such as the Business Associate Addendum (BAA). With AWS Artifact, you can accept agreements with AWS and designate AWS accounts that can legally process restricted information.

## How AWS Artifact differs
<a name="how_shared_artlong_differs"></a>

There are no differences for this service.

## Documentation
<a name="govcloud-art-docs"></a>
+  [AWS Artifact documentation](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)

## Export-controlled content
<a name="govcloud-artifact-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Function name
+ Description
+ DLQ data (can be exported through Amazon SNS and Amazon SQS)
+ Memory
+ Timeout
+ Runtime
+ Role name for service principals
+ Aliases

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
