---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-databasecdc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase DatabaseCDC
<a name="aws-properties-apptest-testcase-databasecdc"></a>

Defines the Change Data Capture (CDC) of the database.

## Syntax
<a name="aws-properties-apptest-testcase-databasecdc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-databasecdc-syntax.json"></a>

```
{
  "[SourceMetadata](#cfn-apptest-testcase-databasecdc-sourcemetadata)" : {{SourceDatabaseMetadata}},
  "[TargetMetadata](#cfn-apptest-testcase-databasecdc-targetmetadata)" : {{TargetDatabaseMetadata}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-databasecdc-syntax.yaml"></a>

```
  [SourceMetadata](#cfn-apptest-testcase-databasecdc-sourcemetadata): {{
    SourceDatabaseMetadata}}
  [TargetMetadata](#cfn-apptest-testcase-databasecdc-targetmetadata): {{
    TargetDatabaseMetadata}}
```

## Properties
<a name="aws-properties-apptest-testcase-databasecdc-properties"></a>

`SourceMetadata`  <a name="cfn-apptest-testcase-databasecdc-sourcemetadata"></a>
The source metadata of the database CDC.
*Required*: Yes
*Type*: [SourceDatabaseMetadata](aws-properties-apptest-testcase-sourcedatabasemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetMetadata`  <a name="cfn-apptest-testcase-databasecdc-targetmetadata"></a>
The target metadata of the database CDC.
*Required*: Yes
*Type*: [TargetDatabaseMetadata](aws-properties-apptest-testcase-targetdatabasemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
