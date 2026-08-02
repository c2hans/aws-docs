---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/step-3.-update-the-configuration-files.html
---

# Step 3. Update the configuration files
<a name="step-3.-update-the-configuration-files"></a>

Use the following procedure to customize Landing Zone Accelerator on AWS to fit your environment’s needs. These files are stored in either a CodeCommit repository, S3 bucket, or a custom repository using [AWS CodeConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html) depending on parameters selected during deployment. If you aren’t sure, check the `Configuration Repository Location` parameter of your `AWSAccelerator-Installer` stack.

## Using CodeCommit
<a name="using-codecommit"></a>

1. Sign in to the AWS Management Console and navigate to the **CodeCommit** console. Navigate to the repository named **aws-accelerator-configuration**. The repository shows the Landing Zone Accelerator on AWS configuration files.

1. Each configuration file is named based on its purpose in Landing Zone Accelerator on AWS. A [sample configuration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config) is available on our GitHub repository. Customize each configuration file to deploy the additional AWS services and infrastructure required. You can use the CodeCommit console or a compatible Git client to manipulate these files. For more information, refer to [Edit the contents of a file in a CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-file.html) in the *AWS CodeCommit User Guide*.

1. When finished editing the configuration files, navigate to the AWS CodePipeline console. Select **AWSAccelerator-Pipeline**, then **Release change**. This initiates a new pipeline instantiation and deploy the configuration changes to your environment.

1. Await successful completion of the pipeline. If any failures occur, the CodePipeline console displays the failure stage and action in red. To troubleshoot any errors, choose **Details** on the CodeBuild action to navigate to the failed action. In the CodeBuild console, you can view the **Build logs**, which indicates the error encountered during deployment. For more information, refer to [Troubleshooting](troubleshooting.md).

## Using Amazon S3
<a name="using-s3"></a>

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3).

1. Navigate to the bucket named `aws-accelerator-config-<ACCOUNT_ID> `-` <REGION> `.

1. Download the S3 object `zipped/aws-accelerator-config.zip` and extract the contents to view your Landing Zone Accelerator on AWS configuration files.

1. Each conﬁguration ﬁle is named based on its purpose in Landing Zone Accelerator on AWS. A [sample conﬁguration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config) is available on our GitHub repository. Customize each conﬁguration ﬁle to deploy the additional AWS services and infrastructure required. Make desired changes to these files locally, then save your changes.

1. When you’re ﬁnished editing the conﬁguration ﬁles, compress the files into a new zip archive file named `aws-accelerator-config.zip`. Upload this file to the same S3 object path `zipped/aws-accelerator-config.zip` used in Step 1.
**Note**
The `aws-accelerator-config.zip` file contains all of the files at the root of the zip archive file. The following is an example of using the `tree` command to list the contents:

   ```
                 > tree -a .
                 .
                 ├── accounts-config.yaml
                 ├── global-config.yaml
                 ├── iam-config.yaml
                 ├── network-config.yaml
                 ├── organization-config.yaml
                 ├── security-config.yaml
   ```

1. Sign in to the [AWS CodePipeline console](https://console.aws.amazon.com/codepipeline). Select **AWSAccelerator-Pipeline**, then **Release** change. This initiates a new pipeline instantiation and deploys the conﬁguration changes to your environment.

1. Await successful completion of the pipeline. If failures occur, the CodePipeline console displays the failure stage and action in red. To troubleshoot errors, choose **Details** on the CodeBuild action to navigate to the failed action. In the CodeBuild console, you can view the **Build logs**, which indicate the error encountered during deployment. For more information, refer to [Troubleshooting](troubleshooting.md).

## Using AWS CodeConnections
<a name="using-aws-codeconnections"></a>

1. Sign in to the [Amazon Developer Tools console](https://us-east-1.console.aws.amazon.com/codesuite/home?region=us-east-1).

1. From the left-hand sidebar, select the **Settings** drop down and select **Connections**.

1. On the **Connections** page, select the **Create Connection** button.

1. To create a connection, follow the [Create a connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create.html) user guide in the *Developer Tools console*.
**Note**
When creating a connection, select **Install a new app**, otherwise it is possible the source stage in your pipeline may fail while attempting to connect to your configuration repository

1. After creating the Code Connection successfully, make sure to note the Code Connection ARN.

1. Once you have the Code Connection ARN, you can fill out the following Parameters in the LZA Installer Stack:
   + UseExistingConfigRepo: **Yes**
   + ExistingConfigRepositoryName: **aws-accelerator-config**
   + ExistingConfigRepositoryOwner: **awslabs**
**Note**
This needs to be your 3rd party "owner" or namespace
   + ExistingConfigRepositoryBranchName: **main**
**Note**
This needs to match your branch name in the 3rd party repo
   + ConfigurationRepositoryLocation: **codeconnection**
