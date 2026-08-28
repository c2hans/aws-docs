---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/udp-other.html
---

# Fields for other UDP features
<a name="udp-other"></a>

The following field relates to implementing resiliency in a UDP output:
+ **UDP settings** – **Input loss action** – For details about a field on the MediaLive console, choose the **Info** link next to the field. For more information, see [Handling loss of video input](feature-input-loss.md).

The following fields relate to implementing captions in a UDP output:
+ **UDP settings** –** Timed metadata ID3 frame type**
+ **UDP settings** –** Timed metadata ID3 period**

  Complete these fields if you want to insert timed ID3 metadata into all the outputs in this output group. For detailed instructions, see [Working with ID3 metadata](id3-metadata.md)and specifically [Inserting ID3 timed metadata when creating the MediaLive channel](insert-timed-metadata.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
