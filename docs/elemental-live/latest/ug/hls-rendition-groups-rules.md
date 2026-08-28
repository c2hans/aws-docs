---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-rules.html
---

# Rules for rendition groups
<a name="hls-rendition-groups-rules"></a>

Rules exist for associating both audio and video streams in their respective rendition groups. These are described following.
+ A given audio stream can belong to only one audio rendition group.
+ Any given video stream can be associated with more than one rendition group. (For example, “video high” can be associated with both “Dolby audio streams” and “AAC audio streams.” You do not need to create two video streams.)

  With this setup, all the rendition groups associated with the same video stream must contain the same audio streams.( For example, “Dolby audio streams” and “AAC audio streams” must contain the same audio streams (perhaps English, French and Spanish)).
+ Any given audio rendition group can be associated with more than one video stream.( For example, “Dolby audio streams” rendition group can be associated with “video high” and “video low.” You do not need to create two rendition groups, one for each video.)
+ Any video stream can be associated with more than one output group. (For example, “video high” can appear in two different HLS output groups).

You can use a combination of these rules. For more information, see [Examples of HLS rendition groups](hls-rendition-groups-examples.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
