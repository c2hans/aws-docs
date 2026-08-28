---
source_url: https://docs.aws.amazon.com/autoscaling/plans/userguide/migrate-scaling-plan.html
---

# Migrate your scaling plan
<a name="migrate-scaling-plan"></a>

You can migrate from a scaling plan to Amazon EC2 Auto Scaling and Application Auto Scaling scaling policies.

**Topics**
+ [Step 1: Review your existing setup](#review-your-existing-setup)
+ [Step 2: Create predictive scaling policies](#migrate-predictive-scaling-configurations)
+ [Step 3: Review the forecasts that the predictive scaling policies generate](#review-predictive-scaling-policy-forecast)
+ [Step 4: Prepare to delete the scaling plan](#prepare-to-delete-the-scaling-plan)
+ [Step 5: Delete the scaling plan](#delete-scaling-plan)
+ [Step 6: Reactivate dynamic scaling](#create-target-tracking-scaling-policies)
+ [Step 7: Reactivate predictive scaling](#switch-predictive-scaling-to-forecast-and-scale)
+ [Amazon EC2 Auto Scaling reference for migrating target tracking scaling policies](#target-tracking-mapping-reference-ec2-auto-scaling)
+ [Application Auto Scaling reference for migrating target tracking scaling policies](#target-tracking-mapping-reference-application-auto-scaling)
+ [Additional information](#migrate-scaling-plan-more-info)

**Important**
To migrate a scaling plan, you must complete multiple steps in exact order. While you migrate your scaling plan, *don't update it*, as that breaks the order of operations and could cause undesirable behavior.

## Step 1: Review your existing setup
<a name="review-your-existing-setup"></a>

To determine which scaling settings you must move over, use the [describe-scaling-plans](https://docs.aws.amazon.com/cli/latest/reference/autoscaling-plans/describe-scaling-plans.html) command.

```
aws autoscaling-plans describe-scaling-plans \
  --scaling-plan-names {{my-scaling-plan}}
```

Make a note of items that you want to preserve from the existing scaling plan, which can include the following:
+ **`MinCapacity`** – The minimum capacity of the scalable resource.
+ **`MaxCapacity`** – The maximum capacity of the scalable resource.
+ **`PredefinedLoadMetricType`** – A load metric for predictive scaling.
+ **`PredefinedScalingMetricType`** – A scaling metric for target tracking (dynamic) scaling and predictive scaling.
+ **`TargetValue`** – The target value for the scaling metric.

### Differences between scaling plans and scaling policies
<a name="differences"></a>

There are a few important differences between scaling plans and scaling policies:
+ A scaling policy can enable only one type of scaling: either target tracking scaling or predictive scaling. To use both scaling methods, you must create separate policies.
+ Likewise, you must define the scaling metric for predictive scaling and the scaling metric for target tracking scaling separately within their respective policies.

## Step 2: Create predictive scaling policies
<a name="migrate-predictive-scaling-configurations"></a>

If you don't use predictive scaling, then skip ahead to [Step 4: Prepare to delete the scaling plan](#prepare-to-delete-the-scaling-plan).

To provide time to evaluate the forecast, we recommend that you create predictive scaling policies before other scaling policies.

For any Auto Scaling groups with an existing load metric specification, do the following to turn it into an Amazon EC2 Auto Scaling-based predictive scaling policy.

**To create predictive scaling policies**

1. In a JSON file, define a `MetricSpecifications` structure as shown in the following example:

   ```
   {
     "MetricSpecifications":[
       {{{
         ... }}
       }
     ]
   }
   ```

1. In the `MetricSpecifications` structure, for each load metric in your scaling plan, create a `PredefinedLoadMetricSpecification` or `CustomizedLoadMetricSpecification` using the equivalent settings from the scaling plan.

   The following are examples of the structure of the load metric section.

------
#### [ With predefined metrics ]

   ```
   {
     "MetricSpecifications":[
       {{{
         "PredefinedLoadMetricSpecification":{
           "PredefinedMetricType":"ASGTotalCPUUtilization"
         },
         ...}}
       }
     ]
   }
   ```

   For more information, see [PredictiveScalingPredefinedLoadMetric](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingPredefinedLoadMetric.html) in the *Amazon EC2 Auto Scaling API Reference*.

------
#### [ With custom metrics ]

   ```
   {
     "MetricSpecifications":[
       {{{
         "CustomizedLoadMetricSpecification":{
           "MetricDataQueries":[
             {
               "Id":"load_metric",
               "MetricStat":{
                 "Metric":{
                   "MetricName":"MyLoadMetric",
                   "Namespace":"MyNameSpace",
                   "Dimensions":[
                     {
                       "Name":"MyOptionalMetricDimensionName",
                       "Value":"MyOptionalMetricDimensionValue"
                     }
                   ]
                 },
                 "Stat":"Sum"
               }
             }
           ]
         },
         ...}}
       }
     ]
   }
   ```

   For more information, see [PredictiveScalingCustomizedLoadMetric](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingCustomizedLoadMetric.html) in the *Amazon EC2 Auto Scaling API Reference*.

------

1. Add the scaling metric specification to the `MetricSpecifications` and define a target value.

   The following are examples of the structure of the scaling metric and target value sections.

------
#### [ With predefined metrics ]

   ```
   {
     "MetricSpecifications":[
       {
         "PredefinedLoadMetricSpecification":{
           "PredefinedMetricType":"ASGTotalCPUUtilization"
         },{{
         "PredefinedScalingMetricSpecification":{
           "PredefinedMetricType":"ASGCPUUtilization"
         },
         "TargetValue":50
       }
     ],
     ...}}
   }
   ```

   For more information, see [PredictiveScalingPredefinedScalingMetric](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingPredefinedScalingMetric.html) in the *Amazon EC2 Auto Scaling API Reference*.

------
#### [ With custom metrics ]

   ```
   {
     "MetricSpecifications":[
       {
         "CustomizedLoadMetricSpecification":{
           "MetricDataQueries":[
             {
               "Id":"load_metric",
               "MetricStat":{
                 "Metric":{
                   "MetricName":"MyLoadMetric",
                   "Namespace":"MyNameSpace",
                   "Dimensions":[
                     {
                       "Name":"MyOptionalMetricDimensionName",
                       "Value":"MyOptionalMetricDimensionValue"
                     }
                   ]
                 },
                 "Stat":"Sum"
               }
             }
           ]
         },{{
         "CustomizedScalingMetricSpecification":{
           "MetricDataQueries":[
             {
               "Id":"scaling_metric",
               "MetricStat":{
                 "Metric":{
                   "MetricName":"MyUtilizationMetric",
                   "Namespace":"MyNameSpace",
                   "Dimensions":[
                     {
                       "Name":"MyOptionalMetricDimensionName",
                       "Value":"MyOptionalMetricDimensionValue"
                     }
                   ]
                 },
                 "Stat":"Average"
               }
             }
           ]
         },
         "TargetValue":50
       }
     ],
     ...}}
   }
   ```

   For more information, see [PredictiveScalingCustomizedScalingMetric](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingCustomizedScalingMetric.html) in the *Amazon EC2 Auto Scaling API Reference*.

------

1. To forecast only, add the property `Mode` with a value of `ForecastOnly`. After you finish migrating predictive scaling and making sure that the forecast is accurate and reliable, you can change the mode to allow scaling. For more information, see [Step 7: Reactivate predictive scaling](#switch-predictive-scaling-to-forecast-and-scale).

   ```
   {
     "MetricSpecifications":[
     {{...}}
     ],
     "Mode":"ForecastOnly",
     {{...}}
   }
   ```

   For more information, see [PredictiveScalingConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html) in the *Amazon EC2 Auto Scaling API Reference*.

1. If the `ScheduledActionBufferTime` property is present in your scaling plan, then copy its value to the `SchedulingBufferTime` property in your predictive scaling policy.

   ```
   {
     "MetricSpecifications":[
     {{...}}
     ],
     "Mode":"ForecastOnly",{{
     "SchedulingBufferTime":300,
     ...}}
   }
   ```

   For more information, see [PredictiveScalingConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html) in the *Amazon EC2 Auto Scaling API Reference*.

1. If the `PredictiveScalingMaxCapacityBehavior` and `PredictiveScalingMaxCapacityBuffer` properties are present in your scaling plan, then you can configure the `MaxCapacityBreachBehavior` and `MaxCapacityBuffer` properties in your predictive scaling policy. These properties define what should happen if the forecast capacity approaches or exceeds the maximum capacity specified for the Auto Scaling group.
**Warning**
If you set the `MaxCapacityBreachBehavior` property to `IncreaseMaxCapacity`, then more instances could launch than intended unless you monitor and manage the increased maximum capacity. The increased maximum capacity becomes the new normal maximum capacity for the Auto Scaling group until you manually update it. The maximum capacity doesn't automatically decrease back to the original maximum.

   ```
   {
     "MetricSpecifications":[
     {{...}}
     ],
     "Mode":"ForecastOnly",
     "SchedulingBufferTime":300,{{
     "MaxCapacityBreachBehavior": "IncreaseMaxCapacity",
     "MaxCapacityBuffer": 10}}
   }
   ```

   For more information, see [PredictiveScalingConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html) in the *Amazon EC2 Auto Scaling API Reference*.

1. Save the JSON file with a unique name. Make a note of the file name. You need it in the next step and again at the end of the migration procedure when you reactivate your predictive scaling policies. For more information, see [Step 7: Reactivate predictive scaling](#switch-predictive-scaling-to-forecast-and-scale).

1. After you save your JSON file, run the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scaling-policy.html) command. In the following example, replace each {{user input placeholder}} with your own information.

   ```
   aws autoscaling put-scaling-policy --policy-name {{my-predictive-scaling-policy}} \
     --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
     --predictive-scaling-configuration {{file://my-predictive-scaling-config.json}}
   ```

   If successful, this command returns the policy's Amazon Resource Name (ARN).

   ```
   {
     "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/my-predictive-scaling-policy",
     "Alarms": []
   }
   ```

1. Repeat these steps for each load metric specification that you're migrating to an Amazon EC2 Auto Scaling-based predictive scaling policy.

## Step 3: Review the forecasts that the predictive scaling policies generate
<a name="review-predictive-scaling-policy-forecast"></a>

If you don't use predictive scaling, then skip the following procedure.

A forecast is available shortly after you create a predictive scaling policy. After Amazon EC2 Auto Scaling generates the forecast, you can review the forecast for the policy through the Amazon EC2 Auto Scaling console and adjust as necessary.

**To review the forecast for a predictive scaling policy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Auto Scaling Groups**, and then choose the name of your Auto Scaling group from the list.

1. On the **Automatic scaling** tab, in **Predictive scaling policies**, choose your policy.

1. In the **Monitoring** section, you can view your policy's past and future forecasts for load and capacity against actual values.

   For more information, see [Review predictive scaling monitoring graphs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-graphs.html#review-predictive-scaling-monitoring-graphs) in the *Amazon EC2 Auto Scaling User Guide*.

1. Repeat these steps for each predictive scaling policy that you created.

## Step 4: Prepare to delete the scaling plan
<a name="prepare-to-delete-the-scaling-plan"></a>

For any resources with an existing target tracking scaling configuration, do the following to collect any additional information that you need from the scaling plan before deleting it.

To describe the scaling policy information from the scaling plan, use the [describe-scaling-plan-resources](https://docs.aws.amazon.com/cli/latest/reference/autoscaling-plans/describe-scaling-plan-resources.html) command. In the following example command, replace {{my-scaling-plan}} with your own information.

```
aws autoscaling-plans describe-scaling-plan-resources \
  --scaling-plan-name {{my-scaling-plan}} \
  --scaling-plan-version 1
```

Review the output and confirm you want to migrate the scaling policies described. Use this information to create new Amazon EC2 Auto Scaling and Application Auto Scaling-based target tracking scaling polices in [Step 6: Reactivate dynamic scaling](#create-target-tracking-scaling-policies).

## Step 5: Delete the scaling plan
<a name="delete-scaling-plan"></a>

Before creating new target tracking scaling policies, you must delete the scaling plan to delete the scaling policies that it created.

To delete your scaling plan, use the [delete-scaling-plan](https://docs.aws.amazon.com/cli/latest/reference/autoscaling-plans/delete-scaling-plan.html) command. In the following example command, replace {{my-scaling-plan}} with your own information.

```
aws autoscaling-plans delete-scaling-plan \
  --scaling-plan-name {{my-scaling-plan}} \
  --scaling-plan-version 1
```

After you delete the scaling plan, dynamic scaling is deactivated. So if there are sudden surges in traffic or workload, the capacity available for each scalable resource won't increase on its own. As a precaution, you might want to manually increase the capacity of your scalable resources in the short term.

**To increase the capacity of an Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Auto Scaling Groups**, and then choose the name of your Auto Scaling group from the list.

1. On the **Details** tab, choose **Group details**, **Edit**.

1. For **Desired capacity**, increase the desired capacity.

1. When you're finished, choose **Update**.

**To add an Aurora replica to a DB cluster**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select your DB cluster.

1. Make sure that both the cluster and the primary instance are in the **Available** state.

1. Choose **Actions**, **Add reader**.

1. On the **Add reader** page, specify options for your new Aurora replica.

1. Choose **Add reader**.

**To increase the provisioned read and write capacity of a DynamoDB table or global secondary index**

1. Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane, choose **Tables**, and then choose the name of your table from the list.

1. On the **Additional settings** tab, choose **Read/write capacity**, **Edit**.

1. On the **Edit read/write capacity** page, for **Read capacity**, **Provisioned capacity units**, increase the provisioned read capacity of the table.

1. (Optional) If you want your global secondary indexes to use the same read capacity settings as the base table, then select the **Use the same read capacity settings for all global secondary indexes** check box.

1. For **Write capacity**, **Provisioned capacity units**, increase the provisioned write capacity of the table.

1. (Optional) If you want your global secondary indexes to use the same write capacity settings as the base table, then select the **Use the same write capacity settings for all global secondary indexes** check box.

1. If you *didn't* select the check boxes in steps 5 or 7, then scroll down the page to update the read and write capacity of any global secondary indexes.

1. Choose **Save changes** to continue.

**To increase the running task count for your Amazon ECS service**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**, and then choose the name of your cluster from the list.

1. In the **Services** section, select the check box next to the service, and then choose **Update**.

1. For **Desired tasks**, enter the number of tasks that you want to run for the service.

1. Choose **Update**.

**To increase the capacity of a Spot Fleet**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**, and then select your Spot Fleet request.

1. Choose **Actions**, **Modify target capacity**.

1. In **Modify target capacity**, enter the new target capacity and On-Demand Instance portion.

1. Choose **Submit**.

## Step 6: Reactivate dynamic scaling
<a name="create-target-tracking-scaling-policies"></a>

Reactivate dynamic scaling by creating target tracking scaling policies.

When you create a target tracking scaling policy for an Auto Scaling group, you add it directly to the group. When you create a target tracking scaling policy for other scalable resources, you first register the resource as a scalable target and then you add a target tracking scaling policy to the scalable target.

**Topics**
+ [Create target tracking scaling policies for Auto Scaling groups](#target-tracking-for-auto-scaling-groups)
+ [Create target tracking scaling policies for other scalable resources](#target-tracking-for-other-scalable-resources)

### Create target tracking scaling policies for Auto Scaling groups
<a name="target-tracking-for-auto-scaling-groups"></a>

**To create target tracking scaling policies for Auto Scaling groups**

1. In a JSON file, create a `PredefinedMetricSpecification` or `CustomizedMetricSpecification` using the equivalent settings from the scaling plan.

   The following are examples of a target tracking configuration. In these examples, replace each {{user input placeholder}} with your own information.

------
#### [ With predefined metrics ]

   ```
   {
     "TargetValue": {{50.0}},
     "PredefinedMetricSpecification":
       {
         "PredefinedMetricType": "{{ASGAverageCPUUtilization}}"
       }
   }
   ```

   For more information, see [PredefinedMetricSpecification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredefinedMetricSpecification.html) in the *Amazon EC2 Auto Scaling API Reference*.

------
#### [ With custom metrics ]

   ```
   {
     "TargetValue": {{100.0}},
     "CustomizedMetricSpecification": {
       "MetricName": "{{MyBacklogPerInstance}}",
       "Namespace": "{{MyNamespace}}",
       "Dimensions": [{
         "Name": "{{MyOptionalMetricDimensionName}}",
         "Value": "{{MyOptionalMetricDimensionValue}}"
       }],
       "Statistic": "{{Average}}",
       "Unit": "{{None}}"
     }
   }
   ```

   For more information, see [CustomizedMetricSpecification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html) in the *Amazon EC2 Auto Scaling API Reference*.

------

1. To create your scaling policy, use the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scaling-policy.html) command, along with the JSON file that you created in the previous step. In the following example, replace each {{user input placeholder}} with your own information.

   ```
   aws autoscaling put-scaling-policy --policy-name {{my-target-tracking-scaling-policy}} \
     --auto-scaling-group-name {{my-asg}} --policy-type TargetTrackingScaling \
     --target-tracking-configuration {{file://config.json}}
   ```

1. Repeat this process for each scaling plan-based scaling policy that you're migrating to an Amazon EC2 Auto Scaling-based target tracking scaling policy.

### Create target tracking scaling policies for other scalable resources
<a name="target-tracking-for-other-scalable-resources"></a>

Next, create target tracking scaling policies for other scalable resources by performing the following configuration tasks.
+ Register a scalable target for auto scaling with the Application Auto Scaling service.
+ Add a target tracking scaling policy on the scalable target.

**To create target tracking scaling policies for other scalable resources**

1. Use the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command to register the resource as a scalable target and define the scaling limits for the scaling policy.

   In the following example, replace each {{user input placeholder}} with your own information. For the command options, provide the following information:
   + `--service-namespace` – A namespace for the target service (for example, **`ecs`**). To obtain service namespaces, see the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) reference.
   + `--scalable-dimension` – A scalable dimension associated with the target resource (for example, **`ecs:service:DesiredCount`**). To obtain scalable dimensions, see the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) reference.
   + `--resource-id` – A resource ID for the target resource (for example, **`service/{{my-cluster}}/{{my-service}}`**). For information about the syntax and examples of specific resource IDs, see the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) reference.

   ```
   aws application-autoscaling register-scalable-target --service-namespace {{namespace}} \
     --scalable-dimension {{dimension}} \
     --resource-id {{identifier}} \
     --min-capacity {{1}} --max-capacity {{10}}
   ```

   If successful, this command returns the ARN of the scalable target.

   ```
   {
       "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
   }
   ```

1. In a JSON file, create a `PredefinedMetricSpecification` or `CustomizedMetricSpecification` using the equivalent settings from the scaling plan.

   The following are examples of a target tracking configuration.

------
#### [ With predefined metrics ]

   ```
   {
     "TargetValue": {{70.0}},
     "PredefinedMetricSpecification":
       {
         "PredefinedMetricType": "{{ECSServiceAverageCPUUtilization}}"
       }
   }
   ```

   For more information, see [PredefinedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html) in the *Application Auto Scaling API Reference*.

------
#### [ With custom metrics ]

   ```
   {
     "TargetValue": {{70.0}},
     "CustomizedMetricSpecification": {
       "MetricName": "{{MyUtilizationMetric}}",
       "Namespace": "{{MyNamespace}}",
       "Dimensions": [{
         "Name": "{{MyOptionalMetricDimensionName}}",
         "Value": "{{MyOptionalMetricDimensionValue}}"
       }],
       "Statistic": "{{Average}}",
       "Unit": "{{Percent}}"
     }
   }
   ```

   For more information, see [CustomizedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CustomizedMetricSpecification.html) in the *Application Auto Scaling API Reference*.

------

1. To create your scaling policy, use the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command, along with the JSON file that you created in the previous step.

   ```
   aws application-autoscaling put-scaling-policy --service-namespace {{namespace}} \
     --scalable-dimension {{dimension}} \
     --resource-id {{identifier}} \
     --policy-name {{my-target-tracking-scaling-policy}} --policy-type {{TargetTrackingScaling}} \
     --target-tracking-scaling-policy-configuration {{file://config.json}}
   ```

1. Repeat this process for each scaling plan-based scaling policy that you're migrating to an Application Auto Scaling-based target tracking scaling policy.

## Step 7: Reactivate predictive scaling
<a name="switch-predictive-scaling-to-forecast-and-scale"></a>

If you don't use predictive scaling, then skip this step.

Reactivate predictive scaling by switching predictive scaling to forecast and scale.

To make this change, update the JSON files that you created in [Step 2: Create predictive scaling policies](#migrate-predictive-scaling-configurations) and change the value of the `Mode` option to `ForecastAndScale` as in the following example:

```
"Mode":"ForecastAndScale"
```

Then, update each predictive scaling policy with the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scaling-policy.html) command. In this example, replace each {{user input placeholder}} with your own information.

```
aws autoscaling put-scaling-policy --policy-name {{my-predictive-scaling-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://my-predictive-scaling-config.json}}
```

Alternatively, you can make this change from the Amazon EC2 Auto Scaling console by turning on the **Scale based on forecast** setting. For more information, see [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Amazon EC2 Auto Scaling reference for migrating target tracking scaling policies
<a name="target-tracking-mapping-reference-ec2-auto-scaling"></a>

For reference purposes, the following table lists all the target tracking configuration properties in the scaling plan with their corresponding property in the Amazon EC2 Auto Scaling `PutScalingPolicy` API operation.

| Scaling plan source property | Amazon EC2 Auto Scaling target property |
| --- | --- |
| PolicyName | PolicyName |
| PolicyType | PolicyType |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Dimensions.Name | TargetTrackingConfiguration.CustomizedMetricSpecification.Dimensions.Name |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Dimensions.Value | TargetTrackingConfiguration.CustomizedMetricSpecification.Dimensions.Value |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.MetricName | TargetTrackingConfiguration.CustomizedMetricSpecification.MetricName |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Namespace | TargetTrackingConfiguration.CustomizedMetricSpecification.Namespace |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Statistic | TargetTrackingConfiguration.CustomizedMetricSpecification.Statistic |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Unit | TargetTrackingConfiguration.CustomizedMetricSpecification.Unit |
| TargetTrackingConfiguration.DisableScaleIn | TargetTrackingConfiguration.DisableScaleIn |
| TargetTrackingConfiguration.EstimatedInstanceWarmup | TargetTrackingConfiguration.EstimatedInstanceWarmup¹ |
| TargetTrackingConfiguration.PredefinedScalingMetricSpecification.PredefinedScalingMetricType | TargetTrackingConfiguration.PredefinedMetricSpecification.PredefinedMetricType |
| TargetTrackingConfiguration.PredefinedScalingMetricSpecification.ResourceLabel | TargetTrackingConfiguration.PredefinedMetricSpecification.ResourceLabel |
| TargetTrackingConfiguration.ScaleInCooldown | Not available |
| TargetTrackingConfiguration.ScaleOutCooldown | Not available |
| TargetTrackingConfiguration.TargetValue | TargetTrackingConfiguration.TargetValue |

¹ Instance warmup is a feature for Auto Scaling groups that helps to ensure that newly launched instances are ready to receive traffic before contributing their usage data to the scaling metric. While instances are still warming up, Amazon EC2 Auto Scaling slows down the process of adding or removing instances to the group. Instead of specifying a warmup time for a scaling policy, we recommend that you use the default instance warmup setting of your Auto Scaling group to ensure that all instance launches use the same instance warmup time. For more information, see [Set the default instance warmup for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Application Auto Scaling reference for migrating target tracking scaling policies
<a name="target-tracking-mapping-reference-application-auto-scaling"></a>

For reference purposes, the following table lists all the target tracking configuration properties in the scaling plan with their corresponding property in the Application Auto Scaling `PutScalingPolicy` API operation.

| Scaling plan source property | Application Auto Scaling target property |
| --- | --- |
| PolicyName | PolicyName |
| PolicyType | PolicyType |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Dimensions.Name | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.Dimensions.Name |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Dimensions.Value | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.Dimensions.Value |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.MetricName | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.MetricName |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Namespace | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.Namespace |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Statistic | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.Statistic |
| TargetTrackingConfiguration.CustomizedScalingMetricSpecification.Unit | TargetTrackingScalingPolicyConfiguration.CustomizedMetricSpecification.Unit |
| TargetTrackingConfiguration.DisableScaleIn | TargetTrackingScalingPolicyConfiguration.DisableScaleIn |
| TargetTrackingConfiguration.EstimatedInstanceWarmup | Not available |
| TargetTrackingConfiguration.PredefinedScalingMetricSpecification.PredefinedScalingMetricType | TargetTrackingScalingPolicyConfiguration.PredefinedMetricSpecification.PredefinedMetricType |
| TargetTrackingConfiguration.PredefinedScalingMetricSpecification.ResourceLabel | TargetTrackingScalingPolicyConfiguration.PredefinedMetricSpecification.ResourceLabel |
| TargetTrackingConfiguration.ScaleInCooldown¹ | TargetTrackingScalingPolicyConfiguration.ScaleInCooldown |
| TargetTrackingConfiguration.ScaleOutCooldown¹ | TargetTrackingScalingPolicyConfiguration.ScaleOutCooldown |
| TargetTrackingConfiguration.TargetValue | TargetTrackingScalingPolicyConfiguration.TargetValue |

¹ Application Auto Scaling uses cooldown periods to slow down scaling when your scalable resource is scaling out (increasing capacity) and scaling in (reducing capacity). For more information, see [Define cooldown periods](https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown) in the *Application Auto Scaling User Guide*.

## Additional information
<a name="migrate-scaling-plan-more-info"></a>

To learn how to create new predictive scaling policies from the console, see the following topic:
+ **Amazon EC2 Auto Scaling** – [Create a predictive scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-create-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.

To learn how to create new target tracking scaling policies using the console, see the following topics:
+ **Amazon Aurora** – [Using Amazon Aurora Auto Scaling with Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html) in the *Amazon RDS User Guide*.
+ **DynamoDB** – [Using the AWS Management Console with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html) in the *Amazon DynamoDB Developer Guide*.
+ **Amazon EC2 Auto Scaling** – [Create a target tracking scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#policy_creating) in the *Amazon EC2 Auto Scaling User Guide*.
+ **Amazon ECS** – [Updating a service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
+ **Spot Fleet** – [Scale Spot Fleet using a target tracking policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-target-tracking.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
