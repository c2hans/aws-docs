---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-configurationbundle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConfigurationBundle
<a name="aws-resource-bedrockagentcore-configurationbundle"></a>

Specifies a configuration bundle for Amazon Bedrock AgentCore. A configuration bundle packages versioned component configurations for agents.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-configurationbundle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-configurationbundle-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::ConfigurationBundle",
  "Properties" : {
      "[BranchName](#cfn-bedrockagentcore-configurationbundle-branchname)" : {{String}},
      "[BundleName](#cfn-bedrockagentcore-configurationbundle-bundlename)" : {{String}},
      "[CommitMessage](#cfn-bedrockagentcore-configurationbundle-commitmessage)" : {{String}},
      "[Components](#cfn-bedrockagentcore-configurationbundle-components)" : {{{{{Key}}: {{Value}}, ...}}},
      "[CreatedBy](#cfn-bedrockagentcore-configurationbundle-createdby)" : {{VersionCreatedBySource}},
      "[Description](#cfn-bedrockagentcore-configurationbundle-description)" : {{String}},
      "[KmsKeyArn](#cfn-bedrockagentcore-configurationbundle-kmskeyarn)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-configurationbundle-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-configurationbundle-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::ConfigurationBundle
Properties:
  [BranchName](#cfn-bedrockagentcore-configurationbundle-branchname): {{String}}
  [BundleName](#cfn-bedrockagentcore-configurationbundle-bundlename): {{String}}
  [CommitMessage](#cfn-bedrockagentcore-configurationbundle-commitmessage): {{String}}
  [Components](#cfn-bedrockagentcore-configurationbundle-components): {{
    {{Key}}: {{Value}}}}
  [CreatedBy](#cfn-bedrockagentcore-configurationbundle-createdby): {{
    VersionCreatedBySource}}
  [Description](#cfn-bedrockagentcore-configurationbundle-description): {{String}}
  [KmsKeyArn](#cfn-bedrockagentcore-configurationbundle-kmskeyarn): {{String}}
  [Tags](#cfn-bedrockagentcore-configurationbundle-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-configurationbundle-properties"></a>

`BranchName`  <a name="cfn-bedrockagentcore-configurationbundle-branchname"></a>
The branch name for version tracking. Defaults to `mainline` if not specified.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_/-]{0,127}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BundleName`  <a name="cfn-bedrockagentcore-configurationbundle-bundlename"></a>
The name of the configuration bundle.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,99}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CommitMessage`  <a name="cfn-bedrockagentcore-configurationbundle-commitmessage"></a>
A commit message describing the initial version of the configuration bundle.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Components`  <a name="cfn-bedrockagentcore-configurationbundle-components"></a>
A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.
*Required*: Yes
*Type*: Object of [ComponentConfiguration](aws-properties-bedrockagentcore-configurationbundle-componentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedBy`  <a name="cfn-bedrockagentcore-configurationbundle-createdby"></a>
The source that created this version, including the source name and optional ARN.
*Required*: No
*Type*: [VersionCreatedBySource](aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-configurationbundle-description"></a>
The description of the configuration bundle.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-bedrockagentcore-configurationbundle-kmskeyarn"></a>
Optional KMS key ARN for encrypting component configurations.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-configurationbundle-tags"></a>
The tags for the configuration bundle.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-configurationbundle-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-configurationbundle-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-configurationbundle-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-configurationbundle-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-configurationbundle-return-values-fn--getatt-fn--getatt"></a>

`BundleArn`  <a name="BundleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the configuration bundle.

`BundleId`  <a name="BundleId-fn::getatt"></a>
The unique identifier of the configuration bundle.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the configuration bundle was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the configuration bundle was last updated.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The version identifier of this configuration bundle version.
