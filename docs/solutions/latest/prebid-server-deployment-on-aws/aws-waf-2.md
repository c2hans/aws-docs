---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-waf-2.html
---

# AWS WAF
<a name="aws-waf-2"></a>

This alarm is created only when CloudFront and AWS WAF are deployed.

## Blocked requests
<a name="blocked-requests"></a>
+ The alarm changes state if the number of blocked requests rises above the expected band within 1 minute.
+ This alarm indicates that there is something wrong with the requests passing through the WAF or there could be malicious requests in the traffic.
+ The alarm is an anomaly alarm and forms its threshold (2 standard deviations) based on the previous history of the metric.
+ Metric: `BlockedRequests` anomaly (above the upper band)
