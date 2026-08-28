---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutoiral-Delete.html
---

# Step 6: Delete your S3 Express One Zone directory bucket
<a name="s3-express-tutoiral-Delete"></a>

After you empty your directory bucket and abort all in-progress multipart uploads, you can delete your bucket by using the Amazon S3 console.

**To delete a directory bucket**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, choose the name of the currently displayed AWS Region. Next, choose the Region associated with the Availability Zone in which your directory bucket is located.

1. In the left navigation pane, choose **Directory buckets**.

1. In the **Directory buckets** list, choose the option button next to the bucket that you want to delete.

1. Choose **Delete**.

1. On the **Delete bucket** page, enter the name of the bucket in the text field to confirm the deletion of your bucket.
**Important**
Deleting a directory bucket can't be undone.

1. To delete your directory bucket, choose **Delete bucket**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
