---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-differentialprivacy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable DifferentialPrivacy
<a name="aws-properties-cleanrooms-configuredtable-differentialprivacy"></a>

The analysis method allowed for the configured tables.

`DIRECT_QUERY` allows SQL queries to be run directly on this table.

`DIRECT_JOB` allows PySpark jobs to be run directly on this table.

`MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-differentialprivacy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-differentialprivacy-syntax.json"></a>

```
{
  "[Columns](#cfn-cleanrooms-configuredtable-differentialprivacy-columns)" : {{[ DifferentialPrivacyColumn, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-differentialprivacy-syntax.yaml"></a>

```
  [Columns](#cfn-cleanrooms-configuredtable-differentialprivacy-columns): {{
    - DifferentialPrivacyColumn}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-differentialprivacy-properties"></a>

`Columns`  <a name="cfn-cleanrooms-configuredtable-differentialprivacy-columns"></a>
The name of the column, such as user\_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.
*Required*: Yes
*Type*: Array of [DifferentialPrivacyColumn](aws-properties-cleanrooms-configuredtable-differentialprivacycolumn.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
