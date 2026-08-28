---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/example-fleet-machine.html
---

# Example: WorkSpaces Applications fleet machine role cross-service confused deputy prevention
<a name="example-fleet-machine"></a>

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
            "Action": "sts:AssumeRole",
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
If you want to use one IAM role for multiple fleets, we recommend using the `aws:SourceArn` global context condition key with wildcards (\*) to match multiple WorkSpaces Applications fleet resources.
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
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                "aws:SourceArn": "arn:aws:appstream:{{us-east-1}}:{{111122223333}}:fleet/{{your-fleet-name}}"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
