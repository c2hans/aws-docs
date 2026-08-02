---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/getting-stated-with-asr.html
---

# Tutorial: Getting Started with Automated Security Response on AWS
<a name="getting-stated-with-asr"></a>

This is a tutorial that will guide you through your first deployment. It will begin with the prerequisites for deploying the solution and it will end with you remediating example findings in a member account.

## Prepare the accounts
<a name="prepare-the-accounts"></a>

In order to demonstrate the cross-account and cross-Region remediation capabilities of the solution, this tutorial will use two accounts. You can also deploy the solution to a single account.

The following examples use accounts `111111111111` and `222222222222` to demonstrate the solution. `111111111111` will be the admin account and `222222222222` will be the member account. We will set up the solution to remediate findings for resources in the Regions `us-east-1` and `us-west-2`.

The table below is an example to illustrate the actions we will take for each step in each account and Region.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | None |

The admin account is the account that will perform the administration actions of the solution, namely initiating remediations manually or enabling fully automated remediation using the Remediation Configuration DynamoDB table. This account must also be the Security Hub delegated administrator account for all accounts in which you wish to remediate findings, but it does not need to be nor should it be the AWS Organizations administrator account for the AWS Organization to which your accounts belong.

## Enable AWS Config
<a name="enable-aws-config"></a>

Review the following documentation:
+  [AWS Config documentation](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+  [AWS Config pricing](https://aws.amazon.com/config/pricing/)
+  [Enabling AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)

Enable AWS Config in both accounts and both Regions. This will incur charges.

**Important**
Ensure that you select the option to "Include global resources (e.g., AWS IAM resources)." If you do not select this option when enabling AWS Config, you will not see findings related to global resources (e.g. AWS IAM resources)

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Enable AWS Config | Enable AWS Config |
|  `222222222222`  | Member | Enable AWS Config | Enable AWS Config |

## Enable AWS security hub
<a name="enable-aws-security-hub"></a>

Review the following documentation:
+  [AWS Security Hub documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
+  [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/)
+  [Enabling AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html)

Enable AWS Security Hub in both accounts and both Regions. This will incur charges.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Enable AWS Security Hub | Enable AWS Security Hub |
|  `222222222222`  | Member | Enable AWS Security Hub | Enable AWS Security Hub |

## Enable consolidated control findings
<a name="enable-consolidated-findings"></a>

Review the following documentation:
+  [Generating and updating control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html)

For the purposes of this tutorial, we will demonstrate the usage of the solution with the consolidated control findings feature of AWS Security Hub enabled, which is the recommended configuration. In partitions which do not support this feature as of the time of writing, you will need to deploy the standard-specific playbooks rather than SC (Security Control).

Enable consolidated control findings in both accounts and both Regions.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Enable consolidated control findings | Enable consolidated control findings |
|  `222222222222`  | Member | Enable consolidated control findings | Enable consolidated control findings |

It may take some time for findings to be generated with the new feature. You can proceed with the tutorial, but you will be unable to to remediate the findings generated without the new feature. Findings generated with the new feature can be identified by the `GeneratorId` field value `security-control/<control_id>`.

## Configure cross-Region finding aggregation
<a name="configure-cross-region-findings"></a>

Review the following documentation:
+  [Cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html)
+  [Enabling cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-enable.html)

Configure finding aggregation from **us-west-2** to **us-east-1** in both accounts.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Configure aggregation from us-west-2 | None |
|  `222222222222`  | Member | Configure aggregation from us-west-2 | None |

It may take some time for findings to propagate to the aggregation Region. You can proceed with the tutorial, but you will be unable to remediate findings from other Regions until they begin to appear in the aggregation Region.

## Designate a Security Hub administrator account
<a name="designate-a-security-hub-admin"></a>

Review the following documentation:
+  [Managing accounts in AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)
+  [Managing organization member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html)
+  [Managing member accounts by invitation](https://docs.aws.amazon.com/securityhub/latest/userguide/account-management-manual.html)

In the proceeding example, we will use the manual invitation method. For a set of production accounts, we recommend managing Security Hub delegated adminstration through AWS Organizations.

From the AWS Security Hub console in the admin account (`111111111111`), invite the member account (`222222222222`) to accept the admin account as a Security Hub delegated administrator. From the member account, accept the invitation.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Invite the member account | None |
|  `222222222222`  | Member | Accept the invitation | None |

It may take some time for findings to propagate to the admin account. You can proceed with the tutorial, but you will be unable to remediate findings from member accounts until they begin to appear in the admin account.

## Create the roles for self-managed StackSets permissions
<a name="create-roles-for-self-managed-stacksets"></a>

Review the following documentation:
+  [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
+  [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html)

We will be deploying CloudFormation stacks to multiple accounts, so we will use StackSets. We cannot use service-managed permissions because the admin stack and the member stack have nested stacks, which aren’t supported by the service, so we must use self-managed permissions.

Deploy the stacks for basic permissions for StackSet operations. For production accounts, you may wish to narrow the permissions according to the "advanced permissions options" documentation.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Deploy the StackSet administrator role stack<br />Deploy the StackSet Execution role stack | None |
|  `222222222222`  | Member | Deploy the StackSet execution role stack | None |

## Create the insecure resources that will generate example findings
<a name="create-the-insecure-resources"></a>

Review the following documentation:
+  [Security Hub controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html)
+  [AWS Lambda controls](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html)

The following example resource with an insecure configuration in order to demonstrate a remediation. The example control is Lambda.1: Lambda function policies should prohibit public access.

**Important**
We will be intentionally creating a resource with an insecure configuration. Please review the nature of the control and evaluate the risk of creating such a resource in your environment for yourself. Be aware of any tooling your organization may have for detecting and reporting such resources and request an exception if appropriate. If the example control we have selected is inappropriate for you, select another control that the solution supports.

In the second Region of the member account, navigate to the AWS Lambda console and create a function in the latest Python runtime. Under Configuration → Permissions, add a policy statement to allow invoking the function from the URL with no authentication.

Confirm on the console page that the function allows public access. After the solution remediates this issue, compare the permissions to confirm that the public access has been revoked.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | Create a Lambda function with an insecure configuration |

It may take some time for AWS Config to detect the insecure configuration. You can proceed with the tutorial, but you will be unable to remediate the finding until Config detects it.

## Create CloudWatch log groups for related controls
<a name="create-cloudwatch-log-groups"></a>

Review the following documentation:
+  [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
+  [CloudTrail controls](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html)

Various CloudTrail controls supported by the solution require there to be a CloudWatch Log group that is the destination of a multi-Region CloudTrail. In the following example, we will create a placeholder log group. For production accounts, you should properly configure CloudTrail integration with CloudWatch Logs.

Create a log group in each account and Region with the same name, for example: `asr-log-group`.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Create a log group | Create a log group |
|  `222222222222`  | Member | Create a log group | Create a log group |
