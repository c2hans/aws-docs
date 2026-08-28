---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-queue-slurmconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Queue SlurmConfiguration
<a name="aws-properties-pcs-queue-slurmconfiguration"></a>

Additional options related to the Slurm scheduler.

## Syntax
<a name="aws-properties-pcs-queue-slurmconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-queue-slurmconfiguration-syntax.json"></a>

```
{
  "[SlurmCustomSettings](#cfn-pcs-queue-slurmconfiguration-slurmcustomsettings)" : {{[ SlurmCustomSetting, ... ]}}
}
```

### YAML
<a name="aws-properties-pcs-queue-slurmconfiguration-syntax.yaml"></a>

```
  [SlurmCustomSettings](#cfn-pcs-queue-slurmconfiguration-slurmcustomsettings): {{
    - SlurmCustomSetting}}
```

## Properties
<a name="aws-properties-pcs-queue-slurmconfiguration-properties"></a>

`SlurmCustomSettings`  <a name="cfn-pcs-queue-slurmconfiguration-slurmcustomsettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
*Required*: No
*Type*: Array of [SlurmCustomSetting](aws-properties-pcs-queue-slurmcustomsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
