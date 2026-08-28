---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressIpv4Expression
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression"></a>

The union type representing the allowed types for the left hand side of an IP condition.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-evaluate)" : {{IngressIpToEvaluate}},
  "[Operator](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-evaluate): {{
    IngressIpToEvaluate}}
  [Operator](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-operator): {{String}}
  [Values](#cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-evaluate"></a>
The left hand side argument of an IP condition expression.
*Required*: Yes
*Type*: [IngressIpToEvaluate](aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-operator"></a>
The matching operator for an IP condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `CIDR_MATCHES | NOT_CIDR_MATCHES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressipv4expression-values"></a>
The right hand side argument of an IP condition expression.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
