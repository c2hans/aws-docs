---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/deleting-the-amazon-s3-buckets.html
---

# Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

 To prevent accidental data loss, this solution retains the solution-created Amazon S3 bucket (for deploying in an opt-in Region) if you decide to delete the CloudFormation stack. After uninstalling the solution, you can manually delete this S3 bucket if you do not need to retain the data. Follow these steps to delete the Amazon S3 bucket.

1.  Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1.  Choose **Buckets** from the left navigation pane.

1.  Locate the {{<stack-name>}} S3 buckets.

1.  Select the S3 bucket and choose **Delete**.

 To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://{{<bucket-name>}} --force
```

 Alternatively, you can configure the CloudFormation template to delete the S3 buckets automatically. Before deleting the stack, change the deletion behavior in the AWS CloudFormation [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
