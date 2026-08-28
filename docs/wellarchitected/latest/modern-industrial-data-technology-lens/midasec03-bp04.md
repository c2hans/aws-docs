---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp04.html
---

# MIDASEC03-BP04 Implement industrial encryption policies
<a name="midasec03-bp04"></a>

 Apply encryption policies across all layers of the manufacturing data system, including at rest, in transit, and optionally during processing, to help protect sensitive operational and proprietary information.

 **Desired outcome:** Data remains encrypted end-to-end, providing confidentiality and integrity and helping with regulatory alignment.

 **Benefits of establishing this best practice:** Reduces impact of data breaches, supports regulatory compliance, and builds trust with partners and customers.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-17"></a>

 Use AWS KMS for key management and enforce encryption using S3 bucket policies, VPC security, and service-level configurations.

### Implementation steps
<a name="implementation-steps-18"></a>
+  Enable default encryption on all data stores (for example, Amazon S3, Amazon RDS, Amazon Redshift, and Amazon DynamoDB).
+  Use TLS 1.2\+ for all data in transit.
+  Create customer-managed keys (CMKs) using AWS KMS for sensitive workloads.
+  Regularly rotate keys and audit access with AWS CloudTrail.

## Resources
<a name="resources-18"></a>
+  [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
+  [ Setting default server-side encryption behavior for Amazon S3 buckets ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
