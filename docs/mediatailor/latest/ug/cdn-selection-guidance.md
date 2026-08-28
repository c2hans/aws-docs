---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-selection-guidance.html
---

# Select the right CDN for your needs
<a name="cdn-selection-guidance"></a>

Choosing the right content delivery network (CDN) provider is an important decision that can impact your content delivery performance, cost, and viewer experience with AWS Elemental MediaTailor. Consider these factors when selecting a CDN for your MediaTailor implementation:

**Geographic coverage**
Choose a CDN with strong presence in regions where your audience is located. Different CDN providers have varying strengths in different geographic regions.

**Integration with AWS services**
Amazon CloudFront offers the tightest integration with MediaTailor and other AWS services, which can simplify setup and management. Third-party CDNs might offer other advantages like specialized video delivery features or stronger presence in specific regions.

**Video-specific features**
Look for CDNs that offer features specifically designed for video delivery, such as adaptive bitrate optimization, video compression, and analytics focused on viewer experience.

**Cost structure**
Compare pricing models across providers, considering factors like traffic volume, geographic distribution, and feature requirements. Some CDNs offer volume discounts or committed use discounts that might align with your usage patterns.

**Support for advanced features**
Verify that your chosen CDN supports the features you need, such as token authentication, geo-restriction, request collapsing, and proper header forwarding.

For more information about specific CDN providers and their integration with MediaTailor, see the following resources.
+ [CloudFront integration](cloudfront-specific-recommendations.md) for Amazon CloudFront
+ [Third-party CDN setup](cdn-provider-specific.md) for third-party CDN providers

The following topics provide comprehensive guidance on configuring MediaTailor with a CDN for optimal performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
