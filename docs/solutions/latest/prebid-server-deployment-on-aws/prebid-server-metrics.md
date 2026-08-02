---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/prebid-server-metrics.html
---

# Prebid Server metrics
<a name="prebid-server-metrics"></a>

The Prebid Server collects various application metrics, which are submitted to configured backends. These metrics can be used for monitoring and optimizing the performance of the server. The metrics include information such as bid requests, bid responses, and other relevant statistics. For more detailed information on the specific metrics collected and how to integrate custom analytics adapters, refer to the official [Prebid Server documentation](https://docs.prebid.org/prebid-server/developers/pbs-build-an-analytics-adapter.html#prebid-server---building-an-analytics-adapter) and the [metrics.md](https://github.com/prebid/prebid-server-java/blob/master/docs/metrics.md) file in the GitHub repository for the Prebid Server Java implementation.

In this solution, metrics that are emitted by the Prebid Server containers are captured via log files. This is achieved by hooking the operational monitoring system to the Java file logger by modifying the original source file on the GitHub repository - [MetricsConfiguration.java](https://github.com/prebid/prebid-server-java/blob/master/src/main/java/org/prebid/server/spring/config/metrics/MetricsConfiguration.java).

This data is processed through the same ETL pipeline as operational metrics, making it available for analysis through AWS Glue Data Catalog and Amazon Athena. For configuration details, see the [Configuring the analytics adapter](configure-the-solution.md#configuring-analytics-adapter) section.
