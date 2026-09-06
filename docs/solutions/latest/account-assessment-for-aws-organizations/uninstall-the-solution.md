---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Account Assessment for AWS Organizations solution from the AWS Management Console or by using the AWS Command Line Interface (AWS CLI). You must manually delete the Amazon Cognito user pool, DynamoDB tables, CloudWatch logs, and Amazon S3 bucket created by this solution. AWS Solutions Implementations do not automatically delete these resources in case you have stored data to retain.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command for each of the Hub, Spoke, and Org-Management stacks.

```
$ aws cloudformation delete-stack --stack-name <stack-name>
```

## Deleting the Amazon Cognito user pool
<a name="deleting-the-cognito-user-pool"></a>

To prevent accidental data loss, this solution is configured to retain the solution-created Amazon Cognito user pool if you decide to delete the CloudFormation stack. After uninstalling the solution, you can manually delete the user pool if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/users/) to access the **User Pools** tab.

1. Choose the user pool named `account-assessment-for-aws-organizations-hub*`.
**Note**
During deployment, the stacks may truncate the user pool name (for example, `account-assess*`).

1. On that user pool’s page, choose **Delete pool**.

## Deleting the DynamoDB tables
<a name="deleting-the-dynamodb-tables"></a>

To prevent accidental data loss, this solution is configured to retain the solution-created DynamoDB tables if you decide to delete the CloudFormation stack. After uninstalling the solution, you can manually delete these DynamoDB tables if you do not need to retain the data. Follow these steps:

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1. Choose **Tables** from the left navigation pane.

1. Select the `account-assessment-for-aws-organizations-hub*` table and choose **Delete**.
**Note**
During deployment, the stacks may truncate the user pool name (for example, `account-assess*`).

To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws dynamodb delete-table <table-name>
```

## Deleting the CloudWatch logs
<a name="deleting-the-cloudwatch-logs"></a>

To prevent accidental data loss, this solution is configured to retain the solution-created CloudWatch logs if you decide to delete the CloudFormation stack. After uninstalling the solution, you can manually delete the logs if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Choose **Log Groups** from the left navigation pane.

1. Locate the log groups created by the solution.

1. Select one of the log groups.

1. Choose **Actions** and then choose **Delete**.

Repeat the steps until you have deleted all the solution log groups.

## Deleting the Amazon S3 bucket
<a name="deleting-the-amazon-s3-bucket"></a>

To prevent accidental data loss, this solution is configured to retain the solution-created Amazon S3 bucket (for deploying in an opt-in Region) if you decide to delete the CloudFormation stack . After uninstalling the solution, you can manually delete this Amazon S3 bucket if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the `account-assessment-for-aws-organizations-hub*` Amazon S3 bucket.
**Note**
During deployment, the stacks may truncate the user pool name (for example, `account-assess*`).

1. Select the S3 bucket and choose **Delete**.

To delete the Amazon S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```
