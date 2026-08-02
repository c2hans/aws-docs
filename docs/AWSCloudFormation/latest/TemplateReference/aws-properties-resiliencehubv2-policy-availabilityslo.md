---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-policy-availabilityslo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy AvailabilitySlo
<a name="aws-properties-resiliencehubv2-policy-availabilityslo"></a>

Defines the availability service level objective (SLO) for a resilience policy.

## Syntax
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax.json"></a>

```
{
  "[Target](#cfn-resiliencehubv2-policy-availabilityslo-target)" : {{Number}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax.yaml"></a>

```
  [Target](#cfn-resiliencehubv2-policy-availabilityslo-target): {{Number}}
```

## Properties
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-properties"></a>

`Target`  <a name="cfn-resiliencehubv2-policy-availabilityslo-target"></a>
The target availability percentage, expressed as a value between 0 and 100.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
