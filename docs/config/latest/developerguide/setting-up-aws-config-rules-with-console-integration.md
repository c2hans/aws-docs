---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console-integration.html
---

# Sending Rule Evaluations to Security Hub CSPM
<a name="setting-up-aws-config-rules-with-console-integration"></a>

After adding an AWS Config rule, you can also send rule evaluations to AWS Security Hub CSPM. The integration between AWS Config and Security Hub CSPM allows you to triage and remediate rule evaluations alongside other misconfigurations and security issues.

## Send Rule Evaluations to Security Hub CSPM
<a name="w2aac20c41b5"></a>

To send rule evaluations to Security Hub CSPM, you must first set up AWS Security Hub CSPM and AWS Config, and then add at least one AWS Config managed or custom rule. After this, AWS Config immediately starts sending rule evaluations to Security Hub CSPM. Security Hub CSPM enriches the rule evaluations and transforms them into Security Hub CSPM findings.

For more information about this integration, see [Available AWS Service Integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html#integration-config) in the AWS Security Hub CSPM User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
