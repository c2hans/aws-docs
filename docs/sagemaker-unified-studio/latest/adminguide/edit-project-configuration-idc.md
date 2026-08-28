---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/edit-project-configuration-idc.html
---

# Edit project configuration
<a name="edit-project-configuration-idc"></a>

You can edit the project name and description, or modify the project members to reflect changes in business context or project scope.

To edit project details, complete the following procedure:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name that you want to edit from the Projects list.

1. On the project details page, choose **Edit**.

1. In the **Edit Project** dialog, modify the **Project name** and **Description**.

1. Choose **Save** to apply your changes.

To edit project members, complete the following procedure:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name that you want to edit from the Projects list.

1. On the project details page, choose the **Members** tab.

1. Choose **Add members**.

1. For **Type**, select IAM or SSO.

1. For **Members**, select the user to add. If you are adding IAM roles or users, the role or user must have the [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) managed policy attached.

1. Choose **Add** to apply your changes.

Your changes are applied immediately. If you added project members, the new members have access to the project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
