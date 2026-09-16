---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-restconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType RestConfiguration
<a name="aws-properties-glue-connectiontype-restconfiguration"></a>

<a name="aws-properties-glue-connectiontype-restconfiguration-description"></a>The `RestConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-restconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-restconfiguration-syntax.json"></a>

```
{
  "[EntityConfigurations](#cfn-glue-connectiontype-restconfiguration-entityconfigurations)" : {{{{{Key}}: {{Value}}, ...}}},
  "[GlobalSourceConfiguration](#cfn-glue-connectiontype-restconfiguration-globalsourceconfiguration)" : {{SourceConfiguration}},
  "[ValidationEndpointConfiguration](#cfn-glue-connectiontype-restconfiguration-validationendpointconfiguration)" : {{ValidationEndpointConfiguration}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-restconfiguration-syntax.yaml"></a>

```
  [EntityConfigurations](#cfn-glue-connectiontype-restconfiguration-entityconfigurations): {{
    {{Key}}: {{Value}}}}
  [GlobalSourceConfiguration](#cfn-glue-connectiontype-restconfiguration-globalsourceconfiguration): {{
    SourceConfiguration}}
  [ValidationEndpointConfiguration](#cfn-glue-connectiontype-restconfiguration-validationendpointconfiguration): {{
    ValidationEndpointConfiguration}}
```

## Properties
<a name="aws-properties-glue-connectiontype-restconfiguration-properties"></a>

`EntityConfigurations`  <a name="cfn-glue-connectiontype-restconfiguration-entityconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Object of [EntityConfiguration](aws-properties-glue-connectiontype-entityconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GlobalSourceConfiguration`  <a name="cfn-glue-connectiontype-restconfiguration-globalsourceconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [SourceConfiguration](aws-properties-glue-connectiontype-sourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationEndpointConfiguration`  <a name="cfn-glue-connectiontype-restconfiguration-validationendpointconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ValidationEndpointConfiguration](aws-properties-glue-connectiontype-validationendpointconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
