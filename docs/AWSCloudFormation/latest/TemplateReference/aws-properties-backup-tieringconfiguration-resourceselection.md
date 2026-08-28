---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-tieringconfiguration-resourceselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::TieringConfiguration ResourceSelection
<a name="aws-properties-backup-tieringconfiguration-resourceselection"></a>

This contains metadata about resource selection for tiering configurations.

You can specify up to 5 different resource selections per tiering configuration. Data moved to lower-cost tier remains there until deletion (one-way transition).

## Syntax
<a name="aws-properties-backup-tieringconfiguration-resourceselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-tieringconfiguration-resourceselection-syntax.json"></a>

```
{
  "[Resources](#cfn-backup-tieringconfiguration-resourceselection-resources)" : {{[ String, ... ]}},
  "[ResourceType](#cfn-backup-tieringconfiguration-resourceselection-resourcetype)" : {{String}},
  "[TieringDownSettingsInDays](#cfn-backup-tieringconfiguration-resourceselection-tieringdownsettingsindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-backup-tieringconfiguration-resourceselection-syntax.yaml"></a>

```
  [Resources](#cfn-backup-tieringconfiguration-resourceselection-resources): {{
    - String}}
  [ResourceType](#cfn-backup-tieringconfiguration-resourceselection-resourcetype): {{String}}
  [TieringDownSettingsInDays](#cfn-backup-tieringconfiguration-resourceselection-tieringdownsettingsindays): {{Integer}}
```

## Properties
<a name="aws-properties-backup-tieringconfiguration-resourceselection-properties"></a>

`Resources`  <a name="cfn-backup-tieringconfiguration-resourceselection-resources"></a>
An array of strings that either contains ARNs of the associated resources or contains a wildcard `*` to specify all resources. You can specify up to 100 specific resources per tiering configuration.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-backup-tieringconfiguration-resourceselection-resourcetype"></a>
The type of AWS resource; for example, `S3` for Amazon S3. For tiering configurations, this is currently limited to `S3`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_\.]{1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TieringDownSettingsInDays`  <a name="cfn-backup-tieringconfiguration-resourceselection-tieringdownsettingsindays"></a>
The number of days after creation within a backup vault that an object can transition to the low cost warm storage tier. Must be a positive integer between 60 and 36500 days.
*Required*: Yes
*Type*: Integer
*Minimum*: `60`
*Maximum*: `36500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
