---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityScanConfiguration PeriodicScanConfiguration
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration"></a>

Configuration settings for periodic scans that run on a scheduled basis.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-syntax.json"></a>

```
{
  "[frequency](#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequency)" : {{String}},
  "[frequencyExpression](#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequencyexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-syntax.yaml"></a>

```
  [frequency](#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequency): {{String}}
  [frequencyExpression](#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequencyexpression): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-properties"></a>

`frequency`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequency"></a>
The frequency at which periodic scans are performed (such as weekly or monthly).
If you don't provide the `frequencyExpression`Amazon Inspector chooses day for the scan to run. If you provide the `frequencyExpression`, the schedule must match the specified `frequency`.
*Required*: No
*Type*: String
*Allowed values*: `WEEKLY | MONTHLY | NEVER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`frequencyExpression`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequencyexpression"></a>
The schedule expression for periodic scans, in cron format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
