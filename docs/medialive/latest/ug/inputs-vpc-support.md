---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/inputs-vpc-support.html
---

# Support for setup as a VPC input in MediaLive
<a name="inputs-vpc-support"></a>

Some MediaLive inputs can be set up in Amazon Virtual Private Cloud (Amazon VPC). For more information, see [Creating an input](create-input.md).

| MediaLive input type | Can be set up as a VPC input |
| --- | --- |
| CDI | Yes, setup as a VPC input is supported |
| HLS | No |
| Link | No |
| MediaConnect | No |
| MediaConnect Router | No |
| MP4 | No |
| Transport Stream (TS) file | No |
| RTMP Pull | No |
| RTMP Push | Yes, setup as a VPC input is supported |
| RTP | Yes, setup as a VPC input is supported |
| SDI | No |
| SMPTE 2110 | No |
| SRT Caller | No |
| SRT Listener | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
