---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/case-1.html
---

# Receiving an inbound call using the Amazon Chime SDK PSTN audio service
<a name="case-1"></a>

When a `NEW_INCOMING_CALL` event occurs, the Audio Service creates a unique `TransactionID` and unique `CallID` that persist until the `HANGUP` event occurs.

You can respond in several ways to a `NEW_INCOMING_CALL` event. For example:
+ Send `PlayAudio` or `RecordAudio` actions and automatically answer the call.
+ Send a `Pause` action.
+ Send a `Hangup` action, in which case the call isn’t answered and the customer isn’t charged.
+ Send a `CallAndBridge` action and add another user to the call.
+ Do nothing, the call attempt times out after 30 seconds.

When a new inbound call is received, the SIP media application invokes an AWS Lambda function with this payload.

```
{
    "SchemaVersion": "1.0",
    "Sequence": {{2}},
    "InvocationEventType": "NEW_INBOUND_CALL"
    "CallDetails": {
        "TransactionId": "{{transaction-id}}",
        "AwsAccountId": "{{aws-account-id}}",
        "AwsRegion": "{{us-east-1}}",
        "SipRuleId": "{{sip-rule-id}}",
        "SipApplicationId": "{{sip-application-id}}",
        "Participants": [
            {
                "CallId": "{{call-id-1}}",
                "ParticipantTag": "LEG-A",
                "To": "{{+12065551212}}",
                "From": "{{+15105550101}}",
                "Direction": "Inbound",
                "StartTimeInMilliseconds": "{{159700958834234}}",
                "Status": "Connected"
            }
        ]
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
