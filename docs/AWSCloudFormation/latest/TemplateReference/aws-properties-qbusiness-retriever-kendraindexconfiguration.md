---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-retriever-kendraindexconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Retriever KendraIndexConfiguration
<a name="aws-properties-qbusiness-retriever-kendraindexconfiguration"></a>

Stores an Amazon Kendra index as a retriever.

## Syntax
<a name="aws-properties-qbusiness-retriever-kendraindexconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-retriever-kendraindexconfiguration-syntax.json"></a>

```
{
  "[IndexId](#cfn-qbusiness-retriever-kendraindexconfiguration-indexid)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-retriever-kendraindexconfiguration-syntax.yaml"></a>

```
  [IndexId](#cfn-qbusiness-retriever-kendraindexconfiguration-indexid): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-retriever-kendraindexconfiguration-properties"></a>

`IndexId`  <a name="cfn-qbusiness-retriever-kendraindexconfiguration-indexid"></a>
The identifier of the Amazon Kendra index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
