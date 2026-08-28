---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.work-with-resources.html
---

# Work with cross-account resources in Global Accelerator
<a name="cross-account-resources.work-with-resources"></a>

If your account, or an accelerator that you have permission to access, is specified as a principal in a cross-account attachment in AWS Global Accelerator, you can use resources that have been shared with you from another account.

For example, you can select bring your own IP (BYOIP) addresses as static IP addresses when you create an accelerator, or you can add endpoints to accelerator endpoint groups for an accelerator. The resources that you can add must also be specified in the attachment.

The following sections include the steps to add or remove cross-account attachments in Global Accelerator.

**Topics**
+ [Add cross-account BYOIP addresses](cross-account-resources.add-byoip.md)
+ [Add cross-account endpoints](cross-account-resources.add-endpoints.md)
+ [Remove cross-account endpoints](cross-account-resources.remove-endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
