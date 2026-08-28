---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-waf-2.html
---

# AWS WAF
<a name="aws-waf-2"></a>

## Blocked requests
<a name="blocked-requests"></a>
+ The alarm changes state if there is a large amount of blocked requests (greater than 75% of requests are blocked) within 1 minute.
+ This alarm indicates that there is something wrong with the requests passing through the WAF or there could be malicious requests in the traffic.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ Metric: `BlockedRequests` > 75%

## HTTP flood detected
<a name="http-flood-detected"></a>
+ The alarm changes state if there is an HTTP flood attack detected within a 1-minute period.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ If detailed WAF logging is enabled, it will log the HTTP flood requests in the chosen destination. A datapoint will be logged in the CloudWatch metrics for the rule.
+ Metric: `HttpFloodDetected` > 0

## Allowed requests
<a name="allowed-requests"></a>
+ The alarm changes state if there is an anomaly in traffic with a high number of allowed requests within 1 minute.
+ This alarm indicates a spike or burst in traffic.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ The alarm is an anomaly alarm and will form the threshold based on the previous history of the metric.
+ Metric: `AllowedRequests` anomaly

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
