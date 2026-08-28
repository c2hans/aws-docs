---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-2.html
---

# Step 2: Create a Slack application
<a name="slack-step-2"></a>

In this section, you do the following:

1. Create a Slack application in the Slack API Console.

1. Configure the application to add interactive messaging to your bot.

At the end of this section, you get application credentials (Client ID, Client Secret, and Verification Token). In the next step, you use this information to integrate the bot in the Amazon Lex V2 console.

**To create a Slack application**

1. Sign in to the Slack API Console at [https://api.slack.com ](https://api.slack.com).

1. Create an application.

   After you have successfully created the application, Slack displays the **Basic Information** page for the application.

1. Configure the application features as follows:

   1. In the left menu, choose **Interactivity & Shortcuts**.
     + Choose the toggle to turn interactive components on.
     + In the **Request URL** box, specify any valid URL. For example, you can use **https://slack.com**.
**Note**
For now, enter any valid URL to get the verification token that you need in the next step. You will update this URL after you add the bot channel association in the Amazon Lex console.
     + Choose **Save Changes**.

1. In the left menu, in **Settings**, choose **Basic Information**. Record the following application credentials:
   + Client ID
   + Client Secret
   + Verification Token

## Next step
<a name="slack-step-2-next"></a>

[Step 3: Integrate the Slack application with the Amazon Lex V2 bot](slack-step-3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
