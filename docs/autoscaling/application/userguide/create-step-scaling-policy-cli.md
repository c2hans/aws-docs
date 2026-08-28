---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/create-step-scaling-policy-cli.html
---

# Create a step scaling policy for Application Auto Scaling using the AWS CLI
<a name="create-step-scaling-policy-cli"></a>

This example uses AWS CLI commands to create a step scaling policy for an Amazon ECS service. For a different scalable target, specify its namespace in `--service-namespace`, its scalable dimension in `--scalable-dimension`, and its resource ID in `--resource-id`.

When using the AWS CLI, remember that your commands run in the AWS Region configured for your profile. If you want to run the commands in a different Region, either change the default Region for your profile, or use the `--region` parameter with the command.

**Topics**
+ [Step 1: Register a scalable target](#step-scaling-register-scalable-target)
+ [Step 2: Create a step scaling policy](#create-step-scaling-policy)
+ [Step 3: Create an alarm that invokes a scaling policy](#step-scaling-create-alarm)

## Step 1: Register a scalable target
<a name="step-scaling-register-scalable-target"></a>

If you haven't already done so, register the scalable target. Use the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command to register a specific resource in the target service as a scalable target. The following example registers an Amazon ECS service with Application Auto Scaling. Application Auto Scaling can scale the number of tasks at a minimum of 2 tasks and a maximum of 10. Replace each {{user input placeholder}} with your own information.

**Linux, macOS, or Unix**

```
aws application-autoscaling register-scalable-target --service-namespace {{ecs}} \
  --scalable-dimension {{ecs:service:DesiredCount}} \
  --resource-id {{service/my-cluster/my-service}} \
  --min-capacity {{2}} --max-capacity {{10}}
```

**Windows**

```
aws application-autoscaling register-scalable-target --service-namespace {{ecs}} ^
  --scalable-dimension {{ecs:service:DesiredCount}} ^
  --resource-id {{service/my-cluster/my-service}} ^
  --min-capacity {{2}} --max-capacity {{10}}
```

**Output**
If successful, this command returns the ARN of the scalable target. The following is example output.

```
{
    "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
}
```

## Step 2: Create a step scaling policy
<a name="create-step-scaling-policy"></a>

To create a step scaling policy for your scalable target, you can use the following examples to help you get started.

------
#### [ Scale out ]

**To create a step scaling policy for scale out (increase capacity)**

1. Use the following `cat` command to store a step scaling policy configuration in a JSON file named `config.json` in your home directory. The following is an example configuration with an adjustment type of `PercentChangeInCapacity` that increases the capacity of the scalable target based on the following step adjustments (assuming a CloudWatch alarm threshold of 70):
   + Increase capacity by 10 percent when the value of the metric is greater than or equal to 70 but less than 85
   + Increase capacity by 20 percent when the value of the metric is greater than or equal to 85 but less than 95
   + Increase capacity by 30 percent when the value of the metric is greater than or equal to 95

   ```
   $ cat ~/config.json
   {
     "AdjustmentType": "PercentChangeInCapacity",
     "MetricAggregationType": "Average",
     "Cooldown": {{60}},
     "MinAdjustmentMagnitude": {{1}},
     "StepAdjustments": [
       {
         "MetricIntervalLowerBound": {{0.0}},
         "MetricIntervalUpperBound": {{15.0}},
         "ScalingAdjustment": {{10}}
       },
       {
         "MetricIntervalLowerBound": {{15.0}},
         "MetricIntervalUpperBound": {{25.0}},
         "ScalingAdjustment": {{20}}
       },
       {
         "MetricIntervalLowerBound": {{25.0}},
         "ScalingAdjustment": {{30}}
       }
     ]
   }
   ```

   For more information, see [StepScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html) in the *Application Auto Scaling API Reference*.

1. Use the following [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command, along with the `config.json` file that you created, to create a scaling policy named `my-step-scaling-policy`.

   **Linux, macOS, or Unix**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ecs}} \
     --scalable-dimension {{ecs:service:DesiredCount}} \
     --resource-id {{service/my-cluster/my-service}} \
     --policy-name {{my-step-scaling-policy}} --policy-type StepScaling \
     --step-scaling-policy-configuration {{file://config.json}}
   ```

   **Windows**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ecs}} ^
     --scalable-dimension {{ecs:service:DesiredCount}} ^
     --resource-id {{service/my-cluster/my-service}} ^
     --policy-name {{my-step-scaling-policy}} --policy-type StepScaling ^
     --step-scaling-policy-configuration {{file://config.json}}
   ```

**Output**
The output includes the ARN that serves as a unique name for the policy. You need it to create a CloudWatch alarm for your policy. The following is example output.

   ```
   {
       "PolicyARN": "arn:aws:autoscaling:{{region}}:{{123456789012}}:scalingPolicy:{{ac542982-cbeb-4294-891c-a5a941dfa787}}:resource/{{ecs/service/my-cluster/my-service}}:policyName/{{my-step-scaling-policy"}}
   }
   ```

------
#### [ Scale in ]

**To create a step scaling policy for scale in (decrease capacity)**

1. Use the following `cat` command to store a step scaling policy configuration in a JSON file named `config.json` in your home directory. The following is an example configuration with an adjustment type of `ChangeInCapacity` that decreases the capacity of the scalable target based on the following step adjustments (assuming a CloudWatch alarm threshold of 50):
   + Decrease capacity by 1 when the value of the metric is less than or equal to 50 but greater than 40
   + Decrease capacity by 2 when the value of the metric is less than or equal to 40 but greater than 30
   + Decrease capacity by 3 when the value of the metric is less than or equal to 30

   ```
   $ cat ~/config.json
   {
     "AdjustmentType": "ChangeInCapacity",
     "MetricAggregationType": "Average",
     "Cooldown": {{60}},
     "StepAdjustments": [
       {
         "MetricIntervalUpperBound": {{0.0}},
         "MetricIntervalLowerBound": {{-10.0}},
         "ScalingAdjustment": {{-1}}
       },
       {
         "MetricIntervalUpperBound": {{-10.0}},
         "MetricIntervalLowerBound": {{-20.0}},
         "ScalingAdjustment": {{-2}}
       },
       {
         "MetricIntervalUpperBound": {{-20.0}},
         "ScalingAdjustment": {{-3}}
       }
     ]
   }
   ```

   For more information, see [StepScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html) in the *Application Auto Scaling API Reference*.

1. Use the following [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command, along with the `config.json` file that you created, to create a scaling policy named `my-step-scaling-policy`.

   **Linux, macOS, or Unix**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ecs}} \
     --scalable-dimension {{ecs:service:DesiredCount}} \
     --resource-id {{service/my-cluster/my-service}} \
     --policy-name {{my-step-scaling-policy}} --policy-type StepScaling \
     --step-scaling-policy-configuration {{file://config.json}}
   ```

   **Windows**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ecs}} ^
     --scalable-dimension {{ecs:service:DesiredCount}} ^
     --resource-id {{service/my-cluster/my-service}} ^
     --policy-name {{my-step-scaling-policy}} --policy-type StepScaling ^
     --step-scaling-policy-configuration {{file://config.json}}
   ```

**Output**
The output includes the ARN that serves as a unique name for the policy. You need this ARN to create a CloudWatch alarm for your policy. The following is example output.

   ```
   {
       "PolicyARN": "arn:aws:autoscaling:{{region}}:{{123456789012}}:scalingPolicy:{{ac542982-cbeb-4294-891c-a5a941dfa787}}:resource/{{ecs/service/my-cluster/my-service}}:policyName/{{my-step-scaling-policy"}}
   }
   ```

------

## Step 3: Create an alarm that invokes a scaling policy
<a name="step-scaling-create-alarm"></a>

Finally, use the following CloudWatch [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command to create an alarm to use with your step scaling policy. In this example, you have an alarm based on average CPU utilization. The alarm is configured to be in an ALARM state if it reaches a threshold of 70 percent for at least two consecutive evaluation periods of 60 seconds. To specify a different CloudWatch metric or use your own custom metric, specify its name in `--metric-name` and its namespace in `--namespace`.

**Linux, macOS, or Unix**

```
aws cloudwatch put-metric-alarm --alarm-name {{Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service}} \
  --metric-name {{CPUUtilization}} --namespace {{AWS/ECS}} --statistic Average \
  --period {{60}} --evaluation-periods {{2}} --threshold {{70}} \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --dimensions Name=ClusterName,Value={{default}} Name=ServiceName,Value={{sample-app-service}} \
  --alarm-actions {{PolicyARN}}
```

**Windows**

```
aws cloudwatch put-metric-alarm --alarm-name {{Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service}} ^
  --metric-name {{CPUUtilization}} --namespace {{AWS/ECS}} --statistic Average ^
  --period {{60}} --evaluation-periods {{2}} --threshold {{70}} ^
  --comparison-operator GreaterThanOrEqualToThreshold ^
  --dimensions Name=ClusterName,Value={{default}} Name=ServiceName,Value={{sample-app-service}} ^
  --alarm-actions {{PolicyARN}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
