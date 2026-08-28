---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-advanced-optimization.html
---

# Advanced optimization techniques for CDN and MediaTailor integrations
<a name="cdn-advanced-optimization"></a>

After implementing basic caching and routing optimizations, consider these advanced techniques to further enhance performance:

## Origin Shield implementation
<a name="origin-shield-optimization"></a>

Origin Shield adds a caching layer between CDN edge locations and your origin server, reducing origin load and improving performance:
+ Enable Origin Shield for high-traffic content and live streaming
+ Choose Origin Shield locations close to your MediaTailor regions
+ Monitor Origin Shield cache hit ratios and adjust as needed
+ Consider multiple Origin Shield locations for global deployments

## Content compression optimization
<a name="compression-optimization"></a>

Optimize content compression to reduce bandwidth and improve delivery speed:
+ Enable gzip compression for manifest files
+ Configure Accept-Encoding header forwarding for MediaTailor manifest compression
+ Use Brotli compression where supported for additional bandwidth savings
+ Avoid compressing already-compressed video segments

## Regional optimization strategies
<a name="regional-optimization"></a>

Optimize performance for global audiences through regional strategies:
+ Deploy MediaTailor configurations in multiple regions for global audiences
+ Use geo-routing to direct viewers to the nearest MediaTailor region
+ Configure regional failover for high availability
+ Monitor regional performance metrics separately

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
