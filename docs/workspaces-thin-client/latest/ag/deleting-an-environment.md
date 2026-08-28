---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/deleting-an-environment.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Deleting an environment
<a name="deleting-an-environment"></a>

**Note**
You cannot delete an environment if it has any devices registered to it. First, you must [deregister](resetting-and-deregsitering-a-device.md) and [delete](deleting-a-device.md) all devices in an environment.

1. Select the environment that you want to delete. You can either browse through the dropdown list or you can search the environments by using the search field.

1. Select the **Actions** button.

1. Select **Delete** from the dropdown list. The **Delete environment** confirmation window appears.

1. Type "delete" in the confirmation field.

1. Select the **Delete** button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
