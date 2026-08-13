---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-configurationbundleversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConfigurationBundleVersion
<a name="aws-resource-bedrockagentcore-configurationbundleversion"></a>

<a name="aws-resource-bedrockagentcore-configurationbundleversion-description"></a>The `AWS::BedrockAgentCore::ConfigurationBundleVersion` resource Property description not available. for BedrockAgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-configurationbundleversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-configurationbundleversion-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::ConfigurationBundleVersion",
  "Properties" : {
      "[BranchName](#cfn-bedrockagentcore-configurationbundleversion-branchname)" : {{String}},
      "[CommitMessage](#cfn-bedrockagentcore-configurationbundleversion-commitmessage)" : {{String}},
      "[Components](#cfn-bedrockagentcore-configurationbundleversion-components)" : {{{{{Key}}: {{Value}}, ...}}},
      "[CreatedBy](#cfn-bedrockagentcore-configurationbundleversion-createdby)" : {{VersionCreatedBySource}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-configurationbundleversion-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::ConfigurationBundleVersion
Properties:
  [BranchName](#cfn-bedrockagentcore-configurationbundleversion-branchname): {{String}}
  [CommitMessage](#cfn-bedrockagentcore-configurationbundleversion-commitmessage): {{String}}
  [Components](#cfn-bedrockagentcore-configurationbundleversion-components): {{
    {{Key}}: {{Value}}}}
  [CreatedBy](#cfn-bedrockagentcore-configurationbundleversion-createdby): {{
    VersionCreatedBySource}}
```

## Properties
<a name="aws-resource-bedrockagentcore-configurationbundleversion-properties"></a>

`BranchName`  <a name="cfn-bedrockagentcore-configurationbundleversion-branchname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_/-]{0,127}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CommitMessage`  <a name="cfn-bedrockagentcore-configurationbundleversion-commitmessage"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Components`  <a name="cfn-bedrockagentcore-configurationbundleversion-components"></a>
Property description not available.
*Required*: Yes
*Type*: Object of [ComponentConfiguration](aws-properties-bedrockagentcore-configurationbundleversion-componentconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatedBy`  <a name="cfn-bedrockagentcore-configurationbundleversion-createdby"></a>
Property description not available.
*Required*: No
*Type*: [VersionCreatedBySource](aws-properties-bedrockagentcore-configurationbundleversion-versioncreatedbysource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-configurationbundleversion-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-configurationbundleversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-configurationbundleversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-configurationbundleversion-return-values-fn--getatt-fn--getatt"></a>

`BundleArn`  <a name="BundleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the configuration bundle.

`BundleId`  <a name="BundleId-fn::getatt"></a>
The unique identifier of the configuration bundle.

`ParentVersionIds`  <a name="ParentVersionIds-fn::getatt"></a>
Property description not available.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

`VersionCreatedAt`  <a name="VersionCreatedAt-fn::getatt"></a>
The timestamp when this version was created.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The version identifier of this configuration bundle version.
