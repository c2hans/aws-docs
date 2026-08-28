---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you have previously deployed this solution, follow this procedure to update the Landing Zone Accelerator on AWS CloudFormation stack to get the latest version of the solution’s framework.

Before updating the solution, run the Core pipeline [manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) on your current version. [Troubleshoot](troubleshooting.md) any existing issues so that your current version runs smoothly. Performing a dry run of your existing version before proceeding with the following instructions ensures that there is no drift and the environment is stable.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Landing Zone Accelerator on AWS CloudFormation stack, and select **Update**.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the [latest template](https://s3.amazonaws.com/solutions-reference/landing-zone-accelerator-on-aws/latest/AWSAccelerator-InstallerStack.template).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. At minimum, modify the **Branch Name** parameter to the release branch of the version you are updating to. Refer to [Step 1. Launch the stack](step-1.-launch-the-stack.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template might create IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. The CloudFormation stack updates to `UPDATE_COMPLETE` in approximately 10 minutes. The Installer and Core pipelines then run sequentially, which takes an additional 20–60 minutes depending on the number of accounts and regions in your environment.

Updating the stack triggers the Installer pipeline (`AWSAccelerator-InstallerStack*`). After it completes, the Installer pipeline invokes the Core pipeline (`AWSAccelerator-PipelineStack*`). You can monitor both pipelines in the AWS CodePipeline console.

**Note**
If the Installer pipeline does not start automatically, you can invoke it manually. In the AWS CodePipeline console, choose the Installer pipeline, and then choose **Release change**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
