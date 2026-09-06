---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-restartpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition RestartPolicy
<a name="aws-properties-ecs-taskdefinition-restartpolicy"></a>

You can enable a restart policy for each container defined in your task definition, to overcome transient failures faster and maintain task availability. When you enable a restart policy for a container, Amazon ECS can restart the container if it exits, without needing to replace the task. For more information, see [Restart individual containers in Amazon ECS tasks with container restart policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-taskdefinition-restartpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-restartpolicy-syntax.json"></a>

```
{
  "[Enabled](#cfn-ecs-taskdefinition-restartpolicy-enabled)" : {{Boolean}},
  "[IgnoredExitCodes](#cfn-ecs-taskdefinition-restartpolicy-ignoredexitcodes)" : {{[ Integer, ... ]}},
  "[RestartAttemptPeriod](#cfn-ecs-taskdefinition-restartpolicy-restartattemptperiod)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-restartpolicy-syntax.yaml"></a>

```
  [Enabled](#cfn-ecs-taskdefinition-restartpolicy-enabled): {{Boolean}}
  [IgnoredExitCodes](#cfn-ecs-taskdefinition-restartpolicy-ignoredexitcodes): {{
    - Integer}}
  [RestartAttemptPeriod](#cfn-ecs-taskdefinition-restartpolicy-restartattemptperiod): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-restartpolicy-properties"></a>

`Enabled`  <a name="cfn-ecs-taskdefinition-restartpolicy-enabled"></a>
Specifies whether a restart policy is enabled for the container.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IgnoredExitCodes`  <a name="cfn-ecs-taskdefinition-restartpolicy-ignoredexitcodes"></a>
A list of exit codes that Amazon ECS will ignore and not attempt a restart on. You can specify a maximum of 50 container exit codes. By default, Amazon ECS does not ignore any exit codes.
*Required*: No
*Type*: Array of Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestartAttemptPeriod`  <a name="cfn-ecs-taskdefinition-restartpolicy-restartattemptperiod"></a>
A period of time (in seconds) that the container must run for before a restart can be attempted. A container can be restarted only once every `restartAttemptPeriod` seconds. If a container isn't able to run for this time period and exits early, it will not be restarted. You can set a minimum `restartAttemptPeriod` of 60 seconds and a maximum `restartAttemptPeriod` of 1800 seconds. By default, a container must run for 300 seconds before it can be restarted.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
