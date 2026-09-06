---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/create-target-tracking-policy-cli.html
---

# Create a target tracking scaling policy for Application Auto Scaling using the AWS CLI
<a name="create-target-tracking-policy-cli"></a>

This example uses AWS CLI commands to create a target racking policy for an Amazon EC2 Spot Fleet. For a different scalable target, specify its namespace in `--service-namespace`, its scalable dimension in `--scalable-dimension`, and its resource ID in `--resource-id`.

When using the AWS CLI, remember that your commands run in the AWS Region configured for your profile. If you want to run the commands in a different Region, either change the default Region for your profile, or use the `--region` parameter with the command.

**Topics**
+ [Step 1: Register a scalable target](#target-tracking-register-scalable-target)
+ [Step 2: Create a target tracking scaling policy](#create-target-tracking-policy)
+ [Step 3: Describe target tracking scaling policies](#describe-target-tracking-policy)

## Step 1: Register a scalable target
<a name="target-tracking-register-scalable-target"></a>

If you haven't already done so, register the scalable target. Use the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command to register a specific resource in the target service as a scalable target. The following example registers a Spot Fleet request with Application Auto Scaling. Application Auto Scaling can scale the number of instances in the Spot Fleet at a minimum of 2 instances and a maximum of 10. Replace each {{user input placeholder}} with your own information.

**Linux, macOS, or Unix**

```
aws application-autoscaling register-scalable-target --service-namespace {{ec2}} \
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} \
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
  --min-capacity {{2}} --max-capacity {{10}}
```

**Windows**

```
aws application-autoscaling register-scalable-target --service-namespace {{ec2}} ^
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} ^
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} ^
  --min-capacity {{2}} --max-capacity {{10}}
```

**Output**
If successful, this command returns the ARN of the scalable target. The following is example output.

```
{
    "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
}
```

## Step 2: Create a target tracking scaling policy
<a name="create-target-tracking-policy"></a>

To create a target tracking scaling policy, you can use the following examples to help you get started.

**To create a target tracking scaling policy**

1. Use the following `cat` command to store a target value for your scaling policy and a predefined metric specification in a JSON file named `config.json` in your home directory. The following is an example target tracking configuration that keeps the average CPU utilization at 50 percent.

   ```
   $ cat ~/config.json
   {
     "TargetValue": {{50.0}},
     "PredefinedMetricSpecification":
       {
         "PredefinedMetricType": "{{EC2SpotFleetRequestAverageCPUUtilization}}"
       }
   }
   ```

   For more information, see [PredefinedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html) in the *Application Auto Scaling API Reference*.

   Alternatively, you can use a custom metric for scaling by creating a customized metric specification and adding values for each parameter from CloudWatch. The following is an example target tracking configuration that keeps the average utilization of the specified metric at 100.

   ```
   $ cat ~/config.json
   {
      "TargetValue": {{100.0}},
      "CustomizedMetricSpecification":{
         "MetricName": "{{MyUtilizationMetric}}",
         "Namespace": "{{MyNamespace}}",
         "Dimensions": [
            {
               "Name": "{{MyOptionalMetricDimensionName}}",
               "Value": "{{MyOptionalMetricDimensionValue}}"
            }
         ],
         "Statistic": "{{Average}}",
         "Unit": "{{Percent}}"
      }
   }
   ```

   For more information, see [CustomizedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CustomizedMetricSpecification.html) in the *Application Auto Scaling API Reference*.

1. Use the following [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command, along with the `config.json` file you created, to create a scaling policy named `cpu50-target-tracking-scaling-policy`.

   **Linux, macOS, or Unix**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ec2}} \
     --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} \
     --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
     --policy-name {{cpu50-target-tracking-scaling-policy}} --policy-type TargetTrackingScaling \
     --target-tracking-scaling-policy-configuration {{file://config.json}}
   ```

   **Windows**

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{ec2}} ^
     --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} ^
     --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} ^
     --policy-name {{cpu50-target-tracking-scaling-policy}} --policy-type TargetTrackingScaling ^
     --target-tracking-scaling-policy-configuration {{file://config.json}}
   ```

**Output**
If successful, this command returns the ARNs and names of the two CloudWatch alarms created on your behalf. The following is example output.

   ```
   {
       "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:policy-id:resource/ec2/spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE:policyName/cpu50-target-tracking-scaling-policy",
       "Alarms": [
           {
               "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
               "AlarmName": "TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
           },
           {
               "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
               "AlarmName": "TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
           }
       ]
   }
   ```

## Step 3: Describe target tracking scaling policies
<a name="describe-target-tracking-policy"></a>

You can describe all scaling policies for the specified service namespace using the following [describe-scaling-policies](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-policies.html) command.

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ec2}}
```

You can filter the results to just the target tracking scaling policies using the `--query` parameter. For more information about the syntax for `query`, see [Controlling command output from the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html) in the *AWS Command Line Interface User Guide*.

**Linux, macOS, or Unix**

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ec2}} \
  --query 'ScalingPolicies[?PolicyType==`TargetTrackingScaling`]'
```

**Windows**

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ec2}} ^
  --query "ScalingPolicies[?PolicyType==`TargetTrackingScaling`]"
```

**Output**
The following is example output.

```
[
    {
        "PolicyARN": "PolicyARN",
        "TargetTrackingScalingPolicyConfiguration": {
            "PredefinedMetricSpecification": {
                "PredefinedMetricType": "EC2SpotFleetRequestAverageCPUUtilization"
            },
            "TargetValue": 50.0
        },
        "PolicyName": "cpu50-target-tracking-scaling-policy",
        "ScalableDimension": "ec2:spot-fleet-request:TargetCapacity",
        "ServiceNamespace": "ec2",
        "PolicyType": "TargetTrackingScaling",
        "ResourceId": "spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
        "Alarms": [
            {
                "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
                "AlarmName": "TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
            },
            {
                "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
                "AlarmName": "TargetTracking-spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
            }
        ],
        "CreationTime": 1515021724.807
    }
]
```
