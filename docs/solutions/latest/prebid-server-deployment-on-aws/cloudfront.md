---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/cloudfront.html
---

# CloudFront
<a name="cloudfront"></a>

## Alarm: 5xx error rate
<a name="alarm-5xx-error-rate"></a>
+ The alarm changes state if there are any 500 type status codes. Reported as a percentage of total requests within a 1-minute period.
+ This indicates a server failure. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the error rate is within the acceptable threshold for 5 minutes.
+ Metric: `5xxErrorRate` > 0%

## Alarm: 4xx error rate
<a name="alarm-4xx-error-rate"></a>
+ The alarm changes state if greater than or equal to 1% of requests are 400 type status codes. Reported a percentage of total requests within a 1-minute period.
+ This indicates a bad request or a possible configuration error. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the error rate is within the acceptable threshold for 5 minutes.
+ Metric: `4xxErrorRate` > 1%

## Alarm: Requests
<a name="alarm-requests"></a>
+ The alarm changes state if there is an anomaly in traffic with a high number of requests within 1 minute.
+ This indicates a spike or burst in traffic.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ The alarm is an anomaly alarm and will form the threshold based on the previous history of the metric.
+ Metric: `Requests` anomaly

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
