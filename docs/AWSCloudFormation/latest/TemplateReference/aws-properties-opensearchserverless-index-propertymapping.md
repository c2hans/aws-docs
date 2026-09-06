---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-propertymapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index PropertyMapping
<a name="aws-properties-opensearchserverless-index-propertymapping"></a>

Property mappings for the OpenSearch Serverless index.

## Syntax
<a name="aws-properties-opensearchserverless-index-propertymapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-propertymapping-syntax.json"></a>

```
{
  "[Analyzer](#cfn-opensearchserverless-index-propertymapping-analyzer)" : {{String}},
  "[CompressionLevel](#cfn-opensearchserverless-index-propertymapping-compressionlevel)" : {{String}},
  "[DataType](#cfn-opensearchserverless-index-propertymapping-datatype)" : {{String}},
  "[Dimension](#cfn-opensearchserverless-index-propertymapping-dimension)" : {{Integer}},
  "[Index](#cfn-opensearchserverless-index-propertymapping-index)" : {{Boolean}},
  "[Method](#cfn-opensearchserverless-index-propertymapping-method)" : {{Method}},
  "[Properties](#cfn-opensearchserverless-index-propertymapping-properties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SpaceType](#cfn-opensearchserverless-index-propertymapping-spacetype)" : {{String}},
  "[Type](#cfn-opensearchserverless-index-propertymapping-type)" : {{String}},
  "[Value](#cfn-opensearchserverless-index-propertymapping-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-propertymapping-syntax.yaml"></a>

```
  [Analyzer](#cfn-opensearchserverless-index-propertymapping-analyzer): {{String}}
  [CompressionLevel](#cfn-opensearchserverless-index-propertymapping-compressionlevel): {{String}}
  [DataType](#cfn-opensearchserverless-index-propertymapping-datatype): {{String}}
  [Dimension](#cfn-opensearchserverless-index-propertymapping-dimension): {{Integer}}
  [Index](#cfn-opensearchserverless-index-propertymapping-index): {{Boolean}}
  [Method](#cfn-opensearchserverless-index-propertymapping-method): {{
    Method}}
  [Properties](#cfn-opensearchserverless-index-propertymapping-properties): {{
    {{Key}}: {{Value}}}}
  [SpaceType](#cfn-opensearchserverless-index-propertymapping-spacetype): {{String}}
  [Type](#cfn-opensearchserverless-index-propertymapping-type): {{String}}
  [Value](#cfn-opensearchserverless-index-propertymapping-value): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-propertymapping-properties"></a>

`Analyzer`  <a name="cfn-opensearchserverless-index-propertymapping-analyzer"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompressionLevel`  <a name="cfn-opensearchserverless-index-propertymapping-compressionlevel"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `16x | 32x | 8x | 4x | 2x | 1x`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-opensearchserverless-index-propertymapping-datatype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `float | byte`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimension`  <a name="cfn-opensearchserverless-index-propertymapping-dimension"></a>
Dimension size for vector fields, defines the number of dimensions in the vector.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Index`  <a name="cfn-opensearchserverless-index-propertymapping-index"></a>
Whether a field should be indexed.
*Required*: No
*Type*: [Boolean](aws-properties-opensearchserverless-index-index.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Method`  <a name="cfn-opensearchserverless-index-propertymapping-method"></a>
Configuration for k-NN search method.
*Required*: No
*Type*: [Method](aws-properties-opensearchserverless-index-method.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-opensearchserverless-index-propertymapping-properties"></a>
Defines the fields within the mapping, including their types and configurations.
*Required*: No
*Type*: Object of [PropertyMapping](#aws-properties-opensearchserverless-index-propertymapping)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceType`  <a name="cfn-opensearchserverless-index-propertymapping-spacetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `l2 | l1 | linf | cosinesimil | innerproduct | hamming`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-opensearchserverless-index-propertymapping-type"></a>
The field data type. Must be a valid OpenSearch field type.
*Required*: Yes
*Type*: String
*Allowed values*: `text | knn_vector | keyword | integer`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-opensearchserverless-index-propertymapping-value"></a>
Default value for the field when not specified in a document.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
