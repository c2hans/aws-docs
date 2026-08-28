---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-default.html
---

# Using default slot values in intents for your Lex V2 bot
<a name="context-mgmt-default"></a>

When you use a default value, you specify a source for a slot value to be filled for new intents when no slot is provided by the user’s input. This source can be previous dialog, request or session attributes, or a fixed value that you set at build-time.

You can use the following as the source for your default values.
+ Previous dialog (contexts) – \#context-name.parameter-name
+ Session attributes – [attribute-name]
+ Request attributes – <attribute-name>
+ Fixed value – Any value that doesn't match the previous

When you use the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) operation to add slots to an intent, you can add a list of default values. Default values are used in the order that they are listed. For example, suppose you have an intent with a slot with the following definition:

```
"slots": [
    {
        "botId": "{{string}}",
        "defaultValueSpec": {
            "defaultValueList": [
                {
                    "defaultValue": "#book-car-fulfilled.startDate"
                },
                {
                    "defaultValue": "[reservationStartDate]"
                }
            ]
        },
        {{Other slot configuration settings}}
    }
]
```

When the intent is recognized, the slot named "reservation-start-date" has its value set to one of the following.

1. If the "book-car-fulfilled" context is active, the value of the "startDate" parameter is used as the default value.

1. If the "book-car-fulfilled" context is not active, or if the "startDate" parameter is not set, the value of the "reservationStartDate" session attribute is used as the default value.

1. If neither of the first two default values are used, then the slot doesn't have a default value and Amazon Lex V2 will elicit a value as usual.

If a default value is used for the slot, the slot is not elicited even if it is required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
