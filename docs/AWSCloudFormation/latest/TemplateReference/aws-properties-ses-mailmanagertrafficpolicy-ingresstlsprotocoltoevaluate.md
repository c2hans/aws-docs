---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressTlsProtocolToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate"></a>

The union type representing the allowed types for the left hand side of a TLS condition.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute"></a>
The enum type representing the allowed attribute types for the TLS condition.
*Required*: Yes
*Type*: String
*Allowed values*: `TLS_PROTOCOL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
