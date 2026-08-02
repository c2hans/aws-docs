---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html
---

# Manage AWS Organizations policies as code by using AWS CodePipeline and Amazon Bedrock
<a name="manage-organizations-policies-as-code"></a>

*Andre Cavalcante and Mariana Pessoa de Queiroz, Amazon Web Services*

## Summary
<a name="manage-organizations-policies-as-code-summary"></a>

You can use* authorization policies* in AWS Organizations to centrally configure and manage access for principals and resources in your member accounts. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) define the maximum available permissions for the AWS Identity and Access Management (IAM) roles and users in your organization. [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) define the maximum available permissions available for resources in your organization.

This pattern helps you to manage SCPs and RCPs as infrastructure as code (IaC) that you deploy through a continuous integration and continuous deployment (CI/CD) pipeline. By using AWS CloudFormation or Hashicorp Terraform to manage these policies, you can reduce the burden associated with building and maintaining multiple authorization policies.

This pattern includes the following features:
+ You create, delete, and update the authorization policies by using *manifest files* (`scp-management.json` and `rcp-management.json`).
+ You work with guardrails instead of policies. You define your guardrails and their targets in the manifest files.
+ The pipeline, which uses AWS CodeBuild and AWS CodePipeline, merges and optimizes the guardrails in the manifest files. For each statement in the manifest file, the pipeline combines the guardrails into a single SCP or RCP and then applies it to the defined targets.
+ AWS Organizations applies the policies to your targets. A *target* can be an AWS account, an organizational unit (OU), an environment (which is a group of accounts or OUs that you define in the `environments.json` file), or a group of accounts that share an [AWS tag](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html).
+ Amazon Bedrock reads the pipeline logs and summarizes all policy changes.
+ The pipeline requires a manual approval. The approver can review the executive summary that Amazon Bedrock prepared, which helps them understand the changes.

## Prerequisites and limitations
<a name="manage-organizations-policies-as-code-prereqs"></a>

**Prerequisites**
+ Multiple AWS accounts that are managed as an organization in AWS Organizations. For more information, see [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html).
+ The SCP and RCP features are enabled in AWS Organizations. For more information, see [Enabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/enable-policy-type.html).
+ Terraform version 1.9.8 or later is [installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).
+ If you are not deploying this solution through a Terraform pipeline, then the Terraform state file must be [stored](https://developer.hashicorp.com/terraform/language/backend/s3) in an Amazon Simple Storage Service (Amazon S3) bucket in the AWS account where you are deploying the policy management pipeline.
+ Python version 3.13.3 or later is [installed](https://www.python.org/downloads/).

**Limitations**
+ You cannot use this pattern to manage SCPs or RCPs that were created outside of this CI/CD pipeline. However, you can recreate existing policies through the pipeline. For more information, see *Migrating existing policies to the pipeline* in the [Additional information](#manage-organizations-policies-as-code-additional) section of this pattern.
+ The number of accounts, OUs, and policies in each account are subject to the [quotas and service limits](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) for AWS Organizations.
+ This pattern cannot be used to configure [management policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_management_policies.html) in AWS Organizations, such as backup policies, tag policies, chat applications policies, or declarative policies.

## Architecture
<a name="manage-organizations-policies-as-code-architecture"></a>

The following diagram shows the workflow of the policy management pipeline and its associated resources.

![Releasing SCPs and RCPs through a policy management pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/372a1ace-5b2e-4f93-9f88-b5b0519ded48/images/a2cceb99-2b93-48e0-b072-bc61a572201f.png)

The diagram shows the following workflow:

1. A user commits changes to the `scp-management.json` or `rcp-management.json` manifest files in the main branch of the remote repository.

1. The change to the `main` branch initiates the pipeline in AWS CodePipeline.

1. CodePipeline starts the `Validate-Plan` CodeBuild project. This project uses a Python script in the remote repository to validate policies and the policy manifest files. This CodeBuild project does the following:

   1. Checks that the SCP and RCP manifest files contain unique statement IDs (`Sid`).

   1. Uses the `scp-policy-processor/main.py` and `rcp-policy-processor/main.py` Python scripts to concatenate guardrails in the guardrails folder into a single RCP or SCP policy. It combines guardrails that have the same `Resource`, `Action`, and `Condition`.

   1. Uses AWS Identity and Access Management Access Analyzer to validate the final, optimized policy. If any there are any findings, the pipeline stops.

   1. Creates `scps.json` and `rcps.json` files, which Terraform uses to create resources.

   1. Runs the `terraform plan` command, which creates a Terraform execution plan.

1. (Optional) The `Validate-Plan` CodeBuild project uses the `bedrock-prompt/prompt.py` script to send a prompt to Amazon Bedrock. You define the prompt in the `bedrock-prompt/prompt.txt` file. Amazon Bedrock uses Anthropic Claude Sonnet 3.5 to generate a summary of the proposed changes by analyzing the Terraform and Python logs.

1. CodePipeline uses an Amazon Simple Notification Service (Amazon SNS) topic in order to notify approvers that changes must be reviewed. If Amazon Bedrock generated a change summary, the notification includes this summary.

1. A policy approver approves the action in CodePipeline. If Amazon Bedrock generated a change summary, the approver can review the summary in CodePipeline prior to approving.

1. CodePipeline starts the `Apply` CodeBuild project. This project uses Terraform to apply the RCP and SCP changes in AWS Organizations.

The IaC template associated with this architecture also deploys the following resources that support the policy management pipeline:
+ An Amazon S3 bucket for storing the CodePipeline artifacts and scripts, such as `scp-policy-processor/main.py` and `bedrock-prompt/prompt.py`
+ An AWS Key Management Service (AWS KMS) key that encrypts the resources created by this solution

## Tools
<a name="manage-organizations-policies-as-code-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed AI service that makes many high-performing foundation models available for use through a unified API.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an IaC tool that helps you use code to provision and manage cloud infrastructure and resources.

**Code repository **

The code for this pattern is available in the [organizations-policy-pipeline](https://github.com/aws-samples/organizations-policy-pipeline) GitHub repository. The following are the key files that are contained in the `sample-repository` folder:
+ In the `environments` folder, `environments.json` contains a list of environments. *Environments* are a group of targets, and they can contain AWS account IDs or organizational units (OUs).
+ In the `rcp-management` folder:
  + The `guardrails` folder contains the individual guardrails for your RCPs
  + The `policies` folder contains the individual RCPs
  + The `rcp-management.json` manifest file helps you manage RCP guardrails, full RCPs, and their associated targets.
+ In the `scp-management` folder:
  + The `guardrails` folder contains the individual guardrails for your SCPs
  + The `policies` folder contains the individual SCPs
  + The `scp-management.json` manifest file helps you manage SCP guardrails, full SCPs, and their associated targets.
+ The `utils` folder contains scripts that can help you migrate your current SCPs and RCPs so that you can manage them through the pipeline. For more information, see the [Additional information](#manage-organizations-policies-as-code-additional) section of this pattern.

## Best practices
<a name="manage-organizations-policies-as-code-best-practices"></a>
+ Before you set up the pipeline, we recommend that you verify that you have not reached the limits of your AWS Organizations [quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html).
+ We recommend that you use the AWS Organizations management account only for tasks that must be performed in that account. For more information, see [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html#bp_mgmt-acct_use-mgmt).

## Epics
<a name="manage-organizations-policies-as-code-epics"></a>

### Set up the target account
<a name="set-up-the-target-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a repository. | Create a repository from which your security operations team will manage the policies. Use one of the third-party repository providers that AWS CodeConnections [supports](https://docs.aws.amazon.com/dtconsole/latest/userguide/supported-versions-connections.html). | DevOps engineer |
| Delegate policy administration. | Delegate administration of AWS Organizations policies to the member account where you are deploying the pipeline. For instructions, see [Create a resource-based delegation policy with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate.html). For a sample policy, see *Sample resource-based delegation policy* in the [Additional information](#manage-organizations-policies-as-code-additional) section of this pattern. | AWS administrator |
| (Optional) Enable the foundation model. | If you want to generate summaries of the policy changes, enable access to the Anthropic Claude 3.5 Sonnet foundation model in Amazon Bedrock in the AWS account where you are deploying the pipeline. For instructions, see [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html). | General AWS |

### Deploy the resources for the pipeline
<a name="deploy-the-resources-for-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Enter the following command to clone the [organizations-policy-pipeline ](https://github.com/aws-samples/organizations-policy-pipeline)repository from GitHub:<br />`git clone https://github.com/aws-samples/organizations-policy-pipeline.git` | DevOps engineer |
| Define your deployment method. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer |
| Deploy the pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer, Terraform |
| Connect the remote repository. | In the previous step, Terraform created an CodeConnections connection to the third-party repository. In the [AWS Developer Tools console](https://console.aws.amazon.com/codesuite/settings/connections), change the status of the connection from `PENDING` to `AVAILABLE`. For instructions, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html). | AWS DevOps |
| Subscribe to the Amazon SNS topic. | Terraform created an Amazon SNS topic. Subscribe an endpoint to the topic and confirm the subscription so that the approvers receive notifications about pending approval actions in the pipeline. For instructions, see [Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html). | General AWS |

### Define your guardrails and policies
<a name="define-your-guardrails-and-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Populate the remote repository. | From the cloned repository, copy the contents of the `sample-repository` folder to your remote repository. This includes the `environments`, `rcp-management`, `scp-management`, and `utils` folders. | DevOps engineer |
| Define your environments. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer |
| Define your guardrails. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer |
| Define your policies. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer |

### Use the manifest file to manage the policies
<a name="use-the-manifest-file-to-manage-the-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the manifest files. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | DevOps engineer |
| Start the pipeline. | Commit and push the changes to the branch of the remote repository that you defined in the `variables.tf` file. Typically, this is the `main` branch. The CI/CD pipeline automatically starts. If there are any pipeline errors, see the [Troubleshooting](#manage-organizations-policies-as-code-troubleshooting) section of this pattern. | DevOps engineer |
| Approve the changes. | When the `Validate-Plan` CodeBuild project is complete, the policy approvers receive a notification through the Amazon SNS topic that you previously configured. Do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | General AWS, Policy approver |
| Validate the deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) | General AWS |

## Troubleshooting
<a name="manage-organizations-policies-as-code-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Manifest file errors in the `Validate-Plan` phase of the pipeline | A "Pipeline errors in the Validation & Plan phase for manifest files" message appears in the pipeline output if there are any errors in the `scp-management.json` or `rcp-management.json` files. Possible errors include an incorrect environment name, duplicated SIDs, or invalid fields or values. Do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) |
| IAM Access Analyzer findings in the `Validate-Plan` phase of the pipeline | A "Findings in IAM Access Analyzer during Validation & Plan phase" message appears in the pipeline output if there are any errors in the guardrail or policy definitions. This pattern uses IAM Access Analyzer to validate the final policy. Do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-organizations-policies-as-code.html) |

## Related resources
<a name="manage-organizations-policies-as-code-resources"></a>
+ [JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) (IAM documentation)
+ [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (AWS Organizations documentation)
+ [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (AWS Organizations documentation)
+ [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) (Amazon Bedrock documentation)
+ [Approve or reject an approval action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-approve-or-reject.html) (CodePipeline documentation)

## Additional information
<a name="manage-organizations-policies-as-code-additional"></a>

**Sample resource-based delegation policy**

The following is a sample resource-based delegation policy for AWS Organizations. It allows the delegated administer account to manage SCPs and RCPs for the organization. In the following sample policy, replace `<MEMBER_ACCOUNT_ID>` with the ID of the account where you are deploying the policy management pipeline.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DelegationToAudit",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<MEMBER_ACCOUNT_ID>:root"
      },
      "Action": [
        "organizations:ListTargetsForPolicy",
        "organizations:CreatePolicy",
        "organizations:DeletePolicy",
        "organizations:AttachPolicy",
        "organizations:DetachPolicy",
        "organizations:DisablePolicyType",
        "organizations:EnablePolicyType",
        "organizations:UpdatePolicy",
        "organizations:DescribeEffectivePolicy",
        "organizations:DescribePolicy",
        "organizations:DescribeResourcePolicy"
      ],
      "Resource": "*"
    }
  ]
}
```

**Migrating existing policies to the pipeline**

If you have existing SCPs or RCPs that you want to migrate and manage through this pipeline, you can use the Python scripts in the `sample-repository/utils` folder of the code repository. These scripts include:
+ `check-if-scp-exists-in-env.py` – This script checks whether a specified policy applies to any targets in a specific environment, which you define in the `environments.json` file. Enter the following command to run this script:

  ```
  python3 check-if-scp-exists-in-env.py \
     --policy-type <POLICY_TYPE> \
     --policy-name <POLICY_NAME> \
     --env-id <ENV_ID>
  ```

  Replace the following in this command:
  + `<POLICY_TYPE>` is `scp` or `rcp`
  + `<POLICY_NAME>` is the name of the SCP or RCP
  + `<ENV_ID>` is the ID of the environment that you defined in the `environments.json` file
+ `create-environments.py` – This script creates an environments.json file based on the current SCPs and RCPs in your environment. It excludes policies deployed through AWS Control Tower. Enter the following command to run this script, where `<POLICY_TYPE>` is `scp` or `rcp`:

  ```
  python create-environments.py --policy-type <POLICY_TYPE>
  ```
+ `verify-policies-capacity.py` – This script checks each environment that you define to determine how much capacity remains for each AWS Organizations policy-related quota. You define the environments to check in the in `environments.json` file. Enter the following command to run this script, where `<POLICY_TYPE>` is `scp` or `rcp`:

  ```
  python verify-policies-capacity.py --policy-type <POLICY_TYPE>
  ```
