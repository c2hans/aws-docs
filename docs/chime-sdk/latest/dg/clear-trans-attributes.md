---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/clear-trans-attributes.html
---

# Clearing TransactionAttributes
<a name="clear-trans-attributes"></a>

To clear the contents of the `TransactionAttributes` object, pass the `TransactionAttributes` field with an empty JSON Object:

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
    }
}
```

**Note**
You can't clear data from a `TransactionAttributes` structure by setting its value to `null`. Also, omitting the `TransactionAttribute` structure doesn't clear its data. Always pass an empty JSON object with `TransactionAttributes` to clear data from the object.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
