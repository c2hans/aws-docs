---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-ekslabelselectorrequirement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service EksLabelSelectorRequirement
<a name="aws-properties-resiliencehubv2-service-ekslabelselectorrequirement"></a>

A single label requirement in a label selector, expressed as a key, an operator, and an optional list of values.

## Syntax
<a name="aws-properties-resiliencehubv2-service-ekslabelselectorrequirement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-ekslabelselectorrequirement-syntax.json"></a>

```
{
  "[Key](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-key)" : {{String}},
  "[Operator](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-operator)" : {{String}},
  "[Values](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-ekslabelselectorrequirement-syntax.yaml"></a>

```
  [Key](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-key): {{String}}
  [Operator](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-operator): {{String}}
  [Values](#cfn-resiliencehubv2-service-ekslabelselectorrequirement-values): {{
    - String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-ekslabelselectorrequirement-properties"></a>

`Key`  <a name="cfn-resiliencehubv2-service-ekslabelselectorrequirement-key"></a>
The label key that the requirement applies to.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z0-9]([-a-z0-9.]{0,251}[a-z0-9])?/)?[a-zA-Z0-9]([-a-zA-Z0-9_.]{0,61}[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `317`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-resiliencehubv2-service-ekslabelselectorrequirement-operator"></a>
The operator that relates the label key to the values.
*Required*: Yes
*Type*: String
*Allowed values*: `IN | NOT_IN | EXISTS | DOES_NOT_EXIST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-resiliencehubv2-service-ekslabelselectorrequirement-values"></a>
The label values to compare against. Specify values when the operator is IN or NOT\_IN. Leave this empty when the operator is EXISTS or DOES\_NOT\_EXIST.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 1`
*Maximum*: `63 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
