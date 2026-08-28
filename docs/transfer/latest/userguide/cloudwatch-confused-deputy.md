---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/cloudwatch-confused-deputy.html
---

# Examples to limit confused deputy problem
<a name="cloudwatch-confused-deputy"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. For more details, see [Cross-service confused deputy prevention](confused-deputy.md).

**Note**
In the following examples, replace each {{user input placeholder}} with your own information.
In these examples, you can remove the ARN details for a workflow if your server doesn't have any workflows attached to it.

The following example logging/invocation policy allows any server (and workflow) in the account to assume the role.

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAllServersWithWorkflowAttached",
            "Effect": "Allow",
            "Principal": {
                "Service": "transfer.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                },
                "ArnLike": {
                   "aws:SourceArn": [
                     "arn:aws:transfer:{{us-west-2}}:{{111122223333}}:server/*",
                     "arn:aws:transfer:{{us-west-2}}:{{111122223333}}:workflow/*"
                   ]
                }
            }
        }
    ]
}
```

The following example logging/invocation policy allows a specific server (and workflow) to assume the role.

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSpecificServerWithWorkflowAttached",
            "Effect": "Allow",
            "Principal": {
                "Service": "transfer.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                },
                "ArnEquals": {
                   "aws:SourceArn": [
                       "arn:aws:transfer:{{us-west-2}}:{{111122223333}}:server/{{server-id}}",
                       "arn:aws:transfer:{{us-west-2}}:{{111122223333}}:workflow/{{workflow-id}}"
                   ]
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
