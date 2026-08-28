---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-sensitive-data.html
---

# Sensitive data detection and redaction in Amazon Bedrock Data Automation
<a name="bda-sensitive-data"></a>

With Amazon Bedrock Data Automation (BDA), you can detect and redact personally identifiable information (PII) in standard and custom outputs. PII detection uses Sensitive Information Filters in Amazon Bedrock Guardrails. BDA disables this feature by default. To enable it, pass modality-specific overrides in `overrideConfiguration` for each modality you want to process.

**Note**
The sensitive data detection and redaction feature only applies to the JSON results that BDA provides to you. It does not modify your input assets or blueprints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
