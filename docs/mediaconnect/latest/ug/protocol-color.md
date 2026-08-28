---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/protocol-color.html
---

# Color support for CDI protocols
<a name="protocol-color"></a>

MediaConnect CDI flows support multiple configurations of color space, bit depth, and chroma sampling for each protocol. The following table describes the configurations supported by each CDI protocol.

**Note**
MediaLive does not currently support RGB color space for CDI inputs. If you will be outputting a CDI flow from MediaConnect to MediaLive, ensure that you use YCbCr color space.

**CDI color support**

| Protocol | Supported color configurations |
| --- | --- |
| CDI |  +  YCbCr 10-bit 4:2:2 <br />+  RGB 10-bit 4:4:4 <br />+  RGB 12-bit 4:4:4   |
| ST 2110 JPEG XS |  +  YCbCr 10-bit 4:2:2 <br />+  RGB 10-bit 4:4:4 <br />+  RGB 12-bit 4:4:4   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
