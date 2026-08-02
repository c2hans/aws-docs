---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/deleting-the-amazon-s3-buckets.html
---

# Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created Amazon S3 buckets if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete this S3 bucket if you do not need to retain the data. Follow these steps to delete the Amazon S3 buckets.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the *<stack-name>* S3 buckets.

1. Select the S3 buckets and choose **Delete**.

To delete the S3 buckets using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

Alternatively, you can configure the AWS CloudFormation template to delete the Amazon S3 buckets automatically. Before deleting the stack, change the deletion behavior in the AWS CloudFormation [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).
