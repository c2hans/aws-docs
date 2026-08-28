---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/describe-step-scaling-policy.html
---

# Describe step scaling policies for Application Auto Scaling using the AWS CLI
<a name="describe-step-scaling-policy"></a>

You can describe all scaling policies for a service namespace using the [describe-scaling-policies](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-policies.html) command. The following example describes all scaling policies for all Amazon ECS services. To list them for a specific Amazon ECS service only add the `--resource-id` option.

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ecs}}
```

You can filter the results to just the step scaling policies using the `--query` parameter. For more information about the syntax for `query`, see [Controlling command output from the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html) in the *AWS Command Line Interface User Guide*.

**Linux, macOS, or Unix**

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ecs}} \
  --query 'ScalingPolicies[?PolicyType==`StepScaling`]'
```

**Windows**

```
aws application-autoscaling describe-scaling-policies --service-namespace {{ecs}} ^
  --query "ScalingPolicies[?PolicyType==`StepScaling`]"
```

**Output**
The following is example output.

```
[
    {
        "PolicyARN": "PolicyARN",
        "StepScalingPolicyConfiguration": {
            "MetricAggregationType": "Average",
            "Cooldown": 60,
            "StepAdjustments": [
                {
                    "MetricIntervalLowerBound": 0.0,
                    "MetricIntervalUpperBound": 15.0,
                    "ScalingAdjustment": 1
                },
                {
                    "MetricIntervalLowerBound": 15.0,
                    "MetricIntervalUpperBound": 25.0,
                    "ScalingAdjustment": 2
                },
                {
                    "MetricIntervalLowerBound": 25.0,
                    "ScalingAdjustment": 3
                }
            ],
            "AdjustmentType": "ChangeInCapacity"
        },
        "PolicyType": "StepScaling",
        "ResourceId": "service/my-cluster/my-service",
        "ServiceNamespace": "ecs",
        "Alarms": [
            {
                "AlarmName": "Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service",
                "AlarmARN": "arn:aws:cloudwatch:region:012345678910:alarm:Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service"
            }
        ],
        "PolicyName": "my-step-scaling-policy",
        "ScalableDimension": "ecs:service:DesiredCount",
        "CreationTime": 1515024099.901
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
