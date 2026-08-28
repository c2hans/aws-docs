---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-opg-redundant-manifest.html
---

# Fields for redundant manifests
<a name="hls-opg-redundant-manifest"></a>

MediaLive supports redundant manifests as specified in the HLS specification. You can enable this feature in a standard channel.

The following fields relate to redundant manifests:
+ **HLS output group – Manifests and Segments – Redundant manifests** field
+ **HLS output group – Location – the Base URL manifest** fields
+ **HLS output group – Location – the Base URL content** fields

You can’t enable this feature in an HLS output group that has MediaPackage as the downstream system.

For more information about setting up for redundant manifests, see [Creating redundant HLS manifests](hls-redundant-manifests.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
