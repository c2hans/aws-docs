---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3vectors-index-textsearchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::Index TextSearchConfiguration

A full-text search configuration for a single metadata key.

## Syntax
<a name="aws-properties-s3vectors-index-textsearchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3vectors-index-textsearchconfiguration-syntax.json"></a>

```json
{
  "[Language](#cfn-s3vectors-index-textsearchconfiguration-language)" : {{String}},
  "[MetadataKey](#cfn-s3vectors-index-textsearchconfiguration-metadatakey)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3vectors-index-textsearchconfiguration-syntax.yaml"></a>

```yaml
  [Language](#cfn-s3vectors-index-textsearchconfiguration-language): {{String}}
  [MetadataKey](#cfn-s3vectors-index-textsearchconfiguration-metadatakey): {{String}}
```

## Properties
<a name="aws-properties-s3vectors-index-textsearchconfiguration-properties"></a>

`Language`  <a name="cfn-s3vectors-index-textsearchconfiguration-language"></a>
The language that the text search analyzer uses. Valid values are `en` (English), `fr` (French), `es` (Spanish), `pt` (Portuguese), `it` (Italian), `de` (German), `nl` (Dutch), `zh` (Chinese), `ja` (Japanese), and `ko` (Korean). If you don't specify a language, Amazon S3 Vectors uses the default standard analyzer.
*Required*: No
*Type*: String
*Allowed values*: `en | fr | es | pt | it | de | nl | zh | ja | ko`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataKey`  <a name="cfn-s3vectors-index-textsearchconfiguration-metadatakey"></a>
The metadata key to make full-text searchable.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
