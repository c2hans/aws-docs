---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/manual-delete-retained-resources.html
---

# Manual delete retained resources
<a name="manual-delete-retained-resources"></a>

After deleting the core stack, see the following sections for how to delete remaining resources.

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created Amazon S3 bucket (for deploying in an opt-in Region) if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete this S3 bucket if you do not need to retain the data. Follow these steps to delete the Amazon S3 bucket.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the S3 buckets that begin with  *<stack-name>* .

1. Select the S3 bucket and choose **Delete**.

To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

## Deleting the CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

This solution retains the CloudWatch Logs if you decide to delete the AWS CloudFormation stack to prevent against accidental data loss. After uninstalling the solution, you can manually delete the logs if you do not need to retain the data. Follow these steps to delete the CloudWatch Logs.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Choose **Log Groups** from the left navigation pane.

1. Locate the log groups created by the solution.

1. Select one of the log groups.

1. Choose **Actions** and then choose **Delete**.

Repeat the steps until you have deleted all the solution log groups.

## Deleting the Amazon EC2 AMIs
<a name="deleting-the-amazon-ec2-amis"></a>

This solution is configured to retain the Amazon EC2 AMIs if you enable and then disable the Leostream Broker stack. After uninstalling the solution, you can manually delete the Amazon EC2 AMIs if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon EC2 console](https://console.aws.amazon.com/ec2/home).

1. Choose **AMIs** from the left navigation pane under **Images**.

1. Select the **AMIs** you wish to remove, and choose **Actions → Deregister AMI**.

To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws ec2 deregister-image --image-id <image-id>
```

## Deleting the SSM Parameters
<a name="deleting-the-ssm-parameters"></a>

This solution is configured to retain Systems Manager Parameters if you enable and then disable the Leostream Broker stack. After uninstalling the solution, you can manually delete the Systems Manager Parameters if you do not need to retain the data. Follow these steps:

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. Choose **Parameter Store** from the left navigation pane.

1. Select the **Parameters** you wish to remove, and choose **Delete**.

To delete the Parameters tables using AWS CLI, run the following command:

```
$ aws ssm delete-parameter --name <parameter-name>
```

## Deleting the FSx for Windows File Server Backups
<a name="deleting-the-fsx-for-windows-file-server-backups"></a>

This solution retains the FSx for Windows File Server backups if you decide to disable the AWS FSx for Windows File Server module to prevent against accidental data loss. After uninstalling the solution, you can manually delete the backups if you do not need to retain the data. Follow these steps to delete the FSx Backups.

1. Sign in to the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. Choose **Backups** from the left navigation pane.

1. Select the backup created by the Amazon FSx for Windows File Server file system when it was disabled.

1. Choose **Actions**, and then choose **Delete Backup**.
