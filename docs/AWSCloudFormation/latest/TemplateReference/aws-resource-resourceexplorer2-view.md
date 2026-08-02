---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resourceexplorer2-view.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceExplorer2::View
<a name="aws-resource-resourceexplorer2-view"></a>

Creates a view that users can query by using the [Search](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html) operation. Results from queries that you make using this view include only resources that match the view's `Filters`.

## Syntax
<a name="aws-resource-resourceexplorer2-view-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resourceexplorer2-view-syntax.json"></a>

```
{
  "Type" : "AWS::ResourceExplorer2::View",
  "Properties" : {
      "[Filters](#cfn-resourceexplorer2-view-filters)" : {{SearchFilter}},
      "[IncludedProperties](#cfn-resourceexplorer2-view-includedproperties)" : {{[ IncludedProperty, ... ]}},
      "[Scope](#cfn-resourceexplorer2-view-scope)" : {{String}},
      "[Tags](#cfn-resourceexplorer2-view-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ViewName](#cfn-resourceexplorer2-view-viewname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-resourceexplorer2-view-syntax.yaml"></a>

```
Type: AWS::ResourceExplorer2::View
Properties:
  [Filters](#cfn-resourceexplorer2-view-filters): {{
    SearchFilter}}
  [IncludedProperties](#cfn-resourceexplorer2-view-includedproperties): {{
    - IncludedProperty}}
  [Scope](#cfn-resourceexplorer2-view-scope): {{String}}
  [Tags](#cfn-resourceexplorer2-view-tags): {{
    {{Key}}: {{Value}}}}
  [ViewName](#cfn-resourceexplorer2-view-viewname): {{String}}
```

## Properties
<a name="aws-resource-resourceexplorer2-view-properties"></a>

`Filters`  <a name="cfn-resourceexplorer2-view-filters"></a>
An array of strings that include search keywords, prefixes, and operators that filter the results that are returned for queries made using this view. When you use this view in a [Search](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html) operation, the filter string is combined with the search's `QueryString` parameter using a logical `AND` operator.
For information about the supported syntax, see [Search query reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the *AWS Resource Explorer User Guide*.
This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators). It doesn't support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any AWS Region that begin with the letters `us` and are *not* tagged with a key `Stage` that has the value `prod`.
*Required*: No
*Type*: [SearchFilter](aws-properties-resourceexplorer2-view-searchfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedProperties`  <a name="cfn-resourceexplorer2-view-includedproperties"></a>
A list of fields that provide additional information about the view.
*Required*: No
*Type*: Array of [IncludedProperty](aws-properties-resourceexplorer2-view-includedproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-resourceexplorer2-view-scope"></a>
The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-resourceexplorer2-view-tags"></a>
Tag key and value pairs that are attached to the view.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewName`  <a name="cfn-resourceexplorer2-view-viewname"></a>
The name of the new view.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-]{1,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-resourceexplorer2-view-return-values"></a>

### Ref
<a name="aws-resource-resourceexplorer2-view-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the new view. For example:

 `arn:aws:resource-explorer-2:us-east-1:123456789012:view/CFNStackView2/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-resourceexplorer2-view-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-resourceexplorer2-view-return-values-fn--getatt-fn--getatt"></a>

`ViewArn`  <a name="ViewArn-fn::getatt"></a>
The ARN of the new view. For example:
 `arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyView/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`

## Examples
<a name="aws-resource-resourceexplorer2-view--examples"></a>

### Creating a view for users to search an index
<a name="aws-resource-resourceexplorer2-view--examples--Creating_a_view_for_users_to_search_an_index"></a>

#### JSON
<a name="aws-resource-resourceexplorer2-view--examples--Creating_a_view_for_users_to_search_an_index--json"></a>

```
{
    "Description": "Sample stack template that creates a Resource Explorer view for the SampleIndex",
    "Resources": {
        "SampleView": {
            "Type": "AWS::ResourceExplorer2::View",
            "Properties": {
                "ViewName": "mySampleView",
                "IncludedProperties": [
                    {
                        "Name": "tags"
                    }
                ],
                "Tags": {
                    "Purpose": "ResourceExplorer Sample Stack"
                }
            },
            "DependsOn": "SampleIndex"
        }
    }
}
```

#### YAML
<a name="aws-resource-resourceexplorer2-view--examples--Creating_a_view_for_users_to_search_an_index--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template that creates a Resource Explorer view for the SampleIndex
  SampleView:
    Type: 'AWS::ResourceExplorer2::View'
    Properties:
      ViewName: mySampleView
      IncludedProperties:
        - Name: tags
      Tags:
        Purpose: ResourceExplorer Sample Stack
    DependsOn: SampleIndex
```
