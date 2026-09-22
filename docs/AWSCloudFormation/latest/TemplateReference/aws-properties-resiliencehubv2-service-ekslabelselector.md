---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-ekslabelselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service EksLabelSelector
<a name="aws-properties-resiliencehubv2-service-ekslabelselector"></a>

A label selector that filters the Kubernetes objects discovered from an Amazon EKS input source. An object must satisfy both matchLabels and matchExpressions to match the selector. A selector with neither matches every object. The selector must render to 2,048 characters or fewer in Kubernetes label selector syntax.

## Syntax
<a name="aws-properties-resiliencehubv2-service-ekslabelselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-ekslabelselector-syntax.json"></a>

```
{
  "[MatchExpressions](#cfn-resiliencehubv2-service-ekslabelselector-matchexpressions)" : {{[ EksLabelSelectorRequirement, ... ]}},
  "[MatchLabels](#cfn-resiliencehubv2-service-ekslabelselector-matchlabels)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-ekslabelselector-syntax.yaml"></a>

```
  [MatchExpressions](#cfn-resiliencehubv2-service-ekslabelselector-matchexpressions): {{
    - EksLabelSelectorRequirement}}
  [MatchLabels](#cfn-resiliencehubv2-service-ekslabelselector-matchlabels): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-ekslabelselector-properties"></a>

`MatchExpressions`  <a name="cfn-resiliencehubv2-service-ekslabelselector-matchexpressions"></a>
The label requirements that an object must satisfy. All requirements in the list must match for the object to be selected.
*Required*: No
*Type*: Array of [EksLabelSelectorRequirement](aws-properties-resiliencehubv2-service-ekslabelselectorrequirement.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchLabels`  <a name="cfn-resiliencehubv2-service-ekslabelselector-matchlabels"></a>
The label key-value pairs that an object must have. All pairs must match for the object to be selected.
*Required*: No
*Type*: Object of String
*Pattern*: `^([a-z0-9]([-a-z0-9.]{0,251}[a-z0-9])?/)?[a-zA-Z0-9]([-a-zA-Z0-9_.]{0,61}[a-zA-Z0-9])?$`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
