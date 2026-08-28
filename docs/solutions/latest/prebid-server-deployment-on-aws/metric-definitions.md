---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/metric-definitions.html
---

# Metric definitions
<a name="metric-definitions"></a>

System metrics are captured using the [Vert.x Metrics Service Provider Interface (SPI)](https://vertx.io/docs/vertx-dropwizard-metrics/java/#_the_metrics).

Auction metrics are captured both in general auction metrics as well as per-adapter metrics for bid-adapters that have been configured.

The full list of metrics with definitions can be viewed in the [prebid-server-java](https://github.com/prebid/prebid-server-java/blob/master/docs/metrics.md) GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
