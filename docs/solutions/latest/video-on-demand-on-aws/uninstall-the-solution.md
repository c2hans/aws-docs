---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Video on Demand on AWS solution from the AWS Management Console or by using the AWS Command Line Interface. You must manually delete the Amazon S3 buckets, a DynamoDB table, and CloudWatch Logs created by this solution. AWS Solutions do not automatically delete these resources in case you have stored data to retain.

**Note**
AWS CloudFormation StackSets are automatically deleted when you uninstall the solution’s stack.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

Replace {{<installation-stack-name>}} with the name of your CloudFormation stack.

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created Amazon S3 buckets (for deploying in an opt-in Region) if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete these Amazon S3 buckets if you do not need to retain the data. Follow these steps to delete the Amazon S3 buckets.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the {{<stack-name>}} Amazon S3 buckets.

1. Select one of the Amazon S3 buckets and choose **Delete**.

Repeat the steps until you have deleted all the {{<stack-name>}} Amazon S3 buckets.

To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

Alternatively, you can configure the AWS CloudFormation template to delete the Amazon S3 buckets automatically. Before deleting the stack, change the deletion behavior in the AWS CloudFormation [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

## Deleting the DynamoDB table
<a name="deleting-the-dynamodb-table"></a>

This solution is configured to retain the DynamoDB tables if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete the DynamoDB tables if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1. Choose **Tables** from the left navigation pane.

1. Select the {{<stack-name>}} table and choose **Delete**.

To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws dynamodb delete-table <table-name>
```

## Deleting the CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

This solution retains the CloudWatch Logs if you decide to delete the AWS CloudFormation stack to prevent against accidental data loss. After uninstalling the solution, you can manually delete the logs if you do not need to retain the data. Follow these steps to delete the CloudWatch Logs.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Choose **Log Groups** from the left navigation pane.

1. Locate the log groups created by the solution.

1. Select one of the log groups.

1. Choose **Actions** and then choose **Delete.**

   Repeat the steps until you have deleted all the solution log groups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
