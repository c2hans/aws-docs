---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appintegrations-eventintegration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::EventIntegration
<a name="aws-resource-appintegrations-eventintegration"></a>

Creates an event integration. You provide a name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that will push events to that bus. No objects are created in your account, only metadata that is persisted on the EventIntegration control plane.

## Syntax
<a name="aws-resource-appintegrations-eventintegration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appintegrations-eventintegration-syntax.json"></a>

```
{
  "Type" : "AWS::AppIntegrations::EventIntegration",
  "Properties" : {
      "[Description](#cfn-appintegrations-eventintegration-description)" : {{String}},
      "[EventBridgeBus](#cfn-appintegrations-eventintegration-eventbridgebus)" : {{String}},
      "[EventFilter](#cfn-appintegrations-eventintegration-eventfilter)" : {{EventFilter}},
      "[Name](#cfn-appintegrations-eventintegration-name)" : {{String}},
      "[Tags](#cfn-appintegrations-eventintegration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appintegrations-eventintegration-syntax.yaml"></a>

```
Type: AWS::AppIntegrations::EventIntegration
Properties:
  [Description](#cfn-appintegrations-eventintegration-description): {{String}}
  [EventBridgeBus](#cfn-appintegrations-eventintegration-eventbridgebus): {{String}}
  [EventFilter](#cfn-appintegrations-eventintegration-eventfilter): {{
    EventFilter}}
  [Name](#cfn-appintegrations-eventintegration-name): {{String}}
  [Tags](#cfn-appintegrations-eventintegration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appintegrations-eventintegration-properties"></a>

`Description`  <a name="cfn-appintegrations-eventintegration-description"></a>
The event integration description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBridgeBus`  <a name="cfn-appintegrations-eventintegration-eventbridgebus"></a>
The Amazon EventBridge bus for the event integration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/\._\-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventFilter`  <a name="cfn-appintegrations-eventintegration-eventfilter"></a>
The event integration filter.
*Required*: Yes
*Type*: [EventFilter](aws-properties-appintegrations-eventintegration-eventfilter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-appintegrations-eventintegration-name"></a>
The name of the event integration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/\._\-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-appintegrations-eventintegration-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-appintegrations-eventintegration-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appintegrations-eventintegration-return-values"></a>

### Ref
<a name="aws-resource-appintegrations-eventintegration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the EventIntegration name. For example:

 `{ "Ref": "myEventIntegrationName" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-appintegrations-eventintegration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-appintegrations-eventintegration-return-values-fn--getatt-fn--getatt"></a>

`EventIntegrationArn`  <a name="EventIntegrationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the event integration.
