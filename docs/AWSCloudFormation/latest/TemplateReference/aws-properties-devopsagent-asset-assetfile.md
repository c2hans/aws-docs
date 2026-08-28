---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-asset-assetfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Asset AssetFile
<a name="aws-properties-devopsagent-asset-assetfile"></a>

A single file within an asset bundle. `Path` is the key used to match files on update; the file contents are write-only and are not returned by read operations.

## Syntax
<a name="aws-properties-devopsagent-asset-assetfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-asset-assetfile-syntax.json"></a>

```
{
  "[ContentBytes](#cfn-devopsagent-asset-assetfile-contentbytes)" : {{String}},
  "[ContentText](#cfn-devopsagent-asset-assetfile-contenttext)" : {{String}},
  "[Metadata](#cfn-devopsagent-asset-assetfile-metadata)" : {{Json}},
  "[Path](#cfn-devopsagent-asset-assetfile-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-asset-assetfile-syntax.yaml"></a>

```
  [ContentBytes](#cfn-devopsagent-asset-assetfile-contentbytes): {{String}}
  [ContentText](#cfn-devopsagent-asset-assetfile-contenttext): {{String}}
  [Metadata](#cfn-devopsagent-asset-assetfile-metadata): {{Json}}
  [Path](#cfn-devopsagent-asset-assetfile-path): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-asset-assetfile-properties"></a>

`ContentBytes`  <a name="cfn-devopsagent-asset-assetfile-contentbytes"></a>
The base64-encoded binary contents of the file. Mutually exclusive with `ContentText`.
*Required*: No
*Type*: String
*Maximum*: `8388608`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentText`  <a name="cfn-devopsagent-asset-assetfile-contenttext"></a>
The UTF-8 text contents of the file. Mutually exclusive with `ContentBytes`.
*Required*: No
*Type*: String
*Maximum*: `1572864`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-devopsagent-asset-assetfile-metadata"></a>
A per-file metadata document. Values may be strings, numbers, booleans, or lists of any of those, and are validated server-side.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-devopsagent-asset-assetfile-path"></a>
The path of the file within the asset bundle.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_./-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
