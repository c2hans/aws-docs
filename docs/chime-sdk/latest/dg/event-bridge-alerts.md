---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/event-bridge-alerts.html
---

# Using rules to send events to Amazon EventBridge for Amazon Chime SDK messaging
<a name="event-bridge-alerts"></a>

The Amazon Chime SDK delivers EventBridge events when an error prevents it from invoking the Amazon Lex V2 Bot. You can create EventBridge rules that recognize those events and automatically take action when the rule is matched. For more information, see [ Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

The following example shows a typical failure event.

```
{
  version: '0',
  id: '{{12345678-1234-1234-1234-111122223333}}',
  'detail-type': '{{Chime Messaging AppInstanceBot Lex Failure}}',
  source: 'aws.chime',
  account: '{{aws-account-id}}',
  time: '{{yyyy-mm-ddThh:mm:ssZ}}',
  region: "{{region}}",
  resources: [],
  detail: {
    resourceArn: 'arn:aws:chime:{{region}}:{{aws-account-id}}:app-instance/{{app-instance-id}}/bot/{{app-instance-bot-id}}',
    failureReason: "1 validation error detected: Value at 'text' failed to satisfy constraint: Member must have length less than or equal to 1024 (Service: LexRuntimeV2, Status Code: 400, Request ID: {{request-id}})"
  }
}
```
