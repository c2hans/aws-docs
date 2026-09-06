---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-imageloggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ImageLoggingConfiguration
<a name="aws-properties-imagebuilder-image-imageloggingconfiguration"></a>

The logging configuration that's defined for the image. Image Builder uses the defined settings to direct execution log output during image creation.

## Syntax
<a name="aws-properties-imagebuilder-image-imageloggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-imageloggingconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-imagebuilder-image-imageloggingconfiguration-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-imageloggingconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-imagebuilder-image-imageloggingconfiguration-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-imageloggingconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-imagebuilder-image-imageloggingconfiguration-loggroupname"></a>
The log group name that Image Builder uses for image creation. If not specified, the log group name defaults to `/aws/imagebuilder/image-name`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_/\.]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
