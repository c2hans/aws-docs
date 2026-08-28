---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pause.html
---

# Pause
<a name="pause"></a>

Pause a call for a specified time.

```
{
    "Type": "Pause",
    "Parameters": {
        "CallId": "{{call-id-1}}",
        "ParticipantTag": "LEG-A",
        "DurationInMilliseconds": "{{3000}}"
    }
}
```

**CallId**
*Description* – `CallId` of participant in the `CallDetails` of the AWS Lambda function invocation
*Allowed values* – A valid call ID
*Required* – No
*Default value* – None

**ParticipantTag**
*Description* – `ParticipantTag` of one of the connected participants in the `CallDetails`
*Allowed values* – `LEG-A` or `LEG-B`
*Required* – No
*Default value* – `ParticipantTag` of the invoked `callLeg` Ignored if you specify `CallId`

**DurationInMilliseconds**
*Description* – Duration of the pause, in milliseconds
*Allowed values* – An integer >0
*Required* – Yes
*Default value* – None

See working examples on GitHub:
+ [https://github.com/aws-samples/amazon-chime-sma-outbound-call-notifications](https://github.com/aws-samples/amazon-chime-sma-outbound-call-notifications)
+ [https://github.com/aws-samples/amazon-chime-sma-on-demand-recording](https://github.com/aws-samples/amazon-chime-sma-on-demand-recording)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
