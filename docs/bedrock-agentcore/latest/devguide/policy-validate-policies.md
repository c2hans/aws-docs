---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-validate-policies.html
---

# Validate and test policies
<a name="policy-validate-policies"></a>

Before deploying policies to production, Policy in AgentCore provides validation capabilities to catch errors and identify potential issues. Validation works differently depending on whether you are generating policies from natural language or creating and updating policies directly.

Schema checks always run to verify that policies comply with the Cedar schema for your gateways. Semantic validation (automated reasoning) detects security and logic issues and can be controlled through the `validationMode` parameter. For more information about these capabilities and the validation modes, see [Validation and analysis overview](policy-validation-overview.md).

**Topics**
+ [Test a policy in LOG\_ONLY mode](policy-test-a-policy.md)
+ [Validation and analysis overview](policy-validation-overview.md)
+ [Policy generation: per-policy validation](policy-generation-validation.md)
+ [Policy create and update: per-policy engine validation](policy-create-update-validation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
