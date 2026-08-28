---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConfigurationBundle VersionLineageMetadata
<a name="aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata"></a>

The version lineage metadata that tracks parent versions and creation source. Supports git-like two-parent merges for branch management.

## Syntax
<a name="aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata-syntax.json"></a>

```
{
  "[BranchName](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-branchname)" : {{String}},
  "[CommitMessage](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-commitmessage)" : {{String}},
  "[CreatedBy](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-createdby)" : {{VersionCreatedBySource}},
  "[ParentVersionIds](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-parentversionids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata-syntax.yaml"></a>

```
  [BranchName](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-branchname): {{String}}
  [CommitMessage](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-commitmessage): {{String}}
  [CreatedBy](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-createdby): {{
    VersionCreatedBySource}}
  [ParentVersionIds](#cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-parentversionids): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-configurationbundle-versionlineagemetadata-properties"></a>

`BranchName`  <a name="cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-branchname"></a>
The branch name for this version. If not specified, inherits the parent's branch or defaults to `mainline`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_/-]{0,127}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommitMessage`  <a name="cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-commitmessage"></a>
A commit message describing the changes in this version.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedBy`  <a name="cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-createdby"></a>
The source that created this version.
*Required*: No
*Type*: [VersionCreatedBySource](aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentVersionIds`  <a name="cfn-bedrockagentcore-configurationbundle-versionlineagemetadata-parentversionids"></a>
A list of parent version identifiers. Regular commits have 0-1 parents. Merge commits have 2 parents: the target branch parent and the source branch parent. The first parent represents the primary lineage.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
