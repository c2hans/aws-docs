---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/example-confused-deputy.html
---

# Example: WorkSpaces Applications service role cross-service confused deputy prevention
<a name="example-confused-deputy"></a>

WorkSpaces Applications assumes a service role using a variety of resource ARNs, which leads to a complicated conditional statement. We recommend using a wildcard resource type to prevent any unexpected WorkSpaces Applications resources failures.

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
                "aws:SourceArn": "arn:aws:appstream:{{us-east-1}}:{{111122223333}}:*"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
