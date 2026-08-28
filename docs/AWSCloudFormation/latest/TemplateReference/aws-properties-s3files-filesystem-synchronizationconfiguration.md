---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-filesystem-synchronizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::FileSystem SynchronizationConfiguration
<a name="aws-properties-s3files-filesystem-synchronizationconfiguration"></a>

The synchronization configuration for the file system.

## Syntax
<a name="aws-properties-s3files-filesystem-synchronizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-filesystem-synchronizationconfiguration-syntax.json"></a>

```
{
  "[ExpirationDataRules](#cfn-s3files-filesystem-synchronizationconfiguration-expirationdatarules)" : {{[ ExpirationDataRule, ... ]}},
  "[ImportDataRules](#cfn-s3files-filesystem-synchronizationconfiguration-importdatarules)" : {{[ ImportDataRule, ... ]}},
  "[LatestVersionNumber](#cfn-s3files-filesystem-synchronizationconfiguration-latestversionnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3files-filesystem-synchronizationconfiguration-syntax.yaml"></a>

```
  [ExpirationDataRules](#cfn-s3files-filesystem-synchronizationconfiguration-expirationdatarules): {{
    - ExpirationDataRule}}
  [ImportDataRules](#cfn-s3files-filesystem-synchronizationconfiguration-importdatarules): {{
    - ImportDataRule}}
  [LatestVersionNumber](#cfn-s3files-filesystem-synchronizationconfiguration-latestversionnumber): {{Integer}}
```

## Properties
<a name="aws-properties-s3files-filesystem-synchronizationconfiguration-properties"></a>

`ExpirationDataRules`  <a name="cfn-s3files-filesystem-synchronizationconfiguration-expirationdatarules"></a>
The rules that control when cached data expires from the file system.
*Required*: Yes
*Type*: Array of [ExpirationDataRule](aws-properties-s3files-filesystem-expirationdatarule.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportDataRules`  <a name="cfn-s3files-filesystem-synchronizationconfiguration-importdatarules"></a>
The rules that control how data is imported from S3 into the file system.
*Required*: Yes
*Type*: Array of [ImportDataRule](aws-properties-s3files-filesystem-importdatarule.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LatestVersionNumber`  <a name="cfn-s3files-filesystem-synchronizationconfiguration-latestversionnumber"></a>
The latest version number of the synchronization configuration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
