---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account-custom-bus-source.html
---

# Example policy: Send events to a custom bus in a different account in Amazon EventBridge
<a name="eb-event-bus-example-policy-cross-account-custom-bus-source"></a>

The following example policy grants the account 111122223333 permission to publish events to the `central-event-bus` in account 123456789012, but only for events with a source value set to `com.exampleCorp.webStore` and a `detail-type` set to `newOrderCreated`.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "WebStoreCrossAccountPublish",
      "Effect": "Allow",
      "Action": [
        "events:PutEvents"
      ],
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/central-event-bus",
      "Condition": {
        "ForAllValues:StringEquals": {
          "events:source": "com.exampleCorp.webStore",
          "events:detail-type": "newOrderCreated"
        }
      }
    }
  ]
}
```

------
