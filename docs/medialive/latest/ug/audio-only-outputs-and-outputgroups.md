---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/audio-only-outputs-and-outputgroups.html
---

# Setting up the output
<a name="audio-only-outputs-and-outputgroups"></a>

To set up an audio-only output in a MediaLive channel, you must verify that the output groups you want to create can include audio-only encodes, then you must set up the outputs in a specific way.

## Setting up output groups
<a name="audio-only-opg"></a>

You can create an audio-only output in the following types of output groups.
+ HLS that contains a transport stream
+ Microsoft Smooth
+ RTMP
+ UDP

## Setting up outputs
<a name="audio-only-outputs"></a>

The following list describes the number and type of required outputs, based on the output group.

**HLS output group**
Create outputs in the output group as follows:
+ If the output group contains *only one audio encode*, then create one output. Set the container type to **Audio-only**.
+ If the output group contains *more than one audio encode*, then set up an audio rendition group that doesn't include video. See [Audio rendition groups for HLS](audio-renditions.md).

**Microsoft Smooth output group**
Create one output for each audio encode.

**RTMP output groups**
Create one output for the single audio encode. (RTMP always supports only one audio in each output group.)

**UDP output groups**
Create one output for all the audio encodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
