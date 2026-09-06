---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-indexcapacityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index IndexCapacityConfiguration
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration"></a>

Provides information about index capacity configuration.

## Syntax
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax.json"></a>

```
{
  "[Units](#cfn-qbusiness-index-indexcapacityconfiguration-units)" : {{Number}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax.yaml"></a>

```
  [Units](#cfn-qbusiness-index-indexcapacityconfiguration-units): {{Number}}
```

## Properties
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-properties"></a>

`Units`  <a name="cfn-qbusiness-index-indexcapacityconfiguration-units"></a>
The number of storage units configured for an Amazon Q Business index.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
