---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-responseextractionmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ResponseExtractionMapping
<a name="aws-properties-glue-connectiontype-responseextractionmapping"></a>

<a name="aws-properties-glue-connectiontype-responseextractionmapping-description"></a>The `ResponseExtractionMapping` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-responseextractionmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-responseextractionmapping-syntax.json"></a>

```
{
  "[ContentPath](#cfn-glue-connectiontype-responseextractionmapping-contentpath)" : {{String}},
  "[HeaderKey](#cfn-glue-connectiontype-responseextractionmapping-headerkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-responseextractionmapping-syntax.yaml"></a>

```
  [ContentPath](#cfn-glue-connectiontype-responseextractionmapping-contentpath): {{String}}
  [HeaderKey](#cfn-glue-connectiontype-responseextractionmapping-headerkey): {{String}}
```

## Properties
<a name="aws-properties-glue-connectiontype-responseextractionmapping-properties"></a>

`ContentPath`  <a name="cfn-glue-connectiontype-responseextractionmapping-contentpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HeaderKey`  <a name="cfn-glue-connectiontype-responseextractionmapping-headerkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
