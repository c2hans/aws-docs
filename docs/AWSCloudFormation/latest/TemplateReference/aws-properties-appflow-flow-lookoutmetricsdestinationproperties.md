---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-lookoutmetricsdestinationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow LookoutMetricsDestinationProperties
<a name="aws-properties-appflow-flow-lookoutmetricsdestinationproperties"></a>

 The properties that are applied when Amazon Lookout for Metrics is used as a destination.

## Syntax
<a name="aws-properties-appflow-flow-lookoutmetricsdestinationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-lookoutmetricsdestinationproperties-syntax.json"></a>

```
{
  "[Object](#cfn-appflow-flow-lookoutmetricsdestinationproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-lookoutmetricsdestinationproperties-syntax.yaml"></a>

```
  [Object](#cfn-appflow-flow-lookoutmetricsdestinationproperties-object): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-lookoutmetricsdestinationproperties-properties"></a>

`Object`  <a name="cfn-appflow-flow-lookoutmetricsdestinationproperties-object"></a>
 The object specified in the Amazon Lookout for Metrics flow destination.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
