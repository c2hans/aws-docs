---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-event-flow.html
---

# Event flow sequence
<a name="sonic-event-flow"></a>

A typical conversation follows this event sequence:

1. **Session Start** - Initialize the conversation session

1. **System Prompt** - Send system instructions

1. **Chat History** (optional) - Provide conversation context

1. **Audio Chunks** - Stream user audio input

1. **Completion Start** - AI begins processing

1. **ASR Transcripts** (USER) - User speech transcription

1. **Tool Use** (optional) - AI requests tool execution

1. **Tool Handling** (optional) - Process and return tool results

1. **Transcript** (ASSISTANT) - SPECULATIVE - Preliminary AI response

1. **Audio Chunks** - Stream AI audio output

1. **Transcript** (ASSISTANT) - FINAL - Final AI response transcript

1. **Content End Audio** - Marks the end of audio content

1. **Prompt End** - Indicates the completion of the prompt processing

1. **Session End** - Close the conversation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
