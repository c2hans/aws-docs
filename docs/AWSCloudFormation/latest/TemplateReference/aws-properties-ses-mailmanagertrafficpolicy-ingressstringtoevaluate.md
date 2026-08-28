---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressStringToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate"></a>

The union type representing the allowed types for the left hand side of a string condition.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-syntax.json"></a>

```
{
  "[Analysis](#cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-analysis)" : {{IngressAnalysis}},
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-syntax.yaml"></a>

```
  [Analysis](#cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-analysis): {{
    IngressAnalysis}}
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-properties"></a>

`Analysis`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-analysis"></a>
The structure type for a string condition stating the Add On ARN and its returned value.
*Required*: No
*Type*: [IngressAnalysis](aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressstringtoevaluate-attribute"></a>
The enum type representing the allowed attribute types for a string condition.
*Required*: No
*Type*: String
*Allowed values*: `RECIPIENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
