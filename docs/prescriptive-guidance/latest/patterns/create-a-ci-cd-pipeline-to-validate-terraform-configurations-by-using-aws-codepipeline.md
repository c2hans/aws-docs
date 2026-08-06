---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline.html
---

# Create a CI/CD pipeline to validate Terraform configurations by using AWS CodePipeline
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline"></a>

*Aromal Raj Jayarajan and Vijesh Vijayakumaran Nair, Amazon Web Services*

## Summary
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-summary"></a>

This pattern shows how to test HashiCorp Terraform configurations by using a continuous integration and continuous delivery (CI/CD) pipeline deployed by AWS CodePipeline.

Terraform is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources. The solution provided in this pattern creates a CI/CD pipeline that helps you validate the integrity of your Terraform configurations by running five [CodePipeline stages](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-stages):

1. `"checkout"` pulls the Terraform configuration that you’re testing from an AWS CodeCommit repository.

1. `"validate"` runs infrastructure as code (IaC) validation tools, including [tfsec](https://github.com/aquasecurity/tfsec), [TFLint](https://github.com/terraform-linters/tflint), and [checkov](https://www.checkov.io/). The stage also runs the following Terraform IaC validation commands: `terraform validate` and `terraform fmt`.

1. `"plan"` shows what changes will be applied to the infrastructure if the Terraform configuration is applied.

1. `"apply"` uses the generated plan to provision the required infrastructure in a test environment.

1. `"destroy"` removes the test infrastructure that was created during the `"apply"` stage.

## Prerequisites and limitations
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), installed and configured on your local machine
+ [Terraform](https://learn.hashicorp.com/collections/terraform/aws-get-started?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS), installed and configured on your local machine

**Limitations**
+ This pattern’s approach deploys AWS CodePipeline into one AWS account and AWS Region only. Configuration changes are required for multi-account and multi-Region deployments.
+ The AWS Identity and Access Management (IAM) role that this pattern provisions (**codepipeline\_iam\_role**) follows the principle of least privilege. This IAM role’s permissions must be updated based on the specific resources that your pipeline needs to create.** **

**Product versions**
+ AWS CLI  version 2.9.15 or later
+ Terraform version 1.3.7 or later

## Architecture
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-architecture"></a>

**Target technology stack**
+ AWS CodePipeline
+ AWS CodeBuild
+ AWS CodeCommit
+ AWS IAM
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Key Management Service (AWS KMS)
+ Terraform

**Target architecture**

The following diagram shows an example CI/CD pipeline workflow for testing Terraform configurations in CodePipeline.

![Architecture to test Terraform configurations by using an AWS CI/CD pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4df7b1f8-8eef-4d85-a971-a7f158be9691/images/90b931c8-e745-4b52-92de-a367fb0f1f51.png)

The diagram shows the following workflow:

1. In CodePipeline, an AWS user initiates the actions proposed in a Terraform plan by running the `terraform apply` command in the AWS CLI.

1. AWS CodePipeline assumes an IAM service role that includes the policies required to access CodeCommit, CodeBuild, AWS KMS, and Amazon S3.

1. CodePipeline runs the `"checkout"` pipeline stage to pull the Terraform configuration from an AWS CodeCommit repository for testing.

1. CodePipeline runs the `"validate"` stage to test the Terraform configuration by running IaC validation tools and running Terraform IaC validation commands in a CodeBuild project.

1. CodePipeline runs the `"plan"` stage to create a plan in the CodeBuild project based on the Terraform configuration. The AWS user can review this plan before the changes are applied to the test environment.

1. Code Pipeline runs the `"apply"` stage to implement the plan by using the CodeBuild project to provision the required infrastructure in the test environment.

1. CodePipeline runs the `"destroy"` stage, which uses CodeBuild to remove the test infrastructure that was created during the `"apply"` stage.

1. An Amazon S3 bucket stores pipeline artifacts, which are encrypted and decrypted by using an AWS KMS [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk).

## Tools
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-tools"></a>

**Tools**

*AWS services*
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

*Other services*
+ [HashiCorp Terraform](https://www.terraform.io/docs) is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources.

**Code **

The code for this pattern is available in the GitHub [aws-codepipeline-terraform-cicdsamples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository. The repository contains the Terraform configurations required to create the target architecture outlined in this pattern.

## Epics
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-epics"></a>

### Provision the solution components
<a name="provision-the-solution-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | Clone the GitHub [aws-codepipeline-terraform-cicdsamples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository by running the following command in a terminal window:<pre>git clone https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples.git</pre><br />For more information, see [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) in the GitHub documentation. | DevOps engineer |
| Create a Terraform variable definitions file.  | Create a `terraform.tfvars` file based on your use case requirements. You can update the variables in the `examples/terraform.tfvars` file that’s in the cloned repository.<br />For more information, see [Assigning values to root module variables](https://developer.hashicorp.com/terraform/language/values/variables#assigning-values-to-root-module-variables) in the Terraform documentation.The repository’s `Readme.md` file includes more information on the required variables. | DevOps engineer |
| Configure AWS as the Terraform provider. | 1. In a code editor, open the cloned repository’s `main.tf` file.<br />2. Add the necessary configurations for establishing connectivity to the target AWS account.For more information, see [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) in the Terraform documentation. | DevOps engineer |
| Update the Terraform provider configuration for creating the Amazon S3 replication bucket. | 1. Open the repository’s `S3` directory by running the following command:<pre>cd ./modules/s3</pre><br />2. Update the Terraform provider configuration for creating the Amazon S3 replication bucket by updating the `region` value in the `tf`** **file. Make sure that you enter the Region that you want Amazon S3 to replicate objects to.<br />3. **(Optional)** By default, Terraform uses local state files for state management. If you want to add Amazon S3 as the remote backend, you must update the Terraform configuration. For more information, see [Backend configuration](https://developer.hashicorp.com/terraform/language/backend) in the Terraform documentation.Replication activates automatic, asynchronous copying of objects across Amazon S3 buckets. | DevOps engineer |
| Initialize the Terraform configuration. | To initialize your working directory that contains the Terraform configuration files, run the following command in the cloned repository’s root folder:<pre>terraform init</pre> | DevOps engineer |
| Create the Terraform plan. | To create a Terraform plan, run the following command in the cloned repository’s root folder:<pre>terraform plan --var-file=terraform.tfvars -out=tfplan</pre>Terraform evaluates the configuration files to determine the target state for the declared resources. It then compares the target state against the current state and creates a plan. | DevOps engineer |
| Verify the Terraform plan. | Review the Terraform plan and confirm that it configures the required architecture in your target AWS account. | DevOps engineer |
| Deploy the solution. | 1. To apply the Terraform plan, run the following command in the cloned repository’s root folder:<pre>terraform apply "tfplan"</pre><br />2. Enter **yes** to confirm that you want to deploy the resources.Terraform creates, updates, or destroys infrastructure to achieve the target state declared in the configuration files. | DevOps engineer |

### Validate Terraform configurations by running the pipeline
<a name="validate-terraform-configurations-by-running-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the source code repository. | 1. From the Terraform output, get the **source repository** details for the repository that contains the Terraform configurations that you want to validate.<br />2. Sign in to the AWS Management Console. Then, open the [CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).<br />3. Create a new branch in the source repository named `main`. For instructions, see [Create a branch in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-branch.html) in the CodeCommit documentation.<br />4. Clone the `main` branch of the **source repository** to your local workstation. For instructions, see [Setup steps for HTTPS connections to AWS CodeCommit repositories on Windows with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html) in the CodeCommit documentation.<br />5. Copy the** **`templates` folder from the GitHub [aws-codepipeline-terraform-cicdsamples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository by running the following command:<pre>cp -r templates $YOUR_CODECOMMIT_REPO_ROOT</pre>The `templates` folder contains the build specification files and the validation script for the root directory of the source repository.<br />6. Add your required Terraform IaC configurations to the root folder of the **source repository**.<br />7. Add the details for the remote backend in your project's Terraform configuration. For more information, see [S3](https://developer.hashicorp.com/terraform/language/settings/backends/s3) in the Terraform documentation.<br />8. **(Optional)** Update the variables in the `templates` folder to either activate or deactivate the preconfigured scans, tool change versions, and to specify your directory in custom script files. For more information, see the *Additional information* section of this pattern.<br />9. Push the changes to the `main` branch of the **source repository**. | DevOps engineer |
| Validate the pipeline stages. | 1. Sign in to the AWS Management Console and open the [CodePipeline console](http://console.aws.amazon.com/codesuite/codepipeline/home).<br />2. In the output generated from the `terraform apply "tfplan"` command in the previous Epic section, find the name of the generated **CodePipeline**.<br />3. Open the pipeline in the CodePipeline console and choose **Release change**.<br />4. Review each pipeline stage and confirm it’s working as expected.For more information, see [View pipeline details and history (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-console.html) in the *AWS CodePipeline User Guide*.When a change is committed to the main branch of the source repository, the test pipeline is activated automatically. | DevOps engineer |
| Verify the report output. | 1. On the [CodePipeline console](http://console.aws.amazon.com/codesuite/codepipeline/home), in the left navigation pane, choose **Build**. Then, choose **Report history**.<br />2. Review the tfsec and checkov scan reports that the pipeline generates. These reports can help you identify issues through visualizations and graphical representations.The `<project_name>-validate` CodeBuild project generates vulnerability reports for your code during the `"validate"` stage. | DevOps engineer |

### Clean up your resources
<a name="clean-up-your-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the pipeline and associated resources. | To delete the test resources from your AWS account, run the following command in the cloned repository’s root folder:<pre>terraform destroy --var-file=terraform.tfvars</pre> | DevOps engineer |

## Troubleshooting
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| You receive an **AccessDenied **error during the `"apply"` stage. | 1. Review the execution logs of the CodeBuild project associated with the `"apply"` stage to identify any missing IAM permissions. For more information, see [View build details in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html) in the *AWS CodeBuild User Guide*.<br />2. In a code editor, open the cloned repository’s `modules`** **folder. Then, navigate to the `iam-role` folder and open the `main.tf` file that’s in that folder.<br />3. In the `codepipeline_policy` statement, add the IAM policies that are required for provisioning resources in your AWS account. |

## Related resources
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-resources"></a>
+ [Module blocks](https://developer.hashicorp.com/terraform/language/modules/syntax) (Terraform documentation)
+ [How to use CI/CD to deploy and configure AWS security services with Terraform](https://aws.amazon.com/blogs/security/how-use-ci-cd-deploy-configure-aws-security-services-terraform/) (AWS blog post)
+ [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (IAM documentation)
+ [create-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html) (AWS CLI documentation)
+ [Configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/S3-artifact-encryption.html) (AWS CodePipeline documentation)
+ [Quotas for AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html) (AWS CodeBuild documentation)
+ [Data protection in AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/data-protection.html) (AWS CodePipeline documentation)

## Additional information
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-additional"></a>

**Custom Terraform modules**

The following is a list of custom Terraform modules that are used in this pattern:
+ `codebuild_terraform` creates the CodeBuild projects that form each stage of the pipeline.
+ `codecommit_infrastructure_source_repo` captures and creates the source CodeCommit repository.
+ `codepipeline_iam_role` creates the required IAM roles for the pipeline.
+ `codepipeline_kms` creates the required AWS KMS key for Amazon S3 object encryption and decryption.
+ `codepipeline_terraform` creates the test pipeline for the source CodeCommit repository.
+ `s3_artifacts_bucket` creates an Amazon S3 bucket to manage pipeline artifacts.

**Build specification files**

The following is a list of build specification (buildspec) files that this pattern uses to run each pipeline stage:
+ `buildspec_validate.yml` runs the `"validate"` stage.
+ `buildspec_plan.yml` runs the `"plan"` stage.
+ `buildspec_apply.yml` runs the `"apply"` stage.
+ `buildspec_destroy.yml` runs the `"destroy"` stage.

*Build specification file variables*

Each buildspec file uses the following variables to activate different build-specific settings:

|
|
| Variable | Default value | Description |
| --- |--- |--- |
| `CODE_SRC_DIR` | "." | Defines the source CodeCommit directory |
| `TF_VERSION` | "1.3.7" | Defines the Terraform version for the build environment |

The `buildspec_validate.yml` file also supports the following variables to activate different build-specific settings:

|
|
| Variable | Default value | Description |
| --- |--- |--- |
| `SCRIPT_DIR` | "./templates/scripts" | Defines the script directory |
| `ENVIRONMENT` | "dev" | Defines the environment name |
| `SKIPVALIDATIONFAILURE` | "Y" | Skips validation on failures |
| `ENABLE_TFVALIDATE` | "Y" | Activates Terraform validate  |
| `ENABLE_TFFORMAT` | "Y" | Activates Terraform format |
| `ENABLE_TFCHECKOV` | "Y" | Activates checkov scan |
| `ENABLE_TFSEC` | "Y" | Activates tfsec scan |
| `TFSEC_VERSION` | "v1.28.1" | Defines the tfsec version |
