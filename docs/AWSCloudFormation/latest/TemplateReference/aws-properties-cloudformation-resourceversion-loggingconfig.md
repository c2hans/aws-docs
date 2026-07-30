---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-resourceversion-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ResourceVersion LoggingConfig
<a name="aws-properties-cloudformation-resourceversion-loggingconfig"></a>

Logging configuration information for a resource.

## Syntax
<a name="aws-properties-cloudformation-resourceversion-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-resourceversion-loggingconfig-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-cloudformation-resourceversion-loggingconfig-loggroupname)" : {{String}},
  "[LogRoleArn](#cfn-cloudformation-resourceversion-loggingconfig-logrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-resourceversion-loggingconfig-syntax.yaml"></a>

```
  [LogGroupName](#cfn-cloudformation-resourceversion-loggingconfig-loggroupname): {{String}}
  [LogRoleArn](#cfn-cloudformation-resourceversion-loggingconfig-logrolearn): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-resourceversion-loggingconfig-properties"></a>

`LogGroupName`  <a name="cfn-cloudformation-resourceversion-loggingconfig-loggroupname"></a>
The Amazon CloudWatch logs group to which CloudFormation sends error logging information when invoking the type's handlers.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogRoleArn`  <a name="cfn-cloudformation-resourceversion-loggingconfig-logrolearn"></a>
The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
