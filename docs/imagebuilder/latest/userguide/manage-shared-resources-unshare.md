---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-shared-resources-unshare.html
---

# Unshare an Image Builder resource from AWS RAM
<a name="manage-shared-resources-unshare"></a>

To unshare an Image Builder resource that you own, such as a shared component, image, or recipe, you must remove it from the AWS Resource Access Manager resource share. You can do this using the AWS RAM console or the AWS CLI.

**Note**
Owners cannot delete a shared resource until it is no longer shared. An owner cannot unshare these resources until none of the consumers depend on them.

**To unshare a shared component, image, or recipe that you own using the AWS Resource Access Manager console**
See [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared component, image, or recipe that you own using the AWS CLI**
Use the **[disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html)** command to stop sharing the resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
