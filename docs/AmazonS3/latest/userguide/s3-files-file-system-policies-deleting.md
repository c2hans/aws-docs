---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-file-system-policies-deleting.html
---

# Deleting file system policies
<a name="s3-files-file-system-policies-deleting"></a>

You can delete a file system policy using the Amazon S3 console and the AWS CLI.

## Using the S3 console
<a name="s3-files-file-system-policies-deleting-console"></a>

This section explains how to use the Amazon S3 console to delete a file system policy for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, verify you are in the AWS Region where your file system exists.

1. In the left navigation pane, choose **File systems**.

1. Choose your file system.

1. Select the **Permissions** tab and select **Delete**.

1. In the confirmation window, type **confirm** and choose **Delete**.

## Using the AWS CLI
<a name="s3-files-file-system-policies-deleting-cli"></a>

The following `delete-file-system-policy` example command shows how you can use the AWS CLI to delete a file system policy for S3 Files.

```
aws s3files delete-file-system-policy --file-system-id {{file-system-id}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
