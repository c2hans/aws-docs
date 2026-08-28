---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-attachments.html
---

# Configuring attachments in Amazon Chime SDK messaging
<a name="configure-attachments"></a>

The Amazon Chime SDK allows you to use your own storage for message attachments, and include them as message metadata. Amazon Simple Storage Service (S3) is the easiest way to get started with attachments.

**To use S3 for attachments**

1. Create an S3 bucket to store attachments.

1. Create an IAM policy for the bucket that allows Amazon Chime SDK users to upload, download, and delete attachments from your S3 bucket.

1. Create an IAM role for use by your Identity provider to vend credentials to users for attachments.

The [sample application](https://github.com/aws-samples/amazon-chime-sdk/tree/main/apps/chat) provides an example of how to do this with Amazon S3, Amazon Cognito, and the Amazon Chime SDK.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
