---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-packaginggroup-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingGroup LogConfiguration
<a name="aws-properties-mediapackage-packaginggroup-logconfiguration"></a>

Sets a custom Amazon CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: /aws/MediaPackage/EgressAccessLogs.

## Syntax
<a name="aws-properties-mediapackage-packaginggroup-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-packaginggroup-logconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackage-packaginggroup-logconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-mediapackage-packaginggroup-logconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-mediapackage-packaginggroup-logconfiguration-loggroupname"></a>
Sets a custom Amazon CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: /aws/MediaPackage/EgressAccessLogs.
*Required*: No
*Type*: String
*Pattern*: `\A\/aws\/MediaPackage\/[0-9a-zA-Z-_\/\.#]+\Z`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
