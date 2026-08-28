---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html
---

# Create a predictive scaling policy for Application Auto Scaling
<a name="aas-create-predictive-scaling-policy"></a>

The following example policy uses the AWS CLI to configure a predictive scaling policy for Amazon ECS service. Replace each {{user input placeholder}} with your own information.

For more information about the CloudWatch metrics you can specify, see [PredictiveScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingMetricSpecification.html) in the *Amazon EC2 Auto Scaling API Reference*.

The following is an example policy with a predefined memory configuration.

```
cat policy.json
{
    "MetricSpecifications": [
        {
            "TargetValue": {{40}},
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "{{ECSServiceMemoryUtilization}}"
            }
        }
    ],
    "SchedulingBufferTime": {{3600}},
    "MaxCapacityBreachBehavior": "HonorMaxCapacity",
    "Mode": "ForecastOnly"
}
```

The following example illustrates creating the policy by running the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scaling-policy.html) command with the configuration file specified.

```
aws aas put-scaling-policy \
--service-namespace {{ecs}} \
--region {{us-east-1}} \
--policy-name {{predictive-scaling-policy-example}} \
--resource-id {{service/MyCluster/test}} \
--policy-type PredictiveScaling \
--scalable-dimension ecs:service:DesiredCount \
--predictive-scaling-policy-configuration file://policy.json
```

If successful, this command returns the policy's ARN.

```
{
"PolicyARN": "arn:aws:autoscaling:us-east-1:012345678912:scalingPolicy:d1d72dfe-5fd3-464f-83cf-824f16cb88b7:resource/ecs/service/MyCluster/test:policyName/predictive-scaling-policy-example",
"Alarms": []
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
