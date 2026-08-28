---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-functiondefinitionversion-execution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::FunctionDefinitionVersion Execution
<a name="aws-properties-greengrass-functiondefinitionversion-execution"></a>

<a name="aws-properties-greengrass-functiondefinitionversion-execution-description"></a>Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

<a name="aws-properties-greengrass-functiondefinitionversion-execution-inheritance"></a> In an CloudFormation template, `Execution` is a property of the [`DefaultConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html) property type for a function definition version and the [`Environment`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html) property type for a function.

## Syntax
<a name="aws-properties-greengrass-functiondefinitionversion-execution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-functiondefinitionversion-execution-syntax.json"></a>

```
{
  "[IsolationMode](#cfn-greengrass-functiondefinitionversion-execution-isolationmode)" : {{String}},
  "[RunAs](#cfn-greengrass-functiondefinitionversion-execution-runas)" : {{RunAs}}
}
```

### YAML
<a name="aws-properties-greengrass-functiondefinitionversion-execution-syntax.yaml"></a>

```
  [IsolationMode](#cfn-greengrass-functiondefinitionversion-execution-isolationmode): {{String}}
  [RunAs](#cfn-greengrass-functiondefinitionversion-execution-runas): {{
    RunAs}}
```

## Properties
<a name="aws-properties-greengrass-functiondefinitionversion-execution-properties"></a>

`IsolationMode`  <a name="cfn-greengrass-functiondefinitionversion-execution-isolationmode"></a>
The containerization that the Lambda function runs in. Valid values are `GreengrassContainer` or `NoContainer`. Typically, this is `GreengrassContainer`. For more information, see [Containerization](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-group-config.html#lambda-function-containerization) in the * AWS IoT Greengrass Version 1 Developer Guide *.
+ When set on the [`DefaultConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html) property of a function definition version, this setting is used as the default containerization for all Lambda functions in the function definition version.
+ When set on the [`Environment`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html) property of a function, this setting applies to the individual function and overrides the default. Omit this value to run the function with the default containerization.
We recommend that you run in a Greengrass container unless your business case requires that you run without containerization.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunAs`  <a name="cfn-greengrass-functiondefinitionversion-execution-runas"></a>
The user and group permissions used to run the Lambda function. Typically, this is the ggc\_user and ggc\_group. For more information, see [Run as](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-group-config.html#lambda-access-identity.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.
+ When set on the [`DefaultConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html) property of a function definition version, this setting is used as the default access identity for all Lambda functions in the function definition version.
+ When set on the [`Environment`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html) property of a function, this setting applies to the individual function and overrides the default. You can override the user, group, or both. Omit this value to run the function with the default permissions.
Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see [Running a Lambda Function as Root](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-group-config.html#lambda-running-as-root).
*Required*: No
*Type*: [RunAs](aws-properties-greengrass-functiondefinitionversion-runas.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-functiondefinitionversion-execution--seealso"></a>
+ [FunctionExecutionConfig](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functionexecutionconfig.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
