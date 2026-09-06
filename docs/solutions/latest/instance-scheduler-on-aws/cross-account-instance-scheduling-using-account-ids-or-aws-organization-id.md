---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/cross-account-instance-scheduling-using-account-ids-or-aws-organization-id.html
---

# Cross-account instance scheduling using account IDs or AWS Organization ID
<a name="cross-account-instance-scheduling-using-account-ids-or-aws-organization-id"></a>

This solution includes a template ([instance-scheduler-on-aws-remote.template](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws-remote.template)) that creates the [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) roles and other necessary resources to enable the solution to start scheduling in the secondary accounts. You can review and modify permissions in the remote template before you launch the stack.

## Enabling cross account scheduling using Account IDs
<a name="enabling-cross-account-scheduling-using-account-ids"></a>

To apply automated start-stop schedules to resources in secondary accounts:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the [instance-scheduler-on-aws](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template) AWS CloudFormation template in the primary account.

1. Launch the remote template ([instance-scheduler-on-aws-remote](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws-remote.template)) in each applicable secondary account. When each remote stack is launched, it creates a cross-account role Amazon Resource Name (ARN).

1. Update the primary solution stack with the Account ID in the **Provide Organization** **ID** or **List of Remote Account IDs** parameters to allow the solution to perform start and stop actions on instances in the secondary accounts.

## Enabling cross account scheduling using AWS Organization ID
<a name="enabling-cross-account-scheduling-using-aws-organization-id"></a>

To apply automated start-stop schedules to resources in secondary accounts:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the [instance-scheduler-on-aws](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template) AWS CloudFormation template in the primary account.

1. Set the CloudFormation parameter **Using AWS Organizations?** as Yes,and provide the organization ID in the **Provide** **Organization ID** OR **List of Remote Account IDs** CloudFormation parameters.

1. After deploying the stack in the primary account, launch the remote template `(instance-scheduler-on-aws-remote)` in each applicable secondary account in the same Region as the solution in the primary account. When each remote stack is launched successfully, the primary solution account will be updated with the account id without any further changes in the primary account.

## Managing Account IDs with AWS Systems Manager Parameter Store
<a name="managing-account-ids"></a>

Use AWS Systems Manager Parameter Store to store remote account IDs. You can store remote Account IDs as a list parameter where every item is an account ID, or as a string parameter that contains a comma-delimited list of remote account IDs. The parameter has the format {param:\_name\_} where the name is the name of the parameter in Parameter Store.

To leverage this feature, you must launch the Instance Scheduler on AWS hub stack in the same account as your parameter store.
