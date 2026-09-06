---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-retriever-nativeindexconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Retriever NativeIndexConfiguration
<a name="aws-properties-qbusiness-retriever-nativeindexconfiguration"></a>

Configuration information for an Amazon Q Business index.

## Syntax
<a name="aws-properties-qbusiness-retriever-nativeindexconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-retriever-nativeindexconfiguration-syntax.json"></a>

```
{
  "[IndexId](#cfn-qbusiness-retriever-nativeindexconfiguration-indexid)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-retriever-nativeindexconfiguration-syntax.yaml"></a>

```
  [IndexId](#cfn-qbusiness-retriever-nativeindexconfiguration-indexid): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-retriever-nativeindexconfiguration-properties"></a>

`IndexId`  <a name="cfn-qbusiness-retriever-nativeindexconfiguration-indexid"></a>
The identifier for the Amazon Q Business index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
