---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html
---

# Supported inputs and outputs
<a name="supported-inputs"></a>

This section describes the input types, input codecs, and output codecs that AWS Elemental MediaPackage supports for live content.

**Topics**
+ [Supported input types](#supported-types-live)
+ [Supported input codecs](#suported-inputs-codecs-live)
+ [Supported output codecs](#suported-outputs-codecs-live)

The following sections describe supported input types and codecs for live streaming content.

## Supported input types
<a name="supported-types-live"></a>

Use the following input types to push streams from an external source or encoder (such as AWS Elemental MediaLive) using the HTTPS protocol:
+ HLS
+ CMAF

  For information about CMAF ingest, see [CMAF ingest](cmaf-ingest.md).

The following are additional input requirements:
+ You must define a channel policy to enable content to flow into your channel from sources outside of your account.
+ Media segments must not be encrypted.
+ Streams can contain either muxed video and audio tracks, or unmuxed tracks.
+ The input must contain at least one video track. MediaPackage doesn't support inputs that contain no video track.

## Supported input codecs
<a name="suported-inputs-codecs-live"></a>

These are the video, audio, and subtitles codecs that MediaPackage supports for source content streams.

| Input type | Media container | Video codecs | Audio codecs | Subtitles/captions format |
| --- | --- | --- | --- | --- |
| HLS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html) |
| CMAF | CMAF |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |

## Supported output codecs
<a name="suported-outputs-codecs-live"></a>

These are the video, audio, and subtitles codecs that MediaPackage supports when delivering live content.

**Note**
The AV1 video codec is supported only with CMAF endpoint types. If you configure a TS endpoint on a channel with AV1 streams those streams won't show up on the endpoint.

| Endpoint type | Manifest format | Media container | Video codecs | Audio codecs | Subtitles/captions format |
| --- | --- | --- | --- | --- | --- |
| TS | HLS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |
| CMAF | HLS | CMAF |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |
| CMAF | DASH | CMAF |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html)  |
