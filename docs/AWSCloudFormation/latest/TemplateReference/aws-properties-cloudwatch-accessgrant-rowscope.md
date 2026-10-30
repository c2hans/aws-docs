---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-accessgrant-rowscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant RowScope
<a name="aws-properties-cloudwatch-accessgrant-rowscope"></a>

A single additive row-level filter on an access grant. A row is visible when its value for the given field matches the filter's values.

## Syntax
<a name="aws-properties-cloudwatch-accessgrant-rowscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-accessgrant-rowscope-syntax.json"></a>

```
{
  "[Field](#cfn-cloudwatch-accessgrant-rowscope-field)" : {{String}},
  "[Operator](#cfn-cloudwatch-accessgrant-rowscope-operator)" : {{String}},
  "[Values](#cfn-cloudwatch-accessgrant-rowscope-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-accessgrant-rowscope-syntax.yaml"></a>

```
  [Field](#cfn-cloudwatch-accessgrant-rowscope-field): {{String}}
  [Operator](#cfn-cloudwatch-accessgrant-rowscope-operator): {{String}}
  [Values](#cfn-cloudwatch-accessgrant-rowscope-values): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudwatch-accessgrant-rowscope-properties"></a>

`Field`  <a name="cfn-cloudwatch-accessgrant-rowscope-field"></a>
The field the allowlist applies to, for example serviceName or accountId.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Operator`  <a name="cfn-cloudwatch-accessgrant-rowscope-operator"></a>
Match operator applied to this filter's values.
*Required*: Yes
*Type*: String
*Allowed values*: `IN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-cloudwatch-accessgrant-rowscope-values"></a>
The values the field is matched against.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
