---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline.html
---

# Manage AWS IAM Identity Center permission sets as code by using AWS CodePipeline
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline"></a>

*Andre Cavalcante and Claison Amorim, Amazon Web Services*

## Summary
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-summary"></a>

AWS IAM Identity Center helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and applications. You can create and manage user identities in IAM Identity Center, or you can connect an existing identity source, such as a Microsoft Active Directory domain or an external identity provider (IdP). IAM Identity Center provides a unified administration experience to define, customize, and assign fine-grained access to your AWS environment by using [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html). Permission sets apply to the federated users and groups from your IAM Identity Center identity store or your external IdP.

This pattern helps you to manage IAM Identity Center permission sets as code in your multi-account environment that is managed as an organization in AWS Organizations. With this pattern, you can achieve the following:
+ Create, delete, and update permission sets
+ Create, update, or delete permission set assignments to target AWS accounts, organizational units (OUs), or your organization root.

To manage IAM Identity Center permissions and assignments as code, this solution deploys a continuous integration and continuous delivery (CI/CD) pipeline that uses AWS CodeBuild and AWS CodePipeline. You manage the permission sets and assignments in JSON templates that you store in a remote repository. When Amazon EventBridge rules detect a change to the repository or detect modifications to the accounts in the target OU, it starts an AWS Lambda function. The Lambda function initiates the CI/CD pipeline that updates the permission sets and assignments in IAM Identity Center.

## Prerequisites and limitations
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-prereqs"></a>

**Prerequisites**
+ A multi-account environment managed as an organization in AWS Organizations. For more information, see [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html).
+ IAM Identity Center, enabled and configured with an identity source. For more information, see [Getting Started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the IAM Identity Center documentation.
+ A member account that is registered as the delegated administrator for the following AWS services:
  + IAM Identity Center – For instructions, see [Register a member account](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html#delegated-admin-how-to-register) in the IAM Identity Center documentation.
  + AWS Organizations – For instructions, see [Delegated administrator for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html). This account must have permissions to list and describe accounts and OUs.
**Note**
You must use the same account as the delegated administrator for both services.
+ Permissions to deploy AWS CloudFormation stacks in the IAM Identity Center delegated administrator account and in the organization’s management account. For more information, see [Controlling access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) in the CloudFormation documentation.
+ An Amazon Simple Storage Service (Amazon S3) bucket in the IAM Identity Center delegated administrator account. You upload the artifact code into this bucket. For instructions, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation.
+ The account ID of the organization’s management account. For instructions, see [Finding your AWS account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId).
+ A repository in your source code host, such as GitHub.

**Limitations**
+ This pattern cannot be used to manage or assign permission sets for single-account environments or for accounts that are not managed as an organization in AWS Organizations.
+ Permission set names, assignment IDs, and IAM Identity Center principal types and IDs cannot be modified after deployment.
+ This pattern helps you create and manage [custom permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetcustom.html). You cannot use this pattern to manage or assign [predefined permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetpredefined.html).
+ This pattern cannot be used to manage a permission set for the organization’s management account.

## Architecture
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-architecture"></a>

**Target architecture**

![Using a CI/CD pipeline to manage permission sets in IAM Identity Center.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/419aaa80-1b97-402d-9c74-c1b8c1ddd1cb/images/1f143bc4-c2c6-4ab6-8615-742fec617f18.png)

The diagram shows the following workflow:

1. A user makes one of the following changes:
   + Commits one or more changes to the remote repository, such as GitHub
   + Modifies the accounts in the OU in AWS Organizations

1. If the user committed a change to the remote repository to the main branch, the pipeline starts.

   If the user modified the accounts in the OU, then the `MoveAccount` EventBridge rule detects the change and starts a Lambda function in the organization’s management account.

1. The initiated Lambda function starts the CI/CD pipeline in CodePipeline.

1. CodePipeline starts the `TemplateValidation` CodeBuild project. The `TemplateValidation` CodeBuild project uses a Python script in the remote repository to validate the permission set templates. CodeBuild validates the following:
   + The permission set names are unique.
   + The assignment statement IDs (`Sid`) are unique.
   + Policy definitions in the `CustomPolicy` parameter and valid. (This validation uses AWS Identity and Access Management Access Analyzer.)
   + The Amazon Resource Names (ARNs) of the managed policies are valid.

1. The `PermissionSet` action group in the `Deploy` CodeBuild project uses AWS SDK for Python (Boto3) to delete, create, or update the permission sets in IAM Identity Center. Only permission sets with the `SSOPipeline:true` tag are affected. All permission sets that are managed through this pipeline have this tag.

1. The `Assignments` action group in the `Deploy` CodeBuild project uses Terraform to delete, create, or update the assignments in IAM Identity Center. The Terraform backend state files are stored in an Amazon S3 bucket in the same account.

1. CodeBuild updates the permissions sets and assignments in IAM Identity Center.

**Automation and scale**

Because all new accounts in a multi-account environment are moved to a specific organizational unit in AWS Organizations, this solution automatically runs and grants the required permission sets to all accounts that you specify in the assignment templates. No additional automations or scaling actions are necessary.

In large environments, the number of API requests to IAM Identity Center might cause this solution to run more slowly. Terraform and Boto3 automatically manage throttling to minimize any performance degradation.

## Tools
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository **

The code for this pattern is available in the [aws-iam-identity-center-pipeline](https://github.com/aws-samples/aws-iam-identity-center-pipeline) repository. The templates folder in the repository includes sample templates for both permission sets and assignments. It also includes AWS CloudFormation templates for deploying the CI/CD pipeline and AWS resources in the target accounts.

## Best practices
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-best-practices"></a>
+ Before you start modifying the permission set and assignment templates, we recommend that you plan permission sets for your organization. Consider what the permissions should be, which accounts or OUs the permission set should apply to, and which IAM Identity Center principals (users or groups) should be affected by the permission set. Permission set names, association IDs, and IAM Identity Center principal types and IDs cannot be modified after deployment.
+ Adhere to the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the AWS Identity and Access Management (IAM) documentation.

## Epics
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-epics"></a>

### Plan permission sets and assignments
<a name="plan-permission-sets-and-assignments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | In a bash shell, enter the following command. This clones the [aws-iam-identity-center-pipeline](https://github.com/aws-samples/aws-iam-identity-center-pipeline) repository from GitHub.<pre>git clone https://github.com/aws-samples/aws-iam-identity-center-pipeline.git</pre> | DevOps engineer |
| Define the permission sets. | 1. In the cloned repository, navigate to the `templates/permissionsets` folder, and then open one of the available templates.<br />2. In the `Name` parameter, enter a name for the permission set. This value must be unique, and it cannot be changed after deployment.<br />3. In the `Description` parameter, briefly describe the permission set, such as its use case.<br />4. In the `SessionDuration` parameter, specify the length of time that a user can be signed in to an AWS account. Use [ISO-8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) (Wikipedia), such as `PT4H` for 4 hours. If no value is defined, the default in IAM Identity Center is 1 hour.<br />5. In the `RelayState` parameter, specify the URL that provides quick access to the console that is most appropriate for the user’s role.<br />6. Customize the policies in the permission set. All of the following parameters are optional and can be modified after deployment. You must use at least one of the parameters in order to define the policies in the permission set:In the `ManagedPolicies` parameter, enter the ARNs of any [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) that you want to assign.In the `CustomerManagedPolicies` parameter, enter the names of any [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that you want to assign. Do not use the ARN.In the `PermissionBoundary` parameter, do the following to assign a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html):If you’re using an AWS managed policy as a permissions boundary, in `PolicyType`, enter `AWS`, and in `Policy`, enter the ARN of the policy.If you’re using a customer managed policy as a permissions boundary, in `PolicyType`, enter `Customer`, and in `Policy`, enter the name of the policy. Do not use the ARN.In the `CustomPolicy` parameter, define any custom, JSON-formatted policies that you want to assign. For more information about the JSON policy structure, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json).<br />7. Save and close the permission set template. We recommend that you save the file with a name that matches the name of the permission set.<br />8. Repeat this process to create as many permissions sets as needed for your organization, and delete any sample templates that aren’t required. | DevOps engineer |
| Define the assignments. | 1. In the cloned repository, navigate to the `templates/assignments` folder, and then open `iam-identitycenter-assigments.json`. This file describes how you want to assign the permission sets to AWS accounts or OUs.<br />2. In the `SID` parameter, enter an identifier for the assignment. This value must be unique, and it cannot be modified after deployment.<br />3. In the `Target` parameter, define the accounts or organizations where you want to apply the permission set. Valid values are account IDs, OUs, or `root`. `root` assigns the permission set to all member accounts in the organization, excluding the management account. Enter the values in double quotation marks, and separate multiple values with commas. Account IDs and OUs should follow the pattern: `{{account_name}}:{{account_id}}` or `{{ou_name}}:{{ou_id}}`. If you want to assign permissions recursively to nested OUs, use the OU pattern with a wildcard at the end. Example: `{{ou_name}}:{{ou_id}}:*` <br />4. In the `PrincipalType` parameter, enter the type of IAM Identity Center principal that will be affected by the permission set. Valid values are `USER` or `GROUP`. This value cannot be modified after deployment.<br />5. In the `PrincipalID` parameter, enter the name of the user or group in the IAM Identity Center identity store that will be affected by the permission set. This value cannot be modified after deployment.<br />6. In the `PermissionSetName` parameter, enter the name of the permission set that you want to assign.<br />7. Repeat steps 2–6 to create as many assignments as needed in this file. Typically, there is one assignment for each permission set. Delete any sample assignments that aren’t required.<br />8. Save and close the `iam-identitycenter-assigments.json` file. | DevOps engineer |

### Deploy the permission sets and assignments
<a name="deploy-the-permission-sets-and-assignments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy resources in the IAM Identity Center delegated administrator account. | 1. In the IAM Identity Center delegated administrator account, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. Deploy the `iam-identitycenter-pipeline.yaml` template. Give the stack a clear and descriptive name, and update the parameters as instructed. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. | DevOps engineer |
| Deploy resources in the AWS Organizations management account. | 1. Sign in to the organization’s management account.<br />2. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />3. In the navigation bar, choose the name of the currently displayed AWS Region. Then choose the `us-east-1` Region. This Region is required so that the `MoveAccount` EventBridge rule can detect AWS CloudTrail events associated with organization changes.<br />4. Deploy the `iam-identitycenter-organization` template. Give the stack a clear and descriptive name, and update the parameters as instructed. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. | DevOps engineer |
| Finish the remote repository setup. | Change the status of the AWS CodeConnections connection from `PENDING` to `AVAILABLE`. This connection was created when you deployed the CloudFormation stack. For instructions, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html) in the CodeConnections documentation.  | DevOps engineer |
| Upload files to the remote repository. | Upload all of files you have downloaded from the `aws-samples` repository and edited in previous steps to the remote repository. Changes to the `main` branch start the pipeline, which creates or updates the permission sets and assignments. | DevOps engineer |

### Updating the permission sets and assignments
<a name="updating-the-permission-sets-and-assignments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the permission sets and assignments. | When the `MoveAccount` Amazon EventBridge rule detects modifications to the accounts in the organization, the CI/CD pipeline automatically starts and updates the permission sets. For example, if you add an account to an OU specified in the assignments JSON file, then the CI/CD pipeline will apply the permission set to the new account.<br />If you want to modify the deployed permission sets and assignments, update the JSON files and then commit them to the remote repository. <br />Note the following when using the CI/CD pipeline to manage previously deployed permission sets and associations:+ If you change the name of a permission set, the CI/CD pipeline deletes the original permission set and creates a new one.<br />+ This pipeline manages only permission sets that have the `SSOPipeline:true` tag.<br />+ You can have multiple permission set and assignment templates in the same folder in the repository.<br />+ If you delete a template, the pipeline deletes the assignment or permission set.<br />+ If you delete an entire assignment JSON block, the pipeline deletes the assignment from IAM Identity Center.<br />+ You can't delete a permission set that is assigned to an AWS account. First, you must unassign the permission set. | DevOps engineer |

## Troubleshooting
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Access denied errors | Confirm that you have the permissions required to deploy the CloudFormation templates and the resources defined within them. For more information, see [Controlling access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) in the CloudFormation documentation. |
| Pipeline errors in the validation phase | This error appears if there are any errors in the permission set or assignment templates.1. In CodeBuild, view the [build details](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html).<br />2. In the build log, find the validation error that provides more information about what caused the build to fail.<br />3. Update the permission set or assignment templates, and then commit them to the repository.<br />4. The CI/CD pipeline restarts the CodeBuild project. Monitor the status to confirm that the validation error is resolved. |

## Related resources
<a name="manage-aws-iam-identity-center-permission-sets-as-code-by-using-aws-codepipeline-resources"></a>
+ [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) (IAM Identity Center documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
