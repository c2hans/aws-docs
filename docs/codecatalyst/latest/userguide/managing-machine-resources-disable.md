---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-machine-resources-disable.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Disabling space access for machine resources
<a name="managing-machine-resources-disable"></a>

You can choose to disable machine resources that are in use in your space.

**Important**
Disabling machine resources will remove all permissions to all associated blueprints or workflows in the space.

You must have the **Space administrator** role to manage machine resources.

**To disable machine resources**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space, and then choose **Settings**. Choose **Machine resources**.

1. Choose one of the following.
**Important**
Disabling machine resources will remove all permissions to all associated blueprints or workflows in the space.
   + To disable individually, choose the selector next to one or more machine resources you want to disable. Choose **Disable**, and then choose **This resource**.
   + To disable all resources, choose **Disable**, and then choose **All resources**.
   + To disable all workflow actions, choose **Disable**, and then choose **All workflow actions**.
   + To disable all blueprints, choose **Disable**, and then choose **All blueprints**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
