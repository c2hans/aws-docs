---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressIpToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate"></a>

The structure for an IP based condition matching on the incoming mail.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute"></a>
An enum type representing the allowed attribute types for an IP condition.
*Required*: Yes
*Type*: String
*Allowed values*: `SENDER_IP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
