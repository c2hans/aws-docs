---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-create.html
---

# Creating HLS rendition groups
<a name="hls-rendition-groups-create"></a>

The key to creating rendition groups is that each output you create must contain only one stream. Therefore, for each video to include in the output group, you create a stream assembly that contains only one video (no audio or captions). For each audio to include in a rendition group, you create a stream assembly that contains only one audio (no video or captions).

This means that when rendition groups are present in the HLS output group, an output is identical to a stream. (Usually an output contains a mix of several streams and several stream types.)

**Topics**
+ [Getting ready to create HLS rendition groups](hls-rendition-groups-getting-ready-to-create.md)
+ [Creating HLS rendition groups (web interface)](hls-rendition-groups-create-using-web-interface.md)
+ [Creating HLS rendition groups (REST API)](hls-rendition-groups-create-using-rest-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
