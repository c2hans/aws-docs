---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/mss-other-fields.html
---

# Fields for other Microsoft Smooth features
<a name="mss-other-fields"></a>

## Fields for resiliency
<a name="smooth-resiliency"></a>

The following field relates to implementing resiliency in a Microsoft Smooth output.
+ **Microsoft Smooth output group** – **Microsoft Smooth Settings** section – **General configuration** section – **Input loss action**

Optionally change the value of **Input loss action**.

Choose the **Info** link in the MediaLive console to decide which option to choose. For more information, see [Handling loss of video input](feature-input-loss.md).

## Fields for timecode
<a name="smooth-timecode"></a>

The following fields relate to configuring the timecode and timestamp in all the outputs in the output group.
+ **Microsoft Smooth output group** – **Timecode Configuration** section

For details about a field, choose the **Info** link next to the field in the MediaLive console.

## Fields for SCTE-35
<a name="smooth-s35"></a>

The following fields relate to configuring the timecode and timestamp in all the outputs in the output group.
+ **Microsoft Smooth output group** – **Timecode Configuration** section

If you want all the outputs in this output group to include the SCTE-35 messages that are already present in the input, choose **Sparse track**. The messages will be included in a sparse track. For more information, see [Processing SCTE 35 messages](scte-35-message-processing.md) and specifically [Enabling decoration – Microsoft Smooth](procedure-to-enable-decoration-ms-smooth.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
