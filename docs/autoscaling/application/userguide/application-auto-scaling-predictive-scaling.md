---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-predictive-scaling.html
---

# Predictive scaling for Application Auto Scaling
<a name="application-auto-scaling-predictive-scaling"></a>

Predictive scaling proactively scales your application. Predictive scaling analyzes historical load data to detect daily or weekly patterns in traffic flows. It uses this information to forecast future capacity needs to proactively increase the capacity of your application to match the anticipated load.

Predictive scaling is well suited for situations where you have:
+ Cyclical traffic, such as high use of resources during regular business hours and low use of resources during evenings and weekends
+ Recurring on-and-off workload patterns, such as batch processing, testing, or periodic data analysis.
+ Applications that take a long time to initialize, causing a noticeable latency impact on application performance during scale-out events

**Topics**
+ [How it works](aas-predictive-scaling-how-it-works.md)
+ [Create a predictive scaling policy](aas-create-predictive-scaling-policy.md)
+ [Override the forecast](aas-predictive-scaling-overriding-forecast-capacity.md)
+ [Use custom metrics](aas-predictive-scaling-customized-metric-specification.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
