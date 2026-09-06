---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/deployment-process-overview.html
---

# Deployment using installer CloudFormation template
<a name="deployment-process-overview"></a>

This solution uses AWS CloudFormation templates and stacks to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources described in the template.

 **Time to deploy:** Approximately five minutes for the installer CloudFormation stack and up to 45 minutes for the sample configuration you choose to deploy with.

## Prerequisites
<a name="prerequisites"></a>

Before you deploy the Modern Data Architecture Accelerator, verify you have the following prerequisites in place:

### AWS Account Requirements
<a name="aws-account-requirements"></a>
+ An AWS account with permissions to create the required resources
+ IAM permissions to create roles, policies, and CloudFormation stacks
+ Sufficient service quotas for the resources that will be deployed (varies based on the sample configuration you choose)

### Networking Requirements
<a name="networking-requirements"></a>
+ If you plan to deploy resources that require VPC connectivity (such as Amazon Redshift):
  + An existing VPC with at least one subnet
  + The subnet must have internet access for the deployment process
  + Security groups configured to allow necessary traffic

### GitHub Integration (if using GitHub as source)
<a name="github-integration-if-using-github-as-source"></a>
+ A GitHub account with access to the repository containing the solution code
+ A GitHub CodeConnect connection established between AWS and GitHub (instructions provided in the next section)

### S3 Integration (if using S3 as source)
<a name="s3-integration-if-using-s3-as-source"></a>
+ An S3 bucket where you’ve uploaded the solution code zip file
+ Appropriate permissions to access the S3 bucket from your AWS account

### Technical Knowledge
<a name="technical-knowledge"></a>
+ Basic understanding of AWS services and CloudFormation
+ Familiarity with data architecture concepts
+ Understanding of the AWS Management Console

### Browser Requirements
<a name="browser-requirements"></a>
+ A modern web browser (Chrome, Firefox, Safari, or Edge)
+ JavaScript enabled

**Tip**
Before proceeding with deployment, we recommend reviewing the architecture overview and cost sections of this guide to understand the solution components and potential costs.

### AWS Account Requirements
<a name="aws-account-requirements-2"></a>
+ An AWS account with permissions to create the required resources
+ IAM permissions to create roles, policies, and CloudFormation stacks
+ Sufficient service quotas for the resources that will be deployed (varies based on the sample configuration you choose)

### Networking Requirements
<a name="networking-requirements-2"></a>
+ If you plan to deploy resources that require VPC connectivity (such as Amazon Redshift):
  + An existing VPC with at least one subnet
  + The subnet must have internet access for the deployment process
  + Security groups configured to allow necessary traffic

### GitHub Integration (if using GitHub as source)
<a name="github-integration-if-using-github-as-source-2"></a>
+ A GitHub account with access to the repository containing the solution code
+ A GitHub CodeConnect connection established between AWS and GitHub (instructions provided in the next section)

### S3 Integration (if using S3 as source)
<a name="s3-integration-if-using-s3-as-source-2"></a>
+ An S3 bucket where you’ve uploaded the solution code zip file
+ Appropriate permissions to access the S3 bucket from your AWS account

### Technical Knowledge
<a name="technical-knowledge-2"></a>
+ Basic understanding of AWS services and CloudFormation
+ Familiarity with data architecture concepts
+ Understanding of the AWS Management Console

### Browser Requirements
<a name="browser-requirements-2"></a>
+ A modern web browser (Chrome, Firefox, Safari, or Edge)
+ JavaScript enabled

**Tip**
Before proceeding with deployment, we recommend reviewing the architecture overview and cost sections of this guide to understand the solution components and potential costs.

## Source of the Solution Code
<a name="source-of-the-solution-code"></a>

The CloudFormation stack will deploy a CodePipeline pipeline. That pipeline needs to know where the solution source code is. Customers can have the source in a zipped file uploaded to S3 or point the stack to a GitHub repository. For GitHub repository, which is the default, follow these steps.

### Create a GitHub CodeConnect connection
<a name="create-a-github-codeconnect-connection"></a>

The CloudFormation installer stack requires a GitHub CodeConnect connection to access the Modern Data Architecture Accelerator code on GitHub. For detailed instructions on creating a GitHub connection, see [Working with GitHub connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html) in the AWS CodePipeline User Guide.

Follow these steps to create a connection:

1. Navigate to the AWS Developer Tools console and select **Settings** > **Connections**

1. Choose **Create connection**

1. Select **GitHub** as the provider and enter a connection name (e.g., "MDAA-GitHub-Connection")

1. Choose **Connect to GitHub**

1. When prompted, sign in to your GitHub account and authorize the connection

1. After authorization, the connection will be established automatically when created through the console

1. Copy the ARN of the connection for use in the CloudFormation stack

**Note**
If you create the GitHub connection using the AWS CLI instead of the console, the connection will be in a "Pending" status and you’ll need to complete additional steps to update the pending connection through the console.

## Launch the installer stack
<a name="launch-the-installer-stack"></a>

This section provides instructions for deploying the Modern Data Architecture Accelerator CloudFormation template.

### Step 1. Launch the stack
<a name="step-1-launch-the-stack"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the button to launch the Modern Data Architecture Accelerator CloudFormation template.

    [![Launch solution](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fmodern-data-architecture-accelerator%2Flatest%2FMdaaInstallerStack.template&redirectId=SolutionWeb)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is shown in the **Amazon S3 URL** text box and choose **Next**.

### Step 2. Specify stack details
<a name="step-2-specify-stack-details"></a>

1. On the **Specify stack details** page, assign a name to your solution stack.
**Important**
The stack name must be unique within your AWS account. Consider including the sample name in the stack name if you plan to deploy multiple samples, for example, `mdaa-basicdatalake-<accountname>-<region>`.

1. Under **Parameters**, review and modify the parameters for this solution template as needed. The following table describes each parameter.

| Parameter | Default value | Description |
| --- | --- | --- |
|  **OrgName**  |  ` <requires input> `  | The organization name. This will be prefixed to all stacks and generated resources. |
|  **Source**  |  `github`  | Specify the source of the solution code. Valid options: \* `github` - Use a GitHub repository \* `S3` - Use a zipped file in an S3 bucket |
|  **Repository Owner**  |  `aws`  | The owner of the GitHub repository hosting the solution code. |
|  **Repository Name**  |  `modern-data-architecture-accelerator`  | The name of the GitHub repository hosting the solution code. |
|  **Branch Name**  |  `main`  | The name of the git branch to use for installation. The Branch Name parameter defaults to the latest release branch name. To determine the branch name, navigate to the Modern Data Architecture Accelerator on AWS GitHub branches page and choose the release branch you want to deploy. Release branch names align with the semantic versioning of our GitHub releases.  |
|  **GitHub CodeConnect Connection ARN**  |  ` <requires input> ` (required when using GitHub as source) | The ARN of the GitHub CodeConnect connection you created in the prerequisites step. |
|  **Repository Bucket Name**  |  ` <requires input> ` (required when using S3 as source) | The name of the S3 bucket where the zip file of the source is stored. |
|  **Repository Bucket Object**  |  `release/latest.zip` (required when using S3 as source) | The key of the S3 object containing the zipped source code. |
|  **Sample Name**  |  `basic_datalake`  | Sample configuration to deploy with the solution. Allowed values: \* `basic_datalake` \* `basic_datascience_platform` \+ For other starter kits (Minimal, Lakehouse Analytics, MLOps Platform, GenAI Foundation, GAIA Chatbot, DataZone Governed Lakehouse, SMUS Research Environment, SMUS Data Mesh), use the Manual CLI Deploy Method described below. |
|  **Subnet Id**  | (optional) | The subnet ID for resources that require VPC connectivity, such as Amazon Redshift. |
|  **VPC Id**  | (optional) | The VPC ID for resources that require VPC connectivity, such as Amazon Redshift. |

### Step 3. Configure stack options
<a name="step-3-configure-stack-options"></a>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next.**

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template might create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately five minutes.

## Await initial environment deployment
<a name="await-initial-environment-deployment"></a>

Use the following procedure to confirm the Modern Data Architecture Accelerator deploys the configuration to your environment.

1. Sign in to the AWS Management Console and navigate to the **AWS CodePipeline** console. The pipeline with the name you designated should show a status of either `In Progress` or `Complete`. If `In Progress`, wait for the pipeline to complete.

1. Go to CloudFormation page again and you will see new Stacks corresponding to the modules of the solution starting to appear one after another.

1. The pipeline takes approximately 45 minutes to complete, though some sample configurations such as `basic_datalake` will take less.

1. After all the stacks complete successfully, the installer pipeline will finish with a COMPLETE status.
