---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-outputcolumnthreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable OutputColumnThreshold
<a name="aws-properties-cleanrooms-configuredtable-outputcolumnthreshold"></a>

Specifies the minimum number of distinct identities for an individual output column. This value overrides the table-wide `minimumIdentityCount` that you set in `AggregationThreshold`.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-outputcolumnthreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-outputcolumnthreshold-syntax.json"></a>

```
{
  "[MinimumIdentityCount](#cfn-cleanrooms-configuredtable-outputcolumnthreshold-minimumidentitycount)" : {{Integer}},
  "[OutputColumnName](#cfn-cleanrooms-configuredtable-outputcolumnthreshold-outputcolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-outputcolumnthreshold-syntax.yaml"></a>

```
  [MinimumIdentityCount](#cfn-cleanrooms-configuredtable-outputcolumnthreshold-minimumidentitycount): {{Integer}}
  [OutputColumnName](#cfn-cleanrooms-configuredtable-outputcolumnthreshold-outputcolumnname): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-outputcolumnthreshold-properties"></a>

`MinimumIdentityCount`  <a name="cfn-cleanrooms-configuredtable-outputcolumnthreshold-minimumidentitycount"></a>
The minimum number of distinct identities that each query output group must represent for this column. Specify 0 to exempt the column from the threshold, or a value of 2 or greater to enforce a threshold.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputColumnName`  <a name="cfn-cleanrooms-configuredtable-outputcolumnthreshold-outputcolumnname"></a>
The name of the output column that the override applies to. You can specify each column only once.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
