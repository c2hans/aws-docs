---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-get-customize-patching.html
---

# Customize patching in Accelerate
<a name="acc-get-customize-patching"></a>

Patching ensures that your software is up-to-date and meets your compliance policies.

**When to patch**: Patching occurs during a *maintenance window*. You can schedule maintenance windows so that patches are only applied during preset times.

**What to patch**: You have to associate the Amazon EC2 instances you want to patch with a maintenance window. To associate the instances with a maintenance window, the Amazon EC2 instances must be tagged, and the maintenance window should have those tags as a target.

**Which patches to install**: Using patch baselines, you set rules to auto-approve certain types of patches, such as operating system or high-severity patches. You can also specify exceptions to your rules, for example, lists of patches that are always approved or rejected.
+ For general patching recommendations, see [Patching recommendations](acc-patching.md#acc-patching-recos).
+ To create custom maintenance windows, see [Create a patch maintenance window in AMS](acc-p-maint-window.md).
+ To create custom patch baselines, see [Custom patch baseline with AMS Accelerate](acc-patch-baseline-custom.md).
+ To route patch alerts to the resource owner, see [Understand patch notifications and patch failures in AMS Accelerate](acc-patch-mon-remediate.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
