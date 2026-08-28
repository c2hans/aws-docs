---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig.html
---

# Working with packaging configurations in AWS Elemental MediaPackage
<a name="pkg-cfig"></a>

A packaging configuration defines a single delivery point for an asset. The configuration holds all of the information that's needed for AWS Elemental MediaPackage to integrate with a player or content delivery network (CDN), such as Amazon CloudFront. Configure the configuration to output content in one of the available stream formats:
+ Apple HLS – Packages content to Apple HTTP Live Streaming (HLS)
+ Microsoft Smooth – Packages content for Microsoft Smooth Streaming players
+ Common Media Application Format (CMAF) – Packages content to devices that support Apple HLS fragmented MP4 (fMP4)
+ DASH-ISO – Packages content for the DASH-ISO ABR streaming protocol

The packaging configuration also holds information about digital rights management (DRM) and encryption integration, bitrate presentation order, and more.

**Topics**
+ [Creating a packaging configuration](pkg-cfig-create.md)
+ [Viewing packaging configuration details](pkg-cfig-view.md)
+ [Editing a packaging configuration](pkg-cfig-edit.md)
+ [Deleting a packaging configuration](pkg-cfig-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
