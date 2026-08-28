---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-datasourceerrorinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource DataSourceErrorInfo
<a name="aws-properties-quicksight-datasource-datasourceerrorinfo"></a>

Error information for the data source creation or update.

## Syntax
<a name="aws-properties-quicksight-datasource-datasourceerrorinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-datasourceerrorinfo-syntax.json"></a>

```
{
  "[Message](#cfn-quicksight-datasource-datasourceerrorinfo-message)" : {{String}},
  "[Type](#cfn-quicksight-datasource-datasourceerrorinfo-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-datasourceerrorinfo-syntax.yaml"></a>

```
  [Message](#cfn-quicksight-datasource-datasourceerrorinfo-message): {{String}}
  [Type](#cfn-quicksight-datasource-datasourceerrorinfo-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-datasourceerrorinfo-properties"></a>

`Message`  <a name="cfn-quicksight-datasource-datasourceerrorinfo-message"></a>
Error message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-datasource-datasourceerrorinfo-type"></a>
Error type.
*Required*: No
*Type*: String
*Allowed values*: `ACCESS_DENIED | COPY_SOURCE_NOT_FOUND | TIMEOUT | ENGINE_VERSION_NOT_SUPPORTED | UNKNOWN_HOST | GENERIC_SQL_FAILURE | CONFLICT | UNKNOWN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
