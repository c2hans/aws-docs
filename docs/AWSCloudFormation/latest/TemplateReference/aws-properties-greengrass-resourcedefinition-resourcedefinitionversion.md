---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinition ResourceDefinitionVersion
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion"></a>

<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-description"></a>A resource definition version contains a list of resources. (In CloudFormation, resources are named *resource instances*.)

**Note**
After you create a resource definition version that contains the resources you want to deploy, you must add it to your group version. For more information, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-inheritance"></a> In an CloudFormation template, `ResourceDefinitionVersion` is the property type of the `InitialVersion` property in the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-syntax.json"></a>

```
{
  "[Resources](#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources)" : {{[ ResourceInstance, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-syntax.yaml"></a>

```
  [Resources](#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources): {{
    - ResourceInstance}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion-properties"></a>

`Resources`  <a name="cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources"></a>
The resources in this version.
*Required*: Yes
*Type*: Array of [ResourceInstance](aws-properties-greengrass-resourcedefinition-resourceinstance.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinition-resourcedefinitionversion--seealso"></a>
+ [ResourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
