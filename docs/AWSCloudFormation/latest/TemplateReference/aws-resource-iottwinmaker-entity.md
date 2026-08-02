---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iottwinmaker-entity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity
<a name="aws-resource-iottwinmaker-entity"></a>

Use the `AWS::IoTTwinMaker::Entity` resource to declare an entity.

## Syntax
<a name="aws-resource-iottwinmaker-entity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iottwinmaker-entity-syntax.json"></a>

```
{
  "Type" : "AWS::IoTTwinMaker::Entity",
  "Properties" : {
      "[Components](#cfn-iottwinmaker-entity-components)" : {{{{{Key}}: {{Value}}, ...}}},
      "[CompositeComponents](#cfn-iottwinmaker-entity-compositecomponents)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-iottwinmaker-entity-description)" : {{String}},
      "[EntityId](#cfn-iottwinmaker-entity-entityid)" : {{String}},
      "[EntityName](#cfn-iottwinmaker-entity-entityname)" : {{String}},
      "[ParentEntityId](#cfn-iottwinmaker-entity-parententityid)" : {{String}},
      "[Tags](#cfn-iottwinmaker-entity-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[WorkspaceId](#cfn-iottwinmaker-entity-workspaceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iottwinmaker-entity-syntax.yaml"></a>

```
Type: AWS::IoTTwinMaker::Entity
Properties:
  [Components](#cfn-iottwinmaker-entity-components): {{
    {{Key}}: {{Value}}}}
  [CompositeComponents](#cfn-iottwinmaker-entity-compositecomponents): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-iottwinmaker-entity-description): {{String}}
  [EntityId](#cfn-iottwinmaker-entity-entityid): {{String}}
  [EntityName](#cfn-iottwinmaker-entity-entityname): {{String}}
  [ParentEntityId](#cfn-iottwinmaker-entity-parententityid): {{String}}
  [Tags](#cfn-iottwinmaker-entity-tags): {{
    {{Key}}: {{Value}}}}
  [WorkspaceId](#cfn-iottwinmaker-entity-workspaceid): {{String}}
```

## Properties
<a name="aws-resource-iottwinmaker-entity-properties"></a>

`Components`  <a name="cfn-iottwinmaker-entity-components"></a>
An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.
For information on the component object see the [component](https://docs.aws.amazon.com//iot-twinmaker/latest/apireference/API_ComponentResponse.html) API reference.
*Required*: No
*Type*: Object of [Component](aws-properties-iottwinmaker-entity-component.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompositeComponents`  <a name="cfn-iottwinmaker-entity-compositecomponents"></a>
Maps string to `compositeComponent` updates in the request. Each key of the map represents the `componentPath` of the `compositeComponent`.
*Required*: No
*Type*: Object of [CompositeComponent](aws-properties-iottwinmaker-entity-compositecomponent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iottwinmaker-entity-description"></a>
The description of the entity.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityId`  <a name="cfn-iottwinmaker-entity-entityid"></a>
The ID of the entity.
*Required*: No
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityName`  <a name="cfn-iottwinmaker-entity-entityname"></a>
The entity name.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9-.][a-zA-Z_0-9-. ]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentEntityId`  <a name="cfn-iottwinmaker-entity-parententityid"></a>
The ID of the parent entity.
*Required*: No
*Type*: String
*Pattern*: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iottwinmaker-entity-tags"></a>
Metadata that you can use to manage the entity.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceId`  <a name="cfn-iottwinmaker-entity-workspaceid"></a>
The ID of the workspace that contains the entity.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iottwinmaker-entity-return-values"></a>

### Ref
<a name="aws-resource-iottwinmaker-entity-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workspace Id and the entity Id.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iottwinmaker-entity-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iottwinmaker-entity-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The entity ARN.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time the entity was created.

`HasChildEntities`  <a name="HasChildEntities-fn::getatt"></a>
A boolean value that specifies whether the entity has child entities or not.

`UpdateDateTime`  <a name="UpdateDateTime-fn::getatt"></a>
The date and time when the component type was last updated.
