---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-triggers-how-they-work.html
---

# How customization triggers work
<a name="aft-triggers-how-they-work"></a>

When customization triggers are enabled and AFT processes an account provisioning event, it evaluates whether the account's OU has changed and takes appropriate action.

1. AFT detects an OU change by comparing the account's current OU against its previously recorded OU.

1. If the OU changed, AFT enriches the execution with trigger context, including the source and destination OU.

1. AFT invokes the customization pipeline, bypassing provisioning and bootstrap steps that have already completed. For details on bypass configuration, see [Re-invoke customizations](aft-account-customization-options.md#aft-re-invoke-customizations).

1. AFT records an audit entry with the trigger source and target accounts.

If the feature is disabled or if the OU has not changed, standard provisioning continues without triggering customization re-execution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
