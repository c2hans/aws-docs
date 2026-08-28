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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
