---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks-permissions.html
---

# Set up permissions
<a name="guardrails-use-invoke-guardrail-checks-permissions"></a>

To call `InvokeGuardrailChecks`, the caller's IAM identity needs permission to invoke the operation on Amazon Bedrock. Create or use an IAM role or user with the following policy attached.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeGuardrailChecks"
      ],
      "Resource": "*"
    }
  ]
}
```

`InvokeGuardrailChecks` is resourceless — there is no guardrail ARN to scope the policy against. Use IAM identity-based policies, AWS Organizations service control policies, and standard AWS condition keys (such as `aws:SourceIp` or `aws:PrincipalTag`) to restrict who can call the API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
