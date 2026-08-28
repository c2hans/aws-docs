---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/initiating-runbook-on-config-findings.html
---

# Initiate Runbook on Config Findings
<a name="initiating-runbook-on-config-findings"></a>

This solution can initiate runbooks based on custom AWS Config findings. To do this, complete the following steps:

1. Find the AWS Config rule name that you would like to remediate. This can be found in either AWS Config or in the finding that Security Hub generates for this rule.

1. Navigate to [AWS Systems Manager Parameter Store](https://console.aws.amazon.com/systems-manager/parameters) and select Create Parameter.

1. The name of your rule should be `/Solutions/SO0111/`[.replaceable]`Rule name from Step 1`

1. The value should be formatted as such:

 `{`

 `"RunbookName":"Name of SSM runbook",`

 `"RunbookRole": "Role that Orchestrator will assume"`

 `}`

1. RunbookName is a required field. It specifies the runbook that runs when you remediate this AWS Config rule. RunbookRole is the role that the orchestrator assumes when running this remediation. It is not a required field, and if left out, the orchestrator defaults to using the account’s member role.

1. Once this is in place, you can remediate your AWS Config rule using the "Remediate with ASR" custom action found on the Security Hub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
