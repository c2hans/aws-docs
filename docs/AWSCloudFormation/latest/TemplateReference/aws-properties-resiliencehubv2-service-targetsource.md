---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-targetsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service TargetSource
<a name="aws-properties-resiliencehubv2-service-targetsource"></a>

Contains an effective RTO or RPO value and its source.

## Syntax
<a name="aws-properties-resiliencehubv2-service-targetsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-targetsource-syntax.json"></a>

```
{
  "[PolicyName](#cfn-resiliencehubv2-service-targetsource-policyname)" : {{String}},
  "[Value](#cfn-resiliencehubv2-service-targetsource-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-targetsource-syntax.yaml"></a>

```
  [PolicyName](#cfn-resiliencehubv2-service-targetsource-policyname): {{String}}
  [Value](#cfn-resiliencehubv2-service-targetsource-value): {{Integer}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-targetsource-properties"></a>

`PolicyName`  <a name="cfn-resiliencehubv2-service-targetsource-policyname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-resiliencehubv2-service-targetsource-value"></a>
The RTO or RPO value in minutes.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
