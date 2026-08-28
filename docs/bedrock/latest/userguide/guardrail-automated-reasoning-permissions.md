---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrail-automated-reasoning-permissions.html
---

# Permissions for Automated Reasoning policies with ApplyGuardrail
<a name="guardrail-automated-reasoning-permissions"></a>

When using Automated Reasoning policies with the `ApplyGuardrail` API, you need an IAM policy that allows you to invoke the Automated Reasoning policy.

```
{
    "Sid": "AutomatedReasoningChecks",
    "Effect": "Allow",
    "Action": [
        "bedrock:InvokeAutomatedReasoningPolicy"
    ],
    "Resource": [
        "arn:aws:bedrock:{{region}}:{{account-id}}:automated-reasoning-policy/{{policy-id}}:{{policy-version}}"
    ]
}
```

This policy allows you to invoke the specified Automated Reasoning policy in your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
