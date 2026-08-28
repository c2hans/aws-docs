---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onvoiceenhancementmodechanged.html
---

# Subscribe to voice enhancement mode change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onvoiceenhancementmodechanged"></a>

Subscribes a callback function whenever voice enhancements mode is changed in user's profile.

 **Signature**

```
onVoiceEnhancementModeChanged(handler: VoiceEnhancementModeChangedHandler)
```

 **Usage**

```
const handler: VoiceEnhancementModeChangedHandler = async (data: VoiceEnhancementModeChanged) => {
  console.log("User VoiceEnhancementMode changed! " + data);
}

voiceClient.onVoiceEnhancementModeChanged(handler);

// VoiceEnhancementModeChanged structure
{
  voiceEnhancementMode: string
  previous: {
     voiceEnhancementMode: string
  }
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
