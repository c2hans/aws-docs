---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-slosource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service SloSource
<a name="aws-properties-resiliencehubv2-service-slosource"></a>

Contains the effective availability SLO value and its source.

## Syntax
<a name="aws-properties-resiliencehubv2-service-slosource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-slosource-syntax.json"></a>

```
{
  "[PolicyName](#cfn-resiliencehubv2-service-slosource-policyname)" : {{String}},
  "[Value](#cfn-resiliencehubv2-service-slosource-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-slosource-syntax.yaml"></a>

```
  [PolicyName](#cfn-resiliencehubv2-service-slosource-policyname): {{String}}
  [Value](#cfn-resiliencehubv2-service-slosource-value): {{Number}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-slosource-properties"></a>

`PolicyName`  <a name="cfn-resiliencehubv2-service-slosource-policyname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-resiliencehubv2-service-slosource-value"></a>
The availability SLO percentage value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
