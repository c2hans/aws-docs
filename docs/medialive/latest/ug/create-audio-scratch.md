---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/create-audio-scratch.html
---

# Creating an audio encode from scratch
<a name="create-audio-scratch"></a>

1. On the **Create channel** page, find the output group that you [created](creating-a-channel-step4.md).

1. Under that output group, find the output where you want to set up an audio encode.

1. If you need to add a new audio to this output, choose **Add audio**, then choose **Create a new audio description**,

1. Choose the audio encode, and in **Codec settings**, choose the codec to use for this encode. More fields appear.

1. In **Audio selector name**, choose the selector that is the source for this audio encode, according to [your plan](channel-map-output-source.md). You [created this selector](input-audio-selectors.md) earlier.

1. Complete other fields as appropriate. For details about a field, choose the **Info** link next to the field.
   + The fields in the **Codec settings** section are different for each type of codec.
   + The fields in the **Remix settings** section are optional.
   + The fields in the **Audio normalization** settings are optional.
   + The fields in the **Additional settings** section are optional.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
