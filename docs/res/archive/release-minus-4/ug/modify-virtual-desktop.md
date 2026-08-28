---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-4/ug/modify-virtual-desktop.html
---

# Modify a virtual desktop
<a name="modify-virtual-desktop"></a>

You can update the hardware of your virtual desktop or change the session name.

1. Before making changes to the instance size, you must stop the session:

   1. Choose **Actions**.
![Virtual desktops](http://docs.aws.amazon.com/res/archive/release-minus-4/ug/images/res-virtualdesktops.png)

   1. Choose **Virtual Desktop State**.

   1. Choose **Stop**.
**Note**
You cannot update the desktop size for hibernated sessions.

1. Once you have confirmed the desktop has stopped, choose ** Actions** and then choose **Update Session**.

1. Change the session name or choose the desktop size you would like.

1. Choose **Submit**.

1. Once your instances updates, restart your desktop:

   1. Choose **Actions**.

   1. Choose **Virtual Desktop State**.

   1. Choose **Start**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
