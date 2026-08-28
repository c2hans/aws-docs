---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-output-config-vq.html
---

# Decide about enhanced VQ mode
<a name="color-space-output-config-vq"></a>

You must decide if you should enable enhanced VQ mode in each MediaLive output. This mode applies only to outputs that use H.264.

In the following table, find the planned handling in the first column, then read across to identify the action to take. To enable enhanced VQ mode, see [Setting up enhanced VQ mode](video-enhancedvq.md).

| Planned conversion | Details | Action |
| --- | --- | --- |
| Convert to SDR | The inputs contain both SDR and HDR content. <br /> | You must enable the mode. |
| Convert to SDR | The inputs contain only SDR content. For example, all the inputs are Rec. 709, and you want to convert the content to Rec. 601. | You don't need to enable the mode. |
| Any handling | There is no HDR10 or HLG in any of the inputs. | You don't need to enable the mode. |
| Any handling | You have already enabled enhanced VQ to improve the video quality. | Leave the mode enabled. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
