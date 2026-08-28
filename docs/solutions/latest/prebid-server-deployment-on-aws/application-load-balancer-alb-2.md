---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/application-load-balancer-alb-2.html
---

# Application Load Balancer (ALB)
<a name="application-load-balancer-alb-2"></a>

## Target HTTP 4xx error rate
<a name="target-http-4xx-error-rate"></a>
+ The alarm changes state if there are `400` type status codes originating from the target (ECS). Reported as a percentage.
+ This indicates a bad request or a possible configuration error. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the error rate is within the acceptable threshold for 5 minutes.
+ Metric: `HTTPCode_Target_4xxErrorRate` > 1%

## Target HTTP 5xx error rate
<a name="target-http-5xx-error-rate"></a>
+ The alarm changes state if there are `500` type status codes originating from the target (ECS). Reported as a percentage.
+ This indicates a server failure. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the error rate is within the acceptable threshold for 5 minutes.
+ Metric: `HTTPCode_Target_5xxErrorRate` > 0%

## ALB HTTP 4xx error rate
<a name="alb-http-4xx-error-rate"></a>
+ The alarm changes state if there are `400` type status codes originating from ALB. Reported as a percentage.
+ This indicates a bad request or a possible configuration error. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the error rate is within the acceptable threshold for 5 minutes.
+ Metric: `HTTPCode_ELB_4xxErrorRate` > 1%

## ALB HTTP 5xx error rate
<a name="alb-http-5xx-error-rate"></a>
+ The alarm changes state if there are `500` type status codes originating from the target ALB. Reported as a percentage.
+ This indicates a server failure. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ Metric: `HTTPCode_ELB_5xxErrorRate` > 0%

## Target response time (Latency)
<a name="target-reponse-time-latency"></a>
+ The alarm changes state if there is a large amount of latency (greater than 100ms) reported within a 1-minute period.
+ This could indicate a performance issue or scaling failure from ECS. Check the CloudWatch logs to get further detail on the cause of the error.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ Metric: `TargetResponseTime average` > 100 ms

## Unhealthy host count
<a name="unhealthy-host-count"></a>
+ The alarm changes state if there is a target that is considered unhealthy within a 1-minute period.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ Check the CloudWatch logs to get further detail on the cause of the error.
+ Metric: `UnhealthyHotCount` > 0

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
