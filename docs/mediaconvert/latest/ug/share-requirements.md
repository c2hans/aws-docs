---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/share-requirements.html
---

# Requirements
<a name="share-requirements"></a>

To share a job with Support, the following requirements apply:

**Active support case**
You must have an active Support case ID number.

**IAM policy**
Your IAM user or role must have the `mediaconvert:CreateResourceShare` permission. This permission is separate from `mediaconvert:GetJob` and you must grant it explicitly.
The following is an example IAM policy that allows the operation `mediaconvert:CreateResourceShare` for a specific MediaConvert job :
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Sid1",
            "Effect": "Allow",
            "Action": [
                "mediaconvert:CreateResourceShare"
            ],
            "Resource": [
                "arn:aws:mediaconvert:us-west-2:111122223333:jobs/1234567891234-a9abcd"
            ]
        }
    ]
}
```

**Job access**
The job that you want to share must exist and be accessible to your AWS account.

**Input access**
You can only share input files that are stored on Amazon S3. The IAM role specified in the job must have permission to access the input files.

**Rate limits**
MediaConvert limits share requests to one request every ten seconds, per account. You can have a maximum of 100 active shares per account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
