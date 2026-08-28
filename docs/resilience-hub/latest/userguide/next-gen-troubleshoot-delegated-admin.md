---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-delegated-admin.html
---

# Delegated administrator setup errors
<a name="next-gen-troubleshoot-delegated-admin"></a>

| Error | Cause | Resolution |
| --- | --- | --- |
| `AWSOrganizationsNotInUseException` | Organizations not enabled | Enable AWS Organizations with all features. |
| `AccountNotRegisteredException` | Account is not a member of the organization | Verify account membership. |
| `ConstraintViolationException` | Service trust not enabled | Run enable-aws-service-access first. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
