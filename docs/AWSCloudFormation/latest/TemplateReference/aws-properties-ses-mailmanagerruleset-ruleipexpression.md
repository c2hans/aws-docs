---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleipexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleIpExpression
<a name="aws-properties-ses-mailmanagerruleset-ruleipexpression"></a>

An IP address expression matching certain IP addresses within a given range of IP addresses.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleipexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleipexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagerruleset-ruleipexpression-evaluate)" : {{RuleIpToEvaluate}},
  "[Operator](#cfn-ses-mailmanagerruleset-ruleipexpression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagerruleset-ruleipexpression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleipexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagerruleset-ruleipexpression-evaluate): {{
    RuleIpToEvaluate}}
  [Operator](#cfn-ses-mailmanagerruleset-ruleipexpression-operator): {{String}}
  [Values](#cfn-ses-mailmanagerruleset-ruleipexpression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleipexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagerruleset-ruleipexpression-evaluate"></a>
The IP address to evaluate in this condition.
*Required*: Yes
*Type*: [RuleIpToEvaluate](aws-properties-ses-mailmanagerruleset-ruleiptoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagerruleset-ruleipexpression-operator"></a>
The operator to evaluate the IP address.
*Required*: Yes
*Type*: String
*Allowed values*: `CIDR_MATCHES | NOT_CIDR_MATCHES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagerruleset-ruleipexpression-values"></a>
The IP CIDR blocks in format "x.y.z.w/n" (eg 10.0.0.0/8) to match with the email's IP address. For the operator CIDR\_MATCHES, if multiple values are given, they are evaluated as an OR. That is, if the IP address is contained within any of the given CIDR ranges, the condition is deemed to match. For NOT\_CIDR\_MATCHES, if multiple CIDR ranges are given, the condition is deemed to match if the IP address is not contained in any of the given CIDR ranges.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `43 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
