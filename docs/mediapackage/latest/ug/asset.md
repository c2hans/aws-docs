---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/asset.html
---

# Working with assets in AWS Elemental MediaPackage
<a name="asset"></a>

An asset holds all of the information that MediaPackage requires to ingest file-based video content from a source such as Amazon S3. Through the asset, MediaPackage ingests and dynamically packages content in response to playback requests. The configurations associated with the asset determine how it can be packaged for output.

After you ingest an asset, AWS Elemental MediaPackage provides a URL for each playback configuration associated with the asset. This URL is fixed for the lifetime of the asset, regardless of any failures that might happen over time. Downstream devices use the URL to send playback requests.

For supported VOD inputs and codecs, see [VOD supported codecs and input types](supported-inputs-vod.md).

**Topics**
+ [Ingesting an asset](asset-create.md)
+ [Viewing asset details](asset-view.md)
+ [Editing an asset](asset-edit.md)
+ [Deleting an asset](asset-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
