---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/set-trans-attributes.html
---

# Setting TransactionAttributes
<a name="set-trans-attributes"></a>

The following example shows how to set `TransactionAttributes` alongside a [PlayAudio](play-audio.md) action and pass the attributes from an AWS Lambda function to a SIP media application.

```
{
    "SchemaVersion": "1.0",
    "Actions": [
        {
            "Type": "PlayAudio",
            "Parameters": {
                "ParticipantTag": "{{LEG-A}}",
                "AudioSource": {
                    "Type": "S3",
                    "BucketName": "{{mtg1-sipmedia-app-iad}}",
                    "Key": "{{Welcome3.wav}}"
                }
            }
        }
    ],
    "TransactionAttributes": {
        "{{key1}}": "{{value1}}",
        "{{key2}}": "{{value2}}"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
