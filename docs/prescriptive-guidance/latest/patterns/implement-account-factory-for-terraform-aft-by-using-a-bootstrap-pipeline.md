---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html
---

# Implement Account Factory for Terraform (AFT) by using a bootstrap pipeline
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline"></a>

*Vinicius Elias and Edgar Costa Filho, Amazon Web Services*

## Summary
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-summary"></a>

This pattern provides a simple and secure method for deploying AWS Control Tower Account Factory for Terraform (AFT) from the management account of AWS Organizations. The core of the solution is an CloudFormation template that automates the AFT configuration by creating a Terraform pipeline, which is structured to be easily adaptable for initial deployment or subsequent updates.

Security and data integrity are top priorities at AWS, so the Terraform state file, which is a critical component that tracks the state of the managed infrastructure and configurations, is securely stored in an Amazon Simple Storage Service (Amazon S3) bucket. This bucket is configured with several security measures, including server-side encryption and policies to block public access, to help ensure that your Terraform state is safeguarded against unauthorized access and data breaches.

The management account orchestrates and oversees the entire environment, so it is a critical resource in AWS Control Tower. This pattern follows AWS best practices and ensures that the deployment process is not only efficient but also aligns with security and governance standards, to offer a comprehensive, secure, and efficient way to deploy AFT in your AWS environment.

For more information about AFT, see the [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html).

## Prerequisites and limitations
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-prereqs"></a>

**Prerequisites**
+ A basic AWS multi-account environment with the following accounts at the minimum: management account, Log Archive account, Audit account, and one additional account for AFT management.
+ An established AWS Control Tower environment. The management account should be properly configured, because the CloudFormation template will be deployed within it.
+ The necessary permissions in the AWS management account. You'll need sufficient permissions to create and manage resources such as S3 buckets, AWS Lambda functions, AWS Identity and Access Management (IAM) roles, and AWS CodePipeline projects.
+ Familiarity with Terraform. Understanding Terraform's core concepts and workflow is important because the deployment involves generating and managing Terraform configurations.

**Limitations**
+ Be aware of the [AWS resource quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in your account. The deployment might create multiple resources, and encountering service quotas could impede the deployment process.
+ The template is designed for specific versions of Terraform and AWS services. Upgrading or changing versions might require template modifications.
+ The template doesn't support self-managed version control system (VCS) services such as GitHub Enterprise.

**Product versions**
+ Terraform version 1.6.6 or later
+ AFT version 1.11 or later

## Architecture
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-architecture"></a>

**Target technology stack**
+ CloudFormation
+ AWS CodeBuild
+ AWS CodeCommit
+ AWS CodePipeline
+ Amazon EventBridge
+ IAM
+ AWS Lambda
+ Amazon S3

**Target architecture**

The following diagram illustrates the implementation discussed in this pattern.

![Workflow for implementing AFT by using a bootstrap pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/944f9912-87c7-4cc5-8478-7070cf67f7ee/images/4ee74757-940d-4d92-a7f0-fb0db1476247.png)

The workflow consists of three main tasks: creating the resources, generating the content, and running the pipeline.

*Creating the resources*

The [CloudFormation template that's provided with this pattern](https://github.com/aws-samples/aft-bootstrap-pipeline/blob/main/code/aft-deployment-pipeline.yaml) creates and sets up all required resources, depending on the parameters you select when you deploy the template. At the minimum, the template creates the following resources:
+ A CodePipeline pipeline to implement the AFT
+ An S3 bucket to store the Terraform state file that's associated with the AFT implementation
+ Two CodeBuild projects to implement the Terraform plan and apply commands in different stages of the pipeline
+ IAM roles for CodeBuild and CodePipeline services
+ A second S3 bucket to store pipeline runtime artifacts

Depending on the VCS provider you select (CodeCommit or external VCS), the template creates the following resources.
+ For **CodeCommit**:
  + A CodeCommit repository to store the AFT Terraform bootstrap code
  + An EventBridge rule to capture CodeCommit repository changes on the `main` branch
  + Another IAM role for the EventBridge rule
+ For any other **external VCS provider**, such as GitHub:
  + An AWS CodeConnections connection

Additionally, when you select CodeCommit as the VCS provider, if you set the `Generate AFT Files` parameter to `true`, the template creates these additional resources to generate the content:
+ An S3 bucket to store the generated content and to be used as the source of the CodeCommit repository
+ A Lambda function to process the given parameters and generate the appropriate content
+ An IAM function to run the Lambda function
+ A CloudFormation custom resource that runs the Lambda function when the template is deployed

*Generating the content*

To generate the AFT bootstrap files and their content, the solution uses a Lambda function and an S3 bucket. The function creates a folder in the bucket, and then creates two files inside the folder: `main.tf` and `backend.tf`. The function also processes the provided CloudFormation parameters and populates these files with predefined code, replacing the respective parameter values.

To view the code that's used as a template to generate the files, see the solution's [GitHub repository](https://github.com/aws-samples/aft-bootstrap-pipeline). Basically, the files are generated as follows.

**main.tf**

```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory?ref=<aft_version>"

  # Required variables
  ct_management_account_id  = "<ct_management_account_id>"
  log_archive_account_id    = "<log_archive_account_id>"
  audit_account_id          = "<audit_account_id>"
  aft_management_account_id = "<aft_management_account_id>"
  ct_home_region            = "<ct_home_region>"

  # Optional variables
  tf_backend_secondary_region = "<tf_backend_secondary_region>"
  aft_metrics_reporting       = "<false|true>"

  # AFT Feature flags
  aft_feature_cloudtrail_data_events      = "<false|true>"
  aft_feature_enterprise_support          = "<false|true>"
  aft_feature_delete_default_vpcs_enabled = "<false|true>"

  # Terraform variables
  terraform_version      = "<terraform_version>"
  terraform_distribution = "<terraform_distribution>"

  # VCS variables (if you have chosen an external VCS)
  vcs_provider                                  = "<github|githubenterprise|gitlab|gitlabselfmanaged|bitbucket>"
  account_request_repo_name                     = "<org-name>/aft-account-request"
  account_customizations_repo_name              = "<org-name>/aft-account-customizations"
  account_provisioning_customizations_repo_name = "<org-name>/aft-account-provisioning-customizations"
  global_customizations_repo_name               = "<org-name>/aft-global-customizations"

}
```

**backend.tf**

```
terraform {
  backend "s3" {
    region = "<aft-main-region>"
    bucket = "<s3-bucket-name>"
    key    = "aft-setup.tfstate"
  }
}
```

During the CodeCommit repository creation, if you set the `Generate AFT Files` parameter to `true`, the template uses the S3 bucket with the generated content as the source of the `main` branch to automatically populate the repository.

*Running the pipeline*

After the resources have been created and the bootstrap files have been configured, the pipeline runs. The first stage (*Source*) fetches the source code from the main branch of the repository, and the second stage (*Build*) runs the Terraform plan command and generates the results to be reviewed. In the third stage (*Approval*), the pipeline waits for a manual action to approve or reject the last stage (*Deploy*). At the last stage, the pipeline runs the Terraform `apply` command by using the result of the previous Terraform `plan` command as input. Finally, a cross-account role and the permissions in the management account are used to create the AFT resources in the AFT management account.

**Note**
If you select an external VCS provider, you will need to authorize the connection with your VCS provider credentials. To complete the setup, follow the steps in [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html) in the AWS Developer Tools console documentation.

## Tools
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-tools"></a>

**AWS services**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) enables AWS resources and services, such as CodePipeline, to connect to external code repositories, such as GitHub.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that runs your code in response to events and automatically manages compute resources, providing a fast way to create a modern, serverless application for production.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

**Other tools**
+ [Terraform](https://developer.hashicorp.com/terraform?product_intent=terraform) is an infrastructure as code (IaC) tool that lets you build, change, and version infrastructure safely and efficiently. This includes low-level components such as compute instances, storage, and networking; and high-level components such as DNS entries and SaaS features.
+ [Python](https://docs.python.org/3.9/tutorial/index.html) is an easy to learn, powerful programming language. It has efficient high-level data structures and provides a simple but effective approach to object-oriented programming.

**Code repository**

The code for this pattern is available in the GitHub [AFT bootstrap pipeline repository](https://github.com/aws-samples/aft-bootstrap-pipeline).

For the official AFT repository, see [AWS Control Tower Account Factory for Terraform](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main) in GitHub.

## Best practices
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-best-practices"></a>

When you deploy AFT by using the provided CloudFormation template, we recommend that you follow best practices to help ensure a secure, efficient, and successful implementation. Key guidelines and recommendations for implementing and operating the AFT include the following.
+ **Thorough review of parameters**: Carefully review and understand each parameter in the CloudFormation template. Accurate parameter configuration is crucial for the correct setup and functioning of AFT.
+ **Regular template updates**: Keep the template updated with the latest AWS features and Terraform versions. Regular updates help you take advantage of new functionality and maintain security.
+ **Versioning**: Pin your AFT module version and use a separate AFT deployment for testing if possible.
+ **Scope**: Use AFT only to deploy infrastructure guardrails and customizations. Do not use it to deploy your application.
+ **Linting and validation**: The AFT pipeline requires a linted and validated Terraform configuration. Run lint, validate, and test before pushing the configuration to AFT repositories.
+ **Terraform modules**: Build reusable Terraform code as modules, and always specify the Terraform and AWS provider versions to match your organization's requirements.

## Epics
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-epics"></a>

### Set up and configure the AWS environment
<a name="set-up-and-configure-the-aws-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the AWS Control Tower environment. | Set up and configure AWS Control Tower in your AWS environment to ensure centralized management and governance for your AWS accounts. For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in the AWS Control Tower documentation. | Cloud administrator |
| Launch the AFT management account. | Use the AWS Control Tower Account Factory to launch a new AWS account to serve as your AFT management account. For more information, see [Provision accounts with AWS Service Catalog Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/provision-as-end-user.html) in the AWS Control Tower documentation. | Cloud administrator |

### Deploy the CloudFormation template in the management account
<a name="deploy-the-cfnshort-template-in-the-management-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the CloudFormation template. | In this epic, you deploy the CloudFormation template provided with this solution to set up the AFT bootstrap pipeline in your AWS management account. The pipeline deploys the AFT solution in the AFT management account that you set up in the previous epic.<br />**Step 1: Open the CloudFormation console**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 2: Create a new stack**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 3: Configure stack parameters**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 4: Decide on file generation**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 5: Fill in AWS Control Tower and AFT account details**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 6: Configure AFT options**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 7: Specify versions**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 8: Review and create the stack**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 9: Monitor stack creation**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 10: Verify the deployment**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html) | Cloud administrator |

### Populate and validate the AFT bootstrap repository and pipeline
<a name="populate-and-validate-the-aft-bootstrap-repository-and-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1: Populate the AFT bootstrap repository for an external VCS. | If you set the VCS provider to an external VCS (not to CodeCommit), follow these steps.<br />(Optional) After you deploy the CloudFormation template, you can populate or validate the content in the newly created AFT bootstrap repository, and test whether the pipeline has run successfully.<br />**Step 1: Update the connection**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 2: Populate the repository**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 2: Commit and push your changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html) | Cloud administrator |
| Option 2: Populate the AFT bootstrap repository for CodeCommit. | If you set the VCS provider to CodeCommit, follow these steps.<br />(Optional) After you deploy the CloudFormation template, you can populate or validate the content in the newly created AFT bootstrap repository, and test whether the pipeline has run successfully.<br />If you set the `Generate AFT Files` parameter to `true`, skip to the next story (validating the pipeline).<br />**Step 1: Populate the repository**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 2: Commit and push your changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html) | Cloud administrator |
| Validate the AFT bootstrap pipeline. | **Step 1: View the pipeline**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 2: Approve the Terraform plan results**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 3: Wait for the deployment**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html)<br />**Step 4: Check created resources**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline.html) | Cloud administrator |

## Troubleshooting
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The custom Lambda function included in the CloudFormation template fails during deployment. | Check the Amazon CloudWatch logs for the Lambda function to identify the error. The logs provide detailed information and can help pinpoint the specific issue. Confirm that the Lambda function has the necessary permissions and that the environment variables have been set correctly. |
| You encounter failures in resource creation or management caused by inadequate permissions. | Review the IAM roles and policies that are attached to the Lambda function, CodeBuild, and other services involved in the deployment. Confirm that they have the necessary permissions. If there are permission issues, adjust the IAM policies to grant the required access. |
| You’re using an outdated version of the CloudFormation template with newer AWS services or Terraform versions. | Regularly update the CloudFormation template to be compatible with the latest AWS and Terraform releases. Check the release notes or documentation for any version-specific changes or requirements. |
| You reach AWS service quotas during deployment. | Before you deploy the pipeline, check AWS service quotas for resources such as S3 buckets, IAM roles, and Lambda functions. Request increases if necessary. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) on the AWS website. |
| You encounter errors due to incorrect input parameters in the CloudFormation template. | Double-check all input parameters for typos or incorrect values. Confirm that resource identifiers, such as account IDs and Region names, are accurate. |

## Related resources
<a name="implement-account-factory-for-terraform-aft-by-using-a-bootstrap-pipeline-resources"></a>

To implement this pattern successfully, review the following resources. These resources provide additional information and guidance that can be invaluable in setting up and managing AFT by using CloudFormation.

**AWS** **documentation:**
+ [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) offers detailed information on setting up and managing AWS Control Tower.
+ [CloudFormation documentation](https://docs.aws.amazon.com/cloudformation/index.html) provides insights into CloudFormation templates, stacks, and resource management.

**IAM policies and best practices:**
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) explains how to help secure AWS resources by using IAM roles and policies.

**Terraform on AWS:**
+ [Terraform AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) provides comprehensive information about using Terraform with AWS.

**AWS service quotas:**
+ [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) provides information about how to view AWS service quotas and how to request increases.
