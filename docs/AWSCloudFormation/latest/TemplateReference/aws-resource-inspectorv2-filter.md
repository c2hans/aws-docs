---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspectorv2-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter
<a name="aws-resource-inspectorv2-filter"></a>

Details about a filter.

## Syntax
<a name="aws-resource-inspectorv2-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-inspectorv2-filter-syntax.json"></a>

```
{
  "Type" : "AWS::InspectorV2::Filter",
  "Properties" : {
      "[Description](#cfn-inspectorv2-filter-description)" : {{String}},
      "[FilterAction](#cfn-inspectorv2-filter-filteraction)" : {{String}},
      "[FilterCriteria](#cfn-inspectorv2-filter-filtercriteria)" : {{FilterCriteria}},
      "[Name](#cfn-inspectorv2-filter-name)" : {{String}},
      "[Tags](#cfn-inspectorv2-filter-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-inspectorv2-filter-syntax.yaml"></a>

```
Type: AWS::InspectorV2::Filter
Properties:
  [Description](#cfn-inspectorv2-filter-description): {{String}}
  [FilterAction](#cfn-inspectorv2-filter-filteraction): {{String}}
  [FilterCriteria](#cfn-inspectorv2-filter-filtercriteria): {{
    FilterCriteria}}
  [Name](#cfn-inspectorv2-filter-name): {{String}}
  [Tags](#cfn-inspectorv2-filter-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-inspectorv2-filter-properties"></a>

`Description`  <a name="cfn-inspectorv2-filter-description"></a>
A description of the filter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterAction`  <a name="cfn-inspectorv2-filter-filteraction"></a>
The action that is to be applied to the findings that match the filter.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | SUPPRESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterCriteria`  <a name="cfn-inspectorv2-filter-filtercriteria"></a>
Details on the filter criteria associated with this filter.
*Required*: Yes
*Type*: [FilterCriteria](aws-properties-inspectorv2-filter-filtercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-inspectorv2-filter-name"></a>
The name of the filter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-inspectorv2-filter-tags"></a>
The tags attached to the filter.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{2,127}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-inspectorv2-filter-return-values"></a>

### Ref
<a name="aws-resource-inspectorv2-filter-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the filter. For example:

 `arn:aws:inspector2:us-east-1:012345678901:owner/012345678901/filter/c1c0fe5d28e39baa`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-inspectorv2-filter-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-inspectorv2-filter-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Number (ARN) associated with this filter.
