---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/update-trans-attributes.html
---

# Updating TransactionAttributes
<a name="update-trans-attributes"></a>

To modify stored `TransactionAttributes`, update the contents of the JSON object with new values. In the following example, the keys `NewKey1` and `NewKey2` are added to the `TransactionAttributes`. These keys are paired with the values `NewValue1` and `NewValue2`, respectively.

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
        "{{NewKey1}}": "{{NewValue1}}",
        "{{NewKey2}}": "{{NewValue2}}"
    }
}
```

If, in the previous example, you passed `NewValue1` to `key1`, the existing value of `key1` would be replaced with `NewValue1`. However, passing a value to `NewKey1` creates a new key/value pair.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
