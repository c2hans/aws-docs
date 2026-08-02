---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinitionVersion LocalDeviceResourceData
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata"></a>

<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-description"></a>Settings for a local device resource, which represents a file under `/dev`. For more information, see [Access Local Resources with Lambda Functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-local-resources.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-inheritance"></a> In an CloudFormation template, `LocalDeviceResourceData` can be used in the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html) property type.

## Syntax
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-syntax.json"></a>

```
{
  "[GroupOwnerSetting](#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting)" : {{GroupOwnerSetting}},
  "[SourcePath](#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-syntax.yaml"></a>

```
  [GroupOwnerSetting](#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting): {{
    GroupOwnerSetting}}
  [SourcePath](#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata-properties"></a>

`GroupOwnerSetting`  <a name="cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting"></a>
Settings that define additional Linux OS group permissions to give to the Lambda function process.
*Required*: No
*Type*: [GroupOwnerSetting](aws-properties-greengrass-resourcedefinitionversion-groupownersetting.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourcePath`  <a name="cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath"></a>
The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under `/dev`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata--seealso"></a>
+ [LocalDeviceResourceData](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-localdeviceresourcedata.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
