---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/trick-play.html
---

# Enabling trick-play in AWS Elemental MediaPackage
<a name="trick-play"></a>

Trick-play, sometimes called trick mode, provides a visual cue to viewers as they rewind, fast-forward, or seek through content in a digital video player. This helps the person using the video player to visualize where they are in the content timeline.

MediaPackage supports the following trick-play types:

**Supported trick-play types for live workflows**

| Streaming protocol | I-frame only | Image-based |
| --- | --- | --- |
| HLS with TS segments | √ | √ |
| HLS with CMAF segments | √ | √ |
| DASH | √ | √ |

The following sections describe how to enable trick play in MediaPackage.

**Topics**
+ [Using I-frame playlists](using-i-frame-playlists.md)
+ [Using image media playlists](using-image-media-playlists.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
