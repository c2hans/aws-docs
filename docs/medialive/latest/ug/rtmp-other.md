---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/rtmp-other.html
---

# Other fields
<a name="rtmp-other"></a>

The following field relates to implementing resiliency in an RTMP output:
+ **RTMP settings** – **Input loss action** – For details about a field on the MediaLive console, choose the **Info** link next to the field. For more information, see [Handling loss of video input](feature-input-loss.md).

The following field relates to implementing captions in an RTMP output:
+ **RTMP settings** – **Caption data** – Complete this field only if at least one of your outputs includes captions with **embedded** as the source captions format and **RTMP CaptionInfo** as the output format. If there are no captions in any output, the value in this field is ignored.

  For detailed information about setting up for captions, see [Including captions in a channel](captions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
