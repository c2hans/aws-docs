---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/create-cid.html
---

# Step 1: Assign an IAM Identity Center User profile
<a name="create-cid"></a>

To create an instance and use the AWS Supply Chain service, you need to either connect an existing IAM Identity Center user profile or create a new one.

1. Open the [AWS Supply Chain console]( https://console.aws.amazon.com/scn/home). You can also search for "AWS Supply Chain" from the main AWS Management Console.

1. If necessary, change the **AWS Region** by selecting **Select a Region** located at the top of the console. Choose your Region from the drop-down list.

1. Select **Create AWS Supply Chain instance**. A notification will appear.
![Email address input field with Continue button for Supply Chain user authentication.](http://docs.aws.amazon.com/connect-decisions/legacy/adminguide/images/idc-email-notification.png)

1. Enter your email address and select **Continue**. IdC will verify if the email matches an existing user.

1. Do one of the following:
   + **If IdC matches the email address to a user** – Select **Connect your identity source and onboard your team**.
**Note**
This can be used if your organization has an established IdC instance that you would like to use for AWS Supply Chain.
   + **If IdC does not find a match to an existing user** – A **Create a New User** notification appears. Proceed to the next step.

1. In the notification, enter the following then select **Continue**:
   + Email address
   + First name
   + Last name

   IdC creates the user automatically and adds them as the AWS Supply Chain administrator.

1. Do one of the following:
   + **To create an instance using standard configuration** – Select **Create**. See [Use standard configuration](create-instance-standard.md).
   + **To create an instance using a custom configuration** – Select **Edit in advanced setup**. See [Use advanced configuration](create-instance-advanced.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
