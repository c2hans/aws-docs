---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html
---

# How target tracking scaling for Application Auto Scaling works
<a name="target-tracking-scaling-policy-overview"></a>

This topic describes how target tracking scaling works and introduces the key elements of a target tracking scaling policy.

**Topics**
+ [How it works](#target-tracking-how-it-works)
+ [Choose metrics](#target-tracking-choose-metrics)
+ [Define target value](#target-tracking-define-target-value)
+ [Define cooldown periods](#target-tracking-cooldown)
+ [Considerations](#target-tracking-considerations)
+ [Multiple scaling policies](#target-tracking-multiple-scaling-policies)
+ [Commonly used commands](#target-tracking-policy-commonly-used-commands)
+ [Related resources](#target-tracking-related-resources)
+ [Limitations](#target-tracking-limitations)

## How it works
<a name="target-tracking-how-it-works"></a>

To use target tracking scaling, you create a target tracking scaling policy and specify the following:
+ **Metric**—A CloudWatch metric to track, such as average CPU utilization or average request count per target.
+ **Target value**—The target value for the metric, such as 50 percent CPU utilization or 1000 requests per target per minute.

Application Auto Scaling creates and manages the CloudWatch alarms that invoke the scaling policy and calculates the scaling adjustment based on the metric and the target value. It adds and removes capacity as required to keep the metric at, or close to, the specified target value.

When the metric is above the target value, Application Auto Scaling scales out by adding capacity to reduce the difference between the metric value and the target value. When the metric is below the target value, Application Auto Scaling scales in by removing capacity.

Scaling activities are performed with cooldown periods between them to prevent rapid fluctuations in capacity. You can optionally configure the cooldown periods for your scaling policy.

The following diagram shows an overview of how a target tracking scaling policy works when the set up is complete.

![Overview diagram of a target tracking scaling policy](http://docs.aws.amazon.com/autoscaling/application/userguide/images/target-tracking-scaling-policy.png)

Note that a target tracking scaling policy is more aggressive in adding capacity when utilization increases than it is in removing capacity when utilization decreases. For example, if the policy's specified metric reaches its target value, the policy assumes that your application is already heavily loaded. So it responds by adding capacity proportional to the metric value as fast as it can. The higher the metric, the more capacity is added.

When the metric falls below the target value, the policy won't scale-in if it calculates that removing a minimum unit of capacity would likely bring the metric back above the target value. In this case, it slows down scaling by removing capacity only when utilization passes a threshold that is far enough below the target value (usually more than 10% lower) for utilization to be considered to have slowed. The intention of this more conservative behavior is to ensure that removing capacity only happens when the application is no longer experiencing demand at the same high level that it was previously.

## Choose metrics
<a name="target-tracking-choose-metrics"></a>

You can create target tracking scaling policies with either predefined metrics or custom metrics.

When you create a target tracking scaling policy with a predefined metric type, you choose one metric from the list of predefined metrics in [Predefined metrics for target tracking scaling policies](monitoring-cloudwatch.md#predefined-metrics).

Keep the following in mind when choosing a metric:
+ Not all custom metrics work for target tracking. The metric must be a valid utilization metric and describe how busy a scalable target is. The metric value must increase or decrease proportionally to the capacity of the scalable target so that the metric data can be used to proportionally scale the scalable target.
+ To use the `ALBRequestCountPerTarget` metric, you must specify the `ResourceLabel` parameter to identify the target group that is associated with the metric.
+ When a metric emits real 0 values to CloudWatch (for example, `ALBRequestCountPerTarget`), Application Auto Scaling can scale in to 0 when there is no traffic to your application for a sustained period of time. To have your scalable target scale in to 0 when no requests are routed it, the scalable target's minimum capacity must be set to 0.
+ Instead of publishing new metrics to use in your scaling policy, you can use metric math to combine existing metrics. For more information, see [Create a target tracking scaling policy for Application Auto Scaling using metric math](application-auto-scaling-target-tracking-metric-math.md).
+ To see whether the service you are using supports specifying a custom metric in the service's console, consult the documentation for that service.
+ We recommend that you use metrics that are available at one-minute intervals to help you scale faster in response to utilization changes. Target tracking will evaluate metrics aggregated at a one-minute granularity for all predefined metrics and custom metrics, but the underlying metric might publish data less frequently. For example, all Amazon EC2 metrics are sent in five-minute intervals by default, but they are configurable to one minute (known as detailed monitoring). This choice is up to the individual services. Most try to use the smallest interval possible.

## Define target value
<a name="target-tracking-define-target-value"></a>

When you create a target tracking scaling policy, you must specify a target value. The target value represents the optimal average utilization or throughput for your application. To use resources cost efficiently, set the target value as high as possible with a reasonable buffer for unexpected traffic increases. When your application is optimally scaled out for a normal traffic flow, the actual metric value should be at or just below the target value.

When a scaling policy is based on throughput, such as the request count per target for an Application Load Balancer, network I/O, or other count metrics, the target value represents the optimal average throughput from a single entity (such as a single target of your Application Load Balancer target group), for a one-minute period.

## Define cooldown periods
<a name="target-tracking-cooldown"></a>

You can optionally define cooldown periods in your target tracking scaling policy.

A cooldown period specifies the amount of time the scaling policy waits for a previous scaling activity to take effect.

There are two types of cooldown periods:
+ With the *scale-out cooldown period*, the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a scaling policy, it starts to calculate the cooldown time. A scaling policy won‘t increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends. While the scale-out cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity.
+ With the *scale-in cooldown period*, the intention is to scale in conservatively to protect your application‘s availability, so scale-in activities are blocked until the scale-in cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Application Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn‘t complete.

Each cooldown period is measured in seconds and applies only to scaling policy-related scaling activities. During a cooldown period, when a scheduled action starts at the scheduled time, it can trigger a scaling activity immediately without waiting for the cooldown period to expire.

You can start with the default values, which can be later fine-tuned. For example, you might need to increase a cooldown period to prevent your target tracking scaling policy from being too aggressive about changes that occur over short periods of time.

**Default values**

Application Auto Scaling provides a default value of 600 for ElastiCache and a default value of 300 for the following scalable targets:
+ WorkSpaces Applications fleets
+ Aurora DB clusters
+ ECS services
+ Neptune clusters
+ SageMaker AI endpoint variants
+ SageMaker AI inference components
+ SageMaker AI Serverless provisioned concurrency
+ Spot Fleets
+ Pool of WorkSpaces
+ Custom resources

For all other scalable targets, the default value is 0 or null:
+ Amazon Comprehend document classification and entity recognizer endpoints
+ DynamoDB tables and global secondary indexes
+ Amazon Keyspaces tables
+ Lambda provisioned concurrency
+ Amazon MSK broker storage

Null values are treated the same as zero values when Application Auto Scaling evaluates the cooldown period.

You can update any of the default values, including null values, to set your own cooldown periods.

## Considerations
<a name="target-tracking-considerations"></a>

The following considerations apply when working with target tracking scaling policies:
+ Do not create, edit, or delete the CloudWatch alarms that are used with a target tracking scaling policy. Application Auto Scaling creates and manages the CloudWatch alarms that are associated with your target tracking scaling policies and deletes them when no longer needed.
+ If the metric is missing data points, this causes the CloudWatch alarm state to change to `INSUFFICIENT_DATA`. When this happens, Application Auto Scaling cannot scale your scalable target until new data points are found. For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) in the *Amazon CloudWatch User Guide*.
+ If the metric is sparsely reported by design, metric math can be helpful. For example, to use the most recent values, then use the `FILL(m1,REPEAT)` function where `m1` is the metric.
+ You may see gaps between the target value and the actual metric data points. This is because Application Auto Scaling always acts conservatively by rounding up or down when it determines how much capacity to add or remove. This prevents it from adding insufficient capacity or removing too much capacity. However, for a scalable target with a small capacity, the actual metric data points might seem far from the target value.

  For example, suppose that you set a target value of 50 percent for CPU utilization and your Auto Scaling group then exceeds the target. We might determine that adding 1.5 instances will decrease the CPU utilization to close to 50 percent. Because it is not possible to add 1.5 instances, we round up and add two instances. This might decrease the CPU utilization to a value below 50 percent, but it ensures that your application has enough resources to support it. Similarly, if we determine that removing 0.5 instances increases your CPU utilization to above 50 percent, we will choose not to scale-in until the metric lowers enough that we think scaling in won't cause oscillation.

  For a scalable target with a larger capacity, adding or removing capacity causes less of a gap between the target value and the actual metric data points.
+ A target tracking scaling policy assumes that it should perform scale out when the specified metric is above the target value. You cannot use a target tracking scaling policy to scale out when the specified metric is below the target value.

## Multiple scaling policies
<a name="target-tracking-multiple-scaling-policies"></a>

You can have multiple target tracking scaling policies for a scalable target, provided that each of them uses a different metric. The intention of Application Auto Scaling is to always prioritize availability, so its behavior differs depending on whether the target tracking policies are ready for scale out or scale in. It will scale out the scalable target if any of the target tracking policies are ready for scale out, but will scale in only if all of the target tracking policies (with the scale-in portion enabled) are ready to scale in.

If multiple scaling policies instruct the scalable target to scale out or in at the same time, Application Auto Scaling scales based on the policy that provides the largest capacity for both scale in and scale out. This provides greater flexibility to cover multiple scenarios and ensures that there is always enough capacity to process your workloads.

You can disable the scale-in portion of a target tracking scaling policy to use a different method for scale in than you use for scale out. For example, you can use a step scaling policy for scale in while using a target tracking scaling policy for scale out.

We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again.

For workloads that are cyclical in nature, you also have the option to automate capacity changes on a schedule using scheduled scaling. For each scheduled action, a new minimum capacity value and a new maximum capacity value can be defined. These values form the boundaries of the scaling policy. The combination of scheduled scaling and target tracking scaling can help reduce the impact of a sharp increase in utilization levels, when capacity is needed immediately.

## Commonly used commands for scaling policy creation, management, and deletion
<a name="target-tracking-policy-commonly-used-commands"></a>

The commonly used commands for working with scaling policies include:
+ [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) to register AWS or custom resources as scalable targets (a resource that Application Auto Scaling can scale), and to suspend and resume scaling.
+ [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) to add or modify scaling policies for an existing scalable target.
+  [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) to return information about scaling activities in an AWS Region.
+ [describe-scaling-policies](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-policies.html) to return information about scaling policies in an AWS Region.
+ [delete-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scaling-policy.html) to delete a scaling-policy.

## Related resources
<a name="target-tracking-related-resources"></a>

For information about creating target tracking scaling policies for Auto Scaling groups, see [Target tracking scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Limitations
<a name="target-tracking-limitations"></a>

The following are limitations when using target tracking scaling policies:
+ The scalable target can't be an Amazon EMR cluster. Target tracking scaling policies are not supported for Amazon EMR.
+ When an Amazon MSK cluster is the scalable target, scale in is disabled and cannot be enabled.
+ You cannot use the `RegisterScalableTarget` or `PutScalingPolicy` API operations to update an AWS Auto Scaling scaling plan.
+ Console access to view, add, update, or remove target tracking scaling policies on scalable resources depends on the resource that you use. For more information, see [AWS services that you can use with Application Auto Scaling](integrated-services-list.md).
