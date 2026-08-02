---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3vectors-index-metadataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::Index MetadataConfiguration
<a name="aws-properties-s3vectors-index-metadataconfiguration"></a>

The metadata configuration for the vector index. This configuration allows you to specify which metadata keys should be treated as non-filterable.

## Syntax
<a name="aws-properties-s3vectors-index-metadataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3vectors-index-metadataconfiguration-syntax.json"></a>

```
{
  "[NonFilterableMetadataKeys](#cfn-s3vectors-index-metadataconfiguration-nonfilterablemetadatakeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-s3vectors-index-metadataconfiguration-syntax.yaml"></a>

```
  [NonFilterableMetadataKeys](#cfn-s3vectors-index-metadataconfiguration-nonfilterablemetadatakeys): {{
    - String}}
```

## Properties
<a name="aws-properties-s3vectors-index-metadataconfiguration-properties"></a>

`NonFilterableMetadataKeys`  <a name="cfn-s3vectors-index-metadataconfiguration-nonfilterablemetadatakeys"></a>
Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval. Unlike default metadata keys, these keys can't be used as query filters. Non-filterable metadata keys can be retrieved but can't be searched, queried, or filtered. You can access non-filterable metadata keys of your vectors after finding the vectors.
You can specify 1 to 10 non-filterable metadata keys. Each key must be 1 to 63 characters long.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `63 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
