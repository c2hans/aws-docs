---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/vod-content.html
---

# Delivering VOD content from AWS Elemental MediaPackage
<a name="vod-content"></a>

AWS Elemental MediaPackage uses the following resources for video on demand (VOD) content:
+ *Packaging groups* hold one or more packaging configurations. The group enables you to apply multiple output configurations to an asset at the same time. You can associate a group to multiple assets so that they all have the same configurations for their outputs.
+ *Packaging configurations* tell MediaPackage how to package the output from an asset. In the configuration, you define encryption, bitrate, and packaging settings.
+ *Assets* ingest your source content and dynamically apply packaging configurations in response to playback requests.

  For supported VOD inputs and codecs, see [VOD supported codecs and input types](supported-inputs-vod.md).

The following sections describe how to use these resources to manage VOD content in MediaPackage.

**Topics**
+ [Working with packaging groups in AWS Elemental MediaPackage](pkg-group.md)
+ [Working with packaging configurations in AWS Elemental MediaPackage](pkg-cfig.md)
+ [Working with assets in AWS Elemental MediaPackage](asset.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
