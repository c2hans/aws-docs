---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints.html
---

# Working with endpoints in AWS Elemental MediaPackage
<a name="endpoints"></a>

An endpoint defines a single delivery point of a channel. The endpoint holds all the information that's needed for AWS Elemental MediaPackage to integrate with a player or content delivery network (CDN) such as Amazon CloudFront. Configure the endpoint to output content in one of the available stream formats:
+ Apple HLS – Packages content to Apple HTTP Live Streaming (HLS)
+ Microsoft Smooth Streaming – Packages content for Microsoft Smooth Streaming players
+ DASH-ISO – Packages content for the DASH-ISO ABR streaming protocol
+ CMAF – Packages content to devices that support Apple HLS fragmented MP4 (fMP4)

Additionally, the endpoint holds information about digital rights management (DRM) and encryption integration, stream bitrate presentation order, and more.

**Topics**
+ [Creating an endpoint](endpoints-create.md)
+ [Viewing all endpoints associated with a channel](endpoints-view-all.md)
+ [Viewing a single endpoint](endpoints-view-one.md)
+ [Editing an endpoint](endpoints-edit.md)
+ [Deleting an endpoint](endpoints-delete.md)
+ [Previewing an endpoint](endpoints-preview.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
