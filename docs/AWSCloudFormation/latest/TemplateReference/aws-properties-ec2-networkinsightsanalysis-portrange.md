---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsanalysis-portrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis PortRange
<a name="aws-properties-ec2-networkinsightsanalysis-portrange"></a>

Describes a range of ports.

## Syntax
<a name="aws-properties-ec2-networkinsightsanalysis-portrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsanalysis-portrange-syntax.json"></a>

```
{
  "[From](#cfn-ec2-networkinsightsanalysis-portrange-from)" : {{Integer}},
  "[To](#cfn-ec2-networkinsightsanalysis-portrange-to)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsanalysis-portrange-syntax.yaml"></a>

```
  [From](#cfn-ec2-networkinsightsanalysis-portrange-from): {{Integer}}
  [To](#cfn-ec2-networkinsightsanalysis-portrange-to): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsanalysis-portrange-properties"></a>

`From`  <a name="cfn-ec2-networkinsightsanalysis-portrange-from"></a>
The first port in the range.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`To`  <a name="cfn-ec2-networkinsightsanalysis-portrange-to"></a>
The last port in the range.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
