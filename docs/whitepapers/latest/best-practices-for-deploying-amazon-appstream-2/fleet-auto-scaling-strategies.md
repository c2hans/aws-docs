---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/fleet-auto-scaling-strategies.html
---

# Fleet auto scaling strategies
<a name="fleet-auto-scaling-strategies"></a>

## Understanding WorkSpaces Applications instances
<a name="understanding-appstream-2.0-instances"></a>

 WorkSpaces Applications fleet instances have a 1:1 user to fleet instance ratio. This means each user has their own streaming instance. The number of users you connect concurrently will determine the size of the fleet.

## Scaling policies
<a name="scaling-policies"></a>

 WorkSpaces Applications fleets are launched in an Application Auto Scaling Group. This allows the fleet to scale based on usage to meet demand. As usage increases, the fleet scales out, and as users disconnect, the fleet scales back in. This is controlled by setting scaling policies. You can set scheduled-based scaling, step scaling, and target tracking scaling policies. For more information about these scaling policies, refer to [*Fleet Auto Scaling for Amazon WorkSpaces Applications*](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html).

### Step scaling
<a name="step-scaling"></a>

 These policies increase or decrease the fleet capacity by a percentage of the current fleet size or a specific number of instances. Step scaling policies are triggered by [* WorkSpaces Applications CloudWatch metrics*](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html#monitoring-with-cloudwatch) of `Capacity Utilization`, `Available Capacity`, or `Insufficient Capacity Errors`.

 When using step scaling policies, AWS recommends that you add a percentage of capacity and not a fixed number of instances. This ensures that your scaling actions are proportional to the size of your fleet. It will help to avoid situations where you scale out too slowly (because you added a small number of instances relative to your fleet size) or too many instances when your fleet is small.

### Target tracking
<a name="target-tracking"></a>

 With this policy specifies a capacity utilization level for the fleet. Application Autoscaling creates and manages CloudWatch alarms that trigger the scaling policy. This adds or removes capacity to keep the fleet at, or close to, the specified target value. To ensure application availability, your fleet scales out proportionally to the metric as fast as it can, but scales in more gradually. When configuring target tracking, consider the scaling [cooldown](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html#target-tracking-cooldown) to ensure scale-out and scale-in happen in desired intervals.

 Target tracking is effective for high churn situations. Churn is when a large number of users start, or end, sessions in a short period of time. You can identify churn by examining CloudWatch metrics for your fleet. Periods of time when your fleet has non- zero pending capacity without change (or with very little change) in desired capacity indicate that high churn is likely occurring. In high churn situations, configure target tracking policies where (100 – target utilization percent) is more than the churn rate in a 15-minute period. For example, if 10% of your fleet will be terminated in 15 minutes due to user turnover, set a capacity utilization target of 90% or less to offset high churn.

### Scheduled-based scaling
<a name="scheduled-based-scaling"></a>

 These policies enable you to set the desired fleet capacity based on a time-based schedule. This policy is effective when you understand login behavior, and can predict changes in demand.

 For example, at the start of the work day, you might expect 100 users to request streaming connections at 9:00 AM. You can configure a scheduled-based scaling policy to set the minimum fleet size to 100 at 8:40 AM. This allows the fleet instances to be created and become available at the start of the work day, and allows 100 users to connect at the same time. You can then set another scheduled policy to scale in the fleet to a minimum of ten at 5:00 PM. This enables you to save cost, as the demand for sessions after hours is less than during the work day.

### Scaling policies in production
<a name="scaling-policies-in-production"></a>

 You can choose to combine different types of scaling policies in a single fleet to help define precise scaling policies for your user behavior. In the previous example, you can combine the scheduled scaling policy with target tracking or step scaling policies to maintain a specific level of utilization. The combination of scheduled scaling and target tracking scaling can help reduce the impact of a sharp increase in utilization levels when capacity is needed immediately.

 Users connected to streaming sessions when a scaling policy changes the desired number of instances are not affected by a scale-in or scale-out. Scaling policies will not end existing streaming sessions. Existing sessions will continue uninterrupted until the session is ended by the user or a fleet time-out policy.

 Monitoring WorkSpaces Applications usage with CloudWatch metrics can help you optimize your scaling policies over time. For example, it is common to over-provision resources during initial setup and you might see long periods of low utilization. Alternatively, if the fleet is under-provisioned, you might see high-capacity utilization and “Insufficient Capacity” errors. Reviewing CloudWatch metrics can help drive adjustments to your scaling policies to help mitigate these errors. For more information, and examples of WorkSpaces Applications scaling policies that you can use, refer to [*Scale your Amazon WorkSpaces Applications fleets*](https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
