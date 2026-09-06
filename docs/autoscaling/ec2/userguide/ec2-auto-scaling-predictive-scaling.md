---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html
---

# Predictive scaling for Amazon EC2 Auto Scaling
<a name="ec2-auto-scaling-predictive-scaling"></a>

Predictive scaling works by analyzing historical load data to detect daily or weekly patterns in traffic flows. It uses this information to forecast future capacity needs so Amazon EC2 Auto Scaling can proactively increase the capacity of your Auto Scaling group to match the anticipated load.

Predictive scaling is well suited for situations where you have:
+ Cyclical traffic, such as high use of resources during regular business hours and low use of resources during evenings and weekends
+ Recurring on-and-off workload patterns, such as batch processing, testing, or periodic data analysis
+ Applications that take a long time to initialize, causing a noticeable latency impact on application performance during scale-out events

In general, if you have regular patterns of traffic increases and applications that take a long time to initialize, you should consider using predictive scaling. Predictive scaling can help you scale faster by launching capacity in advance of forecasted load, compared to using only dynamic scaling, which is reactive in nature. Predictive scaling can also potentially save you money on your EC2 bill by helping you avoid the need to over provision capacity.

For example, consider an application that has high usage during business hours and low usage overnight. At the start of each business day, predictive scaling can add capacity before the first influx of traffic. This helps your application maintain high availability and performance when going from a period of lower utilization to a period of higher utilization. You don't have to wait for dynamic scaling to react to changing traffic. You also don't have to spend time reviewing your application's load patterns and trying to schedule the right amount of capacity using scheduled scaling.

**Topics**
+ [How predictive scaling works](predictive-scaling-policy-overview.md)
+ [Create a predictive scaling policy](predictive-scaling-create-policy.md)
+ [Evaluate your predictive scaling policies](predictive-scaling-graphs.md)
+ [Override the forecast](predictive-scaling-overriding-forecast-capacity.md)
+ [Use custom metrics](predictive-scaling-customized-metric-specification.md)
