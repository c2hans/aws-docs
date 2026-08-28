---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontactmediaprocessing.html
---

# UpdateContactMediaProcessing
<a name="contact-actions-updatecontactmediaprocessing"></a>

Allows customers to configure their own Lambda processor, which will be applied to in-flight messages.

## Parameter object
<a name="updatecontactmediaprocessing-parameter"></a>

```
{
    "ChatProcessor": { // Configuration for bring-your-own-processor for chat channel.
        "ProcessingEnabled": either "True" or "False". Must be set statically. Determines whether to enable custom Lambda processing for chat messages.
        "LambdaProcessorARN": The ARN of the Lambda function to process chat messages. Must be set statically. Format: arn:aws:lambda:region:account-id:function:function-name
        "ChatProcessorSettings": { // An object that holds chat processor behavior settings
            "DeliverUnprocessedMessages": either "True" or "False". Must be set statically. Determines whether to deliver messages that fail Lambda processing.
        }
    }
}
```

## Results and conditions
<a name="updatecontactmediaprocessing-results"></a>

None.

## Errors
<a name="updatecontactmediaprocessing-errors"></a>
+ **NoMatchingError** - if no other Error matches. Must always be defined.
+ **ChannelMismatch** - if the media channel that initiated the contact is not the same as the one defined in the action. As of now, only chat is supported in this action.

## Corresponding block in the UI
<a name="updatecontactmediaprocessing-ui"></a>

[Set recording, analytics and processing behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-analytics-processing-behavior.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
