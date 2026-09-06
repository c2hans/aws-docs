---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service ResourceTag
<a name="aws-properties-resiliencehubv2-service-resourcetag"></a>

A tag key-value pair used for resource discovery.

## Syntax
<a name="aws-properties-resiliencehubv2-service-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-resiliencehubv2-service-resourcetag-key)" : {{String}},
  "[Values](#cfn-resiliencehubv2-service-resourcetag-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-resiliencehubv2-service-resourcetag-key): {{String}}
  [Values](#cfn-resiliencehubv2-service-resourcetag-values): {{
    - String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-resourcetag-properties"></a>

`Key`  <a name="cfn-resiliencehubv2-service-resourcetag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-resiliencehubv2-service-resourcetag-values"></a>
The list of tag values.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
