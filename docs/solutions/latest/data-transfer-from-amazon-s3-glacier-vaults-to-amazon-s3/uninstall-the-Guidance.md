---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/uninstall-the-Guidance.html
---

# Uninstall the Guidance
<a name="uninstall-the-Guidance"></a>

 You can uninstall the Data Transfer from Amazon Glacier Vaults to Amazon S3 Guidance from the AWS Management Console or by using the AWS Command Line Interface. Manually delete the following resources:
+  S3 buckets (other than the output bucket if you intend to keep the transferred archives)
+  DynamoDB tables
+  CloudWatch Logs

 This Guidance does not automatically delete these resources in case you have stored data to retain.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1.  On the **Stacks** page, select this Guidance's installation stack.

1.  Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

 Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <{{installation-stack-name}}>
```

## Deleting the S3 buckets
<a name="deleting-the-s3-buckets"></a>

 This Guidance is configured to retain the Guidance-created S3 buckets if you decide to delete the CloudFormation stack, to prevent accidental data loss. After uninstalling the Guidance, you can manually delete the S3 buckets if you don't need to retain the data. Follow these steps to delete the S3 buckets.

1.  Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3).

1.  Choose **Buckets** from the left navigation pane.

1.  Locate the `{{<stack-name>}}` S3 buckets.

1.  Select each S3 bucket and choose **Empty.**

1.  Select each S3 bucket and choose **Delete**.

 To delete the S3 bucket using the AWS CLI, run the following command:

```
$ aws s3 rb s3://{{<bucket-name>}} --force
```

## Deleting the DynamoDB tables
<a name="deleting-the-dynamodb-tables"></a>

 This Guidance is configured to retain the Guidance-created DynamoDB tables if you decide to delete the CloudFormation stack, to prevent accidental data loss.

1.  Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb).

1.  Choose **Tables** from the left navigation pane.

1.  Locate the `{{<stack-name>}}` DynamoDB tables.

1.  Select each DynamoDB table and choose **Delete.**

1.  Confirm the deletion.

 To delete the DynamoDB table using the AWS CLI, run the following command:

```
$ aws dynamodb delete-table --table-name {{<table-name>}}
```

## Deleting the CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

1.  Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1.  Choose **Log groups** from the left navigation pane.

1.  Locate the {{<stack-name>}} CloudWatch Logs.

1.  Select each CloudWatch Log and choose **Actions**, then **Delete log groups.**

1.  Confirm the deletion.

 To delete the CloudWatch Logs using the AWS CLI, run the following command:

```
$ aws logs delete-log-group --log-group-name {{<log-group-name>}}
```
