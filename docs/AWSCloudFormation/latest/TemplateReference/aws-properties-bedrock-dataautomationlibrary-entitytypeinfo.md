---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationlibrary-entitytypeinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationLibrary EntityTypeInfo
<a name="aws-properties-bedrock-dataautomationlibrary-entitytypeinfo"></a>

Information about an entity type.

## Syntax
<a name="aws-properties-bedrock-dataautomationlibrary-entitytypeinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationlibrary-entitytypeinfo-syntax.json"></a>

```
{
  "[EntityMetadata](#cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitymetadata)" : {{String}},
  "[EntityType](#cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationlibrary-entitytypeinfo-syntax.yaml"></a>

```
  [EntityMetadata](#cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitymetadata): {{String}}
  [EntityType](#cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitytype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationlibrary-entitytypeinfo-properties"></a>

`EntityMetadata`  <a name="cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitymetadata"></a>
Metadata about the entity type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityType`  <a name="cfn-bedrock-dataautomationlibrary-entitytypeinfo-entitytype"></a>
The entity type.
*Required*: Yes
*Type*: String
*Allowed values*: `VOCABULARY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
