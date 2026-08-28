---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-slurmconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster SlurmConfiguration
<a name="aws-properties-pcs-cluster-slurmconfiguration"></a>

Additional options related to the Slurm scheduler.

## Syntax
<a name="aws-properties-pcs-cluster-slurmconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-slurmconfiguration-syntax.json"></a>

```
{
  "[Accounting](#cfn-pcs-cluster-slurmconfiguration-accounting)" : {{Accounting}},
  "[AuthKey](#cfn-pcs-cluster-slurmconfiguration-authkey)" : {{AuthKey}},
  "[CgroupCustomSettings](#cfn-pcs-cluster-slurmconfiguration-cgroupcustomsettings)" : {{[ CgroupCustomSetting, ... ]}},
  "[JwtAuth](#cfn-pcs-cluster-slurmconfiguration-jwtauth)" : {{JwtAuth}},
  "[ScaleDownIdleTimeInSeconds](#cfn-pcs-cluster-slurmconfiguration-scaledownidletimeinseconds)" : {{Integer}},
  "[SlurmCustomSettings](#cfn-pcs-cluster-slurmconfiguration-slurmcustomsettings)" : {{[ SlurmCustomSetting, ... ]}},
  "[SlurmdbdCustomSettings](#cfn-pcs-cluster-slurmconfiguration-slurmdbdcustomsettings)" : {{[ SlurmdbdCustomSetting, ... ]}},
  "[SlurmRest](#cfn-pcs-cluster-slurmconfiguration-slurmrest)" : {{SlurmRest}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-slurmconfiguration-syntax.yaml"></a>

```
  [Accounting](#cfn-pcs-cluster-slurmconfiguration-accounting): {{
    Accounting}}
  [AuthKey](#cfn-pcs-cluster-slurmconfiguration-authkey): {{
    AuthKey}}
  [CgroupCustomSettings](#cfn-pcs-cluster-slurmconfiguration-cgroupcustomsettings): {{
    - CgroupCustomSetting}}
  [JwtAuth](#cfn-pcs-cluster-slurmconfiguration-jwtauth): {{
    JwtAuth}}
  [ScaleDownIdleTimeInSeconds](#cfn-pcs-cluster-slurmconfiguration-scaledownidletimeinseconds): {{Integer}}
  [SlurmCustomSettings](#cfn-pcs-cluster-slurmconfiguration-slurmcustomsettings): {{
    - SlurmCustomSetting}}
  [SlurmdbdCustomSettings](#cfn-pcs-cluster-slurmconfiguration-slurmdbdcustomsettings): {{
    - SlurmdbdCustomSetting}}
  [SlurmRest](#cfn-pcs-cluster-slurmconfiguration-slurmrest): {{
    SlurmRest}}
```

## Properties
<a name="aws-properties-pcs-cluster-slurmconfiguration-properties"></a>

`Accounting`  <a name="cfn-pcs-cluster-slurmconfiguration-accounting"></a>
The accounting configuration includes configurable settings for Slurm accounting.
*Required*: No
*Type*: [Accounting](aws-properties-pcs-cluster-accounting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthKey`  <a name="cfn-pcs-cluster-slurmconfiguration-authkey"></a>
The shared Slurm key for authentication, also known as the **cluster secret**.
*Required*: No
*Type*: [AuthKey](aws-properties-pcs-cluster-authkey.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CgroupCustomSettings`  <a name="cfn-pcs-cluster-slurmconfiguration-cgroupcustomsettings"></a>
Additional Cgroup-specific configuration that directly maps to Cgroup settings.
*Required*: No
*Type*: Array of [CgroupCustomSetting](aws-properties-pcs-cluster-cgroupcustomsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwtAuth`  <a name="cfn-pcs-cluster-slurmconfiguration-jwtauth"></a>
The JWT authentication configuration for Slurm REST API access.
*Required*: No
*Type*: [JwtAuth](aws-properties-pcs-cluster-jwtauth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleDownIdleTimeInSeconds`  <a name="cfn-pcs-cluster-slurmconfiguration-scaledownidletimeinseconds"></a>
The time (in seconds) before an idle node is scaled down.
Default: `600`
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmCustomSettings`  <a name="cfn-pcs-cluster-slurmconfiguration-slurmcustomsettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
*Required*: No
*Type*: Array of [SlurmCustomSetting](aws-properties-pcs-cluster-slurmcustomsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmdbdCustomSettings`  <a name="cfn-pcs-cluster-slurmconfiguration-slurmdbdcustomsettings"></a>
Additional SlurmDBD-specific configuration that directly maps to SlurmDBD settings.
*Required*: No
*Type*: Array of [SlurmdbdCustomSetting](aws-properties-pcs-cluster-slurmdbdcustomsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmRest`  <a name="cfn-pcs-cluster-slurmconfiguration-slurmrest"></a>
The Slurm REST API configuration for the cluster.
*Required*: No
*Type*: [SlurmRest](aws-properties-pcs-cluster-slurmrest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
