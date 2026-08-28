---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-user-homedirectorymapentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::User HomeDirectoryMapEntry
<a name="aws-properties-transfer-user-homedirectorymapentry"></a>

 Represents an object that contains entries and targets for `HomeDirectoryMappings` .

## Syntax
<a name="aws-properties-transfer-user-homedirectorymapentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-user-homedirectorymapentry-syntax.json"></a>

```
{
  "[Entry](#cfn-transfer-user-homedirectorymapentry-entry)" : {{String}},
  "[Target](#cfn-transfer-user-homedirectorymapentry-target)" : {{String}},
  "[Type](#cfn-transfer-user-homedirectorymapentry-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-user-homedirectorymapentry-syntax.yaml"></a>

```
  [Entry](#cfn-transfer-user-homedirectorymapentry-entry): {{String}}
  [Target](#cfn-transfer-user-homedirectorymapentry-target): {{String}}
  [Type](#cfn-transfer-user-homedirectorymapentry-type): {{String}}
```

## Properties
<a name="aws-properties-transfer-user-homedirectorymapentry-properties"></a>

`Entry`  <a name="cfn-transfer-user-homedirectorymapentry-entry"></a>
Represents an entry for `HomeDirectoryMappings`.
*Required*: Yes
*Type*: String
*Pattern*: `^/.*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-transfer-user-homedirectorymapentry-target"></a>
Represents the map target that is used in a `HomeDirectoryMapEntry`.
*Required*: Yes
*Type*: String
*Pattern*: `^/.*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-transfer-user-homedirectorymapentry-type"></a>
Specifies the type of mapping. Set the type to `FILE` if you want the mapping to point to a file, or `DIRECTORY` for the directory to point to a directory.
By default, home directory mappings have a `Type` of `DIRECTORY` when you create a Transfer Family server. You would need to explicitly set `Type` to `FILE` if you want a mapping to have a file target.
*Required*: No
*Type*: String
*Allowed values*: `FILE | DIRECTORY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
