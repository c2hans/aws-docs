---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/cloudwatch-metrics.html
---

# Available CloudWatch metrics for Amazon Route 53 Global Resolver performance monitoring
<a name="cloudwatch-metrics"></a>

Amazon Route 53 Global Resolver integrates with CloudWatch to provide comprehensive DNS performance and security monitoring. You can monitor Amazon Route 53 Global Resolver using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your Amazon Route 53 Global Resolver DNS resolution service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met.

The following metrics are available for Amazon Route 53 Global Resolver in the `AWS/Route53GlobalResolver` namespace:

| Metric | Description | Unit |
| --- | --- | --- |
| QueryCount | Total number of DNS queries processed | Count |
| BlockedQueryCount | Number of queries blocked by firewall rules | Count |
| AllowedQueryCount | Number of queries allowed through firewall rules | Count |
| AlertQueryCount | Number of queries that triggered alert actions | Count |
| ResponseTime | Time taken to process DNS queries | Milliseconds |
