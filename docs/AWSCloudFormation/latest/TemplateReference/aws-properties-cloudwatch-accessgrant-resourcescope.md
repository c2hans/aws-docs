---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-accessgrant-resourcescope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant ResourceScope
<a name="aws-properties-cloudwatch-accessgrant-resourcescope"></a>

A single resource scope entry within an access grant. Associates a resource type with optional ARN patterns, tag conditions, and row-level filters.

## Syntax
<a name="aws-properties-cloudwatch-accessgrant-resourcescope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-accessgrant-resourcescope-syntax.json"></a>

```
{
  "[ResourceArns](#cfn-cloudwatch-accessgrant-resourcescope-resourcearns)" : {{[ String, ... ]}},
  "[ResourceType](#cfn-cloudwatch-accessgrant-resourcescope-resourcetype)" : {{String}},
  "[RowScopeGroups](#cfn-cloudwatch-accessgrant-resourcescope-rowscopegroups)" : {{[ [ , ... ], ... ]}},
  "[SignalTypes](#cfn-cloudwatch-accessgrant-resourcescope-signaltypes)" : {{[ String, ... ]}},
  "[Tags](#cfn-cloudwatch-accessgrant-resourcescope-tags)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-cloudwatch-accessgrant-resourcescope-syntax.yaml"></a>

```
  [ResourceArns](#cfn-cloudwatch-accessgrant-resourcescope-resourcearns): {{
    - String}}
  [ResourceType](#cfn-cloudwatch-accessgrant-resourcescope-resourcetype): {{String}}
  [RowScopeGroups](#cfn-cloudwatch-accessgrant-resourcescope-rowscopegroups): {{
    -
    - }}
  [SignalTypes](#cfn-cloudwatch-accessgrant-resourcescope-signaltypes): {{
    - String}}
  [Tags](#cfn-cloudwatch-accessgrant-resourcescope-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-cloudwatch-accessgrant-resourcescope-properties"></a>

`ResourceArns`  <a name="cfn-cloudwatch-accessgrant-resourcescope-resourcearns"></a>
Specific resource ARNs or ARN patterns. When set, actions are limited to these resources. When absent, defaults to all resources of the type.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceType`  <a name="cfn-cloudwatch-accessgrant-resourcescope-resourcetype"></a>
The resource type name, for example DataSet or OmniDashboard.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RowScopeGroups`  <a name="cfn-cloudwatch-accessgrant-resourcescope-rowscopegroups"></a>
Row-level filters for this scope, as an OR of AND-groups: a row is visible when it matches every filter in any one group. Requires SignalTypes.
*Required*: No
*Type*: Array of Array
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignalTypes`  <a name="cfn-cloudwatch-accessgrant-resourcescope-signaltypes"></a>
Signal types this scope's row filtering applies to. Required when RowScopeGroups is set.
*Required*: No
*Type*: Array of String
*Allowed values*: `LOGS | TRACES`
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-accessgrant-resourcescope-tags"></a>
Tag-based conditions for dynamic resource scoping. Access applies only to resources carrying all of the specified tag key-value pairs.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
