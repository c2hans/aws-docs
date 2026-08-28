---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/archive-output-with-other-containers.html
---

# Archive output with other containers
<a name="archive-output-with-other-containers"></a>

Other archive outputs do not support passthrough of the SCTE-35 messages or manifest decoration. Therefore, the only workable option is the default behavior:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect |
| --- | --- | --- | --- | --- |
| Not applicable | No | Not applicable | No | Removes SCTE-35 messages from the output. The manifest is not decorated. Do not implement blanking or blackout because, without SCTE-35 messages in the video stream and without manifest decoration, it is impossible to find these blanks and blackouts programmatically. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
