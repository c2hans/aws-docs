---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-trigger-predicate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Trigger Predicate
<a name="aws-properties-glue-trigger-predicate"></a>

Defines the predicate of the trigger, which determines when it fires.

## Syntax
<a name="aws-properties-glue-trigger-predicate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-trigger-predicate-syntax.json"></a>

```
{
  "[Conditions](#cfn-glue-trigger-predicate-conditions)" : {{[ Condition, ... ]}},
  "[Logical](#cfn-glue-trigger-predicate-logical)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-trigger-predicate-syntax.yaml"></a>

```
  [Conditions](#cfn-glue-trigger-predicate-conditions): {{
    - Condition}}
  [Logical](#cfn-glue-trigger-predicate-logical): {{String}}
```

## Properties
<a name="aws-properties-glue-trigger-predicate-properties"></a>

`Conditions`  <a name="cfn-glue-trigger-predicate-conditions"></a>
A list of the conditions that determine when the trigger will fire.
*Required*: No
*Type*: Array of [Condition](aws-properties-glue-trigger-condition.md)
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logical`  <a name="cfn-glue-trigger-predicate-logical"></a>
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.
*Required*: No
*Type*: String
*Allowed values*: `AND | ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-glue-trigger-predicate--seealso"></a>
+ [Predicate Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-Predicate) in the *AWS Glue Developer Guide*
