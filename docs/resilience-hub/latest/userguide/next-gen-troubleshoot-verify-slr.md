---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-verify-slr.html
---

# Verifying the service-linked role exists in a member account
<a name="next-gen-troubleshoot-verify-slr"></a>

From the member account, run the following command to verify the service-linked role exists:

```
aws iam get-role --role-name AWSServiceRoleForResilienceHub
```

If the role doesn't exist, verify that trusted access is enabled and wait for the reconciliation job, which runs every 12 hours.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
