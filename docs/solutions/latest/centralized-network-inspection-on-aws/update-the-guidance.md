---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/update-the-guidance.html
---

# Update the guidance
<a name="update-the-guidance"></a>

 If you have previously deployed the guidance, follow this procedure to update the guidance's CloudFormation stack to get the latest version of the guidance's framework.

**Important**
 The Amazon VPC and related resource configuration cannot be updated using the CloudFormation update stack workflow. To update the [VPC CIDR block](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html), you must delete and recreate the VPC. We recommend consulting your network engineering team to obtain a dedicated CIDR block for the inspection VPC.

**Important**
 The guidance version v1.1.0 uses an S3 bucket in place of a CodeCommit repository. Please review all steps in the update instructions before starting the update process as the Code Pipeline resource will be updated to start using an S3 bucket (location `{{BUCKET_NAME}}/centralized-network-inspection-on-aws/configuration`). Refer to Step 12 for the `{{BUCKET_NAME}}`.

1.  Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Centralized Network Inspection on AWS CloudFormation stack, and select **Update**.

1.  Select **Replace current template**.

1.  Under **Specify template**:

   1.  Select **Amazon S3 URL**.

   1.  Copy the link of the [latest template](https://s3.amazonaws.com/solutions-reference/centralized-network-inspection-on-aws/latest/centralized-network-inspection-on-aws.template).

   1.  Paste the link in the **Amazon S3 URL** box.

   1.  Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1.  Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 2. Launch the Stack](step-2-launch-the-stack.md).

1.  Choose **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1.  Choose **View change set** and verify the changes.

1.  Choose **Update stack** to deploy the stack.

1. You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an UPDATE\_COMPLETE status in approximately 7–10 minutes.

1. Once the update is complete, the code pipeline resource will have a new S3 bucket source stage instead of CodeCommit source code.

1. The guidance stack outputs will display the key `CodeBuildsourcecodebucket`. The value of this key should replace documentation references of `{{BUCKET_NAME}}`.

1. Go to the S3 bucket location `{{BUCKET_NAME}}/centralized-network-inspection-on-aws/configuration` and download the archive file `centralized-network-inspection-on-aws.zip` and unzip the archive to a new folder.

1. Make sure to sync all the files from the CodeCommit repository previously being used by the pipeline to the folder created in the Step 13.

1. Once the files are reviewed to have all the changes from the CodeCommit repository, create a new archive file `centralized-network-inspection-on-aws.zip` and upload it to the S3 bucket location from Step 13.

1. Once the file has been successfully uploaded into the S3 bucket, go to the CodePipeline resource and release the changes.

1. After the update is completed in the AWS CloudFormation Console, there will be no reference to the CodeCommit repository in the guidance.

## Update the Network Firewall log destination
<a name="update-the-network-firewall-log-destination"></a>

 If you previously deployed this guidance, any updates made to the stack will require you to manually initiate CodePipeline to update to the Network Firewall log destination. The Network Firewall configuration should not be updated to manually release changes. To start the AWS CodePipeline manually, refer to [Start a pipeline manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) in the *AWS CodePipeline User Guide*.

 To modify the AWS Network Firewall, firewall policy, and rule groups, refer to [Configuring resources for network firewall](configuring-resources-for-network-firewall.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
