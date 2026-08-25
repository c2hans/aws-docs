---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elementalinference-feed-clippingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Feed ClippingConfig
<a name="aws-properties-elementalinference-feed-clippingconfig"></a>

A type of OutputConfig, used when the output in a feed is for the clip feature.

## Syntax
<a name="aws-properties-elementalinference-feed-clippingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elementalinference-feed-clippingconfig-syntax.json"></a>

```
{
  "[CallbackMetadata](#cfn-elementalinference-feed-clippingconfig-callbackmetadata)" : {{String}},
  "[DataSourceConfiguration](#cfn-elementalinference-feed-clippingconfig-datasourceconfiguration)" : {{DataSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-elementalinference-feed-clippingconfig-syntax.yaml"></a>

```
  [CallbackMetadata](#cfn-elementalinference-feed-clippingconfig-callbackmetadata): {{String}}
  [DataSourceConfiguration](#cfn-elementalinference-feed-clippingconfig-datasourceconfiguration): {{
    DataSourceConfiguration}}
```

## Properties
<a name="aws-properties-elementalinference-feed-clippingconfig-properties"></a>

`CallbackMetadata`  <a name="cfn-elementalinference-feed-clippingconfig-callbackmetadata"></a>
Metadata that you want to include in the event that Elemental Inference sends to Amazon EventBridge. The metadata can help you distinguish between different events.
*Required*: No
*Type*: String
*Pattern*: `^[\w \-\.',@:;]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceConfiguration`  <a name="cfn-elementalinference-feed-clippingconfig-datasourceconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [DataSourceConfiguration](aws-properties-elementalinference-feed-datasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
