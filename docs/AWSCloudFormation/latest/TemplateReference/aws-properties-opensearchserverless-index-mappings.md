---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-mappings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index Mappings
<a name="aws-properties-opensearchserverless-index-mappings"></a>

Index mappings for the OpenSearch Serverless index.

## Syntax
<a name="aws-properties-opensearchserverless-index-mappings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-mappings-syntax.json"></a>

```
{
  "[Properties](#cfn-opensearchserverless-index-mappings-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-mappings-syntax.yaml"></a>

```
  [Properties](#cfn-opensearchserverless-index-mappings-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-mappings-properties"></a>

`Properties`  <a name="cfn-opensearchserverless-index-mappings-properties"></a>
A map of the fields in the index, where each key is a field name that you choose and each value is that field's mapping. The field-name key is required: specify the field's `Type` and other settings under the field name, not directly under `Properties`. To define a nested field, give the field its own `Properties` map.
*Required*: No
*Type*: Object of [PropertyMapping](aws-properties-opensearchserverless-index-propertymapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
