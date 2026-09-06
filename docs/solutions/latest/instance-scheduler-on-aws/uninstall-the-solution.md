---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

**Important**
When uninstalling the solution, make sure to uninstall all custom schedule stacks before uninstalling the solution itself.

You can uninstall the Instance Scheduler on AWS solution from the AWS Management Console or by using the AWS Command Line Interface. To uninstall the solution, delete the hub stack in AWS Cloud Formation along with all installed remote stacks. You can then remove any scheduling tags that had been applied to instances for scheduling purposes.

**Note**
If **Protect DynamoDB Tables** is enabled on the solution’s hub stack, CloudFormation will retain the solution’s DynamoDB tables and KMS key rather than deleting them. If you wish to delete these resources, ensure that this property is set to **Disabled** before deleting the hub stack. Alternatively, you can delete them manually after the hub stack has already been deleted.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
 $ aws cloudformation delete-stack --stack-name
      <installation-stack-name>
```
