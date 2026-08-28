---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-org-policies.html
---

# Applying resilience policies across accounts
<a name="next-gen-org-policies"></a>

A management account or delegated administrator can apply resilience policies across member accounts by associating a policy with a system and then associating services in member accounts to that system. The system-level policy is applied to all associated services.

1. Create a resilience policy in the management account or DA account.

1. Create a system and associate the policy with it.

1. Associate services from member accounts to the system.

The system-level policy applies to all services associated with that system, regardless of which member account owns the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
