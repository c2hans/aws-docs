---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-how-it-works.html
---

# How Application Auto Scaling predictive scaling works
<a name="aas-predictive-scaling-how-it-works"></a>

To use predictive scaling, create a predictive scaling policy that specifies the CloudWatch metric to monitor and analyze. You can use a predefined metric or a custom metric. For predictive scaling to start forecasting future values, this metric must have at least 24 hours of data.

After you create the policy, predictive scaling starts analyzing metric data from up to the past 14 days to identify patterns. It uses this analysis to generate an hourly forecast of capacity requirements for the next 48 hours. The forecast is updated every 6 hours using the latest CloudWatch data. As new data comes in, predictive scaling is able to continuously improve the accuracy of future forecasts.

You can first enable predictive scaling in *forecast only* mode. In this mode, it generates capacity forecasts but does not actually scale your capacity based on those forecasts. This allows you to evaluate the accuracy and suitability of the forecast.

After you review the forecast data and decide to start scaling based on that data, switch the scaling policy to forecast and scale mode. In this mode:
+ If the forecast expects an increase in load, predictive scaling will increase the capacity.
+ If the forecast expects a decrease in load, predictive scaling will not scale in to remove capacity. This ensures that you scale-in only when the demand actually drops, and not just on predictions. To remove capacity that is no longer needed, you must create a Target Tracking or Step Scaling policy because they respond to real time metric data.

By default, predictive scaling scales your scalable targets at the start of each hour based on the forecast for that hour. You can optionally specify an earlier start time by using the `SchedulingBufferTime` property in the `PutScalingPolicy` API operation. This allows you to launch predicted capacity ahead of the forecasted demand, which gives the new capacity adequate time to become ready to handle traffic.

## Maximum capacity limit
<a name="aas-ps-max-capcity-limit"></a>

By default, when scaling policies are set, they cannot increase capacity higher than its maximum capacity.

Alternatively, you can allow the scalable target's maximum capacity to be automatically increased if the forecast capacity approaches or exceeds the maximum capacity of the scalable target. To enable this behavior, use the `MaxCapacityBreachBehavior` and `MaxCapacityBuffer` properties in the `PutScalingPolicy` API operation or the **Max capacity behavior** setting in the AWS Management Console.

**Warning**
Use caution when allowing the maximum capacity to be automatically increased. The maximum capacity does not automatically decrease back to the original maximum.

## Commonly used commands for scaling policy creation, management, and deletion
<a name="aas-ps-common-commands"></a>

The commonly used commands for working with predictive scaling policies include:
+ `register-scalable-target` to register AWS or custom resources as scalable targets, to suspend scaling, and to resume scaling.
+ `put-scaling-policy` to create a predictive scaling policy.
+ `get-predictive-scaling-forecast` to retrieve the forecast data for a predictive scaling policy.
+ `describe-scaling-activities` to return information about scaling activities in an AWS Region.
+ `describe-scaling-policies` to return information about scaling policies in an AWS Region.
+ `delete-scaling-policy` to delete a scaling policy.

**Custom metrics**
Custom metrics can be used to predict the capacity needed for an application. Custom metrics are useful when predefined metrics are not enough to capture the load on your application.

## Considerations
<a name="aas-ps-considerations"></a>

The following considerations apply when working with predictive scaling.
+ Confirm whether predictive scaling is suitable for your application. An application is a good fit for predictive scaling if it exhibits recurring load patterns that are specific to the day of the week or the time of day. Evaluate the forecast before letting predictive scaling actively scale your application.
+ Predictive scaling needs at least 24 hours of historical data to start forecasting. However, forecasts are more effective if historical data spans two full weeks.
+ Choose a load metric that accurately represents the full load on your application and is the aspect of your application that's most important to scale on.
