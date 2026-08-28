---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-ulimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition Ulimit
<a name="aws-properties-ecs-daemontaskdefinition-ulimit"></a>

The `ulimit` settings to pass to the container.

Amazon ECS tasks hosted on AWS Fargate use the default resource limit values set by the operating system with the exception of the `nofile` resource limit parameter which AWS Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is ` 65535` and the default hard limit is `65535`.

You can specify the `ulimit` settings for a container in a task definition.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-ulimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-ulimit-syntax.json"></a>

```
{
  "[HardLimit](#cfn-ecs-daemontaskdefinition-ulimit-hardlimit)" : {{Integer}},
  "[Name](#cfn-ecs-daemontaskdefinition-ulimit-name)" : {{String}},
  "[SoftLimit](#cfn-ecs-daemontaskdefinition-ulimit-softlimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-ulimit-syntax.yaml"></a>

```
  [HardLimit](#cfn-ecs-daemontaskdefinition-ulimit-hardlimit): {{Integer}}
  [Name](#cfn-ecs-daemontaskdefinition-ulimit-name): {{String}}
  [SoftLimit](#cfn-ecs-daemontaskdefinition-ulimit-softlimit): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-ulimit-properties"></a>

`HardLimit`  <a name="cfn-ecs-daemontaskdefinition-ulimit-hardlimit"></a>
The hard limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ecs-daemontaskdefinition-ulimit-name"></a>
The `type` of the `ulimit`.
*Required*: Yes
*Type*: String
*Allowed values*: `core | cpu | data | fsize | locks | memlock | msgqueue | nice | nofile | nproc | rss | rtprio | rttime | sigpending | stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SoftLimit`  <a name="cfn-ecs-daemontaskdefinition-ulimit-softlimit"></a>
The soft limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
