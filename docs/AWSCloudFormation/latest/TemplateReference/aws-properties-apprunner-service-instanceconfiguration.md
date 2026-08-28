---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-instanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service InstanceConfiguration
<a name="aws-properties-apprunner-service-instanceconfiguration"></a>

Describes the runtime configuration of an AWS App Runner service instance (scaling unit).

## Syntax
<a name="aws-properties-apprunner-service-instanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-instanceconfiguration-syntax.json"></a>

```
{
  "[Cpu](#cfn-apprunner-service-instanceconfiguration-cpu)" : {{String}},
  "[InstanceRoleArn](#cfn-apprunner-service-instanceconfiguration-instancerolearn)" : {{String}},
  "[Memory](#cfn-apprunner-service-instanceconfiguration-memory)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-instanceconfiguration-syntax.yaml"></a>

```
  [Cpu](#cfn-apprunner-service-instanceconfiguration-cpu): {{String}}
  [InstanceRoleArn](#cfn-apprunner-service-instanceconfiguration-instancerolearn): {{String}}
  [Memory](#cfn-apprunner-service-instanceconfiguration-memory): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-instanceconfiguration-properties"></a>

`Cpu`  <a name="cfn-apprunner-service-instanceconfiguration-cpu"></a>
The number of CPU units reserved for each instance of your App Runner service.
Default: `1 vCPU`
*Required*: No
*Type*: String
*Pattern*: `256|512|1024|2048|4096|(0.25|0.5|1|2|4) vCPU`
*Minimum*: `3`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRoleArn`  <a name="cfn-apprunner-service-instanceconfiguration-instancerolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any AWS APIs.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
*Minimum*: `29`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Memory`  <a name="cfn-apprunner-service-instanceconfiguration-memory"></a>
The amount of memory, in MB or GB, reserved for each instance of your App Runner service.
Default: `2 GB`
*Required*: No
*Type*: String
*Pattern*: `512|1024|2048|3072|4096|6144|8192|10240|12288|(0.5|1|2|3|4|6|8|10|12) GB`
*Minimum*: `3`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
