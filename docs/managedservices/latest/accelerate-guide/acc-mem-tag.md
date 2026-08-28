---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tag.html
---

# Accelerate Alarm Manager tags
<a name="acc-mem-tag"></a>

By default, when you onboard with AMS Accelerate, your configuration is deployed to AWS AppConfig, defining an alarm baseline for your resources. The alarm definitions are applied only to resources with the **ams:rt:\*** tags. We recommend that these tags be applied using the [Accelerate Resource Tagger](acc-resource-tagger.md): you set up a basic Resource Tagger configuration in order to let AMS Accelerate know which resources you want managed.

Use Resource Tagger to apply the tag key **ams:rt:ams-managed** with tag value **true** to any resources you want AMS Accelerate to monitor.

**Topics**
+ [Accelerate tags using Resource Tagger](acc-mem-tag-alarms-use-rt.md)
+ [Accelerate tags without Resource Tagger](acc-mem-tags-no-rt.md)
+ [Accelerate tags using CloudFormation](acc-mem-tags-cfn.md)
+ [Accelerate tags using Terraform](acc-mem-tags-terraform.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
