---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/uninstall-the-guidance.html
---

# Uninstall the guidance
<a name="uninstall-the-guidance"></a>

You can uninstall the Guidance for Account Assessment for AWS Organizations by using the AWS CDK or the AWS Management Console. Some application resources are retained to prevent data loss. If you no longer need their data, manually delete the Amazon Cognito user pool, Amazon DynamoDB tables, Amazon CloudWatch Logs log groups, and Amazon S3 buckets.

Delete the Spoke stacks first, followed by the Org-Management stack and the Hub stack. This order removes the cross-account trust relationships before deleting the Hub roles that they reference.

Before deleting the Hub stack, record the physical IDs of retained resources that you plan to delete manually. You can find these IDs on the stack’s **Resources** tab in the AWS CloudFormation console.

## Using AWS CDK
<a name="using-aws-cdk"></a>

Use the same source checkout, Region, environment variables, and AWS CLI profiles that you used to deploy the guidance.

1. From the `source/infra` directory, destroy the Spoke stack in each account where you deployed it.

   ```
   $ npm run cdk -- destroy account-assessment-for-aws-organizations-spoke \
       --profile "${PROFILE_SPOKE}"
   ```

   Repeat this command with the AWS CLI profile for each Spoke account.

1. Destroy the Org-Management stack.

   ```
   $ npm run cdk -- destroy account-assessment-for-aws-organizations-org-management \
       --profile "${PROFILE_ORG_MGMT}"
   ```

1. Destroy the Hub stack.

   ```
   $ npm run cdk -- destroy account-assessment-for-aws-organizations-hub \
       --profile "${PROFILE_HUB}"
   ```

1. Confirm each deletion when prompted, and wait for each stack to reach `DELETE_COMPLETE`.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Delete the Spoke stack from every account where you deployed it.

1. Delete the Org-Management stack from the Organizations management account.

1. Delete the Hub stack from the Hub account.

1. Wait for each stack to reach `DELETE_COMPLETE`.

## Deleting the Amazon Cognito user pool
<a name="deleting-the-cognito-user-pool"></a>

To prevent accidental data loss, this guidance retains the Amazon Cognito user pool when you delete the Hub stack. After uninstalling the guidance, you can manually delete the user pool if you do not need to retain the data.

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/users/) to access the **User pools** page.

1. Choose the user pool whose physical ID you recorded before deleting the Hub stack.

1. Choose **Delete pool**.

## Deleting the DynamoDB tables
<a name="deleting-the-dynamodb-tables"></a>

To prevent accidental data loss, this guidance retains the DynamoDB tables when you delete the Hub stack. After uninstalling the guidance, you can manually delete the tables if you do not need to retain the data.

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1. Choose **Tables**.

1. Select each table whose physical ID you recorded before deleting the Hub stack, and choose **Delete**.

To delete a DynamoDB table using the AWS CLI, run the following command:

```
$ aws dynamodb delete-table --table-name <TABLE_NAME>
```

## Deleting the CloudWatch Logs log groups
<a name="deleting-the-cloudwatch-logs"></a>

To prevent accidental data loss, this guidance retains the CloudWatch Logs log groups when you delete the Hub stack. After uninstalling the guidance, you can manually delete the log groups if you do not need to retain the data.

1. Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Choose **Log groups**.

1. Select a log group created by the guidance.

1. Choose **Actions**, and then choose **Delete log group**.

1. Repeat these steps for each guidance log group.

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-bucket"></a>

To prevent accidental data loss, this guidance retains the Amazon S3 buckets that host the web UI and store CloudFront logs. The Regional staging bucket that you created before deployment is also outside the AWS CDK stacks. After uninstalling the guidance, manually delete these buckets if you do not need their data.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets**.

1. Locate the application buckets whose physical IDs you recorded before deleting the Hub stack and the staging bucket named `<ASSET_BUCKET_NAME>`.

1. Empty and delete each bucket.

To empty and delete a bucket using the AWS CLI, run the following command:

```
$ aws s3 rb s3://<BUCKET_NAME> --force
```
