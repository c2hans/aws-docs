---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline.html
---

# Create a CI/CD pipeline to validate Terraform configurations by using AWS CodePipeline

*Aromal Raj Jayarajan and Vijesh Vijayakumaran Nair, Amazon Web Services*

## Summary
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-summary"></a>

This pattern shows how to test HashiCorp Terraform configurations by using a continuous integration and continuous delivery (CI/CD) pipeline that you deploy with [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/).

Terraform is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources. The solution provided in this pattern creates a CI/CD pipeline that helps you validate the integrity of your Terraform configurations by running five [CodePipeline stages](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-stages):

1. `"checkout"` pulls the Terraform configuration that you’re testing from an AWS CodeCommit repository.

1. `"validate"` runs infrastructure as code (IaC) validation tools, including [checkov](https://www.checkov.io/) and [Trivy](https://trivy.dev/docs/). The stage also runs the following Terraform IaC validation commands: `terraform validate` and `terraform fmt -check`.

1. `"plan"` shows the changes that Terraform makes to the infrastructure when it applies the configuration.

1. `"apply"` uses the generated plan to provision the required infrastructure in a test environment.

1. `"destroy"` removes the test infrastructure that was created during the `"apply"` stage.

Use this pipeline only with a test account, because the `"apply"` and `"destroy"` stages run automatically after the `"plan"` stage.

## Prerequisites and limitations
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-prereqs"></a>

**Prerequisites**
+ An active AWS account that you use for testing, with permissions to create the resources in this pattern (AWS Identity and Access Management (IAM) roles and policies, AWS Key Management Service (AWS KMS) keys, Amazon Simple Storage Service (Amazon S3) buckets in two AWS Regions, an AWS CodeCommit repository, AWS CodeBuild projects, and an AWS CodePipeline pipeline)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), installed and configured on your local machine
+ [Terraform](https://developer.hashicorp.com/terraform/install), installed and configured on your local machine

**Limitations**
+ This pattern deploys a pipeline in AWS CodePipeline in one AWS account and AWS Region only. Multi-account and multi-Region deployments require configuration changes.
+ The IAM role that this pattern provisions (**codepipeline\_iam\_role**) follows the principle of least privilege for the pipeline itself. It doesn’t include permissions to create the resources that your Terraform configuration manages. You must update this IAM role’s permissions based on the specific resources that your pipeline needs to create.
+ The pipeline has no manual approval step. The `apply` and `destroy` stages run automatically after the `plan` stage.
+ As an example, this pattern replicates the Amazon S3 artifact bucket to a second Region. Replication skips objects that you encrypt with the pipeline’s AWS KMS key unless you add a key in the destination Region and update the replication rule.

**Product versions**
+ AWS CLI version 2.9.15 or later
+ Terraform version 1.5.0 or later (the build projects use Terraform 1.17.2 by default)
+ AWS provider for Terraform version 6.0 or later

## Architecture
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-architecture"></a>

**Target technology stack**
+ AWS CodePipeline
+ AWS CodeBuild
+ AWS CodeCommit
+ AWS IAM
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Key Management Service (AWS KMS)
+ Amazon CloudWatch Logs
+ Terraform

**Target architecture**

The following diagram shows an example continuous integration and continuous delivery (CI/CD) pipeline workflow for testing Terraform configurations in CodePipeline.

![Architecture to test Terraform configurations by using an AWS CI/CD pipeline.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4df7b1f8-8eef-4d85-a971-a7f158be9691/images/90b931c8-e745-4b52-92de-a367fb0f1f51.png)

The diagram shows the following workflow:

1. In CodePipeline, an AWS user initiates the actions proposed in a Terraform plan by running the `terraform apply` command in the AWS CLI.

1. AWS CodePipeline assumes an IAM service role that includes the policies required to access CodeCommit, CodeBuild, AWS KMS, and Amazon S3.

1. CodePipeline runs the `"checkout"` pipeline stage to pull the Terraform configuration from an AWS CodeCommit repository for testing.

1. CodePipeline runs the `"validate"` stage to test the Terraform configuration by running IaC validation tools and running Terraform IaC validation commands in a CodeBuild project.

1. CodePipeline runs the `"plan"` stage to create a plan in the CodeBuild project based on the Terraform configuration. The AWS user can review this plan before the changes are applied to the test environment.

1. CodePipeline runs the `"apply"` stage to implement the plan by using the CodeBuild project to provision the required infrastructure in the test environment.

1. CodePipeline runs the `"destroy"` stage, which uses CodeBuild to remove the test infrastructure that was created during the `"apply"` stage.

1. An Amazon S3 bucket stores pipeline artifacts, which are encrypted and decrypted by using an AWS KMS [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). The bucket is replicated to a bucket in a second Region. S3 server access logs for both buckets go to separate log buckets in each Region.

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
+ [Checkov](https://www.checkov.io/) is a static code analysis tool that scans infrastructure as code (IaC) files for security and compliance misconfigurations.
+ [Trivy](https://trivy.dev/docs/) is an open source security scanner that includes a scanner for IaC misconfigurations. This pattern uses Trivy to scan the Terraform configuration. Trivy replaces tfsec, which is now part of Trivy.

**Code **

The code for this pattern is available in the GitHub [aws-codepipeline-terraform-cicd-samples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository. The repository contains the Terraform configurations required to create the target architecture outlined in this pattern.

## Epics
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-epics"></a>

### Provision the solution components
<a name="provision-the-solution-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | Clone the GitHub [aws-codepipeline-terraform-cicd-samples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository by running the following command in a terminal window:<pre>git clone https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples.git</pre><br />For more information, see [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) in the GitHub documentation. | DevOps engineer |
| Create a Terraform variable definitions file.  | Create a `terraform.tfvars` file based on your use case requirements. You can update the variables in the `examples/terraform.tfvars` file that’s in the cloned repository.<br />For more information, see [Assigning values to root module variables](https://developer.hashicorp.com/terraform/language/values/variables#assigning-values-to-root-module-variables) in the Terraform documentation.The repository’s `Readme.md` file includes more information on the required variables. | DevOps engineer |
| Configure AWS as the Terraform provider. | 1. In a code editor, open the cloned repository’s `main.tf` file.<br />2. Add the necessary configurations for establishing connectivity to the target AWS account.For more information, see [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) in the Terraform documentation. | DevOps engineer |
| Update the Terraform provider configuration for creating the Amazon S3 replication bucket. | 1. Open the repository’s `S3` directory by running the following command:<pre>cd ./modules/s3</pre><br />2. Update the Terraform provider configuration for creating the Amazon S3 replication bucket by updating the `region` value in the `provider.tf` file. Make sure that you enter the Region that you want Amazon S3 to replicate objects to. The module also creates an access log bucket in that Region.<br />3. **(Optional)** By default, Terraform uses local state files for state management. If you want to add Amazon S3 as the remote backend, you must update the Terraform configuration. For more information, see [Backend configuration](https://developer.hashicorp.com/terraform/language/backend) in the Terraform documentation.Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. | DevOps engineer |
| Initialize the Terraform configuration. | To initialize your working directory that contains the Terraform configuration files, run the following command in the cloned repository’s root folder:<pre>terraform init</pre> | DevOps engineer |
| Create the Terraform plan. | To create a Terraform plan, run the following command in the cloned repository’s root folder:<pre>terraform plan --var-file=terraform.tfvars -out=tfplan</pre>Terraform evaluates the configuration files to determine the target state for the declared resources. It then compares the target state against the current state and creates a plan. | DevOps engineer |
| Verify the Terraform plan. | Review the Terraform plan and confirm that it configures the required architecture in your target AWS account. | DevOps engineer |
| Deploy the solution. | 1. To apply the Terraform plan, run the following command in the cloned repository’s root folder:<pre>terraform apply "tfplan"</pre><br />2. Enter **yes** to confirm that you want to deploy the resources.Terraform creates, updates, or destroys infrastructure to achieve the target state declared in the configuration files. | DevOps engineer |

### Validate Terraform configurations by running the pipeline
<a name="validate-terraform-configurations-by-running-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the source code repository. | 1. From the Terraform output, get the **source repository** details for the repository that contains the Terraform configurations that you want to validate.<br />2. Sign in to the AWS Management Console. Then, open the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).<br />3. Create a new branch in the source repository named `main`. For instructions, see [Create a branch in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-branch.html) in the CodeCommit documentation.<br />4. Clone the `main` branch of the **source repository** to your local workstation. For instructions, see [Setup steps for HTTPS connections to AWS CodeCommit repositories on Windows with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html) in the CodeCommit documentation.<br />5. Copy the** **`templates` folder from the GitHub [aws-codepipeline-terraform-cicd-samples](https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples) repository by running the following command:<pre>cp -r templates $YOUR_CODECOMMIT_REPO_ROOT</pre>The `templates` folder contains the build specification files and the validation script for the root directory of the source repository.<br />6. Add your required Terraform infrastructure as code (IaC) configurations to the root folder of the **source repository**.<br />7. Add the details for the remote backend in your project's Terraform configuration. For more information, see [S3](https://developer.hashicorp.com/terraform/language/settings/backends/s3) in the Terraform documentation.<br />8. **(Optional)** Update the variables in the buildspec files in the `templates` folder to turn the preconfigured scans on or off, to change the tool versions, and to specify your directory in custom script files. If you change `TF_VERSION` or `TRIVY_VERSION`, also update the matching SHA256 variable (`TF_SHA256` or `TRIVY_SHA256`) from the checksum file that is published with the release. For more information, see the *Additional information* section of this pattern.<br />9. Push the changes to the `main` branch of the **source repository**. | DevOps engineer |
| Validate the pipeline stages. | 1. Sign in to the AWS Management Console and open the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home).<br />2. In the output from the `terraform apply "tfplan"` command in the previous epic, find the name of the pipeline that Terraform created.<br />3. Open the pipeline in the CodePipeline console and choose **Release change**.<br />4. Review each pipeline stage and confirm it’s working as expected.For more information, see [View pipeline details and history (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-console.html) in the *AWS CodePipeline User Guide*.When you commit a change to the main branch of the source repository, the test pipeline starts automatically. | DevOps engineer |
| Verify the report output. | 1. On the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home), in the left navigation pane, choose **Build**. Then, choose **Report history**.<br />2. Review the Checkov and Trivy scan reports that the pipeline generates. These reports can help you identify issues through visualizations.The `<project_name>-validate` AWS CodeBuild project generates the reports for your code during the `validate` stage. By default, the stage reports findings but doesn’t fail. To fail the stage when a check fails, set `SKIPVALIDATIONFAILURE` to `"N"` in `templates/buildspec_validate.yml`. | DevOps engineer |

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
| An AWS CodeBuild stage fails with `terraform.zip: FAILED` or `trivy.tar.gz: FAILED` during the install phase. | You changed `TF_VERSION` or `TRIVY_VERSION` without changing the matching SHA256 value. Get the checksum for your version from the release’s checksum file (for Terraform: `https://releases.hashicorp.com/terraform/<version>/terraform_<version>_SHA256SUMS`), update `TF_SHA256` or `TRIVY_SHA256` in the buildspec files, and push the change. |

## Related resources
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-resources"></a>
+ [Module blocks](https://developer.hashicorp.com/terraform/language/modules/syntax) (Terraform documentation)
+ [How to use CI/CD to deploy and configure AWS security services with Terraform](https://aws.amazon.com/blogs/security/how-use-ci-cd-deploy-configure-aws-security-services-terraform/) (AWS blog post)
+ [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (IAM documentation)
+ [create-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html) (AWS CLI documentation)
+ [Configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/S3-artifact-encryption.html) (AWS CodePipeline documentation)
+ [Quotas for AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html) (AWS CodeBuild documentation)
+ [Data protection in AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/data-protection.html) (AWS CodePipeline documentation)
+ [Trivy documentation](https://trivy.dev/docs/)
+ [Checkov documentation](https://www.checkov.io/)
+ [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (AWS CodeBuild documentation)

## Additional information
<a name="create-a-ci-cd-pipeline-to-validate-terraform-configurations-by-using-aws-codepipeline-additional"></a>

**Custom Terraform modules**

This pattern uses the following custom Terraform modules:
+ `codebuild_terraform` creates the AWS CodeBuild projects that form each stage of the pipeline.
+ `codecommit_infrastructure_source_repo` captures and creates the source AWS CodeCommit repository.
+ `codepipeline_iam_role` creates the required IAM roles for the pipeline.
+ `codepipeline_kms` creates the required AWS KMS key for Amazon S3 object encryption and decryption.
+ `codepipeline_terraform` creates the test pipeline for the source CodeCommit repository.
+ `s3_artifacts_bucket` creates an Amazon S3 bucket to manage pipeline artifacts.
+ `s3_access_logs` (in the `s3_artifacts_bucket` module) creates the Amazon S3 buckets that receive the server access logs for the artifact bucket and the replication bucket.

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
| `TF_VERSION` | "1.17.2" | Defines the Terraform version for the build environment |
| `TF_SHA256` | "e6f16b2f0b137ee5729caa8c4e79a3bae4ee261acd198a1fcfa8584a6296605b" | SHA256 checksum of the Terraform download. The build stops if it doesn’t match `TF_VERSION`. |

The `buildspec_validate.yml` file also supports the following variables to activate different build-specific settings:

|
|
| Variable | Default value | Description |
| --- |--- |--- |
| `SCRIPT_DIR` | "./templates/scripts" | Defines the script directory |
| `ENVIRONMENT` | "dev" | Defines the environment name |
| `SKIPVALIDATIONFAILURE` | "Y" | When "Y", failed checks are reported but don’t stop the build. Set it to "N" to fail the stage when a check fails. |
| `ENABLE_TFVALIDATE` | "Y" | Activates Terraform validate  |
| `ENABLE_TFFORMAT` | "Y" | Checks Terraform formatting (`terraform fmt -check`) |
| `ENABLE_TFCHECKOV` | "Y" | Activates the Checkov scan |
| `ENABLE_TRIVY` | "Y" | Activates Trivy scan |
| `TRIVY_VERSION` | "v0.76.2" | Defines the Trivy version |
| `TRIVY_SHA256` | "bc0fc726e017b8927a62b2d3531d7a84ee01769daf5c99ed866dced54089fdbf" | SHA256 checksum of the Trivy download |
| `CHECKOV_VERSION` | "3.4.5" | Defines the Checkov version |
