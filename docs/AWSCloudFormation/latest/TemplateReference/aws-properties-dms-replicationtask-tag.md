---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-replicationtask-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::ReplicationTask Tag
<a name="aws-properties-dms-replicationtask-tag"></a>

A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:
+  `AddTagsToResource`
+  `ListTagsForResource`
+  `RemoveTagsFromResource`

## Syntax
<a name="aws-properties-dms-replicationtask-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-replicationtask-tag-syntax.json"></a>

```
{
  "[Key](#cfn-dms-replicationtask-tag-key)" : {{String}},
  "[Value](#cfn-dms-replicationtask-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-replicationtask-tag-syntax.yaml"></a>

```
  [Key](#cfn-dms-replicationtask-tag-key): {{String}}
  [Value](#cfn-dms-replicationtask-tag-value): {{String}}
```

## Properties
<a name="aws-properties-dms-replicationtask-tag-properties"></a>

`Key`  <a name="cfn-dms-replicationtask-tag-key"></a>
A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-' (Java regular expressions: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-dms-replicationtask-tag-value"></a>
A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-' (Java regular expressions: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
