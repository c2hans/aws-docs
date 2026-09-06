---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iottwinmaker-scene.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Scene
<a name="aws-resource-iottwinmaker-scene"></a>

Use the `AWS::IoTTwinMaker::Scene` resource to declare a scene.

## Syntax
<a name="aws-resource-iottwinmaker-scene-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iottwinmaker-scene-syntax.json"></a>

```
{
  "Type" : "AWS::IoTTwinMaker::Scene",
  "Properties" : {
      "[Capabilities](#cfn-iottwinmaker-scene-capabilities)" : {{[ String, ... ]}},
      "[ContentLocation](#cfn-iottwinmaker-scene-contentlocation)" : {{String}},
      "[Description](#cfn-iottwinmaker-scene-description)" : {{String}},
      "[SceneId](#cfn-iottwinmaker-scene-sceneid)" : {{String}},
      "[SceneMetadata](#cfn-iottwinmaker-scene-scenemetadata)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tags](#cfn-iottwinmaker-scene-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[WorkspaceId](#cfn-iottwinmaker-scene-workspaceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iottwinmaker-scene-syntax.yaml"></a>

```
Type: AWS::IoTTwinMaker::Scene
Properties:
  [Capabilities](#cfn-iottwinmaker-scene-capabilities): {{
    - String}}
  [ContentLocation](#cfn-iottwinmaker-scene-contentlocation): {{String}}
  [Description](#cfn-iottwinmaker-scene-description): {{String}}
  [SceneId](#cfn-iottwinmaker-scene-sceneid): {{String}}
  [SceneMetadata](#cfn-iottwinmaker-scene-scenemetadata): {{
    {{Key}}: {{Value}}}}
  [Tags](#cfn-iottwinmaker-scene-tags): {{
    {{Key}}: {{Value}}}}
  [WorkspaceId](#cfn-iottwinmaker-scene-workspaceid): {{String}}
```

## Properties
<a name="aws-resource-iottwinmaker-scene-properties"></a>

`Capabilities`  <a name="cfn-iottwinmaker-scene-capabilities"></a>
A list of capabilities that the scene uses to render.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `256 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentLocation`  <a name="cfn-iottwinmaker-scene-contentlocation"></a>
The relative path that specifies the location of the content definition file.
*Required*: Yes
*Type*: String
*Pattern*: `[sS]3://[A-Za-z0-9._/-]+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iottwinmaker-scene-description"></a>
The description of this scene.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SceneId`  <a name="cfn-iottwinmaker-scene-sceneid"></a>
The ID of the scene.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SceneMetadata`  <a name="cfn-iottwinmaker-scene-scenemetadata"></a>
The scene metadata.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iottwinmaker-scene-tags"></a>
The ComponentType tags.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceId`  <a name="cfn-iottwinmaker-scene-workspaceid"></a>
The ID of the workspace.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iottwinmaker-scene-return-values"></a>

### Ref
<a name="aws-resource-iottwinmaker-scene-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workspace ID and the scene ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iottwinmaker-scene-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iottwinmaker-scene-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The scene ARN.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time when the scene was created.

`UpdateDateTime`  <a name="UpdateDateTime-fn::getatt"></a>
The scene the update time.
