---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/designing-output-format.html
---

# Output transcript format
<a name="designing-output-format"></a>

The output transcript format is nearly the same as the input transcript format. However it also includes some customer metadata and a field listing segments that influenced the suggestion of intents and slot types. You can download the output transcript from the **Review** page in the console or using the Amazon Lex V2 API. For more information, see [Input transcript format](designing-input-format.md).

```
{
    "Participants": [
        {
            "ParticipantId": "string",
            "ParticipantRole": "AGENT | CUSTOMER"
        }
    ],
    "Version": "1.1.0",
    "ContentMetadata": {

        "RedactionTypes": [
            "PII"
        ],
        "Output": "Raw | Redacted"
    },
    "CustomerMetadata": {
        "ContactId": "string",
        "FileName": "string",
        "InputFormat": "Lex"
    },
    "InfluencingSegments": [
        {
            "Id": "string",
            "StartTurnIndex": number,
            "EndTurnIndex": number,
            "Intents": [
                {
                    "Id": "string",
                    "Name": "string",
                    "SampleUtteranceIndex": [
                        {
                            "Index": number,
                            "Content": "String"
                        }
                    ]
                }
            ],
            "SlotTypes": [
                {
                    "Id": "string",
                    "Name": "string",
                    "SlotValueIndex": [
                        {
                            "Index": number,
                            "Content": "String"
                        }
                    ]
                }
            ]
        }
    ],
    "Transcript": [
        {

            "ParticipantId": "string",
            "Id": "string",
            "Content": "string"
        }
    ]
}
```
+ **CustomerMetadata** – There are two fields added to the `CustomerMetadata` field, the name of the input file that contains the conversation and the input format, which is always "Lex".
+ **InfluencingSegments** – Identifies the segments of the conversation that influenced the suggestion of an intent or slot type. The ID of the intent or slot type identifies the specific one influenced by the conversation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
