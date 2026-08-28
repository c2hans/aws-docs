---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-filemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase FileMetadata
<a name="aws-properties-apptest-testcase-filemetadata"></a>

Specifies a file metadata.

## Syntax
<a name="aws-properties-apptest-testcase-filemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-filemetadata-syntax.json"></a>

```
{
  "[DatabaseCDC](#cfn-apptest-testcase-filemetadata-databasecdc)" : {{DatabaseCDC}},
  "[DataSets](#cfn-apptest-testcase-filemetadata-datasets)" : {{[ DataSet, ... ]}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-filemetadata-syntax.yaml"></a>

```
  [DatabaseCDC](#cfn-apptest-testcase-filemetadata-databasecdc): {{
    DatabaseCDC}}
  [DataSets](#cfn-apptest-testcase-filemetadata-datasets): {{
    - DataSet}}
```

## Properties
<a name="aws-properties-apptest-testcase-filemetadata-properties"></a>

`DatabaseCDC`  <a name="cfn-apptest-testcase-filemetadata-databasecdc"></a>
The database CDC of the file metadata.
*Required*: No
*Type*: [DatabaseCDC](aws-properties-apptest-testcase-databasecdc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSets`  <a name="cfn-apptest-testcase-filemetadata-datasets"></a>
The data sets of the file metadata.
*Required*: No
*Type*: Array of [DataSet](aws-properties-apptest-testcase-dataset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
