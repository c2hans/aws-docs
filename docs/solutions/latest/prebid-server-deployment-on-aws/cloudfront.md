---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/cloudfront.html
---

# CloudFront

These alarms are created only when CloudFront and AWS WAF are deployed.

## Alarm: 5xx error rate
<a name="alarm-5xx-error-rate"></a>
+ The alarm changes state if there are any 500 type status codes. Reported as a percentage of total requests within a 1-minute period.
+ This indicates a server failure. Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `5xxErrorRate` > 0%

## Alarm: 4xx error rate
<a name="alarm-4xx-error-rate"></a>
+ The alarm changes state if more than 1% of requests are 400 type status codes. Reported as a percentage of total requests within a 1-minute period.
+ This indicates a bad request or a possible configuration error. Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `4xxErrorRate` > 1%

## Alarm: Total error rate
<a name="alarm-total-error-rate"></a>
+ The alarm changes state if more than 1% of requests return 400 or 500 type status codes. Reported as a percentage of total requests within a 1-minute period.
+ Check the [4xx error rate](#alarm-4xx-error-rate) and [5xx error rate](#alarm-5xx-error-rate) alarms and the CloudWatch logs to identify the cause of the errors.
+ Metric: `TotalErrorRate` > 1%

## Alarm: Requests
<a name="alarm-requests"></a>
+ The alarm changes state if the number of requests within 1 minute is above or below the expected band.
+ This indicates a spike, burst, or drop in traffic.
+ The alarm is an anomaly alarm and forms its threshold (2 standard deviations) based on the previous history of the metric.
+ Metric: `Requests` anomaly
