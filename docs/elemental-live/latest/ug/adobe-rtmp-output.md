---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/adobe-rtmp-output.html
---

# Adobe RTMP output
<a name="adobe-rtmp-output"></a>

Adobe RTMP output does not support passthrough of the SCTE-35 messages but does support manifest decoration. Therefore, the workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect |
| --- | --- | --- | --- | --- |
| Not applicable | Yes or No | Enabled | Yes or No | Removes SCTE-35 messages from the video stream. But instructions are included in the manifest. You could insert extra messages: although they are not included in the video stream of the output, they are represented by instructions in the manifest. You could also implement blanking and blackout. |
| Not applicable | No | Disabled | No | Removes SCTE-35 messages from the output. The manifest is not decorated. Do not implement blanking or blackout because, without SCTE-35 messages in the video stream and without manifest decoration, it is impossible to find these blanks and blackouts programmatically. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
