---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/sample-policies-privacy.html
---

# Sample privacy-related policies
<a name="sample-policies-privacy"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

Many organizations that handle sensitive data take a preventative-forward approach, with layers of detective and reactive controls implemented throughout. This section provides examples of privacy-related policies for AWS Identity and Access Management (IAM), AWS Organizations, and AWS Key Management Service (AWS KMS). These policies can help your organization meet various use, disclosure limitation, and cross-border data transfer privacy goals by using a preventative approach. Many of these policies are referenced in previous sections in this guide.

This section contains the following sample policies:
+ [Require access from specific IP addresses](require-access-from-specific-ip-addresses.md)
+ [Require organization membership to access VPC resources](require-organization-membership.md)
+ [Restrict data transfers across AWS Regions](restrict-data-transfers-across-regions.md)
+ [Grant access to specific Amazon DynamoDB attributes](grant-access-dynamodb-attributes.md)
+ [Restrict changes to VPC configurations](restrict-changes-vpc-configurations.md)
+ [Require attestation to use an AWS KMS key](require-attestation-for-kms-key.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
