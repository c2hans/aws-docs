---
source_url: https://docs.aws.amazon.com/sns/latest/dg/data-identifiers.html
---

# Amazon SNS data identifiers
<a name="data-identifiers"></a>

**Important**
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

Amazon SNS uses a combination of criteria and techniques, including machine learning and pattern matching, to detect sensitive data. These criteria and techniques, collectively referred to as *data identifiers*, can detect a large and growing list of sensitive data types for many countries and regions. Amazon SNS managed data identifiers offer preconfigured data types for protecting financial data, personal health information (PHI), and personally identifiable information (PII). You can also use custom data identifiers to create your own data identifiers tailored to your specific use case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
