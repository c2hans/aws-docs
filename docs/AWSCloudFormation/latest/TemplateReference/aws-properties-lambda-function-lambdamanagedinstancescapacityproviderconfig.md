---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function LambdaManagedInstancesCapacityProviderConfig
<a name="aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig"></a>

Configuration for Lambda-managed instances used by the capacity provider.

## Syntax
<a name="aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig-syntax.json"></a>

```
{
  "[CapacityProviderArn](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-capacityproviderarn)" : {{String}},
  "[ExecutionEnvironmentMemoryGiBPerVCpu](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-executionenvironmentmemorygibpervcpu)" : {{Number}},
  "[PerExecutionEnvironmentMaxConcurrency](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-perexecutionenvironmentmaxconcurrency)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig-syntax.yaml"></a>

```
  [CapacityProviderArn](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-capacityproviderarn): {{String}}
  [ExecutionEnvironmentMemoryGiBPerVCpu](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-executionenvironmentmemorygibpervcpu): {{Number}}
  [PerExecutionEnvironmentMaxConcurrency](#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-perexecutionenvironmentmaxconcurrency): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig-properties"></a>

`CapacityProviderArn`  <a name="cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-capacityproviderarn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionEnvironmentMemoryGiBPerVCpu`  <a name="cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-executionenvironmentmemorygibpervcpu"></a>
The amount of memory in GiB allocated per vCPU for execution environments.
*Required*: No
*Type*: Number
*Minimum*: `2`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerExecutionEnvironmentMaxConcurrency`  <a name="cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig-perexecutionenvironmentmaxconcurrency"></a>
The maximum number of concurrent executions that can run on each execution environment.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
