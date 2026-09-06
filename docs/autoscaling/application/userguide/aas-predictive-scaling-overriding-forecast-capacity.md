---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-overriding-forecast-capacity.html
---

# Override forecast values using scheduled actions
<a name="aas-predictive-scaling-overriding-forecast-capacity"></a>

Sometimes, you might have additional information about your future application requirements that the forecast calculation is unable to take into account. For example, forecast calculations might underestimate the capacity needed for an upcoming marketing event. You can use scheduled actions to temporarily override the forecast during future time periods. The scheduled actions can run on a recurring basis, or at a specific date and time when there are one-time demand fluctuations.

For example, you can create a scheduled action with a higher minimum capacity than what is forecasted. At runtime, Application Auto Scaling updates the minimum capacity of your scalable target. Because predictive scaling optimizes for capacity, a scheduled action with a minimum capacity that is higher than the forecast values is honored. This prevents capacity from being less than expected. To stop overriding the forecast, use a second scheduled action to return the minimum capacity to its original setting.

The following procedure outlines the steps for overriding the forecast during future time periods.

**Topics**
+ [Step 1: (Optional) Analyze time series data](#analyzing-time-series-data)
+ [Step 2: Create two scheduled actions](#scheduling-capacity)

**Important**
This topic assumes that you are trying to override the forecast to scale to a higher capacity than what is forecasted. If you need to temporarily decrease capacity without interference from a predictive scaling policy, use *forecast only* mode instead. While in forecast only mode, predictive scaling will continue to generate forecasts, but it will not automatically increase capacity. You can then monitor resource utilization and manually decrease the size of your group as needed.

## Step 1: (Optional) Analyze time series data
<a name="analyzing-time-series-data"></a>

Start by analyzing the forecast time series data. This is an optional step, but it is helpful if you want to understand the details of the forecast.

1. **Retrieve the forecast**

   After the forecast is created, you can query for a specific time period in the forecast. The goal of the query is to get a complete view of the time series data for a specific time period.

   Your query can include up to two days of future forecast data. If you have been using predictive scaling for a while, you can also access your past forecast data. However, the maximum time duration between the start and end time is 30 days.

   To retrieve the forecast, use the [get-predictive-scaling-forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/get-predictive-scaling-forecast.html) command. The following example gets the predictive scaling forecast for the Amazon ECS service.

   ```
   aws application-autoscaling get-predictive-scaling-forecast --service-namespace {{ecs}} \
       --scalable-dimension {{ecs:service:DesiredCount}} \
       --resource-id {{1234567890abcdef0}}
       --policy-name {{predictive-scaling-policy}} \
       --start-time "{{2021-05-19T17:00:00Z}}" \
       --end-time "{{2021-05-19T23:00:00Z}}"
   ```

   The response includes two forecasts: `LoadForecast` and `CapacityForecast`. `LoadForecast` shows the hourly load forecast. `CapacityForecast` shows forecast values for the capacity that is needed on an hourly basis to handle the forecasted load while maintaining a specified `TargetValue`.

1. **Identify the target time period**

   Identify the hour or hours when the one-time demand fluctuation should take place. Remember that dates and times shown in the forecast are in UTC.

## Step 2: Create two scheduled actions
<a name="scheduling-capacity"></a>

Next, create two scheduled actions for a specific time period when your application will have a higher than forecasted load. For example, if you have a marketing event that will drive traffic to your site for a limited period of time, you can schedule a one-time action to update the minimum capacity when it starts. Then, schedule another action to return the minimum capacity to the original setting when the event ends.

**To create two scheduled actions for one-time events (AWS CLI)**
To create the scheduled actions, use the [ put-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scheduled-action.html) command.

The following example defines an schedule for Amazon EC2 Auto Scaling that maintains a minimum capacity of three instances on May 19 at 5:00 PM for eight hours. The following commands show how to implement this scenario.

The first [put-scheduled-update-group-action](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scheduled-update-group-action.html) command instructs Amazon EC2 Auto Scaling to update the minimum capacity of the specified Auto Scaling group at 5:00 PM UTC on May 19, 2021.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name {{my-event-start}} \
  --auto-scaling-group-name {{my-asg}} --start-time "{{2021-05-19T17:00:00Z}}" --minimum-capacity {{3}}
```

The second command instructs Amazon EC2 Auto Scaling to set the group's minimum capacity to one at 1:00 AM UTC on May 20, 2021.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name {{my-event-end}} \
  --auto-scaling-group-name {{my-asg}} --start-time "{{2021-05-20T01:00:00Z}}" --minimum-capacity {{1}}
```

After you add these scheduled actions to the Auto Scaling group, Amazon EC2 Auto Scaling does the following:
+ At 5:00 PM UTC on May 19, 2021, the first scheduled action runs. If the group currently has fewer than three instances, the group scales out to three instances. During this time and for the next eight hours, Amazon EC2 Auto Scaling can continue to scale out if the predicted capacity is higher than the actual capacity or if there is a dynamic scaling policy in effect.
+ At 1:00 AM UTC on May 20, 2021, the second scheduled action runs. This returns the minimum capacity to its original setting at the end of the event.

### Scaling based on recurring schedules
<a name="scheduling-recurring-actions"></a>

To override the forecast for the same time period every week, create two scheduled actions and provide the time and date logic using a cron expression.

The cron expression format consists of five fields separated by spaces: [Minute] [Hour] [Day\_of\_Month] [Month\_of\_Year] [Day\_of\_Week]. Fields can contain any allowed values, including special characters.

For example, the following cron expression runs the action every Tuesday at 6:30 AM. The asterisk is used as a wildcard to match all values for a field.

```
30 6 * * 2
```
