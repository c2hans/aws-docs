---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iottwinmaker-workspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Workspace
<a name="aws-resource-iottwinmaker-workspace"></a>

Use the `AWS::IoTTwinMaker::Workspace` resource to declare a workspace.

## Syntax
<a name="aws-resource-iottwinmaker-workspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iottwinmaker-workspace-syntax.json"></a>

```
{
  "Type" : "AWS::IoTTwinMaker::Workspace",
  "Properties" : {
      "[Description](#cfn-iottwinmaker-workspace-description)" : {{String}},
      "[Role](#cfn-iottwinmaker-workspace-role)" : {{String}},
      "[S3Location](#cfn-iottwinmaker-workspace-s3location)" : {{String}},
      "[Tags](#cfn-iottwinmaker-workspace-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[WorkspaceId](#cfn-iottwinmaker-workspace-workspaceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iottwinmaker-workspace-syntax.yaml"></a>

```
Type: AWS::IoTTwinMaker::Workspace
Properties:
  [Description](#cfn-iottwinmaker-workspace-description): {{String}}
  [Role](#cfn-iottwinmaker-workspace-role): {{String}}
  [S3Location](#cfn-iottwinmaker-workspace-s3location): {{String}}
  [Tags](#cfn-iottwinmaker-workspace-tags): {{
    {{Key}}: {{Value}}}}
  [WorkspaceId](#cfn-iottwinmaker-workspace-workspaceid): {{String}}
```

## Properties
<a name="aws-resource-iottwinmaker-workspace-properties"></a>

`Description`  <a name="cfn-iottwinmaker-workspace-description"></a>
The description of the workspace.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-iottwinmaker-workspace-role"></a>
The ARN of the execution role associated with the workspace.
*Required*: Yes
*Type*: String
*Pattern*: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Location`  <a name="cfn-iottwinmaker-workspace-s3location"></a>
The ARN of the S3 bucket where resources associated with the workspace are stored.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iottwinmaker-workspace-tags"></a>
Metadata that you can use to manage the workspace.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceId`  <a name="cfn-iottwinmaker-workspace-workspaceid"></a>
The ID of the workspace.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iottwinmaker-workspace-return-values"></a>

### Ref
<a name="aws-resource-iottwinmaker-workspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workspace Id and the entity Id.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iottwinmaker-workspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iottwinmaker-workspace-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The workspace ARN.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time the workspace was created.

`UpdateDateTime`  <a name="UpdateDateTime-fn::getatt"></a>
The date and time the workspace was updated.
