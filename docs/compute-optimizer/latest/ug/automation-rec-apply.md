---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rec-apply.html
---

# Apply recommended actions
<a name="automation-rec-apply"></a>

You can select up to 10 recommended actions at a time to apply. Once you apply the recommended action, it will be removed from the Recommended action page and an automation event will be created. You can view and monitor the status of the action in the [Automation events](automation-events.md) page. Automation events awaiting execution will be in Ready status. You can have up to 100 automation events in Ready status per account per region.

**To apply recommended actions**

1. On the **Recommended actions** page, select up to 10 recommended actions that you want to apply.

1. Choose **Review and apply**. You will be able to review and confirm your selection on the next page before implementing actions.

1. Review your selection. You can remove selected recommended by clicking on the in-line remove icon.

1. Choose **Confirm and apply**.

1. When prompted to confirm, type `“confirm”` and choose **Apply changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
