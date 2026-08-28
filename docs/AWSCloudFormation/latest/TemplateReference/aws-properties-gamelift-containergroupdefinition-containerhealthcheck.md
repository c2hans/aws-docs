---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition ContainerHealthCheck
<a name="aws-properties-gamelift-containergroupdefinition-containerhealthcheck"></a>

Instructions on when and how to check the health of a support container in a container fleet. These properties override any Docker health checks that are set in the container image. For more information on container health checks, see [HealthCheck command](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HealthCheck.html#ECS-Type-HealthCheck-command) in the *Amazon Elastic Container Service API*. Game server containers don't have a health check parameter; Amazon GameLift Servers automatically handles health checks for these containers.

The following example instructs the container to initiate a health check command every 60 seconds and wait 10 seconds for it to succeed. If it fails, retry the command 3 times before flagging the container as unhealthy. It also tells the container to wait 100 seconds after launch before counting failed health checks.

 `{"Command": [ "CMD-SHELL", "ps cax | grep "processmanager" || exit 1" ], "Interval": 60, "Timeout": 10, "Retries": 3, "StartPeriod": 100 }`

**Part of:**[SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-containerhealthcheck-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-containerhealthcheck-syntax.json"></a>

```
{
  "[Command](#cfn-gamelift-containergroupdefinition-containerhealthcheck-command)" : {{[ String, ... ]}},
  "[Interval](#cfn-gamelift-containergroupdefinition-containerhealthcheck-interval)" : {{Integer}},
  "[Retries](#cfn-gamelift-containergroupdefinition-containerhealthcheck-retries)" : {{Integer}},
  "[StartPeriod](#cfn-gamelift-containergroupdefinition-containerhealthcheck-startperiod)" : {{Integer}},
  "[Timeout](#cfn-gamelift-containergroupdefinition-containerhealthcheck-timeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-containerhealthcheck-syntax.yaml"></a>

```
  [Command](#cfn-gamelift-containergroupdefinition-containerhealthcheck-command): {{
    - String}}
  [Interval](#cfn-gamelift-containergroupdefinition-containerhealthcheck-interval): {{Integer}}
  [Retries](#cfn-gamelift-containergroupdefinition-containerhealthcheck-retries): {{Integer}}
  [StartPeriod](#cfn-gamelift-containergroupdefinition-containerhealthcheck-startperiod): {{Integer}}
  [Timeout](#cfn-gamelift-containergroupdefinition-containerhealthcheck-timeout): {{Integer}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-containerhealthcheck-properties"></a>

`Command`  <a name="cfn-gamelift-containergroupdefinition-containerhealthcheck-command"></a>
A string array that specifies the command that the container runs to determine if it's healthy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-gamelift-containergroupdefinition-containerhealthcheck-interval"></a>
The time period (in seconds) between each health check.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Retries`  <a name="cfn-gamelift-containergroupdefinition-containerhealthcheck-retries"></a>
The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.
*Required*: No
*Type*: Integer
*Minimum*: `5`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartPeriod`  <a name="cfn-gamelift-containergroupdefinition-containerhealthcheck-startperiod"></a>
The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-gamelift-containergroupdefinition-containerhealthcheck-timeout"></a>
The time period (in seconds) to wait for a health check to succeed before counting a failed health check.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
