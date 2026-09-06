---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/manually-deleting-retained-resources.html
---

# Manually deleting retained resources
<a name="manually-deleting-retained-resources"></a>

After deleting the stack, see the following sections for how to delete remaining resources.

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created Amazon S3 buckets if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete these S3 buckets if you do not need to retain the data. Follow these steps to delete the Amazon S3 buckets.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. In the navigation pane, choose **Buckets**.

1. Locate the S3 buckets created by the solution.

1. Select an S3 bucket and choose **Empty**.

1. Enter **permanently delete** in the verification field and choose **Empty**.

1. Select the S3 bucket you just emptied and choose **Delete**.

1. Enter the S3 bucket name in the verification field and choose **Delete bucket**.

Repeat the steps until you have deleted all the solution S3 buckets.

To delete the S3 buckets using AWS CLI, run the following command for each bucket:

```
$ aws s3 rb s3://<bucket-name> --force
```

## Deleting the Amazon DynamoDB tables
<a name="deleting-the-amazon-dynamodb-tables"></a>

This solution is configured to retain the solution-created DynamoDB tables if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete these tables if you do not need to retain the data. Follow these steps to delete the DynamoDB tables.

1. Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodbv2/home).

1. In the navigation pane, choose **Tables**.

1. Locate the tables created by the solution.

1. Select a table and choose **Delete**.

1. Confirm the deletion by entering **delete** and choose **Delete table**.

Repeat the steps until you have deleted all the solution tables.

To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws dynamodb delete-table --table-name <table-name>
```

## Deleting the CloudWatch log groups
<a name="deleting-the-cloudwatch-log-groups"></a>

This solution retains the CloudWatch log groups if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete the log groups if you do not need to retain the data. Follow these steps to delete the CloudWatch log groups.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, choose **Log groups**.

1. Locate the log groups created by the solution.

1. Select the log groups you want to delete.

1. Choose **Actions** and then choose **Delete**.

Repeat the steps until you have deleted all the solution log groups.

To delete log groups using AWS CLI, run the following commands:

```
$ aws logs describe-log-groups --log-group-name-prefix <stack-name> --query 'logGroups[].logGroupName' --output text
$ aws logs delete-log-group --log-group-name <log-group-name>
```

**Note**
If you deployed regional stacks, repeat this process in each Region where a regional stack was deployed.

## Deleting the CloudWatch dashboards
<a name="deleting-the-cloudwatch-dashboards"></a>

This solution creates a CloudWatch dashboard for each test scenario in each Region where the test runs. These dashboards follow the naming pattern `EcsLoadTesting-<testId>-<region>` and incur a monthly charge for as long as they exist. They are cleaned up when you delete a test through the DLT console, but will remain if the stack is deleted without first deleting all tests.

After uninstalling the solution, you can manually delete these dashboards if they were not already cleaned up. Follow these steps to delete the CloudWatch dashboards.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, choose **Dashboards**.

1. In the filter field, enter `EcsLoadTesting` to find the solution’s dashboards.

1. Select the dashboards you want to delete.

1. Choose **Delete**.

To delete dashboards using AWS CLI, run the following commands:

```
$ aws cloudwatch list-dashboards --dashboard-name-prefix EcsLoadTesting --query 'DashboardEntries[].DashboardName' --output text
$ aws cloudwatch delete-dashboards --dashboard-names <dashboard-name-1> <dashboard-name-2>
```
