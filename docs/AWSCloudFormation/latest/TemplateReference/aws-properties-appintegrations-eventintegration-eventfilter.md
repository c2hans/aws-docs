---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appintegrations-eventintegration-eventfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::EventIntegration EventFilter
<a name="aws-properties-appintegrations-eventintegration-eventfilter"></a>

The event integration filter.

## Syntax
<a name="aws-properties-appintegrations-eventintegration-eventfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appintegrations-eventintegration-eventfilter-syntax.json"></a>

```
{
  "[Source](#cfn-appintegrations-eventintegration-eventfilter-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-appintegrations-eventintegration-eventfilter-syntax.yaml"></a>

```
  [Source](#cfn-appintegrations-eventintegration-eventfilter-source): {{String}}
```

## Properties
<a name="aws-properties-appintegrations-eventintegration-eventfilter-properties"></a>

`Source`  <a name="cfn-appintegrations-eventintegration-eventfilter-source"></a>
The source of the events.
*Required*: Yes
*Type*: String
*Pattern*: `^aws\.(partner\/.*|cases)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
