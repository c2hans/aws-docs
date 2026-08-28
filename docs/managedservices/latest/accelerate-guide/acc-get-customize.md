---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-get-customize.html
---

# Step 4. Customize features in Accelerate
<a name="acc-get-customize"></a>

In this stage, you have already onboarded monitoring, patching, and backup with default policies. Now you have the opportunity to customize policies to suit your needs.

You can choose to use the default policies for patch, backup or monitoring, or choose a custom policy based on your needs. AMS uses tags to associate resources to operational policies. AMS provides a Resource Tagger that allows you to specify rules on how tags are applied to your AWS resources based on application grouping or other grouping logic For more information, see [Accelerate Resource Tagger](acc-resource-tagger.md).

The customer-provided tags feature allows you to add and delete custom tags to AMS resources. For more information, see [Customer-provided tags in Accelerate](acc-tag-cust-provided.md).

**Topics**
+ [Customize monitoring in Accelerate](acc-get-customize-monitoring.md)
+ [Customize backup in Accelerate](acc-get-customize-backup.md)
+ [Customize patching in Accelerate](acc-get-customize-patching.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
