---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/initiating-runbook-on-config-findings.html
---

# Initiate Runbook on Config Findings
<a name="initiating-runbook-on-config-findings"></a>

This solution can initiate runbooks based on custom AWS Config findings. To do this you will need to:

1. Find the AWS Config rule name that you would like to remediate. This can be found in either AWS Config or in the finding that Security Hub generates for this rule.

1. Navigate to AWS Systems Manager Parameter Store and select Create Parameter.

1. The name of your rule should be `/Solutions/SO0111/`[.replaceable]`Rule name from Step 1`

1. The value should be formatted as such:

 `{`

 `"RunbookName":"Name of SSM runbook",`

 `"RunbookRole": "Role that Orchestrator will assume"`

 `}`

1. RunbookName is a required field and will be the runbook that is run when you remediate this Config rule. RunbookRole is the role that the orchestrator will assume when running this role. It is not a required field, and if left out, the orchestrator will default to using the account’s member role.

1. Once this is in place, you can remediate your Config rule using the "Remediate with ASR" custom action found on the Security Hub.
