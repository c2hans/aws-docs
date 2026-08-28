---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-input-setup.html
---

# Set up inputs to correct metadata
<a name="color-space-input-setup"></a>

In the previous step, you identified how to correct color space metadata in each MediaLive input. This section describes how to set up each input for the required correction.

**Note**
This section assumes that you are familiar with creating or editing a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md).

**To set up each input attached to the channel**

1. On the **Create Channel** page, in the **Input attachments** section, for **Video selector**, choose **Video selector**.

1. Set the appropriate values for **Color space** and **Color space usage**. See the table after this procedure.

1. This step applies only if you chose **HDR10** and the attached input is for a MediaLive device such as AWS Elemental Link, and you plan to convert the content to another color space. You must specify the values for the Max CLL and Max FALL for the content. You should have obtained this information from the content provider.

   In the **Max CLL** field and the **Max FALL** field, enter the values.

In the following table, each row shows a valid combination of the two fields and the result of that combination.

|  **Color space** field  |  **Color space usage** field  | Result |
| --- | --- | --- |
| **FOLLOW**  | This field is ignored. | Passthrough. MediaLive doesn't change the color space metadata.  |
| **REC\_601** or <br />**REC\_709** or<br />**HDR10** or<br />**HLG** or<br />**Dolby Vision 8.1** | **Force**  | Cleanup. MediaLive marks all the content as using the specified color space.  |
| **REC\_601** or<br />**REC\_709** or<br />**HDR10** or<br />**HLG** or <br />**Dolby Vision 8.1** | **Fallback**  | Cleanup. MediaLive marks the content as using the specified color space only for portions of the content that are unmarked or marked as unknown or marked with an unsupported color space.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
