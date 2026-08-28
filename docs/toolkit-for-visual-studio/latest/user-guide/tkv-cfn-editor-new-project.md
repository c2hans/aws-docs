---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-cfn-editor-new-project.html
---

# Creating an CloudFormation Template Project in Visual Studio
<a name="tkv-cfn-editor-new-project"></a>

 **To create a template project**

1. In Visual Studio, choose **File**, choose **New**, and then choose **Project**.

1. **For Visual Studio 2017**:

   In the **New Project** dialog box, expand **Installed** and select **AWS**.
![New Project dialog box with AWS CloudFormation Project and AWS Lambda Function Project templates.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/CreateNewProject-04-CloudFormation-VS2017.png)

   **For Visual Studio 2019**:

   In the **New Project** dialog box, ensure that the **Language**, **Platform**, and **Project type** drop-down boxes are set to "All ..." and type **aws** in the **Search** field.
![Create a new project dialog box with aws search filter and AWS project templates listed.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/CreateNewProject-04-CloudFormation-VS2019.png)

1. Select the **AWS CloudFormation Project** template.

1. **For Visual Studio 2017**:

   Enter the desired **Name**, **Location**, etc., for your template project, and then click **OK**.

   **For Visual Studio 2019**:

   Click **Next**. In the next dialog, enter the desired **Name**, **Location**, etc., for your template project, and then click **Create**.

1. On the **Select Project Source** page, choose the source of the template you will create:
   +  **Create with empty template** generates a new, empty CloudFormation template.
   +  **Create from existing AWS \|CFN\| stack** generates a template from an existing stack in your AWS account. (The stack doesn't need to have a status of `CREATE_COMPLETE`.)
   +  **Select sample template** generates a template from one of the CloudFormation sample templates.
![New AWS CloudFormation Project dialog with options to create empty template or from existing stack.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/vs-editor-new-template-empty-2.png)

1. To complete the creation of your CloudFormation template project, choose **Finish**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
