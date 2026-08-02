---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/set-up-the-cost-feature.html
---

# Set up the cost feature
<a name="set-up-the-cost-feature"></a>

The cost feature requires manual set up of AWS Cost and Usage reports (CUR). Following the instructions below you will:

1. Set up a scheduled CUR.

1. Set up Amazon S3 replication (when CURs are outside the deployment account)

## Create the AWS Cost and Usage Report in the deployment account
<a name="create-the-aws-cost-and-usage-report-in-the-deployment-account"></a>

1. Sign in to the [Billing and Cost Management console](https://console.aws.amazon.com/costmanagement) of the account from which you would like to gather cost data.

1. In the navigation menu, under **Legacy Pages**, select **Cost and Usage Reports**.

1. Choose **Create Report.**

1. Use `workload-discovery-cost-and-usage-` {{<your-workload-discovery-deployment-account-ID>}} as the **Report name.**
**Note**
You must follow this naming convention because a small amount of infrastructure will be deployed to facilitate the querying of the CURs.

1. Select the **Include resource IDs** box.
**Note**
You must select the **Include resource IDs** box to view cost data. This ID must match with the resources discovered by Workload Discovery on AWS.

1. Choose **Next**.

1. On the Delivery options page, choose **Configure** *0*

1. Select the {{<stack-name>}} `-s3buc-costandusagereportbucket-` {{<ID-string>}} Amazon S3 bucket to store the CUR. Choose **Next**.

1. Review the policy, select the confirmation box, and choose **Save**.

1. Set the **Report prefix path** to `aws-perspective`.

1. Select **Daily** for the time granularity.

1. Under **Enable report data integration for,** select **Amazon Athena**.

1. Choose **Next**.

1. Choose **Review and Complete**.

To verify that the report is correctly set up, check the Amazon S3 bucket for the test file.

**Note**
It can take up to 24 hours for the reports to be uploaded to your bucket.

## Create the AWS Cost and Usage Report in an external account
<a name="create-the-aws-cost-and-usage-report-in-an-external-account"></a>

1. Sign in to the [Billing and Cost Management console](https://console.aws.amazon.com/costmanagement) of the account from which you would like to gather cost data.

1. In the navigation menu, under **Legacy Pages**, select **Cost and Usage Reports**.

1. Choose **Create Report.**

1. Use `workload-discovery-cost-and-usage-` {{<your-external-account-ID>}} as the **Report name.**
**Note**
You must follow this naming convention because a small amount of infrastructure will be deployed to facilitate the querying of the CURs.

1. Check the **Include resource IDs** box.
**Note**
You must select the **Include resource IDs** box to view cost data. This ID is needed to match with the resources discovered by Workload Discovery on AWS.

1. Choose **Next**.

1. On the **Delivery options** page, choose **Configure** *0*

1. Create a new Amazon S3 bucket to store the CURs.

1. Review the policy, select the confirmation box, and choose **Save**.

1. Set the **Report prefix path** to `aws-perspective`.

1. Select **Daily** for the time granularity.

1. Under **Enable report data integration for**, select **Amazon Athena**.

1. Choose **Next**.

1. Choose **Review and Complete**. To verify that the report is correctly set up, check the Amazon S3 bucket for the test file.

**Note**
It can take up to 24 hours for the reports to be uploaded to your bucket.

Next, set up replication to the deployment account.

## Set up replication
<a name="set-up-replication"></a>

Set up replication into the Amazon S3 bucket created during deployment. The Amazon S3 bucket follows the following format: {{<stack-name>}} `-s3buc-costandusagereportbucket-` {{<ID-string>}}. This allows the solution to query the bucket with Amazon Athena.

1. Sign in to the AWS account in [Amazon S3 console](https://console.aws.amazon.com/s3/) that contains the created CUR that needs to be replicated.

1. Select the Amazon S3 bucket created when configuring your CUR. For more information, look at Step 8 of *Create and schedule the AWS Cost and Usage Report*.

1. Choose the **Management** tab.

1. Under **Replication rules**, choose **Create replication rule**.

1. Under **Replication rule configuration**, in the **Replication rule name** box, enter a descriptive rule ID.

1. Under **Source bucket**, select **Apply to all objects in the bucket** to configure the rule scope.

1. Under **Destination**, configure the following:

   1. Select **Specify a bucket in another account**.

   1. Enter the account ID.

   1. Enter a value for the **Bucket name** that was created during deployment of Workload Discovery on AWS. You can find this by following the instructions in [Locating deployment resources](locating-deployment-resources.md), using the logical ID `CostAndUsageReportBucket` and the stack name you specified when first deploying Workload Discovery on AWS.

   1. Select the box for **Change object ownership to destination bucket owner**.

1. Under **IAM role**, choose **Create new role**.
**Note**
A replication role might already exist. You can select it and ensure that it has the required [S3 replication role actions](amazon-s3-replication-role-actions.md).

1. Choose **Save**.

1. Sign in to the AWS Management Console where the CUR is installed, navigate to the **S3** service page and select the `CostAndUsageReportBucket` S3 bucket. For details, refer to [Locating deployment resources](locating-deployment-resources.md).

1. Select the **Management** tab.

1. Under **Replication rules**, from the **Actions** drop-down menu, select **Receive replicated objects**.

1. Under **Source bucket account settings**:

   1. Enter the source bucket account ID.

   1. Choose **Generate policies**.

   1. Under **Policies,** select **view bucket policy**.

   1. Select **Include permission to change object ownership to destination bucket owner**.

   1. Choose **Apply settings**. This gives it access to copy objects to it. Refer to [Cost Bucket replication policy](s3-bucket-policy.md) for an example S3 bucket policy.

**Note**
When replicating CURs from multiple AWS accounts. You need to ensure the bucket policy on the destination bucket (within the Workload Discovery on AWS account) has the ARN of each IAM Role you are using from each account. Refer to [Cost Bucket replication policy](s3-bucket-policy.md) for more details.

When the reports are in the account, cost data appears on the bounding boxes and individual resources.

![Example of a bounding box with estimated cost data.](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/example-bounding-box-estimated-cost.png)
