---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-4/ug/control-desktop-state.html
---

# Control your desktop state
<a name="control-desktop-state"></a>

To control your desktop's state:

1. Choose **Actions**.
![Virtual desktops](http://docs.aws.amazon.com/res/archive/release-minus-4/ug/images/res-virtualdesktops.png)

1. Choose **Virtual Desktop State**. You have four states to select from:
   + **Stop**

     A stopped session will not suffer data loss, and you can restart a stopped session at any time.
   + **Reboot**

     Reboots current session.
   + **Terminate**

     Permanently ends a session. Terminating a session may cause data loss if you are using ephemeral storage. You should backup your data to the RES filesystem before terminating.
   + **Hibernate**

     Your desktop state will be saved in memory. When you restart the desktop, your applications will resume but any remote connections may be lost. Not all instances support hibernation, and the option is only available if it was enabled during instance creation. To verify if your instance supports this state, see [Hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
