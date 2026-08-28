---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-in-vbi-data.html
---

# Passing through VBI data
<a name="captions-in-vbi-data"></a>

Elemental Live supports passthrough of VBI data. You can pass through this data if the following statements are true:
+ The input includes VBI data.
+ You want to include all that data in the output. This data might include embedded captions.

**To pass through VBI data**

1. Create an output for the asset that is to include VBI data.

1. In the **Outputs** section, choose the **Settings** link for the output that contains the video asset.

1. Go to the **Stream** section. Display the **Video** fields. Click **Advanced**. More fields appear.

1. Check the **VBI Passthrough** field.

**Important**
Do not create a **Captions** object in this output.

All the VBI data (including embedded captions) from the input will be included in the output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
