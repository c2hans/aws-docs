---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/application-load-balancer-alb-2.html
---

# Application Load Balancer (ALB)

These alarms monitor the internet-facing ALB.

## ALB HTTP 4xx errors
<a name="alb-http-4xx-error-rate"></a>
+ The alarm changes state if the average count of `400` type status codes originating from the ALB is greater than 1 within a 1-minute period.
+ This indicates a bad request or a possible configuration error. Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `HTTPCode_ELB_4XX_Count` > 1

## ALB HTTP 5xx errors
<a name="alb-http-5xx-error-rate"></a>
+ The alarm changes state if there are any `500` type status codes originating from the ALB within a 1-minute period.
+ This indicates a server failure. Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `HTTPCode_ELB_5XX_Count` > 0

## Target response time (Latency)
<a name="target-reponse-time-latency"></a>
+ The alarm changes state if the average target response time is greater than 1 second within a 1-minute period.
+ This could indicate a performance issue or scaling failure from ECS. Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `TargetResponseTime` average > 1 second

## Request count anomaly
<a name="alb-requests-anomaly"></a>
+ The alarm changes state if the number of requests within 1 minute is above or below the expected band.
+ This indicates a spike, burst, or drop in traffic.
+ The alarm is an anomaly alarm and forms its threshold (2 standard deviations) based on the previous history of the metric.
+ Metric: `RequestCount` anomaly
