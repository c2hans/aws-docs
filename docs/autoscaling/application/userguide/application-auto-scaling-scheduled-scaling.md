---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html
---

# Scheduled scaling for Application Auto Scaling
<a name="application-auto-scaling-scheduled-scaling"></a>

With scheduled scaling, you can set up automatic scaling for your application based on predictable load changes by creating scheduled actions that increase or decrease capacity at specific times. This allows you to scale your application proactively to match predictable load changes.

For example, let's say you experience a regular weekly traffic pattern where load increases mid-week and declines toward the end of the week. You can configure a scaling schedule in Application Auto Scaling that aligns with this pattern:
+ On Wednesday morning, one scheduled action increases capacity by increasing the previously set minimum capacity of the scalable target.
+ On Friday evening, another scheduled action decreases capacity by decreasing the previously set maximum capacity of the scalable target.

These scheduled scaling actions allow you to optimize costs and performance. Your application has sufficient capacity to handle the mid-week traffic peak, but does not over-provision unneeded capacity at other times.

You can use scheduled scaling and scaling policies together to get the benefits of proactive and reactive approaches to scaling. After a scheduled scaling action runs, the scaling policy can continue to make decisions about whether to further scale capacity. This helps you ensure that you have sufficient capacity to handle the load for your application. While your application scales to match demand, current capacity must fall within the minimum and maximum capacity that was set by your scheduled action.

**Topics**
+ [How scheduled scaling works](scheduled-scaling-policy-overview.md)
+ [Create scheduled actions](create-scheduled-actions.md)
+ [Describe scheduled scaling](describe-scheduled-scaling.md)
+ [Schedule recurring scaling actions](scheduled-scaling-using-cron-expressions.md)
+ [Turn off scheduled scaling](suspend-scheduled-scaling.md)
+ [Delete a scheduled action](delete-scheduled-action.md)
