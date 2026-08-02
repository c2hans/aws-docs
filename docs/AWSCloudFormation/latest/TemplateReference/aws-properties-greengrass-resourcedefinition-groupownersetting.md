---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinition-groupownersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinition GroupOwnerSetting
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting"></a>

<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-description"></a>Settings that define additional Linux OS group permissions to give to the Lambda function process. You can give the permissions of the Linux group that owns the resource or choose another Linux group. These permissions are in addition to the function's `RunAs` permissions.

<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-inheritance"></a> In an CloudFormation template, `GroupOwnerSetting` is a property of the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html) and [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html) property types.

## Syntax
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-syntax.json"></a>

```
{
  "[AutoAddGroupOwner](#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner)" : {{Boolean}},
  "[GroupOwner](#cfn-greengrass-resourcedefinition-groupownersetting-groupowner)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-syntax.yaml"></a>

```
  [AutoAddGroupOwner](#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner): {{Boolean}}
  [GroupOwner](#cfn-greengrass-resourcedefinition-groupownersetting-groupowner): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting-properties"></a>

`AutoAddGroupOwner`  <a name="cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner"></a>
Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process. This gives the Lambda process the file access permissions of the Linux group.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupOwner`  <a name="cfn-greengrass-resourcedefinition-groupownersetting-groupowner"></a>
The name of the Linux group whose privileges you want to add to the Lambda process. This value is ignored if `AutoAddGroupOwner` is true.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinition-groupownersetting--seealso"></a>
+ [GroupOwnerSetting](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupownersetting.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
