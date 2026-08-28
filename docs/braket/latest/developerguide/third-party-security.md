---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/third-party-security.html
---

# Security of Amazon Braket Hardware Providers
<a name="third-party-security"></a>

QPUs on Amazon Braket are hosted by third-party hardware providers. When you run your quantum task on a QPU, Amazon Braket uses the DeviceARN as an identifier when sending the circuit to the specified QPU for processing.

If you use Amazon Braket for access to quantum computing hardware operated by one of the third-party hardware providers, your circuit and its associated data are processed by hardware providers outside of facilities operated by AWS. Information about the physical location and AWS Region where each QPU is available can be found in the **Device Details** section of the Amazon Braket console.

Your content is anonymized. Only the content necessary to process the circuit is sent to third parties. AWS account information is not transmitted to third parties.

All data is encrypted at rest and in transit. Data is decrypted for processing only. Amazon Braket third-party providers are not permitted to store or use your content for purposes other than processing your circuit. Once the circuit completes, the results are returned to Amazon Braket and stored in your S3 bucket.

The security of Amazon Braket third-party quantum hardware providers is audited periodically, to ensure that standards of network security, access control, data protection, and physical security are met.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
