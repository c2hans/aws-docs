---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-permission-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Permission Condition
<a name="aws-properties-qbusiness-permission-condition"></a>

<a name="aws-properties-qbusiness-permission-condition-description"></a>The `Condition` property type specifies Property description not available. for an [AWS::QBusiness::Permission](aws-resource-qbusiness-permission.md).

## Syntax
<a name="aws-properties-qbusiness-permission-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-permission-condition-syntax.json"></a>

```
{
  "[ConditionKey](#cfn-qbusiness-permission-condition-conditionkey)" : {{String}},
  "[ConditionOperator](#cfn-qbusiness-permission-condition-conditionoperator)" : {{String}},
  "[ConditionValues](#cfn-qbusiness-permission-condition-conditionvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-qbusiness-permission-condition-syntax.yaml"></a>

```
  [ConditionKey](#cfn-qbusiness-permission-condition-conditionkey): {{String}}
  [ConditionOperator](#cfn-qbusiness-permission-condition-conditionoperator): {{String}}
  [ConditionValues](#cfn-qbusiness-permission-condition-conditionvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-qbusiness-permission-condition-properties"></a>

`ConditionKey`  <a name="cfn-qbusiness-permission-condition-conditionkey"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^aws:PrincipalTag/qbusiness-dataaccessor:[a-zA-Z]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionOperator`  <a name="cfn-qbusiness-permission-condition-conditionoperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `StringEquals`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionValues`  <a name="cfn-qbusiness-permission-condition-conditionvalues"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
