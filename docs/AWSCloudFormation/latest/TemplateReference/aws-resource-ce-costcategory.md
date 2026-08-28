---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ce-costcategory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CE::CostCategory
<a name="aws-resource-ce-costcategory"></a>

The `AWS::CE::CostCategory` resource creates groupings of cost that you can use across products in the AWS Billing and Cost Management console, such as Cost Explorer and AWS Budgets. For more information, see [Managing Your Costs with Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) in the *AWS Billing and Cost Management User Guide*.

## Syntax
<a name="aws-resource-ce-costcategory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ce-costcategory-syntax.json"></a>

```
{
  "Type" : "AWS::CE::CostCategory",
  "Properties" : {
      "[DefaultValue](#cfn-ce-costcategory-defaultvalue)" : {{String}},
      "[Name](#cfn-ce-costcategory-name)" : {{String}},
      "[Rules](#cfn-ce-costcategory-rules)" : {{String}},
      "[RuleVersion](#cfn-ce-costcategory-ruleversion)" : {{String}},
      "[SplitChargeRules](#cfn-ce-costcategory-splitchargerules)" : {{String}},
      "[Tags](#cfn-ce-costcategory-tags)" : {{[ ResourceTag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ce-costcategory-syntax.yaml"></a>

```
Type: AWS::CE::CostCategory
Properties:
  [DefaultValue](#cfn-ce-costcategory-defaultvalue): {{String}}
  [Name](#cfn-ce-costcategory-name): {{String}}
  [Rules](#cfn-ce-costcategory-rules): {{String}}
  [RuleVersion](#cfn-ce-costcategory-ruleversion): {{String}}
  [SplitChargeRules](#cfn-ce-costcategory-splitchargerules): {{String}}
  [Tags](#cfn-ce-costcategory-tags): {{
    - ResourceTag}}
```

## Properties
<a name="aws-resource-ce-costcategory-properties"></a>

`DefaultValue`  <a name="cfn-ce-costcategory-defaultvalue"></a>
The default value for the cost category.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ce-costcategory-name"></a>
The unique name of the Cost Category.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Rules`  <a name="cfn-ce-costcategory-rules"></a>
 The array of CostCategoryRule in JSON array format.
Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleVersion`  <a name="cfn-ce-costcategory-ruleversion"></a>
The rule schema version in this particular Cost Category.
*Required*: Yes
*Type*: String
*Allowed values*: `CostCategoryExpression.v1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SplitChargeRules`  <a name="cfn-ce-costcategory-splitchargerules"></a>
 The split charge rules that are used to allocate your charges between your cost category values.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ce-costcategory-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-ce-costcategory-resourcetag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ce-costcategory-return-values"></a>

### Ref
<a name="aws-resource-ce-costcategory-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Arn of the Cost Category that is created by the template.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ce-costcategory-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ce-costcategory-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique identifier for your Cost Category.

`EffectiveStart`  <a name="EffectiveStart-fn::getatt"></a>
The Cost Category's effective start date.

## Examples
<a name="aws-resource-ce-costcategory--examples"></a>

### Cost Category Department with two rules
<a name="aws-resource-ce-costcategory--examples--Cost_Category_Department_with_two_rules"></a>

The following example creates a Cost Category "Department" with two rules.

#### JSON
<a name="aws-resource-ce-costcategory--examples--Cost_Category_Department_with_two_rules--json"></a>

```
{
  "CostCategoryDepartment": {
    "Type": "AWS::CE::CostCategory",
    "Properties": {
      "Name": "Department",
      "RuleVersion": "CostCategoryExpression.v1",
      "Rules": "[
        {
          \"Value\":\"Engineering\",
          \"Rule\": {
            \"Dimensions\": {
            \"Key\": \"LINKED_ACCOUNT\",
            \"Values\": [ \"111111111111\" ]
            }
          }
        },
        {
          \"Value\": \"Marketing\",
          \"Rule\": {
            \"Dimensions\": {
            \"Key\": \"LINKED_ACCOUNT\",
            \"Values\": [ \"222222222222\" ]
            }
          }
        }
        ]"
      }
    }
  }
```

#### YAML
<a name="aws-resource-ce-costcategory--examples--Cost_Category_Department_with_two_rules--yaml"></a>

```
  CostCategoryDepartment:
    Type: 'AWS::CE::CostCategory'
    Properties:
      Name: Department
      RuleVersion: CostCategoryExpression.v1
      Rules: '
        [
          {
            "Value":"Engineering",
            "Rule": {
              "Dimensions": {
                "Key": "LINKED_ACCOUNT",
                "Values": [ "111111111111" ]
          }
        }
      },
      {
        "Value":"Marketing",
        "Rule": {
          "Dimensions": {
          "Key": "LINKED_ACCOUNT",
          "Values": [ "222222222222" ]
          }
        }

    ]'
```

## See also
<a name="aws-resource-ce-costcategory--seealso"></a>
+ [CostCategory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html) in the *AWS Billing and Cost Management API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
