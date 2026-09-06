---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-ulimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition Ulimit
<a name="aws-properties-ecs-taskdefinition-ulimit"></a>

The `ulimit` settings to pass to the container.

Amazon ECS tasks hosted on AWS Fargate use the default resource limit values set by the operating system with the exception of the `nofile` resource limit parameter which AWS Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is ` 65535` and the default hard limit is `65535`.

You can specify the `ulimit` settings for a container in a task definition.

## Syntax
<a name="aws-properties-ecs-taskdefinition-ulimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-ulimit-syntax.json"></a>

```
{
  "[HardLimit](#cfn-ecs-taskdefinition-ulimit-hardlimit)" : {{Integer}},
  "[Name](#cfn-ecs-taskdefinition-ulimit-name)" : {{String}},
  "[SoftLimit](#cfn-ecs-taskdefinition-ulimit-softlimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-ulimit-syntax.yaml"></a>

```
  [HardLimit](#cfn-ecs-taskdefinition-ulimit-hardlimit): {{Integer}}
  [Name](#cfn-ecs-taskdefinition-ulimit-name): {{String}}
  [SoftLimit](#cfn-ecs-taskdefinition-ulimit-softlimit): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-ulimit-properties"></a>

`HardLimit`  <a name="cfn-ecs-taskdefinition-ulimit-hardlimit"></a>
The hard limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ecs-taskdefinition-ulimit-name"></a>
The `type` of the `ulimit`.
*Required*: Yes
*Type*: String
*Allowed values*: `core | cpu | data | fsize | locks | memlock | msgqueue | nice | nofile | nproc | rss | rtprio | rttime | sigpending | stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SoftLimit`  <a name="cfn-ecs-taskdefinition-ulimit-softlimit"></a>
The soft limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
