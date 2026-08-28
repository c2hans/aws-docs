---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-same-account.html
---

# Example policy: Send events to an event bus in the same account in Amazon EventBridge
<a name="eb-event-bus-example-policy-same-account"></a>

The following example policy attached to an event bus named `CustomBus1` allows the event bus to receive events from the same account and Region.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "events:PutEvents"
            ],
            "Resource": [
                "arn:aws:events:us-east-1:{{111122223333}}:event-bus/CustomBus1"
            ]
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
