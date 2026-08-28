---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/outputs-supported-containers-downstream-systems.html
---

# Containers, protocols, and downstream systems
<a name="outputs-supported-containers-downstream-systems"></a>

The following table lists the output formats and protocols that MediaLive supports. In the table, find a type of output in the first column, then read across the row for information about how the type is supported.

| MediaLive output type (output group) | Use case | Downstream system and supported protocol | Live output supported | VOD output supported |
| --- | --- | --- | --- | --- |
| Archive | Send transport stream (TS) files to an Amazon S3 bucket. See [Amazon S3 Bucket Names](#s3-bucket-rule-anchor), after this table. | Amazon S3, over a custom protocol | No | Yes. A channel can contain only one Archive output group. |
| CMAF Ingest | Send a CMAF stream to a packager that supports HTTPS PUT. | An HTTPS packager | Yes | No |
| Frame Capture | Send a series of JPEG files to an Amazon S3 bucket. See [Amazon S3 Bucket Names](#s3-bucket-rule-anchor), after this table. | Amazon S3, over a custom protocol | No | Yes. A channel can contain a maximum of three Frame capture output groups. |
| HLS with a standard container or an fMP4 container | Send an HLS stream to a server that supports HTTP PUT or WebDav. | HTTP server | Yes | Yes, when the output group is set up for VOD mode |
| HLS with a standard container or an fMP4 container | Send an HLS stream to a server that supports HTTPS PUT or WebDav. | HTTPS server | Yes | Yes, when the output group is set up for VOD mode |
| HLS with a standard container or an fMP4 container | Send an HLS stream to an Akamai CDN. | Akamai CDN, over HTTP or HTTPS | Yes | No |
| HLS with a standard container only | Send an HLS stream to a MediaPackage channel using the HTTPS protocol. | AWS Elemental MediaPackage, over HTTPS with WebDAV | Yes | No |
| HLS with a standard container only | Send an HLS stream to a MediaPackage v2 channel using the HTTPS protocol. | AWS Elemental MediaPackage over HTTPS with Basic PUT | Yes | No |
| HLS with a standard container or an fMP4 container | Send an HLS stream to a container on MediaStore. | AWS Elemental MediaStore, with a custom protocol | Yes | Yes, when the output group is set up for VOD mode |
| HLS with a standard container or an fMP4 container | Send an HLS stream to an Amazon S3 bucket. See [Amazon S3 Bucket Names](#s3-bucket-rule-anchor), after this table. | Amazon S3, over a custom protocol | Yes | Yes, when the output group is set up for VOD mode |
| MediaConnect Router | Send output to AWS Elemental MediaConnect Router for further use and distribution. | MediaConnect Router | Yes | Yes |
| MediaPackage | Send output to a MediaPackage channel. Supports both MediaPackage v2 (CMAF Ingest) and v1 (HLS ingest). See [Delivering to MediaPackage](delivering-to-mediapackage.md). | AWS Elemental MediaPackage over HTTPS (Basic PUT for v2, WebDAV for v1) | Yes | No |
| Microsoft Smooth | Send a stream to an origin server or CDN that supports Microsoft Smooth Streaming. | A supported CDN, over HTTP or HTTPS | Yes | No |
| Multiplex | Create a transport stream (TS) that is part of a MediaLive multiplex. |  | Yes | No |
| RTMP | Send a stream to a server that supports the RTMP protocol. | RTMP server | Yes | No |
| RTMPS | Send a stream to a server that supports the RTMPS protocol. | RTMPS server | Yes | No |
| SRT | Send a stream to a downstream system that supports the SRT protocol. MediaLive can act as the SRT caller (initiating connections) or SRT listener (accepting connections). The output is always encrypted. AWS Elemental MediaConnect is an example of a downstream system that can handle encrypted SRT. | SRT | Yes | No |
| UDP | Send a transport stream (TS) to a server that supports UDP. | UDP server | Yes | No | <a name="s3-bucket-rule-anchor"></a>

**Amazon S3 bucket names**

With MediaLive, the bucket name can't use *dot* notation. For example, `mycompany-videos` is valid, but `mycompany.videos` isn't.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
