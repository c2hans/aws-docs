---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/creating-archive-output-group.html
---

# Create an Archive output group
<a name="creating-archive-output-group"></a>

You create the output group and its outputs when you [create or edit a MediaLive channel](creating-a-channel-step4.md).

1. On the **Create channel** page, under **Output groups**, choose **Add**.

1. In the **Add output group** section, choose **Archive**, and then choose **Confirm**. More sections appear:
   + **Archive group destination** – This section contains fields for the [output destination](archive-destinations.md).
   + **Archive settings** – This section contains fields for the [output destination](archive-destinations.md).
   + **Archive outputs** – This section shows the output that is added by default. An Archive output can contain only one output, so don't click **Add output**

1. In **Archive outputs**, choose the **Settings** link to view the sections for the individual output:
   + **Output settings** – This section contains fields for the [output destination](archive-destinations.md) and the [output container](archive-container.md).
   + **Stream settings** – This section contains fields for the [output streams](archive-streams.md) (the video, audio, and captions).

1. (Optional) Enter names for the output group and the output:
   + In **Archive settings**, for **Name**, enter a name for the output group. This name is internal to MediaLive; it doesn't appear in the output. For example, **Sports Game 10122017 ABR** or **tvchannel59**.
   + In **Archive outputs**, for **Name**, enter a name for the output. This name is internal to MediaLive; it doesn't appear in the output.

1. To complete the other fields, see the topics listed after this procedure.

**Topics**
+ [Fields for the output destination](archive-destinations.md)
+ [Fields for the output container](archive-container.md)
+ [Fields for the video, audio, and captions streams (encodes)](archive-streams.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
