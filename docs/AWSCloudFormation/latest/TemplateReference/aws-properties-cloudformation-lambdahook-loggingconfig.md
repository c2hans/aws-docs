---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::LambdaHook LoggingConfig
<a name="aws-properties-cloudformation-lambdahook-loggingconfig"></a>

Contains logging configuration information for an extension.

## Syntax
<a name="aws-properties-cloudformation-lambdahook-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-lambdahook-loggingconfig-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-cloudformation-lambdahook-loggingconfig-loggroupname)" : {{String}},
  "[LogRoleArn](#cfn-cloudformation-lambdahook-loggingconfig-logrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-lambdahook-loggingconfig-syntax.yaml"></a>

```
  [LogGroupName](#cfn-cloudformation-lambdahook-loggingconfig-loggroupname): {{String}}
  [LogRoleArn](#cfn-cloudformation-lambdahook-loggingconfig-logrolearn): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-lambdahook-loggingconfig-properties"></a>

`LogGroupName`  <a name="cfn-cloudformation-lambdahook-loggingconfig-loggroupname"></a>
The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogRoleArn`  <a name="cfn-cloudformation-lambdahook-loggingconfig-logrolearn"></a>
The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.+:iam::[0-9]{12}:role/.+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
