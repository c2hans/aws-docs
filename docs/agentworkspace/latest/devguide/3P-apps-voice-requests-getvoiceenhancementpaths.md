---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getvoiceenhancementpaths.html
---

# Get voice enhancement model paths in Connect Customer agent workspace
<a name="3P-apps-voice-requests-getvoiceenhancementpaths"></a>

Returns the voice enhancements models static assets URL paths.

 **Signature**

```
async getVoiceEnhancementPaths(): Promise<VoiceEnhancementPaths>
```

 **Usage**

```
voiceClient.getVoiceEnhancementPaths();

// VoiceEnhancementPaths structure
interface VoiceEnhancementPaths {
  processors: string;
  workers: string;
  wasm: string;
  models: string;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
