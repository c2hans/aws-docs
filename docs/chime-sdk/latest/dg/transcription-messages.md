---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-messages.html
---

# Understanding transcription files for Amazon Chime SDK media capture pipelines
<a name="transcription-messages"></a>

The transcription-messages folder contains transcription files in the .txt format. However, the folder only receives files when you enable live transcription. For more information about enabling live transcription, see [Using Amazon Chime SDK live transcription](meeting-transcription.md).

The folder includes all partial and complete transcription messages, and each message is a JSON object. File names contain the <yyyy-mm-dd-hour-min-seconds-milleseconds> timestamp. You can see transcription file examples at [Processing a received Amazon Chime SDK live transcript event](delivery-examples.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
