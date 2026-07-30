---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-caseruledetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule CaseRuleDetails
<a name="aws-properties-cases-caserule-caseruledetails"></a>

Represents what rule type should take place, under what conditions. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-properties-cases-caserule-caseruledetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-caseruledetails-syntax.json"></a>

```
{
  "[Hidden](#cfn-cases-caserule-caseruledetails-hidden)" : {{HiddenCaseRule}},
  "[Required](#cfn-cases-caserule-caseruledetails-required)" : {{RequiredCaseRule}}
}
```

### YAML
<a name="aws-properties-cases-caserule-caseruledetails-syntax.yaml"></a>

```
  [Hidden](#cfn-cases-caserule-caseruledetails-hidden): {{
    HiddenCaseRule}}
  [Required](#cfn-cases-caserule-caseruledetails-required): {{
    RequiredCaseRule}}
```

## Properties
<a name="aws-properties-cases-caserule-caseruledetails-properties"></a>

`Hidden`  <a name="cfn-cases-caserule-caseruledetails-hidden"></a>
Whether a field is visible, based on values in other fields.
*Required*: No
*Type*: [HiddenCaseRule](aws-properties-cases-caserule-hiddencaserule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-cases-caserule-caseruledetails-required"></a>
Required rule type, used to indicate whether a field is required.
*Required*: No
*Type*: [RequiredCaseRule](aws-properties-cases-caserule-requiredcaserule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
