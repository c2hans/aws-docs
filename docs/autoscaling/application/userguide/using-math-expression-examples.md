---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/using-math-expression-examples.html
---

# Use metric math expressions
<a name="using-math-expression-examples"></a>

The following section provides information and examples of predictive scaling policies that show how you can use metric math in your policy.

**Topics**
+ [Understand metric math](#custom-metrics-metric-math)
+ [Example predictive scaling policy for Amazon EC2 Auto Scaling that combines metrics using metric math (AWS CLI)](#custom-metrics-ex2)
+ [Example predictive scaling policy to use in a blue/green deployment scenario (AWS CLI)](#custom-metrics-ex3)

## Understand metric math
<a name="custom-metrics-metric-math"></a>

If all you want to do is aggregate existing metric data, CloudWatch metric math saves you the effort and cost of publishing another metric to CloudWatch. You can use any metric that AWS provides, and you can also use metrics that you define as part of your applications.

For more information, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide*.

If you choose to use a metric math expression in your predictive scaling policy, consider the following points:
+ Metric math operations use the data points of the unique combination of metric name, namespace, and dimension keys/value pairs of metrics.
+ You can use any arithmetic operator (\+ - \* / ^), statistical function (such as AVG or SUM), or other function that CloudWatch supports.
+ You can use both metrics and the results of other math expressions in the formulas of the math expression.
+ Your metric math expressions can be made up of different aggregations. However, it's a best practice for the final aggregation result to use `Average` for the scaling metric and `Sum` for the load metric.
+ Any expressions used in a metric specification must eventually return a single time series.

To use metric math, do the following:
+ Choose one or more CloudWatch metrics. Then, create the expression. For more information, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide*.
+ Verify that the metric math expression is valid by using the CloudWatch console or the CloudWatch [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) API.

## Example predictive scaling policy for Amazon EC2 Auto Scaling that combines metrics using metric math (AWS CLI)
<a name="custom-metrics-ex2"></a>

Sometimes, instead of specifying the metric directly, you might need to first process its data in some way. For example, you might have an application that pulls work from an Amazon SQS queue, and you might want to use the number of items in the queue as criteria for predictive scaling. The number of messages in the queue does not solely define the number of instances that you need. Therefore, more work is needed to create a metric that can be used to calculate the backlog per instance.

The following is an example predictive scaling policy for this scenario. It specifies scaling and load metrics that are based on the Amazon SQS `ApproximateNumberOfMessagesVisible` metric, which is the number of messages available for retrieval from the queue. It also uses the Amazon EC2 Auto Scaling `GroupInServiceInstances` metric and a math expression to calculate the backlog per instance for the scaling metric.

```
aws autoscaling put-scaling-policy --policy-name {{my-sqs-custom-metrics-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://config.json}}
{
  "MetricSpecifications": [
    {
      "TargetValue": {{100}},
      "CustomizedScalingMetricSpecification": {
        "MetricDataQueries": [
          {
            "Label": "Get the queue size (the number of messages waiting to be processed)",
            "Id": "{{queue_size}}",
            "MetricStat": {
              "Metric": {
                "MetricName": "{{ApproximateNumberOfMessagesVisible}}",
                "Namespace": "{{AWS/SQS}}",
                "Dimensions": [
                  {
                    "Name": "{{QueueName}}",
                    "Value": "{{my-queue}}"
                  }
                ]
              },
              "Stat": "{{Sum}}"
            },
            "ReturnData": false
          },
          {
            "Label": "Get the group size (the number of running instances)",
            "Id": "{{running_capacity}}",
            "MetricStat": {
              "Metric": {
                "MetricName": "{{GroupInServiceInstances}}",
                "Namespace": "{{AWS/AutoScaling}}",
                "Dimensions": [
                  {
                    "Name": "{{AutoScalingGroupName}}",
                    "Value": "{{my-asg}}"
                  }
                ]
              },
              "Stat": "{{Sum}}"
            },
            "ReturnData": false
          },
          {
            "Label": "Calculate the backlog per instance",
            "Id": "{{scaling_metric}}",
            "Expression": "{{queue_size / running_capacity}}",
            "ReturnData": true
          }
        ]
      },
      "CustomizedLoadMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "{{load_metric}}",
            "MetricStat": {
              "Metric": {
                "MetricName": "{{ApproximateNumberOfMessagesVisible}}",
                "Namespace": "{{AWS/SQS}}",
                "Dimensions": [
                  {
                    "Name": "{{QueueName}}",
                    "Value": "{{my-queue}}"
                  }
                ],
              },
              "Stat": "{{Sum}}"
            },
            "ReturnData": true
          }
        ]
      }
    }
  ]
}
```

The example returns the policy's ARN.

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/my-sqs-custom-metrics-policy",
  "Alarms": []
}
```

## Example predictive scaling policy to use in a blue/green deployment scenario (AWS CLI)
<a name="custom-metrics-ex3"></a>

A search expression provides an advanced option in which you can query for a metric from multiple Auto Scaling groups and perform math expressions on them. This is especially useful for blue/green deployments.

**Note**
A *blue/green deployment* is a deployment method in which you create two separate but identical Auto Scaling groups. Only one of the groups receives production traffic. User traffic is initially directed to the earlier ("blue") Auto Scaling group, while a new group ("green") is used for testing and evaluation of a new version of an application or service. User traffic is shifted to the green Auto Scaling group after a new deployment is tested and accepted. You can then delete the blue group after the deployment is successful.

When new Auto Scaling groups get created as part of a blue/green deployment, the metric history of each group can be automatically included in the predictive scaling policy without you having to change its metric specifications. For more information, see [Using EC2 Auto Scaling predictive scaling policies with Blue/Green deployments](https://aws.amazon.com/blogs/compute/retaining-metrics-across-blue-green-deployment-for-predictive-scaling/) on the AWS Compute Blog.

The following example policy shows how this can be done. In this example, the policy uses the `CPUUtilization` metric emitted by Amazon EC2. It uses the Amazon EC2 Auto Scaling `GroupInServiceInstances` metric and a math expression to calculate the value of the scaling metric per instance. It also specifies a capacity metric specification to get the `GroupInServiceInstances` metric.

The search expression finds the `CPUUtilization` of instances in multiple Auto Scaling groups based on the specified search criteria. If you later create a new Auto Scaling group that matches the same search criteria, the `CPUUtilization` of the instances in the new Auto Scaling group is automatically included.

```
aws autoscaling put-scaling-policy --policy-name {{my-blue-green-predictive-scaling-policy}} \
  --auto-scaling-group-name {{my-asg}} --policy-type PredictiveScaling \
  --predictive-scaling-configuration {{file://config.json}}
{
  "MetricSpecifications": [
    {
      "TargetValue": {{25}},
      "CustomizedScalingMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "{{load_sum}}",
            "Expression": "{{SUM(SEARCH('{AWS/EC2,AutoScalingGroupName} MetricName=\"CPUUtilization\" ASG-myapp', 'Sum', 300))}}",
            "ReturnData": false
          },
          {
            "Id": "{{capacity_sum}}",
            "Expression": "{{SUM(SEARCH('{AWS/AutoScaling,AutoScalingGroupName} MetricName=\"GroupInServiceInstances\" ASG-myapp', 'Average', 300))}}",
            "ReturnData": false
          },
          {
            "Id": "{{weighted_average}}",
            "Expression": "{{load_sum / capacity_sum}}",
            "ReturnData": true
          }
        ]
      },
      "CustomizedLoadMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "{{load_sum}}",
            "Expression": "{{SUM(SEARCH('{AWS/EC2,AutoScalingGroupName} MetricName=\"CPUUtilization\" ASG-myapp', 'Sum', 3600))}}"
          }
        ]
      },
      "CustomizedCapacityMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "{{capacity_sum}}",
            "Expression": "{{SUM(SEARCH('{AWS/AutoScaling,AutoScalingGroupName} MetricName=\"GroupInServiceInstances\" ASG-myapp', 'Average', 300))}}"
          }
        ]
      }
    }
  ]
}
```

The example returns the policy's ARN.

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/my-blue-green-predictive-scaling-policy",
  "Alarms": []
}
```
