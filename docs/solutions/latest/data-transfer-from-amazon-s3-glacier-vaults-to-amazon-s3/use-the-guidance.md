---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/use-the-guidance.html
---

# Use the Guidance
<a name="use-the-guidance"></a>

 This section provides a user guide for using the AWS Guidance.

## Validate your inventory
<a name="validate-your-inventory"></a>

After you deploy this Guidance and transfer your archives, you can validate your Amazon S3 inventory to confirm whether all of your archives transferred. We recommend confirming that all of your archives transferred before deleting your original archive. See [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) for more information.

## Access the CloudWatch dashboard
<a name="access-the-cloudwatch-dashboard"></a>

1.  Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1.  Choose **Dashboards** from the left navigation pane.

1.  Select the dashboard that starts with `Data-Transfer-from-Amazon-S3-Glacier-to-Amazon-S3-Dashboard-`.

1.  In the dashboard, you can find:
   +  The total number of archives in the inventory file, and their collective size.
   +  The total number of archives that you requested for download, and their collective size.
   +  The total number of archives that are staged by the Amazon Glacier service for download, and their collective size.
   +  The total number of archives that won't be downloaded because they're larger than 5 GB in size.
   +  The total number of downloaded archives.

1.  When the number of downloaded archives matches the total number of requested archives, the transfer is complete.

## Manage your Amazon S3 storage
<a name="manage-your-amazon-s3-storage"></a>

 After you transfer your Amazon Glacier data to the Amazon S3 service, you can change your storage classes to fit your use cases. For information about how to do this, see the following resources:
+  [Managing your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-storage.html) in the *Amazon Simple Storage Service User Guide*
+  [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) in the *Amazon Simple Storage Service User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
