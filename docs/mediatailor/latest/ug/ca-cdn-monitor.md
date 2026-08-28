---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-monitor.html
---

# Monitor MediaTailor channel assembly CDN operations
<a name="ca-cdn-monitor"></a>

AWS Elemental MediaTailor channel assembly requires effective monitoring when integrated with a content delivery network (CDN) to ensure reliable content delivery. Implement monitoring strategies for your channel assembly and CDN integration to help ensure reliable content delivery and quick problem resolution.

For comprehensive CDN monitoring guidance including essential metrics, monitoring tools setup, alert configuration, and troubleshooting strategies that apply to all MediaTailor implementations, see [CDN monitoring](cdn-monitoring.md). This section focuses on channel assembly-specific monitoring requirements.

Implement specific monitoring for your channel assembly and CDN integration:
+ Track manifest generation metrics in channel assembly.
+ Monitor time-shifted viewing requests and their impact on CDN cache hit rates.
+ Configure alerts for unusual patterns in manifest requests.
+ Implement tracking for segment availability across your content sources.

For Amazon CloudFront, create a dashboard that integrates CDN metrics with MediaTailor metrics to visualize your entire delivery pipeline using [CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

If you're also using SSAI with your channel assembly, see [Monitor CDN operations](ssai-cdn-monitor.md) for additional monitoring recommendations specific to ad insertion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
