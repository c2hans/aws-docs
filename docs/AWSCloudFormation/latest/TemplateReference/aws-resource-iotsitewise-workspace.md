---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-workspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Workspace
<a name="aws-resource-iotsitewise-workspace"></a>

<a name="aws-resource-iotsitewise-workspace-description"></a>The `AWS::IoTSiteWise::Workspace` resource Property description not available. for IoTSiteWise.

## Syntax
<a name="aws-resource-iotsitewise-workspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-workspace-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Workspace",
  "Properties" : {
      "[EncryptionConfiguration](#cfn-iotsitewise-workspace-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[KmsKeyId](#cfn-iotsitewise-workspace-kmskeyid)" : {{String}},
      "[Tags](#cfn-iotsitewise-workspace-tags)" : {{[ Tag, ... ]}},
      "[WorkspaceDescription](#cfn-iotsitewise-workspace-workspacedescription)" : {{String}},
      "[WorkspaceName](#cfn-iotsitewise-workspace-workspacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-workspace-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Workspace
Properties:
  [EncryptionConfiguration](#cfn-iotsitewise-workspace-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [KmsKeyId](#cfn-iotsitewise-workspace-kmskeyid): {{String}}
  [Tags](#cfn-iotsitewise-workspace-tags): {{
    - Tag}}
  [WorkspaceDescription](#cfn-iotsitewise-workspace-workspacedescription): {{String}}
  [WorkspaceName](#cfn-iotsitewise-workspace-workspacename): {{String}}
```

## Properties
<a name="aws-resource-iotsitewise-workspace-properties"></a>

`EncryptionConfiguration`  <a name="cfn-iotsitewise-workspace-encryptionconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [EncryptionConfiguration](aws-properties-iotsitewise-workspace-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-iotsitewise-workspace-kmskeyid"></a>
The customer managed AWS KMS key used when `encryptionType` is `KMS_BASED_ENCRYPTION`. Accepts a key ID, key ARN, or key alias. Required for `KMS_BASED_ENCRYPTION`; must be omitted for `SITEWISE_DEFAULT_ENCRYPTION`. After a workspace's customer managed key configuration becomes active, the key can't be changed.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotsitewise-workspace-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-workspace-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceDescription`  <a name="cfn-iotsitewise-workspace-workspacedescription"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceName`  <a name="cfn-iotsitewise-workspace-workspacename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotsitewise-workspace-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-workspace-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iotsitewise-workspace-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotsitewise-workspace-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date the workspace was created, in Unix epoch time.

`Status`  <a name="Status-fn::getatt"></a>
The status of the workspace.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date the workspace was last updated, in Unix epoch time.

`WorkspaceArn`  <a name="WorkspaceArn-fn::getatt"></a>
Property description not available.
