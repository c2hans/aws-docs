---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-startvoiceidstream.html
---

# StartVoiceIdStream
<a name="flow-control-actions-startvoiceidstream"></a>

Sends audio to Connect Customer Voice ID to verify the caller's identity and match against fraudsters in watchlist, as soon as the call is connected to a flow.

## Parameter object
<a name="startvoiceidstream-parameter"></a>

```
{

}
```

## Execution results and conditions
<a name="startvoiceidstream-results"></a>

None. No conditions are supported.

## Errors
<a name="startvoiceidstream-errors"></a>
+ NoMatchingError if no condition matches.

## Restrictions
<a name="startvoiceidstream-restrictions"></a>

Only supported for the voice channel. If used with the chat or task channels, the action takes the **Error** branch. Not supported in hold flows.

## Corresponding block in the UI
<a name="startvoiceidstream-ui"></a>

[Set Voice ID](https://docs.aws.amazon.com/connect/latest/adminguide/set-voice-id.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
