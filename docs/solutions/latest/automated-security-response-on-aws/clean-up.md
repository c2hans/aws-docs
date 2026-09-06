---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/clean-up.html
---

# Clean up
<a name="clean-up"></a>

## Delete the example resources
<a name="delete-the-example-resources"></a>

In the member account, delete the example Lambda function you created.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | Delete the example Lambda Function |

## Delete the admin stack
<a name="delete-the-admin-stack"></a>

In the admin account, delete the admin stack.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Delete the admin stack | None |
|  `222222222222`  | Member | None | None |

## Delete the member stack
<a name="delete-the-member"></a>

In the Admin account, delete the member StackSet.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Delete the member StackSet<br />Confirm member stack deleted | Confirm member stack deleted |
|  `222222222222`  | Member | Confirm member stack deleted | Confirm member stack deleted |

## Delete the member roles stack
<a name="delete-the-member-roles"></a>

In the Admin account, delete the member roles StackSet.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Delete the member roles StackSet<br />Confirm member roles stack deleted | None |
|  `222222222222`  | Member | Confirm member roles stack deleted | None |

## Delete the retained roles
<a name="delete-the-retained-roles"></a>

In each account, delete the retained IAM roles.

 **Important**: These roles are retained for remediations which require a role in order for the remediation to continue functioning (for example, VPC flow logging). Confirm that you do not require the continued function of any of these roles before deleting them.

Delete any roles prefixed with **SO0111-.**

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Delete retained roles | None |
|  `222222222222`  | Member | Delete retained roles | None |

## Schedule the retained AWS KMS keys for deletion
<a name="schedule-the-retained-kms"></a>

The admin and member stacks both create and retain an AWS KMS key. You incur charges if you keep these keys.

These keys are retained in order to give you access to any resources encrypted by the solution. Confirm that you do not require them before scheduling them for deletion.

Identify the keys deployed by the solution using the aliases created by the solution or from the CloudFormation history. Schedule them for deletion.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Identify and schedule admin key for deletion<br />Identify and schedule member key for deletion | Identify and schedule member key for deletion |
|  `222222222222`  | Member | Identify and schedule member key for deletion | Identify and schedule member key for deletion |

## Delete the stacks for self-managed StackSets permissions
<a name="delete-the-stacks-for-self-managed"></a>

Delete the stacks created to allow for self-managed StackSets permissions

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Delete the StackSet administrator role stack | None |
|  `222222222222`  | Member | Delete the StackSet execution role stack | None |
