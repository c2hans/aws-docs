---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/emergency-admin-login.html
---

# Emergency login to the Connect Customer admin website
<a name="emergency-admin-login"></a>

As a best practice, users assigned to the Connect Customer **Admin** security profile should always use their Connect Customer instance URL to login:
+ Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

This method ensures the appropriate levels security.

However, if there's an emergency, you can log in from the Connect Customer console using your AWS account credentials. For example, you might need to login in this way in the following situations:
+ You forgot your Connect Customer administrator password and no other Connect Customer administrators are around to reset it.
+ Someone deleted the Connect Customer **Admin** security profile by mistake.

**To login for emergency access**

1. Make sure you have your AWS account credentials at hand and that you have the [required permissions](security-iam-amazon-connect-permissions.md#federations).

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. If prompted to login, enter your AWS account credentials.

1. Choose the name of the instance from the **Instance alias** column.
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the navigation pane, choose **Overview**.

1. Choose **Log in for emergency access**.

   You aren't prompted for your credentials because you are federated in from the AWS console.
**Important**
For daily usage, we strongly recommend always using your instance URL to login. The procedure provided in this article should only be used for emergency access when using the instance URL is not an option.

**To log out**
To log out of your instance, go to the title bar at the top of the screen and select the icon with the arrow (**Log out**) that appears next to your user name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
