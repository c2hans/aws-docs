---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/stop-call-recording.html
---

# StopCallRecording
<a name="stop-call-recording"></a>

The `StopCallRecording` action stops the recording of a call leg. Recording stops automatically when a call ends, and your application doesn't need to explicitly return the `StopCallRecording` action. Once recording for a call leg stops, it can’t start again, and the recording is delivered to the destination specified in the `StartCallRecording` action.

The following example stops recording for the `call-id-1` call leg.

```
{
    "SchemaVersion": "1.0",
    "Actions":[
        {
            "Type": "StopCallRecording",
            "Parameters": {
                "CallId": "{{call-id-1}}"
            }
        }
    ]
}
```

**CallId**
*Description* – `CallId` of participant in the `CallDetails` of the AWS Lambda function invocation
*Allowed values* – A valid call ID
*Required* – Yes
*Default value* – None

See a working example on GitHub: [https://github.com/aws-samples/amazon-chime-sma-on-demand-recording](https://github.com/aws-samples/amazon-chime-sma-on-demand-recording)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
