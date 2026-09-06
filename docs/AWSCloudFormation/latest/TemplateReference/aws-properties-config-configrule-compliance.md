---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-compliance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigRule Compliance
<a name="aws-properties-config-configrule-compliance"></a>

Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.

## Syntax
<a name="aws-properties-config-configrule-compliance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configrule-compliance-syntax.json"></a>

```
{
  "[Type](#cfn-config-configrule-compliance-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-configrule-compliance-syntax.yaml"></a>

```
  [Type](#cfn-config-configrule-compliance-type): {{String}}
```

## Properties
<a name="aws-properties-config-configrule-compliance-properties"></a>

`Type`  <a name="cfn-config-configrule-compliance-type"></a>
Indicates whether an AWS resource or AWS Config rule is compliant.
A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
AWS Config returns the `INSUFFICIENT_DATA` value when no evaluation results are available for the AWS resource or AWS Config rule.
For the `Compliance` data type, AWS Config supports only `COMPLIANT`, `NON_COMPLIANT`, and `INSUFFICIENT_DATA` values. AWS Config does not support the `NOT_APPLICABLE` value for the `Compliance` data type.
*Required*: No
*Type*: String
*Allowed values*: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
