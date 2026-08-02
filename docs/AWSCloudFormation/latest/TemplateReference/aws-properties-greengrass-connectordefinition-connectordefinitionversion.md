---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ConnectorDefinition ConnectorDefinitionVersion
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion"></a>

<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-description"></a>A connector definition version contains a list of connectors.

**Note**
After you create a connector definition version that contains the connectors you want to deploy, you must add it to your group version. For more information, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-inheritance"></a> In an CloudFormation template, `ConnectorDefinitionVersion` is the property type of the `InitialVersion` property in the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-syntax.json"></a>

```
{
  "[Connectors](#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors)" : {{[ Connector, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-syntax.yaml"></a>

```
  [Connectors](#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors): {{
    - Connector}}
```

## Properties
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion-properties"></a>

`Connectors`  <a name="cfn-greengrass-connectordefinition-connectordefinitionversion-connectors"></a>
The connectors in this version. Only one instance of a given connector can be added to a connector definition version at a time.
*Required*: Yes
*Type*: Array of [Connector](aws-properties-greengrass-connectordefinition-connector.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-connectordefinition-connectordefinitionversion--seealso"></a>
+ [ConnectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectordefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
