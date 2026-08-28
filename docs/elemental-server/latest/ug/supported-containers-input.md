---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/supported-containers-input.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Reference: Supported Input Containers
<a name="supported-containers-input"></a>

If the source captions are inside the input container, you can include them in the input only if the AWS Elemental encoder can extract the captions from the container. The AWS Elemental encoder can extract captions only from specific input containers types.

If the source captions are an external file (sidecar captions) in one of the supported formats (for example, an SRT file), you can include them in the transcoding regardless of the input container.

**Source Captions Are Inside the Input Container**

| Type of Input | Container | Captions Can Be Extracted from Container? |
| --- | --- | --- |
| File | Adobe Flash® container | No |
| File | Audio Video Interleave (AVI) container | No |
| File | HLS container | Yes |
| File | Matroska container | No |
| File | MP4 container | Yes |
| File | MPEG Transport stream | Yes |
| File | MPEG-1 system stream | No |
| File | MXF container | Yes |
| File | No container | Yes |
| File | QuickTime container | Yes |
| File | Transport stream  | Yes |
| File | VOB container | No |
| File | WMV/ASF container | No |
| Stream | HLS | Yes |
| Stream | RTP | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
