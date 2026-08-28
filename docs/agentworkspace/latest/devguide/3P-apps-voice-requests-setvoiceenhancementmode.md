---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-setvoiceenhancementmode.html
---

# Set the voice enhancement mode in Connect Customer agent workspace
<a name="3P-apps-voice-requests-setvoiceenhancementmode"></a>

Sets the voice enhancement mode of the user that's currently logged in to Connect Customer agent workspace. The voice enhancement mode can have the following values:
+ `VOICE_ISOLATION`: it suppresses background noise and isolates the agent's voice. This mode should only be enabled if the agent uses a wired headsets.
+ `NOISE_SUPPRESSION`: it suppresses the background noise. We recommend using this mode with any type of headset.
+ `NONE`: no voice enhancement applies.

 **Signature**

```
async setVoiceEnhancementMode(voiceEnhancementMode: VoiceEnhancementMode): Promise<void>
```

 **Usage**

```
await voiceClient.setVoiceEnhancementMode(VoiceEnhancementMode.NOISE_SUPPRESSION);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| voiceEnhancementMode Required | VoiceEnhancementMode | The mode to set on the user. Values accepted: VOICE\_ISOLATION, NOISE\_SUPPRESSION, NONE |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
