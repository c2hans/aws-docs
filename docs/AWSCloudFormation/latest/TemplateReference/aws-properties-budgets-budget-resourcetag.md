---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget ResourceTag
<a name="aws-properties-budgets-budget-resourcetag"></a>

The tag structure that contains a tag key and value.

## Syntax
<a name="aws-properties-budgets-budget-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-budgets-budget-resourcetag-key)" : {{String}},
  "[Value](#cfn-budgets-budget-resourcetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-budgets-budget-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-budgets-budget-resourcetag-key): {{String}}
  [Value](#cfn-budgets-budget-resourcetag-value): {{String}}
```

## Properties
<a name="aws-properties-budgets-budget-resourcetag-properties"></a>

`Key`  <a name="cfn-budgets-budget-resourcetag-key"></a>
The key that's associated with the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-budgets-budget-resourcetag-value"></a>
The value that's associated with the tag.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
