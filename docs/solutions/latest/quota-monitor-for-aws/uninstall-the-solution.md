---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Quota Monitor for AWS solution from the AWS Management Console or by using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI).

**Note**
You must manually delete the following:
Delete the DynamoDB summary table from the hub account. The solution doesn’t automatically delete the table, allowing you to maintain historical analysis of the quota usage and alert notifications if desired.
Delete the customer managed key for the hub stack.
Delete one customer managed key per account, per AWS Region, for the spoke stack.
If you deployed the solution with Organizations, delete the StackSet instances from the StackSets before you delete the hub stacks.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the AWS CloudFormation console.

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS CLI is available in your environment. For installation instructions, see What Is the AWS Command Line Interface in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## Deleting StackSet instances
<a name="deleting-stackset-instances"></a>

You can delete the StackSet instances from the AWS Management Console or by using the AWS CLI.

### Using the AWS Management Console
<a name="using-the-aws-management-console-1"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **StackSets** page, select this solution’s installation StackSet.

1. Choose **Actions**, then choose **Delete stacks from StackSet**.

### Using AWS Command Line Interface
<a name="using-aws-command-line-interface-1"></a>

Determine whether the AWS CLI is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack-instances -stack-set-name <installation-stackset-name> --regions <value>
```

## Deleting the DynamoDB table
<a name="deleting-the-dynamodb-table"></a>

This solution is configured to retain the solution-created DynamoDB table. Follow these steps to delete the DynamoDB table.

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1. Choose **Tables** from the left navigation pane.

1. Locate the {{<stack-name>}} prefixed table and choose **Delete**.

To delete the DynamoDB table using AWS CLI, run the following command:

```
$ aws dynamodb delete-table <table-name>
```

## Deleting the customer managed keys (scheduling deletion)
<a name="deleting-the-cmks"></a>

This solution is configured to retain the solution-created customer managed keys along with the DynamoDB table. Follow these steps to delete the customer managed keys.

1. Sign in to the [AWS KMS console](https://console.aws.amazon.com/kms/home).

1. Choose **Customer managed keys** from the left navigation pane.

1. Locate the {{<CMK-stack-name>}} prefixed table and choose **\*ey Actions and schedule key deletion**.

To delete the customer managed keys using AWS CLI, run the following command:

```
$ aws kms schedule-key-deletion --key-id <key-id>
```
