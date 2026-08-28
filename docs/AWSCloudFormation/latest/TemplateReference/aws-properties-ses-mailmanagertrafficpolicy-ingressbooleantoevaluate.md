---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressBooleanToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate"></a>

The union type representing the allowed types of operands for a boolean condition.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-syntax.json"></a>

```
{
  "[Analysis](#cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-analysis)" : {{IngressAnalysis}},
  "[IsInAddressList](#cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-isinaddresslist)" : {{IngressIsInAddressList}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-syntax.yaml"></a>

```
  [Analysis](#cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-analysis): {{
    IngressAnalysis}}
  [IsInAddressList](#cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-isinaddresslist): {{
    IngressIsInAddressList}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-properties"></a>

`Analysis`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-analysis"></a>
The structure type for a boolean condition stating the Add On ARN and its returned value.
*Required*: No
*Type*: [IngressAnalysis](aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsInAddressList`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate-isinaddresslist"></a>
The structure type for a boolean condition that provides the address lists to evaluate incoming traffic on.
*Required*: No
*Type*: [IngressIsInAddressList](aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
