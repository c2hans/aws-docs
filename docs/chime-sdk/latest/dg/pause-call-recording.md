---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pause-call-recording.html
---

# PauseCallRecording
<a name="pause-call-recording"></a>

The `PauseCallRecording` action pauses recording of a call leg. Each time you pause a recording, the recording captures a tone that indicates the pause. When you pause, the recording continues, but it only captures silence. Pausing the recording does not affect the total duration of the recording. You can pause and resume recording as often as needed.

The following example pauses recording.

```
{
    "SchemaVersion": "1.0",
    "Actions":[
        {
            "Type": "PauseCallRecording",
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
