---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html
---

# Target tracking scaling policies for Application Auto Scaling
<a name="application-auto-scaling-target-tracking"></a>

A target tracking scaling policy automatically scales your application based on a target metric value. This allows your application to maintain optimal performance and cost efficiency without manual intervention.

With target tracking, you select a metric and a target value to represent the ideal average utilization or throughput level for your application. Application Auto Scaling creates and manages the CloudWatch alarms that trigger scaling events when the metric deviates from the target. This is similar to how a thermostat maintains a target temperature.

For example, let's say that you currently have an application that runs on Spot Fleet, and you want the CPU utilization of the fleet to stay at around 50 percent when the load on the application changes. This gives you extra capacity to handle traffic spikes without maintaining an excessive number of idle resources.

You can meet this need by creating a target tracking scaling policy that targets an average CPU utilization of 50 percent. Then, Application Auto Scaling will scale out (increase capacity) when CPU exceeds 50 percent to handle increased load. It will scale in (decrease capacity) when CPU drops below 50 percent to optimize costs during periods of low utilization.

Target tracking policies remove the need to manually define CloudWatch alarms and scaling adjustments. Application Auto Scaling handles this automatically based on the target you set.

You can base target tracking policies on either predefined or custom metrics:
+ **Predefined metrics**—Metrics provided by Application Auto Scaling like average CPU utilization or average request count per target.
+ **Custom metrics**—You can use metric math to combine metrics, leverage existing metrics, or use your own custom metrics published to CloudWatch.

Choose a metric that changes inversely proportional to a change in the capacity of your scalable target. So if you double capacity, the metric decreases by 50 percent. This allows the metric data to accurately trigger proportional scaling events.

**Topics**
+ [How target tracking works](target-tracking-scaling-policy-overview.md)
+ [Create a target tracking scaling policy](create-target-tracking-policy-cli.md)
+ [Delete a target tracking scaling policy](delete-target-tracking-policy.md)
+ [Use metric math](application-auto-scaling-target-tracking-metric-math.md)
