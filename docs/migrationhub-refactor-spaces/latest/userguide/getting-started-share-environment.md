---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-share-environment.html
---

AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform).

# Step 3: Share your environment
<a name="getting-started-share-environment"></a>

This step describes how to share an environment as part of the Refactor Spaces **Getting started** wizard. You can also share an environment by choosing **Share environment** under **Quick actions** in the Refactor Spaces navigation pane.

Environments are shared with other AWS accounts using AWS Resource Access Manager (AWS RAM). An environment share must be accepted by the invited account within twelve hours. Otherwise, the environment must be shared again. If you’re in an AWS organization, then you can enable auto-accepting of shares. AWS RAM supports sharing environments with other AWS accounts, organizational units (OUs) in AWS Organizations, or an entire AWS organization.

Because environments are containers of applications, services, routes, and orchestrated AWS resources, sharing the environment provides some access to these resources from the invited accounts. After sharing with other accounts, users in those accounts can create applications, services, and routes within the environment, unless you use AWS Identity and Access Management (IAM) to restrict access.

When sharing an environment with another AWS account, Refactor Spaces also shares the environment’s transit gateway with the other account by orchestrating AWS RAM.

**To share an environment**

1. Select one of the following principal types to share your environment with:
   + AWS account
   + Organization - entire AWS organization
   + Organizational unit (OU)

   AWS RAM supports sharing environments with other AWS accounts, organizational units (OUs) in AWS Organizations, or an entire AWS organization.

1. Environments are shared with other AWS accounts using AWS Resource Access Manager (AWS RAM). AWS RAM supports sharing environments with other AWS accounts, organizational units (OUs) in AWS Organizations, or an entire AWS organization. If you want to share an environment with an entire AWS organization or OU, you must enable sharing with the organization in AWS RAM before trying to share in Refactor Spaces.

1. Enter the AWS account of the principal, and then choose **Add**.

1. Choose **Next** to move to the **Review** page.

1. Review the information you entered in the previous steps.

1. If everything looks correct, choose **Create environment**. If you want to change something, choose **Previous**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
