---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsanalysis-alternatepathhint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis AlternatePathHint
<a name="aws-properties-ec2-networkinsightsanalysis-alternatepathhint"></a>

Describes an potential intermediate component of a feasible path.

## Syntax
<a name="aws-properties-ec2-networkinsightsanalysis-alternatepathhint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsanalysis-alternatepathhint-syntax.json"></a>

```
{
  "[ComponentArn](#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentarn)" : {{String}},
  "[ComponentId](#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsanalysis-alternatepathhint-syntax.yaml"></a>

```
  [ComponentArn](#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentarn): {{String}}
  [ComponentId](#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentid): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsanalysis-alternatepathhint-properties"></a>

`ComponentArn`  <a name="cfn-ec2-networkinsightsanalysis-alternatepathhint-componentarn"></a>
The Amazon Resource Name (ARN) of the component.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentId`  <a name="cfn-ec2-networkinsightsanalysis-alternatepathhint-componentid"></a>
The ID of the component.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
