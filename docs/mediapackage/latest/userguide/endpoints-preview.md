---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-preview.html
---

# Previewing a manifest from AWS Elemental MediaPackage
<a name="endpoints-preview"></a>

Preview an endpoint's manifest to ensure that MediaPackage is receiving the content stream and can package it. The preview is helpful for avoiding playback failures after the endpoint is published and for troubleshooting later if there are any playback issues.

You can use the MediaPackage console to preview playback from the endpoint.

**To preview an endpoint's playback**

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md).

1. Under **Origin endpoints**, select the endpoint that you want to preview.

1. To preview playback, do one of the following:
   + Choose **Preview** to play content with the embedded player.
   + Choose **QR code** to view and scan the QR code for playback on a compatible device.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
