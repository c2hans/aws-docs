---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/configuration-aliases-overview.html
---

# MediaTailor configuration aliases overview
<a name="configuration-aliases-overview"></a>

AWS Elemental MediaTailor configuration aliases enable dynamic variable replacement in URL domains and other supported fields. Use this feature to use multiple domains and dynamically configure URLs during session initialization.

## Use cases
<a name="configuration-aliases-use-cases"></a>

Configuration aliases enable sophisticated multi-configuration architectures for the following scenarios:
+ **Geographic routing:** Route requests to different origins or ad servers based on viewer location using region-specific aliases. For implementation guidance, see [CloudFront Origin Failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html).
+ **Content-based routing:** Direct different content types to specialized origins or processing pipelines. For routing behavior configuration, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md).
+ **Failover scenarios:** Implement backup origins and ad servers with automatic failover using alias switching. For detailed implementation, see [Implement multi-Region resilience for MediaTailor with MQAR](media-quality-resiliency.md) and [Plan your CDN integration for AWS Elemental MediaTailor](planning-cdn-integration.md).
+ **A/B testing:** Test different ad servers, origins, or configurations by routing traffic based on player parameters. For load testing guidance, see [Prepare and run performance tests for Amazon CloudFront with real user monitoring](https://aws.amazon.com/blogs/networking-and-content-delivery/prepare-and-run-performance-tests-for-amazon-cloudfront-with-real-user-monitoring/).
+ **Device-specific optimization:** Optimize content delivery and ad serving for different device types or capabilities. For comprehensive guidance, see [Set up manifest filtering with MediaTailor, MediaPackage, and CDN](cdn-emp-manifest-filtering.md).
+ **Load balancing:** Distribute load across multiple origins or ad servers using dynamic routing. For implementation guidance, see [Implement multi-Region resilience for MediaTailor with MQAR](media-quality-resiliency.md) and [Plan your CDN integration for AWS Elemental MediaTailor](planning-cdn-integration.md).

## Supported fields
<a name="configuration-aliases-supported"></a>

You can use dynamic variables in the following configuration fields:
+ `VideoContentSourceUrl`
+ `AdDecisionServerUrl`
+ `LivePreroll.AdDecisionServerUrl`
+ `AdSegmentUrlPrefix`
+ `ContentSegmentUrlPrefix`
+ `TranscodeProfileName`
+ `SlateAdUrl`
+ `StartUrl`
+ `EndUrl`

The following sections describe how to use configuration aliases.

**Topics**
+ [Use cases](#configuration-aliases-use-cases)
+ [Supported fields](#configuration-aliases-supported)
+ [Creating and using](creating-configuration-aliases.md)
+ [Example flow](configuration-aliases-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
