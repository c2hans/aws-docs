---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-responseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ResponseConfiguration
<a name="aws-properties-glue-connectiontype-responseconfiguration"></a>

<a name="aws-properties-glue-connectiontype-responseconfiguration-description"></a>The `ResponseConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-responseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-responseconfiguration-syntax.json"></a>

```
{
  "[ErrorPath](#cfn-glue-connectiontype-responseconfiguration-errorpath)" : {{String}},
  "[ResultPath](#cfn-glue-connectiontype-responseconfiguration-resultpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-responseconfiguration-syntax.yaml"></a>

```
  [ErrorPath](#cfn-glue-connectiontype-responseconfiguration-errorpath): {{String}}
  [ResultPath](#cfn-glue-connectiontype-responseconfiguration-resultpath): {{String}}
```

## Properties
<a name="aws-properties-glue-connectiontype-responseconfiguration-properties"></a>

`ErrorPath`  <a name="cfn-glue-connectiontype-responseconfiguration-errorpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResultPath`  <a name="cfn-glue-connectiontype-responseconfiguration-resultpath"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
