---
source_url: https://docs.aws.amazon.com/cloud9/latest/user-guide/settings-aws.html
---

 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

# Working with AWS project and user settings in the AWS Cloud9 IDE
<a name="settings-aws"></a>

AWS service settings, located in the **AWS Settings** pane of the **Preferences** tab, include the following settings:
+ Which AWS Region to use for the **AWS Resources** window
+ Whether to use AWS managed temporary credentials
+ Whether to display the AWS Serverless Application Model (AWS SAM) template editor in plain text or visual mode

To view or change these settings, choose **AWS Cloud9, Preferences** in the menu bar of an IDE for an environment.

In the following lists, project-level settings apply only to the current AWS Cloud9 development environment. In contrast, user-level settings apply across each environment associated with your IAM user. For more information, see [Apply the Current Project Settings for an Environment to Another Environment](settings-project.md#settings-project-apply) and [Share Your User Settings with Another User](settings-user.md#settings-user-share).
+  [Project-Level Settings](#settings-aws-project)
+  [User-Level Settings](#settings-aws-user)

## Project-level settings
<a name="settings-aws-project"></a>

** **AWS Region** **
Which AWS Region to use for the **Lambda** section of the **AWS Resources** window.

** **AWS managed temporary credentials** **
If turned on, AWS managed temporary credentials are used when you call AWS services from the AWS CLI, the AWS CloudShell, or AWS SDK code from an environment. For more information, see [AWS Managed Temporary Credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials).

## User-level settings
<a name="settings-aws-user"></a>

** **Use AWS SAM visual editor** **
If turned on, the AWS Serverless Application Model (AWS SAM) template editor is displayed in visual mode when you use the **Lambda** section of the **AWS Resources** window. If turned off, the editor is displayed in text mode.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud9. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud9` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
