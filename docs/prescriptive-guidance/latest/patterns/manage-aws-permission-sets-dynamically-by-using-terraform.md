---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-aws-permission-sets-dynamically-by-using-terraform.html
---

# Manage AWS permission sets dynamically by using Terraform
<a name="manage-aws-permission-sets-dynamically-by-using-terraform"></a>

*Vinicius Elias and Marcos Vinicius Pinto Jordao, Amazon Web Services*

## Summary
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-summary"></a>

AWS IAM Identity Center enhances AWS Identity and Access Management (IAM) by providing a centralized hub for managing single sign-on access to AWS accounts and cloud applications. However, manual management of IAM Identity Center [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) can become increasingly complex and error-prone as your organization grows. This complexity can lead to potential security gaps and administrative overhead.

This solution enables you to manage permission sets through infrastructure as code (IaC) using a continuous integration and continuous delivery (CI/CD) pipeline built with native AWS services. It enables a seamless integration of the permission set assignment mechanism with AWS Control Tower lifecycle events or an [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) environment. This approach provides dynamic identity configurations for both new and existing AWS accounts.

Amazon EventBridge rules monitor AWS account creation and updates, which helps your identity configurations to remain synchronized with your organizational structure. After creating or updating accounts in AWS Control Tower or AFT, the pipeline is triggered. It evaluates a set of JSON files with permission set definitions and assignment rules. Then the pipeline applies and synchronizes the settings across all accounts.

This approach provides the following benefits:
+ **Consistency** – Eliminates manual configuration drift across your AWS organization
+ **Auditability** – Maintains a complete history of all identity management changes
+ **Scalability** – Automatically applies configurations as your AWS environment grows
+ **Security** – Reduces human error in permission assignments
+ **Compliance** – Facilitates meeting regulatory requirements through documented changes and assignment rules

## Prerequisites and limitations
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-prereqs"></a>
+ A multi-account environment with AWS Control Tower and AWS Organizations set up. Optionally, you can use AFT with AWS Control Tower.
+ An IAM Identity Center delegated administrator AWS account to receive the solution. For more information, see [Delegated administration](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html) in the IAM Identity Center documentation.
+ A version control system (VCS) repository to handle the main code. For a sample, see the solution’s GitHub [repository](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline/tree/main/samples/basic).
+ Necessary AWS resources for the Terraform backend management, such as an Amazon Simple Storage Service (Amazon S3) bucket and Amazon DynamoDB table.

**Limitations**
+ The pipeline uses AWS native resources and open source Terraform. The pipeline is not prepared to make calls to third-party ecosystems.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-architecture"></a>

The following diagram shows the components and workflow for this pattern.

![Components and workflow to manage AWS permission sets using Terraform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/69dc79c7-b4cd-4ad0-b0d2-d58cf0c7adaa/images/649e299c-1142-405a-8982-4a6b2e595d53.png)

**AWS Control Tower events flow**

The solution begins with the integration of events coming from either AWS Control Tower or AFT. The choice between one or the other service is made at the implementation time through variable definition. Regardless of the method used, the pipeline is triggered whenever an account is created or updated. The pipeline reconciles the policies stored in the permission sets management repository.

Following are the AWS Control Tower lifecycle events:
+ `CreateManagedAccount` – When a new account is created
+ `UpdateManagedAccount` – When an existing account is updated

**Event routing**

EventBridge serves as the central event processing service, capturing events generated in the AWS Control Tower account. When events occur, EventBridge intelligently routes them to a centralized event bus in the solution account. AWS Control Tower lifecycle events follow distinct routing patterns. If AFT is defined as the event source, the AFT management account handles the events instead of the AWS Control Tower account. This event-driven architecture enables automated responses to organizational changes without manual intervention.

**AFT integration process**

When AWS Control Tower lifecycle events reach the AFT management account, they automatically trigger multiple downstream processes that are intrinsic to AFT. After the AFT account customization workflow completes, it publishes a message to the dedicated `aft-notifications` Amazon Simple Notification Service (Amazon SNS) topic. That topic triggers the `aft-new-account-forward-event` AWS Lambda function that’s implemented by this solution. The Lambda function sends the event to the solution account event bus, where it’s used to start the pipeline.

**Infrastructure as code pipeline**

The solution pipeline operates as a fully automated deployment mechanism. The AWS CodePipeline service continuously monitors the repository for changes. Upon detecting new commits, it automatically initiates the deployment workflow and initiates a sequential process that includes validation and execution phases. The system runs Terraform `plan` operations to identify proposed changes, followed by Terraform `apply` commands to implement those changes in the AWS environment. Notably, the pipeline runs without any manual approval gates. This approach enables rapid deployment of infrastructure changes while maintaining auditability through pipeline logs and Terraform state files.

The pipeline leverages AWS CodeBuild to run Terraform operations in a controlled environment with appropriate permissions. Through this IaC approach, the pipeline can perform comprehensive permission management operations including:
+ Create new permission sets.
+ Update existing permission sets.
+ Remove unnecessary permission sets.
+ Manage the assignment of these permissions across accounts and groups within the AWS organizations.

To maintain infrastructure consistency and prevent conflicting changes, the solution implements the Terraform backend state management system using an Amazon S3 bucket and dedicated Amazon DynamoDB table. This approach provides persistent storage location for Terraform state files and state locking mechanisms to prevent concurrent modifications to the same resources.

The main Terraform code uses the official AWS `permission-sets` Terraform module. This module can dynamically manage permission sets in IAM Identity Center, based on permission set templates.

**Source control management**

The permission set templates (JSON files) reside in an external version control system, such as GitHub, that provides a centralized repository for identity management configurations. This approach establishes a single source of truth for permission set definitions, while enabling collaborative development through standard code review practices. Authorized users can commit changes to these templates following organizational change management processes. These commits serve as the primary trigger for the automated deployment pipeline, initiating the infrastructure update process.

For an example of how to configure the permission sets using the JSON file in the repository, see [Additional information](#manage-aws-permission-sets-dynamically-by-using-terraform-additional).

## Tools
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) enables AWS resources and services, such as CodePipeline, to connect to external code repositories, such as GitHub.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command line shell.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses. It enables push notifications for account management events, ensuring that relevant parties are informed of important changes or actions within the system.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the AWS Samples organization on GitHub in the [sample-terraform-aws-permission-sets-pipeline ](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline)repository.

## Best practices
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-best-practices"></a>
+ Always pin the versions of the Terraform modules and providers used to run code in production.
+ Use a static code analysis tool, such as [Checkov](https://www.checkov.io/), to scan your code and then solve the security issues.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-epics"></a>

### Create the prerequisites (optional)
<a name="create-the-prerequisites-optional"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Terraform backend resources. | If you haven't created your Terraform backend AWS resources yet, use the following steps to create an Amazon S3 bucket (`s3-tf-backend-{ACCOUNT_ID}` ) and a DynamoDB table (`ddb-tf-backend`).1. Sign in to the AWS account where you will deploy the solution, and open [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) in the AWS Control Tower home AWS Region.<br />2. Run the following commands, replacing the placeholder `{ACCOUNT_ID}` with your AWS account ID:<pre>aws s3api create-bucket --bucket s3-tf-backend-{ACCOUNT_ID}<br />aws s3api put-bucket-versioning --bucket s3-tf-backend-{ACCOUNT_ID} --versioning-configuration Status=Enabled<br />aws dynamodb create-table --table-name ddb-tf-backend --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1</pre> | AWS administrator |
| Create a cross-account role. | You must provide a cross-account IAM role in the `event-source-account` Terraform AWS provider configuration. If you haven't created this role yet, use the following steps to create it:1. Sign in to the AWS account that will be your event source (AWS Control Tower management account or AFT account), and open AWS CloudShell.<br />2. Run the following command, replacing the placeholder `{ACCOUNT_ID}` with the AWS account ID that you’re using for this solution, not your current AWS account ID:<pre>aws iam create-role \<br />    --role-name CrossAccountRole \<br />    --assume-role-policy-document '{<br />        "Version": "2012-10-17",		 	 	 <br />        "Statement": [<br />            {<br />                "Effect": "Allow",<br />                "Principal": {<br />                    "AWS": "arn:aws:iam::{ACCOUNT_ID}:root"<br />                },<br />                "Action": "sts:AssumeRole"<br />            }<br />        ]<br />    }'</pre>1. Check the command output and copy the role Amazon Resource Name (ARN) (for example, `arn:aws:iam::111122223333:role/CrossAccountRole`).<br />2. To attach an IAM policy to the role, run the following command:<pre>aws iam attach-role-policy \<br />    --role-name CrossAccountRole \<br />    --policy-arn arn:aws:iam::aws:policy/AdministratorAccess</pre><br />This example uses the AWS managed IAM policy [AdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html). If you prefer, you can use a more specific policy. | AWS administrator |

### Prepare the permission set repository
<a name="prepare-the-permission-set-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a dedicated repository. | This task assumes that you’re using GitHub. Create a dedicated repository to store the main Terraform code and the permission set template JSON files. | DevOps engineer |
| Prepare the permission set code. | For information about how you can structure the following files, see the [sample code](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline/tree/main/samples/basic) on the solution repository:<br />├── main.tf<br />├── outputs.tf<br />├── providers.jinja<br />└── templates<br />Copy the content, keep the `providers.jinja` values, and make the necessary adjustments to the other files. For example, add permission set template files into `templates` or pin the `aws-ia/permission-sets/aws` module version in the `main.tf` file. | DevOps engineer |
| Commit your changes. | Commit and push the changes to the repository that you created earlier. Save the repository name and its GitHub organization, for example, `myorg/aws-ps-pipeline`. | DevOps engineer |

### Prepare the deployment code
<a name="prepare-the-deployment-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the content. | Download (clone) the content from the solution [repository](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline). | DevOps engineer |
| Fulfill the variables. | Create a `terraform.tfvars` file and add the following necessary variables:+ `repository_name` – Name of permission set repository that you created earlier<br />+ `branch_name` – Name of the permission set repository branch<br />+ `vcs_provider` – Your VCS provider<br />+ `account_lifecycle_events_source` – The source of events to trigger the pipeline (AWS Control Tower or AFT)<pre>repository_name                 = "myorg/aws-ps-pipeline"<br />branch_name                     = "main"<br />vcs_provider                    = "github"<br />account_lifecycle_events_source = "CT"</pre><br />For information about additional variable options, see the [variables.tf](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline/blob/main/variables.tf) file in this pattern’s GitHub repository. | DevOps engineer |
| Adjust the Terraform backend configuration. | In the `backend.tf` file, replace the placeholders with your own values. Use the AWS Control Tower home AWS Region, and provide the names of the previously created Amazon S3 bucket and DynamoDB table.<pre>terraform {<br />  required_version = ">=1.6"<br />  backend "s3" {<br />    region         = "{region}"<br />    bucket         = "{bucket_name}"<br />    key            = "terraform.tfstate"<br />    dynamodb_table = "{table_name}"<br />    encrypt        = "true"<br />  }<br />}</pre><br />If you prefer, you can use your own Terraform backend configuration. | DevOps engineer |
| Adjust the Terraform provider configuration. | In the `providers.tf` file, replace the placeholders with your own information. Use the AWS Control Tower home Region, and provide the ARN of the previously created cross-account IAM role for the `event-source-account` provider.<pre>provider "aws" {<br />  region = "{region}"<br />}<br /><br />provider "aws" {<br />  alias  = "event-source-account"<br />  region = "{region}"<br />  assume_role {<br />    role_arn = "{role_arn}"<br />  }<br />}<br /></pre> | DevOps engineer |

### Deploy the solution manually
<a name="deploy-the-solution-manually"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select the AWS account. | We recommend that you deploy the solution in the IAM Identity Center delegated administrator account. However, you can also deploy it in the AWS Organizations management account.<br />To sign in to the selected account in the same Region as the IAM Identity Center instance, use the AWS CLI. Make sure that the IAM role you’re using has permission to assume the role that’s specified for the `event-source-account` provider in the previous steps. Also, this role must have access to the AWS resources that are used in the Terraform backend configuration. | AWS administrator |
| Run Terraform manually. | To initialize, plan and apply the configurations, run the following Terraform commands in the order shown:1. `terraform init`<br />2. `terraform plan`<br />3. `terraform apply` | DevOps engineer |
| Check the deployment results. | In the IAM Identity Center delegated administrator account, check that the `aws-ps-pipeline` pipeline has been created. Also check that there is a AWS CodeConnections connection with **Pending** status. | AWS DevOps |
| Finish the CodeConnections configuration. | To finish the CodeConnections configuration, use the following steps:1. Go to CodeConnections, select the connection that was created, and choose **Update pending connection**. <br />2. Provide your GitHub credentials, install a new GitHub App or select an existing one that has access to the permission set repository, and choose **Connect**.<br />The pipeline should now have access to the permission set repository.<br />For detailed instructions, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html) in the Developer Tools console documentation.  | AWS DevOps |

### Choose a pipeline execution flow to test the solution
<a name="choose-a-pipeline-execution-flow-to-test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the pipeline by AWS Control Tower or AFT updates. | After an account is created or changed by using AWS Control Tower or AFT (depending on the type of lifecycle events that you chose), the pipeline starts. | AWS administrator |
| Run the pipeline by changing the code. | After you change the code and commit it to the `main` branch, the pipeline starts. | AWS DevOps |
| Run the pipeline manually. | To start the pipeline manually, use the [Release change](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) feature in AWS CodePipeline. | AWS DevOps |

## Troubleshooting
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Access denied | Verify that you have the permissions required to deploy the solution. |
| CodeConnections issues | + Check that the connection status is **Available** rather than **Pending**.<br />+ Verify that the CodeConnections configuration is properly completed with GitHub credentials. For more information, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html) in the Developer Tools console documentation.<br />+ Make sure that the GitHub app has proper access permissions to the permission set repository. |
| Pipeline execution problems | + Check Amazon CloudWatch logs for pipeline execution errors.<br />+ Make sure that the IAM Identity Center delegation is set up correctly. Otherwise, it can cause pipeline failures when reading AWS account metadata. |
| Permission sets deployment issues | + Validate that the JSON syntax in the permission set template files is correct.<br />+ Verify that the IAM managed policies referenced in templates exist.<br />+ Check if the specified groups and users in assignments exist in IAM Identity Center. |

## Related resources
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-resources"></a>

**AWS service documentation**
+ [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [Manage AWS accounts with permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) (IAM Identity Center documentation)

**Other resources**
+ [AWS Permission Sets module](https://registry.terraform.io/modules/aws-ia/permission-sets/aws/latest) (Terraform)

## Additional information
<a name="manage-aws-permission-sets-dynamically-by-using-terraform-additional"></a>

**JSON file with sample permission set**

The following example shows how to configure a permission set by using the JSON file in the repository:

```
{
  "Name": "ps-billing", // Permission set identifier
  "Comment": "Sample permission set for billing access", // Comment to document the purpose of the permission set
  "Description": "Billing access in AWS", // Detailed description
  "SessionDuration": "PT4H", // Session duration = 4 hours (ISO 8601 format)
  "ManagedPolicies": [ // List of AWS IAM managed policies
    "arn:aws:iam::aws:policy/job-function/Billing",
    "arn:aws:iam::aws:policy/job-function/SupportUser",
    "arn:aws:iam::aws:policy/AWSSupportAccess",
    "arn:aws:iam::aws:policy/job-function/ViewOnlyAccess"
  ],
  "CustomerPolicies": [], // References to IAM policies previously created
  "CustomPolicy": {}, // Inline IAM policy defined directly in the permission set
  "PermissionBoundary": {  // AWS or customer managed IAM policy to be used as boundary
    "ManagedPolicy": "",
    "CustomerPolicy": ""
  },
  "Assignments": [ // Define the assignment rules
    {
      "all_accounts": true, // Apply to ALL active AWS accounts in organization
      "principal": "G_BILLING_USERS", // Group/user name in Identity Center
      "type": "GROUP", // Can be "GROUP" or "USER"
      "account_id": [], // List of AWS account ID (empty since all_accounts=true)
      "account_ou": [], // List of AWS Organizational Unit IDs with target AWS accounts
      "account_tag": [] // List of tags (key:value) to match AWS Organization accounts tags
    }
  ]
}
```

For more information, see the JSON schema in the [AWS Permission Sets module](https://registry.terraform.io/modules/aws-ia/permission-sets/aws/latest#json-file-templates) documentation on the Terraform website.

**Tips**
+ You can use Terraform [import blocks](https://developer.hashicorp.com/terraform/language/import) to import an existing permission set to the solution.
+ You can use AFT to implement the AWS permission set pipeline in a delegated account. For more information, see [AFT Blueprints](https://awslabs.github.io/aft-blueprints/index.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
