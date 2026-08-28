---
source_url: https://docs.aws.amazon.com/datatransferterminal/latest/userguide/createteam.html
---

# Create a Transfer team
<a name="createteam"></a>

To access a Data Transfer Terminal facility you’ll need to schedule a reservation in the AWS Management Console. Log into your AWS account to access the Data Transfer Terminal console and complete the following steps to schedule your reservation.

1. From the Data Transfer Terminal home page, select the **Get started** button.

1. If you don’t already have a Transfer team set up in your account, the **Create reservation** button will be disabled. You will need to create and name a Transfer team to begin.

   1. Select the **Create Transfer team** button.

   1. Give the team a name.
      + The name must be between two and 64 characters long, starting with a letter or number.
      + Only use letters, numbers, periods, and dashes. Special characters are not recognized.
      + Do not include any sensitive identifying information.

   1. Create a Transfer team description.
      + Provide a description that helps identify the team, such as describing the purpose of the team for a specific time period, campaign, or project.

   1. Select the **Create Transfer team** button.

      You’ll be returned to the Transfer team page and your newly created team will appear under the **Transfer teams** section.

## Updating Transfer teams on your Data Transfer Terminal account
<a name="edit-teams"></a>

To set up a new Transfer team, refer to the [Schedule a Data Transfer Terminal reservation](setting-up.md) section of this guide.

To modify or remove a Transfer team, do the following:

1. On the **Transfer teams** page, select the Transfer team you would like to modify.

1. To modify the Transfer team name and description, select the **Edit** button.

1. To add or remove personnel, select the **personnel** tab and complete the steps described in the *How do I modify, add, or remove personnel from my account?* section of this FAQ.

1. To add or cancel a reservation for the selected Transfer team, refer to the [Updating personnel on your Data Transfer Terminal account](addusers.md#edit-users) section of this FAQ.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Transfer Terminal. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datatransferterminal` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
