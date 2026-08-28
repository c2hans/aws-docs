---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-hdr-hls-outputs-that-comply-with-the-apple-specification.html
---

# Creating HDR HLS outputs that comply with the Apple specification
<a name="creating-hdr-hls-outputs-that-comply-with-the-apple-specification"></a>

For information about which Apple devices play back HDR content, see [Find and watch movies with 4K, HDR, Dolby Vision, or Dolby Atmos](https://support.apple.com/en-us/HT207949) in the Apple support documentation.

To create HDR outputs that comply with the Apple specification, you must make specific choices for your encoding settings. Specify the following settings:
+ **Output group** – Choose **CMAF**
+ **Encoding settings**, **Video codec** – Choose **HEVC (H.265)**.
+ **Encoding settings**, **Codec details**, **MP4 packaging type** – **HVC1**.
+ **Encoding settings**, **Codec details**, **Profile** – Choose **Main10/High**.
+ **Encoding settings**, **Codec details**, **Level** – Choose **5**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
