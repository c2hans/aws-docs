---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-caserule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule
<a name="aws-resource-cases-caserule"></a>

Creates a new case rule. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-resource-cases-caserule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-caserule-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::CaseRule",
  "Properties" : {
      "[Description](#cfn-cases-caserule-description)" : {{String}},
      "[DomainId](#cfn-cases-caserule-domainid)" : {{String}},
      "[Name](#cfn-cases-caserule-name)" : {{String}},
      "[Rule](#cfn-cases-caserule-rule)" : {{CaseRuleDetails}},
      "[Tags](#cfn-cases-caserule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cases-caserule-syntax.yaml"></a>

```
Type: AWS::Cases::CaseRule
Properties:
  [Description](#cfn-cases-caserule-description): {{String}}
  [DomainId](#cfn-cases-caserule-domainid): {{String}}
  [Name](#cfn-cases-caserule-name): {{String}}
  [Rule](#cfn-cases-caserule-rule): {{
    CaseRuleDetails}}
  [Tags](#cfn-cases-caserule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cases-caserule-properties"></a>

`Description`  <a name="cfn-cases-caserule-description"></a>
Description of a case rule.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainId`  <a name="cfn-cases-caserule-domainid"></a>
Unique identifier of a Cases domain.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: Updates are not supported.

`Name`  <a name="cfn-cases-caserule-name"></a>
Name of the case rule.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[\S]$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rule`  <a name="cfn-cases-caserule-rule"></a>
Represents what rule type should take place, under what conditions.
*Required*: Yes
*Type*: [CaseRuleDetails](aws-properties-cases-caserule-caseruledetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cases-caserule-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-caserule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cases-caserule-return-values"></a>

### Ref
<a name="aws-resource-cases-caserule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the case rule. For example:

 `arn:aws:cases:us-west-2:123456789012:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/case-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cases-caserule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cases-caserule-return-values-fn--getatt-fn--getatt"></a>

`CaseRuleArn`  <a name="CaseRuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the case rule.

`CaseRuleId`  <a name="CaseRuleId-fn::getatt"></a>
Unique identifier of a case rule.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp when the resource was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Timestamp when the resource was created or last modified.
