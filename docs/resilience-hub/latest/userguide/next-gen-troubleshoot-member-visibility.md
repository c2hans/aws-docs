---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-member-visibility.html
---

# Member account visibility gaps
<a name="next-gen-troubleshoot-member-visibility"></a>

**Symptom:** The delegated administrator cannot see services in a member account.

The following table lists possible causes and solutions.

| Cause | Solution |
| --- | --- |
| Service-linked role not yet created | For large organizations, service-linked role creation may take time. Wait and check again. |
| Account was suspended during setup | Unsuspend the account. The 12-hour reconciliation job will create the service-linked role. |
| Account recently joined organization | New accounts receive service-linked roles automatically, but there may be a brief delay. |
| Service trust disabled | Re-enable trusted access from the management account. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
