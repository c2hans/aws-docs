---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account.html
---

# Example policy: Send events to the default bus in a different account in Amazon EventBridge
<a name="eb-event-bus-example-policy-cross-account"></a>

The following example policy grants the account 111122223333 permission to publish events to the default event bus in the account 123456789012.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [
       {
        "Sid": "sid1",
        "Effect": "Allow",
        "Principal": {"AWS":"arn:aws:iam::111112222333:root"},
        "Action": "events:PutEvents",
        "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/default"
        }
    ]
  }
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
