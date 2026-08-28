---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cloudfront-specific-recommendations.html
---

# Integrating AWS Elemental MediaTailor with Amazon CloudFront
<a name="cloudfront-specific-recommendations"></a>

AWS Elemental MediaTailor integrates with Amazon CloudFront to improve content delivery performance and reliability. CloudFront is a content delivery network (CDN) that distributes your content through a worldwide network of data centers called edge locations. When viewers request your content from MediaTailor, CloudFront routes requests to the nearest edge location. This approach reduces latency and improves performance for your viewers.

Integrating MediaTailor with CloudFront provides several key benefits:
+ Reduced latency for viewers accessing personalized content
+ Improved scalability for handling large audience sizes
+ Enhanced reliability through redundant delivery paths
+ Cost optimization through efficient caching strategies
+ Advanced features like multi-Region failover with Media Quality-Aware Resiliency (MQAR)

For comprehensive information about CloudFront features, see the [CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). For information about CloudFront pricing, see [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/).

For brevity, we sometimes use "manifests" to refer collectively to multivariant playlists, media playlists, and MPDs.

**Topics**
+ [Basic CloudFront setup](cloudfront-basic-setup.md)
+ [Performance optimization](cloudfront-performance-optimization.md)
+ [Multi-Region resilience](media-quality-resiliency.md)
+ [Monitoring and troubleshooting](monitoring-and-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
