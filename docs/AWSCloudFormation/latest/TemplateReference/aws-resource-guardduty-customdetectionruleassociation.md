---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-customdetectionruleassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::CustomDetectionRuleAssociation
<a name="aws-resource-guardduty-customdetectionruleassociation"></a>

<a name="aws-resource-guardduty-customdetectionruleassociation-description"></a>The `AWS::GuardDuty::CustomDetectionRuleAssociation` resource Property description not available. for GuardDuty.

## Syntax
<a name="aws-resource-guardduty-customdetectionruleassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-customdetectionruleassociation-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::CustomDetectionRuleAssociation",
  "Properties" : {
      "[Mode](#cfn-guardduty-customdetectionruleassociation-mode)" : {{String}},
      "[RuleId](#cfn-guardduty-customdetectionruleassociation-ruleid)" : {{String}},
      "[Tags](#cfn-guardduty-customdetectionruleassociation-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-customdetectionruleassociation-syntax.yaml"></a>

```
Type: AWS::GuardDuty::CustomDetectionRuleAssociation
Properties:
  [Mode](#cfn-guardduty-customdetectionruleassociation-mode): {{String}}
  [RuleId](#cfn-guardduty-customdetectionruleassociation-ruleid): {{String}}
  [Tags](#cfn-guardduty-customdetectionruleassociation-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-customdetectionruleassociation-properties"></a>

`Mode`  <a name="cfn-guardduty-customdetectionruleassociation-mode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LIVE | DRY_RUN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleId`  <a name="cfn-guardduty-customdetectionruleassociation-ruleid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-guardduty-customdetectionruleassociation-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-customdetectionruleassociation-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-customdetectionruleassociation-return-values"></a>

### Ref
<a name="aws-resource-guardduty-customdetectionruleassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-guardduty-customdetectionruleassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-guardduty-customdetectionruleassociation-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
