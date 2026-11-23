---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/set-trans-attributes.html
---

# Setting TransactionAttributes

The following example shows how to set `TransactionAttributes` alongside a [PlayAudio](play-audio.md) action and pass the attributes from an AWS Lambda function to a SIP media application.

```json
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
