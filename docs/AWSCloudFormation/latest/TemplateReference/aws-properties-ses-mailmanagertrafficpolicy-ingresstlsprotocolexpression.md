---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressTlsProtocolExpression
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression"></a>

The structure for a TLS related condition matching on the incoming mail.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-evaluate)" : {{IngressTlsProtocolToEvaluate}},
  "[Operator](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-operator)" : {{String}},
  "[Value](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-evaluate): {{
    IngressTlsProtocolToEvaluate}}
  [Operator](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-operator): {{String}}
  [Value](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-value): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-evaluate"></a>
The left hand side argument of a TLS condition expression.
*Required*: Yes
*Type*: [IngressTlsProtocolToEvaluate](aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-operator"></a>
The matching operator for a TLS condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `MINIMUM_TLS_VERSION | IS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression-value"></a>
The right hand side argument of a TLS condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `TLS1_2 | TLS1_3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
