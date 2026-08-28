---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/designing-input-format.html
---

# Input transcript format
<a name="designing-input-format"></a>

The following is the input file format for generating intents and slot types for your bot. The input file must contain these fields. Other fields are ignored.

The input format is compatible with the output format from Contact Lens for Connect Customer. If you are using Contact Lens, you don't need to modify your transcript files. For more information, see [ Example Contact Lens output files ](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-example-output-files.html). If you are using another contact center application, you must transform your transcript file to this format.

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
        "ContactId": "string"
    },
    "Transcript": [
        {
            "ParticipantId": "string",
            "Id": "string",
            "Content": "string"
        }
    ]
}
```

The following fields must be present in the input file:
+ **Participants**   Identifies the participants in the conversation and the role that they play.
+ **Version**   The version of the input file format. Always "1.1.0".
+ **ContentMetadata**   Indicates whether you removed sensitive information from the transcript. Set the `Output` field to "Raw" if the transcript contains sensitive information.
+ **CustomerMetadata**   A unique identifier for the conversation.
+ **Transcript**   The text of the conversation between parties in the conversation. Each turn of the conversation is identified with a unique identifier.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
