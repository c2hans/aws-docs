---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontactmediastreamingbehavior.html
---

# UpdateContactMediaStreamingBehavior
<a name="contact-actions-updatecontactmediastreamingbehavior"></a>

Enables or disables contact media streaming for a set of participants.

## Parameter object
<a name="updatecontactmediastreamingbehavior-parameter"></a>

```
{
    "MediaStreamingState": One of "Enabled" or "Disabled". Must be specified statically.
    "Participants": [  A list of participants to include in the stream if enabling the stream, or disable if disabling the stream
        {
            "ParticipantType": The type of participant to stream. Currently, only "Customer" is supported. Must be defined statically.
            "MediaDirections": [ ] A list of the directions of media to include in the stream - "From" and "To".  Must be defined statically.
        }
    ],
    "MediaStreamType": The type of media to enable or disable from the stream. Currently, only "Audio" is supported. Must be defined statically.
}
```

## Results and conditions
<a name="updatecontactmediastreamingbehavior-results"></a>

None.

## Errors
<a name="updatecontactmediastreamingbehavior-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatecontactmediastreamingbehavior-restrictions"></a>

This is supported in contact flows, customer queue flows, transfer flows, and whisper flows. It is not supported in hold flows.

This is supported only by the voice channel.

## Corresponding block in the UI
<a name="updatecontactmediastreamingbehavior-ui"></a>

[Start media streaming](https://docs.aws.amazon.com/connect/latest/adminguide/start-media-streaming.html) and [Stop media streaming](https://docs.aws.amazon.com/connect/latest/adminguide/stop-media-streaming.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
