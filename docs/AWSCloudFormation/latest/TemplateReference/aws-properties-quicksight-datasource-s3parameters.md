---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-s3parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource S3Parameters
<a name="aws-properties-quicksight-datasource-s3parameters"></a>

The parameters for S3.

## Syntax
<a name="aws-properties-quicksight-datasource-s3parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-s3parameters-syntax.json"></a>

```
{
  "[ManifestFileLocation](#cfn-quicksight-datasource-s3parameters-manifestfilelocation)" : {{ManifestFileLocation}},
  "[RoleArn](#cfn-quicksight-datasource-s3parameters-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-s3parameters-syntax.yaml"></a>

```
  [ManifestFileLocation](#cfn-quicksight-datasource-s3parameters-manifestfilelocation): {{
    ManifestFileLocation}}
  [RoleArn](#cfn-quicksight-datasource-s3parameters-rolearn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-s3parameters-properties"></a>

`ManifestFileLocation`  <a name="cfn-quicksight-datasource-s3parameters-manifestfilelocation"></a>
Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded into Quick Sight.
*Required*: Yes
*Type*: [ManifestFileLocation](aws-properties-quicksight-datasource-manifestfilelocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-quicksight-datasource-s3parameters-rolearn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific S3 data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
