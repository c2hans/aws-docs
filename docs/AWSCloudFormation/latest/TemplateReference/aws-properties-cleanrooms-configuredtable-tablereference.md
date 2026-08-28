---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-tablereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable TableReference
<a name="aws-properties-cleanrooms-configuredtable-tablereference"></a>

A pointer to the dataset that underlies this table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-tablereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-tablereference-syntax.json"></a>

```
{
  "[Athena](#cfn-cleanrooms-configuredtable-tablereference-athena)" : {{AthenaTableReference}},
  "[Glue](#cfn-cleanrooms-configuredtable-tablereference-glue)" : {{GlueTableReference}},
  "[Snowflake](#cfn-cleanrooms-configuredtable-tablereference-snowflake)" : {{SnowflakeTableReference}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-tablereference-syntax.yaml"></a>

```
  [Athena](#cfn-cleanrooms-configuredtable-tablereference-athena): {{
    AthenaTableReference}}
  [Glue](#cfn-cleanrooms-configuredtable-tablereference-glue): {{
    GlueTableReference}}
  [Snowflake](#cfn-cleanrooms-configuredtable-tablereference-snowflake): {{
    SnowflakeTableReference}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-tablereference-properties"></a>

`Athena`  <a name="cfn-cleanrooms-configuredtable-tablereference-athena"></a>
 If present, a reference to the Athena table referred to by this table reference.
*Required*: No
*Type*: [AthenaTableReference](aws-properties-cleanrooms-configuredtable-athenatablereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Glue`  <a name="cfn-cleanrooms-configuredtable-tablereference-glue"></a>
If present, a reference to the AWS Glue table referred to by this table reference.
*Required*: No
*Type*: [GlueTableReference](aws-properties-cleanrooms-configuredtable-gluetablereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Snowflake`  <a name="cfn-cleanrooms-configuredtable-tablereference-snowflake"></a>
 If present, a reference to the Snowflake table referred to by this table reference.
*Required*: No
*Type*: [SnowflakeTableReference](aws-properties-cleanrooms-configuredtable-snowflaketablereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
