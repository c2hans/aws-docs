---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offvoiceenhancementmodechanged.html
---

# Unsubscribe from voice enhancement mode change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offvoiceenhancementmodechanged"></a>

Unsubscribes a callback function registered for voice enhancements mode changed event.

 **Signature**

```
offVoiceEnhancementModeChanged(handler: VoiceEnhancementModeChangedHandler)
```

 **Usage**

```
const handler: VoiceEnhancementModeChangedHandler = async (data: VoiceEnhancementModeChanged) => {
  console.log("User VoiceEnhancementMode changed! " + data);
}

// subscribe a callback for mode change
voiceClient.onVoiceEnhancementModeChanged(handler);

// unsubsribes a callback for mode change
voiceClient.offVoiceEnhancementModeChanged(handler);
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
