---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-access-to-your-output-amazon-s3-bucket.html
---

# Granting access to your output Amazon S3 bucket
<a name="granting-access-to-your-output-amazon-s3-bucket"></a>

Suppose that you want the outputs of your MediaConvert jobs to reside in an Amazon S3 bucket that you own, but you want users that belong to another AWS account to have access to them. To grant access, you can add an Amazon S3 bucket policy to your output bucket.

For a tutorial about how to grant this access, see [Example 2: Bucket owner granting cross-account bucket permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.html) in the *Amazon Simple Storage Service User Guide*.

The following example bucket policy grants access to your output bucket:

```
{
    "Id": "Policy1572454561447",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1572454547712",
            "Action": [
                "s3:GetObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "111122223333"
                ]
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
