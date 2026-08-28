---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/using-codepipeline.html
---

# Using CodePipeline to deploy Terraform and CloudFormation templates
<a name="using-codepipeline"></a>

In the DPA, you use building blocks for AWS CodePipeline to create accelerators for Terraform and CloudFormation IaC. This section describes the following for this use case:
+ Standardized pipeline structure
+ Reusable stages and jobs
+ Integrated tools for security scans

The DPA repository contains folders for [Terraform](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/aws-codepipeline/terraform) and [CloudFormation](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/aws-codepipeline/cloudformation). Each of these folders contains the following two subfolders:
+ **pipeline-modules** – This folder contains the code for deploying the standardized pipeline structure.
+ **shared** – This folder contains ready-to-use buildspec files for the DPA stages and jobs.

## Prerequisites
<a name="prerequisites-codepipeline"></a>
+ An active AWS account
+ Permissions to provision resources using IaC templates
+ Permissions to create AWS CodeCommit repositories and CodePipeline components

## Tools
<a name="tools-codepipeline"></a>
+ [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) is a linter that checks CloudFormation YAML or JSON templates against the [AWS CloudFormation resource specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html). It also performs other checks, such as checking for valid values for resource properties and adherence to best practices.
+ [cfn\_nag](https://github.com/stelligent/cfn_nag) is an open source tool that identifies potential security issues in CloudFormation templates by searching for patterns.
+ [Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) is a static code-analysis tool that checks IaC for security and compliance misconfigurations.
+ [TFLint](https://github.com/terraform-linters/tflint) is a linter that checks Terraform code for potential errors and adherence to best practices.
+ [tfsec](https://github.com/aquasecurity/tfsec) is a static code-analysis tool that checks Terraform code for potential misconfigurations.

## Instructions
<a name="instructions-codepipeline"></a>

### Create CodeCommit repositories
<a name="create-9999999999999999acc--repositories.544b9fa5-5fb9-5ad4-8bae-cfdade62bd65"></a>

1. Create two separate CodeCommit repositories as follows:
   + `common-repo` – This repository contains the shared libraries, buildspec files, and dependencies.
   + `app-repo` – This repository contains the Terraform or CloudFormation templates to deploy your infrastructure.

   For instructions, see [Create an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html).

1. In the `common-repo` repo, create a folder named `shared`. Copy the buildspec files from the [Terraform](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/aws-codepipeline/terraform/shared) or [CloudFormation](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/aws-codepipeline/cloudformation/shared) **shared **folder in the GitHub DPA repo to the new folder. For instructions, see [Create or add a file to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-file.html).

1. In the `app-repo` repository, create a folder named `entrypoint`. Copy the file from the [Terraform](https://github.com/aws-samples/aws-devops-pipeline-accelerator/blob/main/examples/aws_codepipeline/terraform/entrypoint/terraform-infrastructure.json) or [CloudFormation](https://github.com/aws-samples/aws-devops-pipeline-accelerator/blob/main/examples/aws_codepipeline/cloudformation/entrypoint/config.json) **entrypoint** folder in the GitHub DPA repo to the new folder. For more information about these files, see [Understanding the entry point JSON file](#understanding-json-file).

1. Review the [Terraform](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/examples/aws_codepipeline/terraform) or [CloudFormation](https://github.com/aws-samples/aws-devops-pipeline-accelerator/tree/main/examples/aws_codepipeline/cloudformation) **examples** directory, and then structure your `app-repo` folder according to these examples. These directories contain examples for deploying an Amazon Elastic Compute Cloud (Amazon EC2) instance or Amazon Simple Storage Service (Amazon S3) bucket.

1. Continue to the one of the following two sections:
   + Create the pipeline and define stages (Terraform)
   + Create the pipeline and define stages (CloudFormation)

### Create the pipeline and define stages (Terraform)
<a name="create-the-pipeline-and-define-stages--terraform-.0df878d0-67ed-5fcb-9d26-c3854e2b4423"></a>

1. Clone the[ DevOps Pipeline Accelerator (DPA) repository](https://github.com/aws-samples/aws-devops-pipeline-accelerator) from GitHub to your local workstation.

1. In the cloned repository, navigate to the `aws-codepipeline/terraform/pipeline-modules` folder.

1. In the **terraform.tfvars** file, update and validate the Terraform state and AWS Identity and Access Management (IAM) role-specific variables.

1. Create a Docker image. For instructions, see [Docker image creation for using in CodeBuild](https://github.com/aws-samples/aws-devops-pipeline-accelerator/blob/main/shared-docker/docker-images/README.md) (GitHub).

1. Update the `builder_image` variable that is defined in the **terraform.tfvars** file.

1. Enter the following commands. This initializes, previews, and deploys the infrastructure through Terraform.

   ```
   terraform init
   terraform plan
   terraform apply
   ```

1. Sign in to the AWS account. In the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home), confirm that the new pipeline has been created.
**Note**
If the first run is in a `failed` state, repeat the previous step.

1. When the new CodePipeline pipeline is created, a new IAM role for AWS CodeBuild is created automatically. The name of this automatically created role ends in `-codebuild-role`. Update this role with the permissions that are required to deploy your infrastructure.

### Create the pipeline and define stages (CloudFormation)
<a name="create-the-pipeline-and-define-stages--9999999999999999cfnshort--.e6bef383-b775-5767-af55-d60c295e5735"></a>

1. Clone the[ DevOps Pipeline Accelerator (DPA) repository](https://github.com/aws-samples/aws-devops-pipeline-accelerator) from GitHub to your local workstation.

1. In the cloned repository, navigate to the `aws-codepipeline/cloudformation/pipeline-modules` folder.

1. Deploy the **pipeline-cft.yaml** CloudFormation template. The following are the required parameters that you must pass to the stack.
   + `ArtifactsBucket` – Name of the repo that contains the pipeline artifacts to be updated
   + `EcrDockerRepository` – Uniform resource identifier (URI) of the Amazon ECR repository with the `image` tag
   + `CodeCommitAppRepo` – Name of the CodeCommit repository that contains the templates
   + `CodeCommitBaseRepo` – Name of the CodeCommit repository that contains the shared files
   + `CodeCommitRepoBranch` – Name of the CodeCommit repository branch
   + `SNSMailAddress` – Email address that will receive Amazon Simple Notification Service (Amazon SNS) notifications about pipeline status

   For instructions, see [Working with stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the CloudFormation documentation.

1. Sign in to the AWS account. In the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home), confirm that the new pipeline has been created.

1. When the new CodePipeline pipeline is created, a new IAM role for AWS CodeBuild is created automatically. The name of this automatically created role ends in `-codebuild-role`. Update this role with the permissions that are required to deploy your infrastructure.

## Understanding the entry point JSON file
<a name="understanding-json-file"></a>

### Terraform entry point file
<a name="terraform-entry-point-file.cb77ea9e-0aae-56d1-bfec-d4f4df3b0efd"></a>

This is the main configuration file. In this file, you can customize and enable or disable a stage. If you disable a stage, it does not delete or remove the stage from the pipeline. Instead, the stage is skipped during runtime.

```
{
    "build_stage_required" : "true",
    "test_stage_required" : "true",
    "predeploy_stage_required": "true",
    "deploy_stage_required": "true",
    "postdeploy_stage_required": "true",
    "destroy_stage_required": "true",
    "bucket":"tf-state-dpa",                # S3 bucket used for Terraform backend
    "key":"terraform_test.tfstate",         # S3 key to be used
    "region":"us-east-1",
    "dynamodb_table":"tf-state-dpa"         # DynamoDB Table for Terraform backend
}
```

### CloudFormation entry point file
<a name="9999999999999999cfnshort--entry-point-file.dc44e117-831e-597e-ba95-66a1cf99b6ba"></a>

This is the main configuration file. In this file, you customize stages and enable or disable them. If you disable a stage, it does not delete or remove the stage from the pipeline. Instead, the pipeline skips the stage during runtime.

```
{
    "init_stage_required" : "true",
    "test_stage_required" : "true",
    "createinfra_stage_required": "true",
    "envType" : "cloudformation",
    "stage_required" : "true",
    "cft_s3_bucket" : "pipeline-bucket",               #S3 bucket from the destination account to keep CFT templates
    "stack_name" : "aws-cft-poc",                      #CloudFormation stack name
    "account" : "************",                        #Destination AWS account to deploy stack
    "roleName" : "codestack-poc-cross-account-role",   #Cross-account IAM role name
    "region" : "us-east-1",
    "destroy_stack" : "false"                          #To destroy the provisioned stack, set this value to "true"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
