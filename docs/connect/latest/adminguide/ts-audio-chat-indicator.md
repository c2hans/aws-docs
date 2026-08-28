---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/ts-audio-chat-indicator.html
---

# Agents not hearing the indicator for incoming chat
<a name="ts-audio-chat-indicator"></a>

If an agent can't hear the audio indicator for an incoming chat, the problem is likely because Google added an audio policy flag to Chrome. This flag exists in Chrome versions 71 - 75.

To fix this, add the CCP website to the allowlist in the agent's Chrome settings. For instructions, see this [Google Chrome Help article](https://support.google.com/chrome/answer/114662).

For more information about solving audio problems, see [Troubleshooting Issues with the Contact Control Panel (CCP)](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
