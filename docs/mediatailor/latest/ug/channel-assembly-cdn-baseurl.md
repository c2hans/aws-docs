---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-cdn-baseurl.html
---

# Configure base URLs for MediaTailor channel assembly CDN
<a name="channel-assembly-cdn-baseurl"></a>

AWS Elemental MediaTailor channel assembly requires proper base URL configuration to ensure content routing through your content delivery network (CDN) works correctly. Configure the base URL settings in channel assembly to enable successful content delivery to viewers.

## Content segment URL configuration
<a name="channel-assembly-cdn-content-segment"></a>

In your channel assembly channel configuration, set the **Base URL** to your CDN domain. This ensures that all segment URLs in the assembled manifest point to your CDN rather than directly to your origin server.

For example, if your origin content is at `http://origin.example.com/content/` and your CDN domain is `https://cdn.example.com/`, set the Base URL to `https://cdn.example.com/content/`.

## Access restriction configuration
<a name="channel-assembly-cdn-access-restriction"></a>

To enhance security, configure your CDN to restrict direct access to your origin server:

1. Set up origin access controls in your CDN.

1. Configure your origin server to only accept requests from your CDN.

1. Use signed URLs or cookies for viewer authentication if needed.

For Amazon CloudFront, you can use Origin Access Control (OAC) to secure access to your origin. For more information about securing your CloudFront integration, see [CloudFront integration](cloudfront-specific-recommendations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
