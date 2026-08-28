---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-policycondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy PolicyCondition
<a name="aws-properties-ses-mailmanagertrafficpolicy-policycondition"></a>

The email traffic filtering conditions which are contained in a traffic policy resource.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-policycondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-policycondition-syntax.json"></a>

```
{
  "[BooleanExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-booleanexpression)" : {{IngressBooleanExpression}},
  "[IpExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-ipexpression)" : {{IngressIpv4Expression}},
  "[Ipv6Expression](#cfn-ses-mailmanagertrafficpolicy-policycondition-ipv6expression)" : {{IngressIpv6Expression}},
  "[StringExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-stringexpression)" : {{IngressStringExpression}},
  "[TlsExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-tlsexpression)" : {{IngressTlsProtocolExpression}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-policycondition-syntax.yaml"></a>

```
  [BooleanExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-booleanexpression): {{
    IngressBooleanExpression}}
  [IpExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-ipexpression): {{
    IngressIpv4Expression}}
  [Ipv6Expression](#cfn-ses-mailmanagertrafficpolicy-policycondition-ipv6expression): {{
    IngressIpv6Expression}}
  [StringExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-stringexpression): {{
    IngressStringExpression}}
  [TlsExpression](#cfn-ses-mailmanagertrafficpolicy-policycondition-tlsexpression): {{
    IngressTlsProtocolExpression}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-policycondition-properties"></a>

`BooleanExpression`  <a name="cfn-ses-mailmanagertrafficpolicy-policycondition-booleanexpression"></a>
This represents a boolean type condition matching on the incoming mail. It performs the boolean operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
*Required*: No
*Type*: [IngressBooleanExpression](aws-properties-ses-mailmanagertrafficpolicy-ingressbooleanexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpExpression`  <a name="cfn-ses-mailmanagertrafficpolicy-policycondition-ipexpression"></a>
This represents an IP based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
*Required*: No
*Type*: [IngressIpv4Expression](aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Expression`  <a name="cfn-ses-mailmanagertrafficpolicy-policycondition-ipv6expression"></a>
This represents an IPv6 based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
*Required*: No
*Type*: [IngressIpv6Expression](aws-properties-ses-mailmanagertrafficpolicy-ingressipv6expression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringExpression`  <a name="cfn-ses-mailmanagertrafficpolicy-policycondition-stringexpression"></a>
This represents a string based condition matching on the incoming mail. It performs the string operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
*Required*: No
*Type*: [IngressStringExpression](aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsExpression`  <a name="cfn-ses-mailmanagertrafficpolicy-policycondition-tlsexpression"></a>
This represents a TLS based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
*Required*: No
*Type*: [IngressTlsProtocolExpression](aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
