---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-policy-overview.html
---

# How predictive scaling works
<a name="predictive-scaling-policy-overview"></a>

This topic explains how predictive scaling works and describes what to consider when you create a predictive scaling policy.

**Topics**
+ [How it works](#how-predictive-scaling-works)
+ [Maximum capacity limit](#predictive-scaling-maximum-capacity-limit)
+ [Considerations](#predictive-scaling-considerations)
+ [Supported Regions](#predictive-scaling-regions)

## How it works
<a name="how-predictive-scaling-works"></a>

To use predictive scaling, create a predictive scaling policy that specifies the CloudWatch metric to monitor and analyze. For predictive scaling to start forecasting future values, this metric must have at least 24 hours of data.

After you create the policy, predictive scaling starts analyzing metric data from up to the past 14 days to identify patterns. It uses this analysis to generate an hourly forecast of capacity requirements for the next 48 hours. The forecast is updated every 6 hours using the latest CloudWatch data. As new data comes in, predictive scaling is able to continuously improve the accuracy of future forecasts.

When you first enable predictive scaling, it runs in *forecast only* mode. In this mode, it generates capacity forecasts but does not actually scale your Auto Scaling group based on those forecasts. This allows you to evaluate the accuracy and suitability of the forecast. You can view forecast data by using the `GetPredictiveScalingForecast` API operation or the AWS Management Console.

After you review the forecast data and decide to start scaling based on that data, switch the scaling policy to *forecast and scale* mode. In this mode:
+ If the forecast expects an increase in load, Amazon EC2 Auto Scaling will increase capacity by scaling out.
+ If the forecast expects a decrease in load, it will not scale in to remove capacity. If you want to remove capacity that is no longer needed, you must create dynamic scaling policies.

By default, Amazon EC2 Auto Scaling scales your Auto Scaling group at the start of each hour based on the forecast for that hour. You can optionally specify an earlier start time by using the `SchedulingBufferTime` property in the `PutScalingPolicy` API operation or the **Pre-launch instances** setting in the AWS Management Console. This causes Amazon EC2 Auto Scaling to launch new instances ahead of the forecasted demand, giving them time to boot and become ready to handle traffic.

To support launching new instances ahead of the forecasted demand, we strongly recommend that you enable the *default instance warmup* for your Auto Scaling group. This specifies a time period after a scale-out activity during which Amazon EC2 Auto Scaling won't scale in, even if dynamic scaling policies indicate capacity should be decreased. This helps you ensure that newly launched instances have adequate time to start serving the increased traffic before being considered for scale-in operations. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

## Maximum capacity limit
<a name="predictive-scaling-maximum-capacity-limit"></a>

Auto Scaling groups have a maximum capacity setting that limits the maximum number of EC2 instances that can be launched for the group. By default, when scaling policies are set, they cannot increase capacity higher than its maximum capacity.

Alternatively, you can allow the group's maximum capacity to be automatically increased if the forecast capacity approaches or exceeds the maximum capacity of the Auto Scaling group. To enable this behavior, use the `MaxCapacityBreachBehavior` and `MaxCapacityBuffer` properties in the `PutScalingPolicy` API operation or the **Max capacity behavior** setting in the AWS Management Console.

**Warning**
Use caution when allowing the maximum capacity to be automatically increased. This can lead to more instances being launched than intended if the increased maximum capacity is not monitored and managed. The increased maximum capacity then becomes the new normal maximum capacity for the Auto Scaling group until you manually update it. The maximum capacity does not automatically decrease back to the original maximum.

## Considerations
<a name="predictive-scaling-considerations"></a>
+ Confirm whether predictive scaling is suitable for your workload. A workload is a good fit for predictive scaling if it exhibits recurring load patterns that are specific to the day of the week or the time of day. To check this, configure predictive scaling policies in *forecast only* mode and then refer to the recommendations in the console. Amazon EC2 Auto Scaling provides recommendations based on observations about potential policy performance. Evaluate the forecast and the recommendations before letting predictive scaling actively scale your application.
+ Predictive scaling needs at least 24 hours of historical data to start forecasting. However, forecasts are more effective if historical data spans two full weeks. If you update your application by creating a new Auto Scaling group and deleting the old one, then your new Auto Scaling group needs 24 hours of historical load data before predictive scaling can start generating forecasts again. You can use custom metrics to aggregate metrics across old and new Auto Scaling groups. Otherwise, you might have to wait a few days for a more accurate forecast.
+ Choose a load metric that accurately represents the full load on your application and is the aspect of your application that's most important to scale on.
+ Using dynamic scaling with predictive scaling helps you follow the demand curve for your application closely, scaling in during periods of low traffic and scaling out when traffic is higher than expected. When multiple scaling policies are active, each policy determines the desired capacity independently, and the desired capacity is set to the maximum of those. For example, if 10 instances are required to stay at the target utilization in a target tracking scaling policy, and 8 instances are required to stay at the target utilization in a predictive scaling policy, then the group's desired capacity is set to 10. If you are new to dynamic scaling, we recommend using target tracking scaling policies. For more information, see [Dynamic scaling for Amazon EC2 Auto Scaling](as-scale-based-on-demand.md).
+ A core assumption of predictive scaling is that the Auto Scaling group is homogenous and all instances are of equal capacity. If this isn’t true for your group, forecasted capacity can be inaccurate. Therefore, use caution when creating predictive scaling policies for [mixed instances groups](ec2-auto-scaling-mixed-instances-groups.md) because instances of different types can be provisioned that are of unequal capacity. Following are some examples where the forecasted capacity will be inaccurate:
  + Your predictive scaling policy is based on CPU utilization, but the number of vCPUs on each Auto Scaling instance varies between instance types.
  + Your predictive scaling policy is based on network in or network out, but the network bandwidth throughput for each Auto Scaling instance varies between instance types. For example, the M5 and M5n instance types are similar, but the M5n instance type delivers significantly higher network throughput.

## Supported Regions
<a name="predictive-scaling-regions"></a>
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Canada West (Calgary)
+ China (Beijing)
+ China (Ningxia)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Milan)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Stockholm)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Middle East (Bahrain)
+ Middle East (UAE)
+ South America (São Paulo)
+ AWS GovCloud (US-East)
+ AWS GovCloud (US-West)
