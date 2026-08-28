---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-verify-role.html
---

# Verifying role configuration
<a name="next-gen-troubleshoot-verify-role"></a>

Check that your invoker role is correctly configured using the following AWS CLI commands.

To verify that the role exists:

```
aws iam get-role --role-name AWSResilienceHubAssessmentRole
```

To verify the trust policy:

```
aws iam get-role --role-name AWSResilienceHubAssessmentRole \
  --query 'Role.AssumeRolePolicyDocument'
```

To simulate whether a principal can perform required actions:

```
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/AWSResilienceHubAssessmentRole \
  --action-names resiliencehub:GetService resiliencehub:StartFailureModeAssessment
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
