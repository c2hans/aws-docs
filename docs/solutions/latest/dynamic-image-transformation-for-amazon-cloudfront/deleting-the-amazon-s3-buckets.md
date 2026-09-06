---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/deleting-the-amazon-s3-buckets.html
---

# Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created S3 buckets if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete this S3 bucket if you don’t need to retain the data. Follow these steps to delete the Amazon S3 buckets.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the *<stack-name>* S3 buckets.

1. Select the S3 bucket and choose **Delete**.

To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

Alternatively, you can configure the CloudFormation template to delete the Amazon S3 bucket automatically. Before deleting the stack, change the deletion behavior in the CloudFormation [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

**Note**
Neither of these methods deletes the source bucket you created and provided as a parameter to the CloudFormation template.
