---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-indexstatistics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index IndexStatistics
<a name="aws-properties-qbusiness-index-indexstatistics"></a>

Provides information about the number of documents in an index.

## Syntax
<a name="aws-properties-qbusiness-index-indexstatistics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-indexstatistics-syntax.json"></a>

```
{
  "[TextDocumentStatistics](#cfn-qbusiness-index-indexstatistics-textdocumentstatistics)" : {{TextDocumentStatistics}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-indexstatistics-syntax.yaml"></a>

```
  [TextDocumentStatistics](#cfn-qbusiness-index-indexstatistics-textdocumentstatistics): {{
    TextDocumentStatistics}}
```

## Properties
<a name="aws-properties-qbusiness-index-indexstatistics-properties"></a>

`TextDocumentStatistics`  <a name="cfn-qbusiness-index-indexstatistics-textdocumentstatistics"></a>
The number of documents indexed.
*Required*: No
*Type*: [TextDocumentStatistics](aws-properties-qbusiness-index-textdocumentstatistics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
