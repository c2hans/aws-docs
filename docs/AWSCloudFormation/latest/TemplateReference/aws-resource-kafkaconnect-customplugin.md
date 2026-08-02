---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kafkaconnect-customplugin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::CustomPlugin
<a name="aws-resource-kafkaconnect-customplugin"></a>

Creates a custom plugin using the specified properties.

## Syntax
<a name="aws-resource-kafkaconnect-customplugin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kafkaconnect-customplugin-syntax.json"></a>

```
{
  "Type" : "AWS::KafkaConnect::CustomPlugin",
  "Properties" : {
      "[ContentType](#cfn-kafkaconnect-customplugin-contenttype)" : {{String}},
      "[Description](#cfn-kafkaconnect-customplugin-description)" : {{String}},
      "[Location](#cfn-kafkaconnect-customplugin-location)" : {{CustomPluginLocation}},
      "[Name](#cfn-kafkaconnect-customplugin-name)" : {{String}},
      "[Tags](#cfn-kafkaconnect-customplugin-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kafkaconnect-customplugin-syntax.yaml"></a>

```
Type: AWS::KafkaConnect::CustomPlugin
Properties:
  [ContentType](#cfn-kafkaconnect-customplugin-contenttype): {{String}}
  [Description](#cfn-kafkaconnect-customplugin-description): {{String}}
  [Location](#cfn-kafkaconnect-customplugin-location): {{
    CustomPluginLocation}}
  [Name](#cfn-kafkaconnect-customplugin-name): {{String}}
  [Tags](#cfn-kafkaconnect-customplugin-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kafkaconnect-customplugin-properties"></a>

`ContentType`  <a name="cfn-kafkaconnect-customplugin-contenttype"></a>
The format of the plugin file.
*Required*: Yes
*Type*: String
*Allowed values*: `JAR | ZIP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-kafkaconnect-customplugin-description"></a>
The description of the custom plugin.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-kafkaconnect-customplugin-location"></a>
Information about the location of the custom plugin.
*Required*: Yes
*Type*: [CustomPluginLocation](aws-properties-kafkaconnect-customplugin-custompluginlocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-kafkaconnect-customplugin-name"></a>
The name of the custom plugin.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-kafkaconnect-customplugin-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kafkaconnect-customplugin-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kafkaconnect-customplugin-return-values"></a>

### Ref
<a name="aws-resource-kafkaconnect-customplugin-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kafkaconnect-customplugin-return-values-fn--getatt"></a>

####
<a name="aws-resource-kafkaconnect-customplugin-return-values-fn--getatt-fn--getatt"></a>

`CustomPluginArn`  <a name="CustomPluginArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the custom plugin.

`Revision`  <a name="Revision-fn::getatt"></a>
The revision of the custom plugin.
