---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

To uninstall the solution, use the AWS Management Console or the AWS Command Line Interface (AWS CLI).

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

### AWS CloudFormation
<a name="aws-cloudformation"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

### AWS Launch Wizard
<a name="aws-launch-wizard"></a>

1. Sign in to the [AWS Launch Wizard console](https://console.aws.amazon.com/launchwizard/home).

1. On the **Launch Wizard Deployments** page, select this solution’s deployment.

1. Choose **Actions**, then **Delete**.

1. Confirm the deletion.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## Deleting retained resources
<a name="deleting-retained-resources"></a>

This solution is configured to retain certain resources after stack deletion to prevent accidental data loss.

### Deleting Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

By default, the solution will retain any solution-created Amazon S3 buckets (for deploying in an opt-in region) to prevent accidental data loss if you decide to delete the AWS CloudFormation stack. After uninstalling the solution, you can manually delete these S3 buckets if you do not need to retain the data. Follow these steps to delete the Amazon S3 buckets.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. In the **Find buckets by name** field, enter the name of this solution’s stack.

1. Select one of the solution’s S3 buckets and choose **Empty**.

1. Enter **permanently delete** in the verification field and choose **Empty**.

1. Select the S3 bucket you just emptied and choose **Delete**.

1. Enter the S3 bucket name in the verification field and choose **Delete bucket**.

Repeat steps 4 through 7 until you delete all the S3 buckets.

To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

### Deleting Amazon CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

Amazon CloudWatch Log Groups are also retained following stack deletion, and will remain in your AWS account until they are manually deleted. This configuration is by design to prevent loss of log data and to align with security and operational best practices.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Choose **Log Management** from the left navigation pane.

1. In the **Filter log groups or try pattern search** field, enter the name of this solution’s stack.

1. Select all log groups that belong to the solution.

1. In the **Actions** menu, click **Delete log group(s)**.

1. Review and confirm your selection by clicking **Delete**.

To delete a log group using AWS CLI, run the following command:

```
$ aws logs delete-log-group --log-group-name <log-group-name>
```
