---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressStringExpression
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression"></a>

The structure for a string based condition matching on the incoming mail.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-evaluate)" : {{IngressStringToEvaluate}},
  "[Operator](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-evaluate): {{
    IngressStringToEvaluate}}
  [Operator](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-operator): {{String}}
  [Values](#cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-evaluate"></a>
The left hand side argument of a string condition expression.
*Required*: Yes
*Type*: [IngressStringToEvaluate](aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-operator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS | STARTS_WITH | ENDS_WITH | CONTAINS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressstringexpression-values"></a>
The right hand side argument of a string condition expression.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
