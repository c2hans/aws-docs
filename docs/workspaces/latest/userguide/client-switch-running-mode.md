---
source_url: https://docs.aws.amazon.com/workspaces/latest/userguide/client-switch-running-mode.html
---

# Switching running mode for a WorkSpace
<a name="client-switch-running-mode"></a>

You can specify whether your WorkSpace is always running or whether it stops after a specified period of inactivity. WorkSpaces provides the following two running modes that you can choose from.
+ **AlwaysOn** — Keeps your WorkSpace always running.
+ **AutoStop** — Your WorkSpace starts when you sign in and stops after a specified period of inactivity. After your WorkSpace stops, the state of your apps and data is saved.

**Note**
Switching your WorkSpace running mode will change the amount that your organization pays for your WorkSpace.

## To switch your WorkSpace running mode for 3.0\+ clients
<a name="client-switch-running-mode-new-clients"></a>

1. Open your WorkSpaces client and connect to your WorkSpace.

1. Choose **Settings**, **Switch Running Mode**.

1. In the **Switch Running Mode** dialog box, choose a different running mode, and then choose **Switch**.

1. A message confirms your choice. Close the message box.

## To switch your WorkSpace running mode for 1.0\+ and 2.0\+ clients
<a name="client-switch-running-mode-credentials-legacy-clients"></a>

1. Open your WorkSpaces client and connect to your WorkSpace.

1. Choose **My WorkSpace**, **Switch running mode**.

1. In the **Switch running mode** dialog box, choose a different running mode, and then choose **Switch**.

1. A message confirms your choice. Choose **Close**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
