---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-snowflaketableschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable SnowflakeTableSchema
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschema"></a>

 The schema of a Snowflake table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschema-syntax.json"></a>

```
{
  "[V1](#cfn-cleanrooms-configuredtable-snowflaketableschema-v1)" : {{[ SnowflakeTableSchemaV1, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschema-syntax.yaml"></a>

```
  [V1](#cfn-cleanrooms-configuredtable-snowflaketableschema-v1): {{
    - SnowflakeTableSchemaV1}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschema-properties"></a>

`V1`  <a name="cfn-cleanrooms-configuredtable-snowflaketableschema-v1"></a>
 The schema of a Snowflake table.
*Required*: Yes
*Type*: Array of [SnowflakeTableSchemaV1](aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.md)
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
