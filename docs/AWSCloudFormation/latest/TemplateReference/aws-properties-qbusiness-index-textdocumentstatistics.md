---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-textdocumentstatistics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index TextDocumentStatistics
<a name="aws-properties-qbusiness-index-textdocumentstatistics"></a>

Provides information about text documents in an index.

## Syntax
<a name="aws-properties-qbusiness-index-textdocumentstatistics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-textdocumentstatistics-syntax.json"></a>

```
{
  "[IndexedTextBytes](#cfn-qbusiness-index-textdocumentstatistics-indexedtextbytes)" : {{Number}},
  "[IndexedTextDocumentCount](#cfn-qbusiness-index-textdocumentstatistics-indexedtextdocumentcount)" : {{Number}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-textdocumentstatistics-syntax.yaml"></a>

```
  [IndexedTextBytes](#cfn-qbusiness-index-textdocumentstatistics-indexedtextbytes): {{Number}}
  [IndexedTextDocumentCount](#cfn-qbusiness-index-textdocumentstatistics-indexedtextdocumentcount): {{Number}}
```

## Properties
<a name="aws-properties-qbusiness-index-textdocumentstatistics-properties"></a>

`IndexedTextBytes`  <a name="cfn-qbusiness-index-textdocumentstatistics-indexedtextbytes"></a>
The total size, in bytes, of the indexed documents.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexedTextDocumentCount`  <a name="cfn-qbusiness-index-textdocumentstatistics-indexedtextdocumentcount"></a>
The number of text documents indexed.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
