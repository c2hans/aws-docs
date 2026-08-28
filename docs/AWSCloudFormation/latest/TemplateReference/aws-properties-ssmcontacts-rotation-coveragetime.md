---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-rotation-coveragetime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Rotation CoverageTime
<a name="aws-properties-ssmcontacts-rotation-coveragetime"></a>

Information about when an on-call shift begins and ends.

## Syntax
<a name="aws-properties-ssmcontacts-rotation-coveragetime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-rotation-coveragetime-syntax.json"></a>

```
{
  "[EndTime](#cfn-ssmcontacts-rotation-coveragetime-endtime)" : {{String}},
  "[StartTime](#cfn-ssmcontacts-rotation-coveragetime-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-rotation-coveragetime-syntax.yaml"></a>

```
  [EndTime](#cfn-ssmcontacts-rotation-coveragetime-endtime): {{String}}
  [StartTime](#cfn-ssmcontacts-rotation-coveragetime-starttime): {{String}}
```

## Properties
<a name="aws-properties-ssmcontacts-rotation-coveragetime-properties"></a>

`EndTime`  <a name="cfn-ssmcontacts-rotation-coveragetime-endtime"></a>
Information about when an on-call rotation shift ends.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-ssmcontacts-rotation-coveragetime-starttime"></a>
Information about when an on-call rotation shift begins.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
