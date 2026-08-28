---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/govern-permission-sets-aft.html
---

# Govern permission sets for multiple accounts by using Account Factory for Terraform
<a name="govern-permission-sets-aft"></a>

*Anand Krishna Varanasi and Siamak Heshmati, Amazon Web Services*

## Summary
<a name="govern-permission-sets-aft-summary"></a>

This pattern helps you integrate [AWS Control Tower Account Factory Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) with [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in order to configure permissions for multiple AWS accounts at scale. This approach uses custom AWS Lambda functions to automate [permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) assignments to AWS accounts that are managed as an organization. This streamlines the process because it doesn’t require manual intervention from your platform engineering team. This solution can enhance operational efficiency, security and consistency. It promotes a secure and standardized onboarding process for AWS Control Tower, making it indispensable for enterprises that prioritize agility and reliability for their cloud infrastructure.

## Prerequisites and limitations
<a name="govern-permission-sets-aft-prereqs"></a>

**Prerequisites**
+ AWS accounts, managed through AWS Control Tower. For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html).
+ Account Factory for Terraform, deployed in a dedicated account in your environment. For more information, see [Deploy AWS Control Tower Account Factory for Terraform](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html).
+ An IAM Identity Center instance, set up in your environment. For more information, see [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).
+ An active IAM Identity Center [group](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html#groups-concept), configured.  For more information, see [Add groups to your IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html).
+ Python version 3.9 or later, installed

**Limitations**
+ This solution can be used only with accounts that are managed through AWS Control Tower. This solution is deployed by using Account Factory for Terraform.
+ This pattern does not include instructions for setting up identity federation with an identity source. For more information about how to complete this set up, see [IAM Identity Center identity source tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) in the IAM Identity Center documentation.

## Architecture
<a name="govern-permission-sets-aft-architecture"></a>

**AFT overview**

AFT sets up a Terraform pipeline that helps you provision and customize your accounts in AWS Control Tower. AFT follows a GitOps model that automates the processes of account provisioning in AWS Control Tower. You create an *account request Terraform file* and commit it to repository. This initiates the AFT workflow for account provisioning. After account provisioning is complete, AFT can automatically run additional customization steps. For more information, see [AFT architecture](https://docs.aws.amazon.com/controltower/latest/userguide/aft-architecture.html) in the AWS Control Tower documentation.

AFT provides the following main repositories:
+ `aft-account-request` – This repository contains Terraform code to create or update AWS accounts.
+ `aft-account-customizations` – This repository contains Terraform code to create or customize resources on a per-account basis.
+ `aft-global-customizations` – This repository contains Terraform code to create or customize resources for all accounts, at scale.
+ `aft-account-provisioning-customizations` – This repository manages customizations that are applied only to specific accounts created by and managed with AFT. For example, you might use this repository to customize user or groups assignments in IAM Identity Center or to automate account closures.

**Solution overview**

This custom solution includes an AWS Step Functions state machine and an AWS Lambda function that assign permission sets to users and groups for multiple accounts. The state machine deployed through this pattern operates in conjunction with pre-existing AFT `aft_account_provisioning_customizations` state machine. A user submits a request to update IAM Identity Center user and group assignments either when a new AWS account is created or after the account is created. They do this by pushing a change to the `aft-account-request` repository. The request to create or update an account initiates a stream in [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html). This starts the Lambda function, which updates IAM Identity Center users and groups for the target AWS accounts.

The following is an example of the parameters you can provide in the Lambda function for permission set assignments to target users and groups:

```
custom_fields = {
    "InstanceArn"         = "<Organization ID>",
    "PermissionSetArn"    = "<Permission set ARN>",
    "PrincipalId"         = "<Principal ID>",
  }
```

The following are the parameters in this statement:
+ `InstanceArn` – The Amazon Resource Name (ARN) of the organization
+ `PermissionSetArn` – The ARN of the permission set
+ `PrincipalId` – The identifier of a user or group in IAM Identity Center to which the permission set will be applied

**Note**
You must create the target permission set, users, and groups before running this solution.

While the `InstanceArn` value must remain consistent, you can modify the Lambda function to assign multiple permission sets to multiple target identities. The parameters for permission sets must end in `PermissionSetArn`, and the parameters for users and groups must end in `PrincipalId`. You must define both attributes. The following is an example of how to define multiple permission sets and target users and groups:

```
custom_fields = {
    "InstanceArn"                    = "<Organization ID>",
    "AdminAccessPermissionSetArn"    = "<Admin privileges permission set ARN>",
    "AdminAccessPrincipalId"         = "<Admin principal ID>",
    "ReadOnlyAccessPermissionSetArn" = "<Read-only privileges permission set ARN>",
    "ReadOnlyAccessPrincipalId"      = "<Read-only principal ID>",
  }
```

The following diagram shows a step-by-step workflow of how the solution updates permissions sets for users and groups in the target AWS accounts at scale. When the user initiates an account creation request, AFT initiates the `aft-account-provisioning-framework` Step Functions state machine. This state machine starts the `extract-alternate-sso` Lambda function. The Lambda function assigns permissions sets to users and groups in the target AWS accounts. These users or groups can be from any configured identity source in IAM Identity Center. Examples of identity sources include Okta, Active Directory, or Ping Identity.

![Workflow of updating permission sets when an account is created or updated.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/14751255-3781-48db-a6b7-1a03e28c1020/images/d1de252d-8ac9-4f7d-a559-4ab3e852f325.png)

The diagram shows the following workflow when new accounts are created:

1. A user pushes a `custom_fields` change to the `aft-account-request` repository.

1. AWS CodePipeline starts an AWS CodeBuild job that records the user-defined metadata into the `aft-request-audit` Amazon DynamoDB table. This table has attributes to record user-defined metadata. The `ddb_event_name` attribute defines the type of AFT operation:
   + If the value is `INSERT`, then the solution assigns the permissions set to the target identities when the new AWS account is created.
   + If the value is `UPDATE`, then the solution assigns the permissions set to the target identities after the AWS account is created.

1. Amazon DynamoDB Streams initiates the `aft_alternate_sso_extract` Lambda function.

1. The `aft_alternate_sso_extract` Lambda function assumes an AWS Identity and Access Management (IAM) role in the AWS Control Tower management account.

1. The Lambda function assigns the permissions sets to the target users and groups by making an AWS SDK for Python (Boto3) [create\_account\_assignment](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin/client/create_account_assignment.html) API call to IAM Identity Center. It retrieves the permission set and identity assignments from the `aft-request-audit` Amazon DynamoDB table.

1. When the Step Functions workflow completes, the permission sets are assigned to the target identities.

**Automation and scale**

AFT operates at scale by using AWS services such as CodePipeline, AWS CodeBuild, DynamoDB, and Lambda, which are highly scalable. For additional automation, you can integrate this solution with a ticket or issue management system, such as Jira. For more information, see the [Additional information](#govern-permission-sets-aft-additional) section of this pattern.

## Tools
<a name="govern-permission-sets-aft-tools"></a>

**AWS services**
+ [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) is the main tool in this solution. The `aft-account-provisioning-customizations` repository contains the Terraform code for creating customizations for AWS accounts, such as custom IAM Identity Center user or group assignments.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code repository for AFT is available in the GitHub [AWS Control Tower Account Factory for Terraform](https://github.com/aws-ia/terraform-aws-control_tower_account_factory) repository. The code for this pattern is available in the [Govern SSO Assignments for AWS accounts using Account Factory for Terraform (AFT)](https://github.com/aws-samples/aft-custom-sso-assignment) repository.

## Best practices
<a name="govern-permission-sets-aft-best-practices"></a>
+ Understand the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).
+ Follow the security recommendations for AWS Control Tower. For more information, see [Security in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/security.html).
+ Follow the principle of least privilege. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
+ Build specific and focused permission sets and IAM roles for groups and business units.

## Epics
<a name="govern-permission-sets-aft-epics"></a>

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role. | In the AWS Control Tower management account, use Terraform to create an IAM role. This role has cross-account access and a trust policy that allows federated access from the identity provider. It also has permissions to grant access to other accounts through AWS Control Tower. The Lambda function will assume this role. Do the following:1. Download the `AFTCrossAccountRole.tf` file from the GitHub [code repository](https://github.com/aws-samples/aft-custom-sso-assignment/blob/main/aft-cross-account-role/AFTCrossAccountRole.tf).<br />2. Modify the `AFTCrossAccountRole.tf` file as necessary for your AWS environment.<br />3. In Terraform, enter the following commands to create this IAM role:<pre>terraform init<br />terraform plan<br />terraform apply</pre><br />4. Validate that the role was successfully deployed and has the expected cross-account access. | AWS DevOps, Cloud architect |
| Customize the solution for your environment. | 1. Enter the following command to clone the [Govern SSO Assignments for AWS accounts using Account Factory for Terraform (AFT)](https://github.com/aws-samples/aft-custom-sso-assignment) repository to your local workstation.<pre>git clone https://github.com/aws-samples/aft-custom-sso-assignment.git</pre><br />2. In the `aft-account-provisioning-customizations/terraform` folder, open the `variables.tf` file.<br />3. Modify the variables as needed for your environment.<br />4. Save and close the `variables.tf` file.<br />5. Open the `account-request.tf` file in your `aft-account-request` repository.<br />6. Modify the `custom_fields` parameters to define the permission sets and target users and groups. For more information, see the [Architecture](#govern-permission-sets-aft-architecture) section of this pattern.<br />7. Save and close the `account-request.tf` file. | AWS DevOps, Cloud architect |
| Deploy the solution. | 1. In the cloned repository, copy the contents of `terraform` folder, and then paste them into the `terraform` folder in the `aft-account-provisioning-customizations` repository.<br />2. In the AFT management account, start the `ct-aft-account-provisioning-customizations` pipeline. This deploys the custom solution. For instructions, see [Start a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-about-starting.html).<br />3. Validate that the resources were successfully deployed in the AFT management account. | AWS DevOps, Cloud architect |
| Set up a code repository connection. | Set up a connection between the code repository where you will store the configuration files and your AWS account. For instructions, see the [Add third-party source providers to pipelines using CodeConnections](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-connections.html) in the AWS CodePipeline documentation. | AWS DevOps, Cloud architect |

### Use the solution
<a name="use-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start AFT pipeline to deploy a new account. | Follow the instructions in [Provision a new account with AFT](https://docs.aws.amazon.com/controltower/latest/userguide/aft-provision-account.html) in order to start the pipeline that creates a new AWS account in your AWS Control Tower environment. Wait for the account creation process to complete. | AWS DevOps, Cloud architect |
| Validate the changes. | 1. Open the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon).<br />2. In the list of accounts, choose the newly created account.<br />3. Validate that permission sets have been assigned to grant access to the target users and groups. | AWS DevOps, Cloud architect |

## Troubleshooting
<a name="govern-permission-sets-aft-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Permission set assignment is not working. | Make sure the group ARN, organization id, and Lambda parameters are correct. For examples, see the *Solution overview* section of this pattern. |
| Updating code in the repository does not start the pipeline. | This issue is related to the connectivity between your AWS account and the repository. In the AWS Management Console, validate that the connection is active. For more information, see [GitHub connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html) in the AWS CodePipeline documentation. |

## Additional information
<a name="govern-permission-sets-aft-additional"></a>

**Integrating with a ticket management tool  **

You can choose to integrate this solution with a ticket or issue management tool, such as Jira or ServiceNow. The following diagram shows an example workflow for this option. You can integrate the ticket management tool with the AFT solution repositories by using your tool’s connectors. For Jira connectors, see [Integrate Jira with GitHub](https://support.atlassian.com/jira-cloud-administration/docs/integrate-jira-software-with-github/). For ServiceNow connectors, see [Integrating with GitHub](https://www.servicenow.com/docs/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrate-with-github.html). You can even build custom solutions that require users to provide a ticket ID as part of the pull request approval. If a request to create a new AWS account by using AFT is approved, that event could initiate a workflow that adds custom fields to the `aft-account-request` GitHub repository. You can design any custom workflow that meets the requirements of your use case.

![Workflow that uses GitHub Actions and a ticket management tool.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/14751255-3781-48db-a6b7-1a03e28c1020/images/83763f65-32ea-4de0-932f-14a1b2d1d3ad.png)

The diagram shows the following workflow:

1. Users request a custom permission set assignment in a ticket management tool, such as Jira.

1. After the case is approved, a workflow begins to update the permission set assignment. (Optional) You can use plugins for custom automation of this step.

1. Operators send the Terraform code with the updated permission set parameters to the `aft-account-request` repository into a development or feature branch.

1. GitHub Actions initiates AWS CodeBuild by using an OpenID Connect (OIDC) call. CodeBuild performs infrastructure as code (IaC) security scans by using tools such as [tfsec](https://aquasecurity.github.io/tfsec/v1.20.0/) and [checkov](https://www.checkov.io/). It warns the operators of any security violations.

1. If no violations are found, GitHub Actions creates an automated pull request and assigns a code review to the code owners. It also creates a tag for the pull request.

1. If the code owner approves the code review, another GitHub Actions workflow starts. It checks pull request standards, including:
   + If the pull request title meets requirements.
   + If pull request body contains approved case numbers.
   + If the pull request is properly tagged.

1. If the pull requests meets standards, GitHub Actions starts the AFT product workflow. It uses starts the `ct-aft-account-request` pipeline in AWS CodePipeline. This pipeline starts the `aft-account-provisioning-framework` custom state machine in Step Functions. This state machine works as previously described in the *Solution overview* section of this pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
