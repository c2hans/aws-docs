---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-documentattributeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index DocumentAttributeConfiguration
<a name="aws-properties-qbusiness-index-documentattributeconfiguration"></a>

Configuration information for document attributes. Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document.

For more information, see [Understanding document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html).

## Syntax
<a name="aws-properties-qbusiness-index-documentattributeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-documentattributeconfiguration-syntax.json"></a>

```
{
  "[Name](#cfn-qbusiness-index-documentattributeconfiguration-name)" : {{String}},
  "[Search](#cfn-qbusiness-index-documentattributeconfiguration-search)" : {{String}},
  "[Type](#cfn-qbusiness-index-documentattributeconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-documentattributeconfiguration-syntax.yaml"></a>

```
  [Name](#cfn-qbusiness-index-documentattributeconfiguration-name): {{String}}
  [Search](#cfn-qbusiness-index-documentattributeconfiguration-search): {{String}}
  [Type](#cfn-qbusiness-index-documentattributeconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-index-documentattributeconfiguration-properties"></a>

`Name`  <a name="cfn-qbusiness-index-documentattributeconfiguration-name"></a>
The name of the document attribute.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Search`  <a name="cfn-qbusiness-index-documentattributeconfiguration-search"></a>
Information about whether the document attribute can be used by an end user to search for information on their web experience.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-qbusiness-index-documentattributeconfiguration-type"></a>
The type of document attribute.
*Required*: No
*Type*: String
*Allowed values*: `STRING | STRING_LIST | NUMBER | DATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
