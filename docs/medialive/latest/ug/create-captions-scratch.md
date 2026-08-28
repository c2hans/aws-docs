---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/create-captions-scratch.html
---

# Creating a captions encode from scratch
<a name="create-captions-scratch"></a>

1. On the **Create channel** page, find the output group that you [created](creating-a-channel-step4.md).

1. Under that output group, find the output where you want to set up a captions encode.

1. If you need to add a new captions to this output, choose **Add captions**, then choose **Create a new captions description**,

1. Choose the captions encode, and in **Codec settings**, choose the format to use for this encode. More fields appear.

1. In **Captions selector name**, choose the selector that is the source for this captions encode, according to [your plan](channel-map-output-source.md). You [created this selector](input-audio-selectors.md) earlier.

1. Complete other fields as appropriate, to configure the captions encode. For detailed information about setting up captions encodes, see [Create captions encodes](create-captions-encodes.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
