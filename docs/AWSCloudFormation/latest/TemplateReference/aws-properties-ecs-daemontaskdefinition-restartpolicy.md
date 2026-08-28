---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-restartpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition RestartPolicy
<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy"></a>

<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy-description"></a>The `RestartPolicy` property type specifies Property description not available. for an [AWS::ECS::DaemonTaskDefinition](aws-resource-ecs-daemontaskdefinition.md).

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy-syntax.json"></a>

```
{
  "[Enabled](#cfn-ecs-daemontaskdefinition-restartpolicy-enabled)" : {{Boolean}},
  "[IgnoredExitCodes](#cfn-ecs-daemontaskdefinition-restartpolicy-ignoredexitcodes)" : {{[ Integer, ... ]}},
  "[RestartAttemptPeriod](#cfn-ecs-daemontaskdefinition-restartpolicy-restartattemptperiod)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy-syntax.yaml"></a>

```
  [Enabled](#cfn-ecs-daemontaskdefinition-restartpolicy-enabled): {{Boolean}}
  [IgnoredExitCodes](#cfn-ecs-daemontaskdefinition-restartpolicy-ignoredexitcodes): {{
    - Integer}}
  [RestartAttemptPeriod](#cfn-ecs-daemontaskdefinition-restartpolicy-restartattemptperiod): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-restartpolicy-properties"></a>

`Enabled`  <a name="cfn-ecs-daemontaskdefinition-restartpolicy-enabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IgnoredExitCodes`  <a name="cfn-ecs-daemontaskdefinition-restartpolicy-ignoredexitcodes"></a>
Property description not available.
*Required*: No
*Type*: Array of Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestartAttemptPeriod`  <a name="cfn-ecs-daemontaskdefinition-restartpolicy-restartattemptperiod"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
