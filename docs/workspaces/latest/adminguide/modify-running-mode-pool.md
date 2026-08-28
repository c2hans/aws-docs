---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-running-mode-pool.html
---

# Modify the running mode
<a name="modify-running-mode-pool"></a>

You can switch between running modes when a WorkSpaces Pool is in stopped state.

**To modify the running mode of a WorkSpaces Pool**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces** and **Pools**.

1. Select the WorkSpaces Pool to modify and cofirm it’s in stopped state. Then, choose **Actions** and **Modify running mode**.

1. Select the new running mode, **AlwaysOn** or **AutoStop**, and then choose **Save**.

**To modify the running mode of a WorkSpaces Pool using the AWS CLI**
+ Use the [update-workspaces-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/update-workspaces-pool.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
