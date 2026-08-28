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
| Define your deployment method. | 1. In the cloned repository, open the `variables.tf` file.<br />2. For `project_name`, enter the prefix that you want to apply to names of the deployed resources.<br />3. For `provider_type`, enter the provider of the remote repository. Valid values are provided in the file.<br />4. For `full_repository_name`, enter the name of the remote repository.<br />5. For `branch_name`, enter the name of the Git branch that you will use to deploy policies. A push or merge in this branch starts the pipeline. Typically, this is the main branch.<br />6. For `terraform_version`, enter the version of Terraform that you are using.<br />7. For `enable_bedrock`, enter `true` if you want Amazon Bedrock to summarize the changes. Enter `false` if you do not want to generate a summary of the changes.<br />8. For `tags`, enter the key-value pairs that you want to assign as tags to the deployed resources.<br />9. Save and close the `variables.tf` file. | DevOps engineer |
| Deploy the pipeline. | 1. Enter the following command to create a plan and review the changes:<pre>terraform plan</pre><br />2. Enter the following command to apply the plan and create the pipeline infrastructure:<pre>terraform apply</pre> | DevOps engineer, Terraform |
| Connect the remote repository. | In the previous step, Terraform created an CodeConnections connection to the third-party repository. In the [AWS Developer Tools console](https://console.aws.amazon.com/codesuite/settings/connections), change the status of the connection from `PENDING` to `AVAILABLE`. For instructions, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html). | AWS DevOps |
| Subscribe to the Amazon SNS topic. | Terraform created an Amazon SNS topic. Subscribe an endpoint to the topic and confirm the subscription so that the approvers receive notifications about pending approval actions in the pipeline. For instructions, see [Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html). | General AWS |

### Define your guardrails and policies
<a name="define-your-guardrails-and-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Populate the remote repository. | From the cloned repository, copy the contents of the `sample-repository` folder to your remote repository. This includes the `environments`, `rcp-management`, `scp-management`, and `utils` folders. | DevOps engineer |
| Define your environments. | 1. In the `environments` folder, open the `environments.json` file. This is the file where you define the target AWS accounts and OUs for your RCPs and SCPs.<br />2. Delete the example environments.<br />3. Add your target environments in the following format:<pre>[<br />    {<br />        "ID": "<environment-name>",<br />        "Target": [<br />            "<ou-name>:<ou-id>",<br />            "<account-name>:<account-id>"<br />        ]<br />    }<br />]</pre><br />Where:`<environment-name>` is the name you assign to the group of OUs and AWS accounts. You can use this name in the manifest file to define where you want to apply your policies.`<ou-name>` is the name of the target OU.`<ou-id>` is the ID of the target OU.`<account-name>` is the name of the target AWS account.`<account-id>` is the ID of the target AWS account.<br />For examples, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/blob/main/sample-repository/environments/environments.json).<br />4. Save and close the `environments.json` file. | DevOps engineer |
| Define your guardrails. | 1. Navigate to the `rcp-management/guardrails` folder in your remote repository. This is the folder where you define the guardrails for your RCP manifest file. Each guardrail must in an individual file. Guardrail files can contain one or more statements.You can use the same guardrail in multiple statements in the manifest files for SCPs and RCPs. If you modify the guardrail, any policies that include this guardrail are affected.<br />2. Delete any example guardrails that were copied from the source code repository.<br />3. Create a new .json file and give it a descriptive name.<br />4. Open the .json file you created.<br />5. Define the guardrail in the following format:<pre>[<br />    {<br />        "Sid": "<guardrail-name>",<br />        "Effect": "<effect-value>",<br />        "Action": [<br />            "<action-name>"<br />        ],<br />        "Resource": "<resource-arn>",<br />        "Condition": {<br />            "<condition-operator>": {<br />                "<condition-key>": [<br />                    "<condition-value>"<br />                ]<br />            }<br />        }<br />    }<br />]</pre><br />Where:`<guardrail-name>` is a unique name for the guardrail. This name cannot be used for any other guardrails.`<effect-value>` must be `Allow` or `Deny`. For more information, see [Effect](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html).`<action-name>` must be a valid name of an action that the service supports. For more information, see [Action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html).`<resource-arn>` is the Amazon Resource Name (ARN) of the resource that the guardrail applies to. You can also use wildcard characters, such as `*` or `?`. For more information, see [Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html).`<condition-operator>` is a valid condition operator. For more information, see [Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html).`<condition-key>` is a valid global condition context key or a service-specific context key. For more information, see [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html).`<condition-value>` is the specific value used in a condition to evaluate whether a guardrail applies. For more information, see [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html).<br />For example RCP guardrails, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/tree/main/sample-repository/rcp-management/guardrails).<br />6. Save and close the .json file.<br />7. Repeat these steps to create as many RCP guardrails as needed.<br />8. Repeat these steps in the `scp-management/guardrails` folder to create as many guardrails as you need for your SCPs. For example SCP guardrails, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/tree/main/sample-repository/scp-management/guardrails). | DevOps engineer |
| Define your policies. | 1. Navigate to the `rcp-management/policies` folder in your remote repository. This is the folder where you define full policies for your RCP manifest file. Each policy must be an individual file.If you modify a policy in this folder, the policy changes affect any accounts or OUs that this policy is applied to, as defined in the manifest file.<br />2. Delete any example policies that were copied from the source code repository.<br />3. Create a new .json file and give it a descriptive name.<br />4. Open the .json file you created.<br />5. Define the RCP. For example RCPs, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/tree/main/sample-repository/rcp-management/policies) or see [Resource control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_examples.html) in the AWS Organizations documentation.<br />6. Save and close the .json file.<br />7. Repeat these steps to create as many RCPs as needed.<br />8. Repeat these steps in the `scp-management/policies` folder to create as many SCPs as needed. For example SCPs, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/tree/main/sample-repository/scp-management/policies) or see [Service control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) in the AWS Organizations documentation. | DevOps engineer |

### Use the manifest file to manage the policies
<a name="use-the-manifest-file-to-manage-the-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the manifest files. | 1. In the `rcp-management` folder, open the `rcp-management.json` file. This is the file where you define which RCP guardrails and full RCPs apply to your target environments. For an example of this file, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/blob/main/sample-repository/rcp-management/rcp-management.json).<br />2. Delete the example statement.<br />3. Add a new statement in the following format:<pre>[<br />    {<br />        "SID": "<statement-name>",<br />        "Target": {<br />            "Type": "<target-type>",<br />            "ID": "<target-name>"<br />        },<br />        "Guardrails": [<br />            "<guardrail-name>"<br />        ],<br />        "Policy": "<policy-name>",<br />        "Comments": "<comment-text>"<br />    }<br />]</pre><br />Where:`<statement-name>` is a unique name for the statement.`<target-type>` is the type of target where you want to apply the policy. Valid values are `Account`, `OU`, `Environment`, or `Tag`.`<target-name>` is the identifier of the target where you want to apply the policy. Enter one of the following:For an AWS account, enter the identifier as `<account-name>:<account-id>`.For an OU, enter the identifier as `<OU-name>:<ou-id>`.For an environment, enter the unique name that you defined in the `environments.json` file.For a tag, enter the key-value pair as `<tag-key>:<tag-value>`.`<guardrail-name>` is the unique name of the RCP guardrail that you defined in the `rcp-management/guardrails` folder. You can add multiple guardrails in this element. You can leave this field empty if you do not want to apply a guardrail.`<policy-name>` is the unique name of the RCP that you defined in the `rcp-management/policies` folder. You can add only one policy in this element. You can leave this field empty if you do not want to apply a policy.`<comment-text>` is a description that you can enter for documentation purposes. This field is not used during pipeline processing. You can leave this field empty if you do not want to add a comment.<br />4. Repeat these steps to add as many statements as necessary to configure RCPs for your organization.<br />5. Save and close the `rcp-management.json` file.<br />6. In the `scp-management` folder, repeat these steps in the `scp-management.json` file. This is the file where you define which SCP guardrails and full SCPs apply to your target environments. For an example of this file, see the [source code repository](https://github.com/aws-samples/organizations-policy-pipeline/blob/main/sample-repository/scp-management/scp-management.json). | DevOps engineer |
| Start the pipeline. | Commit and push the changes to the branch of the remote repository that you defined in the `variables.tf` file. Typically, this is the `main` branch. The CI/CD pipeline automatically starts. If there are any pipeline errors, see the [Troubleshooting](#manage-organizations-policies-as-code-troubleshooting) section of this pattern. | DevOps engineer |
| Approve the changes. | When the `Validate-Plan` CodeBuild project is complete, the policy approvers receive a notification through the Amazon SNS topic that you previously configured. Do the following:1. Open the notification message.<br />2. If available, review the summary of policy changes.<br />3. Follow the instructions in [Approve or reject an approval action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-approve-or-reject.html). | General AWS, Policy approver |
| Validate the deployment. | 1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2) in the account that is the delegated administrator for AWS Organizations.<br />2. On the **Service control policies** page, confirm that the SCPs that you created are listed.<br />3. Choose an SCP that is managed through the pipeline and confirm that it applies to the intended targets.<br />4. On the **Resource control policies** page, confirm that the RCPs that you created are listed.<br />5. Choose an RCP that is managed through the pipeline and confirm that it applies to the intended targets. | General AWS |

## Troubleshooting
<a name="manage-organizations-policies-as-code-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Manifest file errors in the `Validate-Plan` phase of the pipeline | A "Pipeline errors in the Validation & Plan phase for manifest files" message appears in the pipeline output if there are any errors in the `scp-management.json` or `rcp-management.json` files. Possible errors include an incorrect environment name, duplicated SIDs, or invalid fields or values. Do the following:1. Follow the instructions in [View build details in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html).<br />2. In the build log, find the validation error. The error provides more information about what caused the build to fail.<br />3. Update the corresponding .json file.<br />4. Commit and push the updated file to the remote repository. The pipeline restarts.<br />5. Monitor the status to confirm that the validation error is resolved. |
| IAM Access Analyzer findings in the `Validate-Plan` phase of the pipeline | A "Findings in IAM Access Analyzer during Validation & Plan phase" message appears in the pipeline output if there are any errors in the guardrail or policy definitions. This pattern uses IAM Access Analyzer to validate the final policy. Do the following:1. Follow the instructions in [View build details in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html).<br />2. In the build log, find the IAM Access Analyzer validation error. The error provides more information about what caused the build to fail. For more information about the finding types, see [IAM policy validation check reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html).<br />3. Update the corresponding .json file for the guardrail or policy.<br />4. Commit and push the updated file to the remote repository. The pipeline restarts.<br />5. Monitor the status to confirm that the validation error is resolved. |

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
