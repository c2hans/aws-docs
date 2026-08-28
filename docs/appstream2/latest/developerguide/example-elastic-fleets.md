---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/example-elastic-fleets.html
---

# Example: WorkSpaces Applications Elastic fleets session script Amazon S3 bucket policy cross-service confused deputy prevention
<a name="example-elastic-fleets"></a>

**Example `aws:SourceAccount` Conditional:**
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "appstream.amazonaws.com"
                ]
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{your-bucket-name}}/{{your-session-script-path}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your AWS account ID}}"
                }
            }
        }
    ]
}
```

**Example `aws:SourceArn` Conditional:**
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "appstream.amazonaws.com"
                ]
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{bucket}}/{{AppStream2}}/*",
            "Condition": {
                "ArnLike": {
                "aws:SourceArn": "arn:aws:appstream:us-east-1:111122223333:fleet/{{yourFleetName}}"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
