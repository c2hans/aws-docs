---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-error-codes.html
---

# Common permission error codes and resolution
<a name="next-gen-troubleshoot-error-codes"></a>

The following table lists common permission error codes and their recommended resolution.

| Error | Cause | Resolution |
| --- | --- | --- |
| `AccessDeniedException: Unable to assume role` | Invoker role trust policy doesn't include resiliencehub.amazonaws.com | Update the role's trust policy. |
| `AccessDeniedException: Cross-account role` | Cross-account role trust policy doesn't allow assumption from the invoker role | Verify the trust policy and ExternalId. |
| `AccessDeniedException: sts:AssumeRole` | Invoker role lacks sts:AssumeRole permission for cross-account roles | Add sts:AssumeRole permission to the invoker role. |
| `InvalidParameterException: Role does not exist` | Role name in permissionModel doesn't match an existing IAM role | Verify the role name and account. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
