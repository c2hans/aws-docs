---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-slurmconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup SlurmConfiguration
<a name="aws-properties-pcs-computenodegroup-slurmconfiguration"></a>

Additional options related to the Slurm scheduler.

## Syntax
<a name="aws-properties-pcs-computenodegroup-slurmconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-slurmconfiguration-syntax.json"></a>

```
{
  "[ScaleDownIdleTimeInSeconds](#cfn-pcs-computenodegroup-slurmconfiguration-scaledownidletimeinseconds)" : {{Integer}},
  "[SlurmCustomSettings](#cfn-pcs-computenodegroup-slurmconfiguration-slurmcustomsettings)" : {{[ SlurmCustomSetting, ... ]}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-slurmconfiguration-syntax.yaml"></a>

```
  [ScaleDownIdleTimeInSeconds](#cfn-pcs-computenodegroup-slurmconfiguration-scaledownidletimeinseconds): {{Integer}}
  [SlurmCustomSettings](#cfn-pcs-computenodegroup-slurmconfiguration-slurmcustomsettings): {{
    - SlurmCustomSetting}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-slurmconfiguration-properties"></a>

`ScaleDownIdleTimeInSeconds`  <a name="cfn-pcs-computenodegroup-slurmconfiguration-scaledownidletimeinseconds"></a>
The time (in seconds) before an idle compute node is scaled down. Overrides the cluster-level ScaleDownIdleTimeInSeconds. If removed from the template, CloudFormation sets the value to -1, reverting to the cluster-level setting. Valid values: 1–10000000. Requires Slurm version 25.11 or later.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmCustomSettings`  <a name="cfn-pcs-computenodegroup-slurmconfiguration-slurmcustomsettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
*Required*: No
*Type*: Array of [SlurmCustomSetting](aws-properties-pcs-computenodegroup-slurmcustomsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
