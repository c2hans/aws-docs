---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/restrict-access-s3-buckets.html
---

# Restrict user access to certain S3 buckets
<a name="restrict-access-s3-buckets"></a>

To restrict access for certain users to specific Amazon S3 buckets, you can add a deny policy to a specific role, user, or group.

The following example restricts permissions to retrieve and place objects into a specific S3 bucket (`arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice`) and also restricts the listing of those objects.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "s3:ListBucket"
      ],
      "NotResource": [
        "arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice"
      ]
    },
    {
      "Effect": "Deny",
      "Action": [
        "s3:GetObject"
      ],
      "NotResource": [
        "arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice/*"
      ]
    }
  ]
}
```

------

To restrict access to the bucket for a certain notebook instance, you can add the preceding policy to the notebook execution role.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
