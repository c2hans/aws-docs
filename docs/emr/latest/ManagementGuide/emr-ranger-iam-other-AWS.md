---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-other-AWS.html
---

# IAM role for other AWS services for Amazon EMR integration
<a name="emr-ranger-iam-other-AWS"></a>

This role provides users who are not trusted execution engines with credentials to interact with AWS services, if needed. Do not use this IAM role to allow access to Amazon S3 data, unless it's data that should be accessible by all users.

This role will be assumed by the EC2 Instance Profile Role. Use the following example to create a trust policy that allows the IAM role for Apache Ranger to be assumed by the EC2 instance profile role.

```
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{<AWS_ACCOUNT_ID>}}:role/{{<EC2 INSTANCE PROFILE ROLE NAME eg. EMR_EC2_DefaultRole>}}"
      },
      "Action": "sts:AssumeRole"
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
