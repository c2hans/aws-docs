---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-create-policy.html
---

# Create a predictive scaling policy for an Auto Scaling group
<a name="predictive-scaling-create-policy"></a>

The following procedures help you create a predictive scaling policy using the AWS Management Console or AWS CLI.

If the Auto Scaling group is new, it must provide at least 24 hours of data before Amazon EC2 Auto Scaling can generate a forecast for it.

**Topics**
+ [Create a predictive scaling policy (console)](#predictive-scaling-policy-console)
+ [Create a predictive scaling policy (AWS CLI)](#predictive-scaling-policy-aws-cli)

## Create a predictive scaling policy (console)
<a name="predictive-scaling-policy-console"></a>

If this is your first time creating a predictive scaling policy, we recommend using the console to create multiple predictive scaling policies in *forecast only* mode. This allows you to test the potential effects of different metrics and target values. You can create multiple predictive scaling policies for each Auto Scaling group, but only one of the policies can be used for active scaling.

### Create a predictive scaling policy in the console (predefined metrics)
<a name="create-a-predictive-scaling-policy-in-the-console"></a>

Use the following procedure to create a predictive scaling policy using predefined metrics (CPU, network I/O, or Application Load Balancer request count per target). The easiest way to create a predictive scaling policy is to use predefined metrics. If you prefer to use custom metrics instead, see [Create a predictive scaling policy in the console (custom metrics)](#create-a-predictive-scaling-policy-in-the-console-custom-metrics).

**To create a predictive scaling policy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up at the bottom of the page.

1. On the **Automatic scaling** tab, in **Scaling policies**, choose **Create predictive scaling policy**.

1. Enter a name for the policy.

1. Turn on **Scale based on forecast** to give Amazon EC2 Auto Scaling permission to start scaling right away.

   To keep the policy in *forecast only* mode, keep **Scale based on forecast** turned off.

1. For **Metrics**, choose your metrics from the list of options. Options include **CPU**, **Network In**, **Network Out**, **Application Load Balancer request count**, and **Custom metric pair**.

   If you chose **Application Load Balancer request count per target**, then choose a target group in **Target group**. **Application Load Balancer request count per target** is only supported if you have attached an Application Load Balancer target group to your Auto Scaling group.

   If you chose **Custom metric pair**, choose individual metrics from the drop-down lists for **Load metric** and **Scaling metric**.

1. For **Target utilization**, enter the target value that Amazon EC2 Auto Scaling should maintain. Amazon EC2 Auto Scaling scales out your capacity until the average utilization is at the target utilization, or until it reaches the maximum number of instances you specified.

<table>
<thead>
  <tr><th>If your scaling metric is...</th><th>Then the target utilization represents...</th></tr>
</thead>
<tbody>
  <tr><td>CPU</td><td>The percentage of CPU that each instance should ideally use.</td></tr>
  <tr><td>Network In</td><td>The average number of bytes per minute that each instance should ideally receive.</td></tr>
  <tr><td>Network Out</td><td>The average number of bytes per minute that each instance should ideally send out. </td></tr>
  <tr><td>Application Load Balancer request count per target</td><td>The average number of requests per minute that each instance should ideally receive.</td></tr>
</tbody>
</table>

1. (Optional) For **Pre-launch instances**, choose how far in advance you want your instances launched before the forecast calls for the load to increase.

1. (Optional) For **Max capacity behavior**, choose whether to let Amazon EC2 Auto Scaling scale out higher than the group's maximum capacity when predicted capacity exceeds the defined maximum. Turning on this setting lets scale out occur during periods when your traffic is forecasted to be at its highest.

1. (Optional) For **Buffer maximum capacity above the forecasted capacity**, choose how much additional capacity to use when the predicted capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the predicted capacity. For example, if the buffer is 10, this means a 10 percent buffer. Therefore, if the predicted capacity is 50 and the maximum capacity is 40, the effective maximum capacity is 55.

   If set to 0, Amazon EC2 Auto Scaling might scale capacity higher than the maximum capacity to equal but not exceed predicted capacity.

1. Choose **Create predictive scaling policy**.

### Create a predictive scaling policy in the console (custom metrics)
<a name="create-a-predictive-scaling-policy-in-the-console-custom-metrics"></a>

Use the following procedure to create a predictive scaling policy using custom metrics. Custom metrics can include other metrics provided by CloudWatch or metrics that you publish to CloudWatch. To use CPU, network I/O, or Application Load Balancer request count per target, see [Create a predictive scaling policy in the console (predefined metrics)](#create-a-predictive-scaling-policy-in-the-console).

To create a predictive scaling policy using custom metrics, you must do the following:
+ You must provide the raw queries that let Amazon EC2 Auto Scaling interact with the metrics in CloudWatch. For more information, see [Advanced predictive scaling policy using custom metrics](predictive-scaling-customized-metric-specification.md). To be sure that Amazon EC2 Auto Scaling can extract the metric data from CloudWatch, confirm that each query is returning data points. Confirm this by using the CloudWatch console or the CloudWatch [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) API operation.
**Note**
We provide sample JSON payloads in the JSON editor in the Amazon EC2 Auto Scaling console. These examples give you a reference for the key-value pairs that are required to add other CloudWatch metrics provided by AWS or metrics that you previously published to CloudWatch. You can use them as a starting point, then customize them for your needs.
+ If you use any metric math, you must manually construct the JSON to fit your unique scenario. For more information, see [Use metric math expressions](using-math-expression-examples.md). Before using metric math in your policy, confirm that metric queries based on metric math expressions are valid and return a single time series. Confirm this by using the CloudWatch console or the CloudWatch [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) API operation.

If you make an error in a query by providing incorrect data, such as the wrong Auto Scaling group name, the forecast won't have any data. For troubleshooting custom metric issues, see [Considerations for custom metrics in a predictive scaling policy](custom-metrics-troubleshooting.md).

**To create a predictive scaling policy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up at the bottom of the page.

1. On the **Automatic scaling** tab, in **Scaling policies**, choose **Create predictive scaling policy**.

1. Enter a name for the policy.

1. Turn on **Scale based on forecast** to give Amazon EC2 Auto Scaling permission to start scaling right away.

   To keep the policy in *forecast only* mode, keep **Scale based on forecast** turned off.

1. For **Metrics**, choose **Custom metric pair**.

   1. For **Load metric**, choose **Custom CloudWatch metric** to use a custom metric. Construct the JSON payload that contains the load metric definition for the policy and paste it into the JSON editor box, replacing what is already in the box.

   1. For **Scaling metric**, choose **Custom CloudWatch metric** to use a custom metric. Construct the JSON payload that contains the scaling metric definition for the policy and paste it into the JSON editor box, replacing what is already in the box.

   1. (Optional) To add a custom capacity metric, select the check box for **Add custom capacity metric**. Construct the JSON payload that contains the capacity metric definition for the policy and paste it into the JSON editor box, replacing what is already in the box.

      You only need to enable this option to create a new time series for capacity if your capacity metric data spans multiple Auto Scaling groups. In this case, you must use metric math to aggregate the data into a single time series.

1. For **Target utilization**, enter the target value that Amazon EC2 Auto Scaling should maintain. Amazon EC2 Auto Scaling scales out your capacity until the average utilization is at the target utilization, or until it reaches the maximum number of instances you specified.

1. (Optional) For **Pre-launch instances**, choose how far in advance you want your instances launched before the forecast calls for the load to increase.

1. (Optional) For **Max capacity behavior**, choose whether to let Amazon EC2 Auto Scaling scale out higher than the group's maximum capacity when predicted capacity exceeds the defined maximum. Turning on this setting lets scale out occur during periods when your traffic is forecasted to be at its highest.

1. (Optional) For **Buffer maximum capacity above the forecasted capacity**, choose how much additional capacity to use when the predicted capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the predicted capacity. For example, if the buffer is 10, this means a 10 percent buffer. Therefore, if the predicted capacity is 50 and the maximum capacity is 40, the effective maximum capacity is 55.

   If set to 0, Amazon EC2 Auto Scaling might scale capacity higher than the maximum capacity to equal but not exceed predicted capacity.

1. Choose **Create predictive scaling policy**.

## Create a predictive scaling policy (AWS CLI)
<a name="predictive-scaling-policy-aws-cli"></a>

Use the AWS CLI as follows to configure predictive scaling policies for your Auto Scaling group. Replace each {{user input placeholder}} with your own information.

For more information about the CloudWatch metrics you can specify, see [PredictiveScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingMetricSpecification.html) in the *Amazon EC2 Auto Scaling API Reference*.

### Example 1: A predictive scaling policy that creates forecasts but doesn't scale
<a name="predictive-scaling-configuration-ex1"></a>

The following example policy shows a complete policy configuration that uses CPU utilization metrics for predictive scaling with a target utilization of `40`. `ForecastOnly` mode is used by default, unless you explicitly specify which mode to use. Save this configuration in a file named `config.json`.

```
{
    "MetricSpecifications": [
        {
            "TargetValue": {{40}},
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "{{ASGCPUUtilization}}"
            }
        }
    ]
}
```

To create the policy from the command line, run the [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html) command with the configuration file specified, as demonstrated in the following example.

```
aws autoscaling put-scaling-policy --policy-name {{cpu40-predictive-scaling-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://config.json}}
```

If successful, this command returns the policy's Amazon Resource Name (ARN).

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/cpu40-predictive-scaling-policy",
  "Alarms": []
}
```

### Example 2: A predictive scaling policy that forecasts and scales
<a name="predictive-scaling-configuration-ex2"></a>

For a policy that allows Amazon EC2 Auto Scaling to forecast and scale, add the property `Mode` with a value of `ForecastAndScale`. The following example shows a policy configuration that uses Application Load Balancer request count metrics. The target utilization is `1000`, and predictive scaling is set to `ForecastAndScale` mode.

```
{
    "MetricSpecifications": [
        {
            "TargetValue": {{1000}},
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "{{ALBRequestCount}}",
                "ResourceLabel": "{{app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff}}"
            }
        }
    ],
    "Mode": "ForecastAndScale"
}
```

To create this policy, run the [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html) command with the configuration file specified, as demonstrated in the following example.

```
aws autoscaling put-scaling-policy --policy-name {{alb1000-predictive-scaling-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://config.json}}
```

If successful, this command returns the policy's Amazon Resource Name (ARN).

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:19556d63-7914-4997-8c81-d27ca5241386:autoScalingGroupName/my-asg:policyName/alb1000-predictive-scaling-policy",
  "Alarms": []
}
```

### Example 3: A predictive scaling policy that can scale higher than maximum capacity
<a name="predictive-scaling-configuration-ex3"></a>

The following example shows how to create a policy that can scale higher than the group's maximum size limit when you need it to handle a higher than normal load. By default, Amazon EC2 Auto Scaling doesn't scale your EC2 capacity higher than your defined maximum capacity. However, it might be helpful to let it scale higher with slightly more capacity to avoid performance or availability issues.

To provide room for Amazon EC2 Auto Scaling to provision additional capacity when the capacity is predicted to be at or very close to your group's maximum size, specify the `MaxCapacityBreachBehavior` and `MaxCapacityBuffer` properties, as shown in the following example. You must specify `MaxCapacityBreachBehavior` with a value of `IncreaseMaxCapacity`. The maximum number of instances that your group can have depends on the value of `MaxCapacityBuffer`.

```
{
    "MetricSpecifications": [
        {
            "TargetValue": {{70}},
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "{{ASGCPUUtilization}}"
            }
        }
    ],
    "MaxCapacityBreachBehavior": "{{IncreaseMaxCapacity}}",
    "MaxCapacityBuffer": {{10}}
}
```

In this example, the policy is configured to use a 10 percent buffer (`"MaxCapacityBuffer": 10`), so if the predicted capacity is 50 and the maximum capacity is 40, then the effective maximum capacity is 55. A policy that can scale capacity higher than the maximum capacity to equal but not exceed predicted capacity would have a buffer of 0 (`"MaxCapacityBuffer": 0`).

To create this policy, run the [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html) command with the configuration file specified, as demonstrated in the following example.

```
aws autoscaling put-scaling-policy --policy-name {{cpu70-predictive-scaling-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://config.json}}
```

If successful, this command returns the policy's Amazon Resource Name (ARN).

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:d02ef525-8651-4314-bf14-888331ebd04f:autoScalingGroupName/my-asg:policyName/cpu70-predictive-scaling-policy",
  "Alarms": []
}
```
