---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-retriever-retrieverconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Retriever RetrieverConfiguration
<a name="aws-properties-qbusiness-retriever-retrieverconfiguration"></a>

Provides information on how the retriever used for your Amazon Q Business application is configured.

## Syntax
<a name="aws-properties-qbusiness-retriever-retrieverconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-retriever-retrieverconfiguration-syntax.json"></a>

```
{
  "[KendraIndexConfiguration](#cfn-qbusiness-retriever-retrieverconfiguration-kendraindexconfiguration)" : {{KendraIndexConfiguration}},
  "[NativeIndexConfiguration](#cfn-qbusiness-retriever-retrieverconfiguration-nativeindexconfiguration)" : {{NativeIndexConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-retriever-retrieverconfiguration-syntax.yaml"></a>

```
  [KendraIndexConfiguration](#cfn-qbusiness-retriever-retrieverconfiguration-kendraindexconfiguration): {{
    KendraIndexConfiguration}}
  [NativeIndexConfiguration](#cfn-qbusiness-retriever-retrieverconfiguration-nativeindexconfiguration): {{
    NativeIndexConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-retriever-retrieverconfiguration-properties"></a>

`KendraIndexConfiguration`  <a name="cfn-qbusiness-retriever-retrieverconfiguration-kendraindexconfiguration"></a>
Provides information on how the Amazon Kendra index used as a retriever for your Amazon Q Business application is configured.
*Required*: No
*Type*: [KendraIndexConfiguration](aws-properties-qbusiness-retriever-kendraindexconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NativeIndexConfiguration`  <a name="cfn-qbusiness-retriever-retrieverconfiguration-nativeindexconfiguration"></a>
Provides information on how a Amazon Q Business index used as a retriever for your Amazon Q Business application is configured.
*Required*: No
*Type*: [NativeIndexConfiguration](aws-properties-qbusiness-retriever-nativeindexconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
