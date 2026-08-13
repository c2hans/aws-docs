---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinitionVersion GroupOwnerSetting
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting"></a>

<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-description"></a>Settings that define additional Linux OS group permissions to give to the Lambda function process. You can give the permissions of the Linux group that owns the resource or choose another Linux group. These permissions are in addition to the function's `RunAs` permissions.

<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-inheritance"></a> In an CloudFormation template, `GroupOwnerSetting` is a property of the [`LocalDeviceResourceData`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html) and [`LocalVolumeResourceData`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html) property types.

## Syntax
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-syntax.json"></a>

```
{
  "[AutoAddGroupOwner](#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner)" : {{Boolean}},
  "[GroupOwner](#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-syntax.yaml"></a>

```
  [AutoAddGroupOwner](#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner): {{Boolean}}
  [GroupOwner](#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting-properties"></a>

`AutoAddGroupOwner`  <a name="cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner"></a>
Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process. This gives the Lambda process the file access permissions of the Linux group.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupOwner`  <a name="cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner"></a>
The name of the Linux group whose privileges you want to add to the Lambda process. This value is ignored if `AutoAddGroupOwner` is true.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinitionversion-groupownersetting--seealso"></a>
+ [GroupOwnerSetting](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupownersetting.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
