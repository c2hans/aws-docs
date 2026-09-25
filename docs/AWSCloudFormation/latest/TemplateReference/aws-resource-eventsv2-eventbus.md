---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eventsv2-eventbus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventBus
<a name="aws-resource-eventsv2-eventbus"></a>

Resource type definition for `AWS::EventsV2::EventBus`, an Amazon EventBridge custom event bus that receives events and delivers them to matching subscribers.

## Syntax
<a name="aws-resource-eventsv2-eventbus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eventsv2-eventbus-syntax.json"></a>

```
{
  "Type" : "AWS::EventsV2::EventBus",
  "Properties" : {
      "[Description](#cfn-eventsv2-eventbus-description)" : {{String}},
      "[EncryptionConfiguration](#cfn-eventsv2-eventbus-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Name](#cfn-eventsv2-eventbus-name)" : {{String}},
      "[StorageConfiguration](#cfn-eventsv2-eventbus-storageconfiguration)" : {{StorageConfiguration}},
      "[Tags](#cfn-eventsv2-eventbus-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-eventsv2-eventbus-syntax.yaml"></a>

```
Type: AWS::EventsV2::EventBus
Properties:
  [Description](#cfn-eventsv2-eventbus-description): {{String}}
  [EncryptionConfiguration](#cfn-eventsv2-eventbus-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Name](#cfn-eventsv2-eventbus-name): {{String}}
  [StorageConfiguration](#cfn-eventsv2-eventbus-storageconfiguration): {{
    StorageConfiguration}}
  [Tags](#cfn-eventsv2-eventbus-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-eventsv2-eventbus-properties"></a>

`Description`  <a name="cfn-eventsv2-eventbus-description"></a>
A description of the event bus. Control characters and Unicode line separators are not allowed.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S])`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-eventsv2-eventbus-encryptionconfiguration"></a>
Encryption configuration for the event bus. The service stores and returns the customer managed key as its key ARN. The key ARN is recommended so that drift detection stays accurate. A key ID is also accepted and is matched to the returned key ARN when CloudFormation checks for drift; a key alias is accepted but can be reported as a value difference, because an alias cannot be matched to the key ARN it points to.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-eventsv2-eventbus-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-eventsv2-eventbus-name"></a>
The name of the event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][\.\-_A-Za-z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageConfiguration`  <a name="cfn-eventsv2-eventbus-storageconfiguration"></a>
The event storage configuration for the event bus, which controls the number of days events are retained on the bus.
*Required*: No
*Type*: [StorageConfiguration](aws-properties-eventsv2-eventbus-storageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-eventsv2-eventbus-tags"></a>
An array of key-value pairs to apply to the event bus. You can apply a maximum of 50 tags.
For more information about tagging, see [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-eventsv2-eventbus-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-eventsv2-eventbus-return-values"></a>

### Ref
<a name="aws-resource-eventsv2-eventbus-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the event bus Amazon Resource Name (ARN), such as `arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eventsv2-eventbus-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eventsv2-eventbus-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the event bus was created, as an ISO 8601 timestamp.

`EventBusArn`  <a name="EventBusArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the event bus.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time the event bus was last modified, as an ISO 8601 timestamp.

`State`  <a name="State-fn::getatt"></a>
The current lifecycle state of the event bus. The state is `ACTIVE` when the event bus is ready to use.

## Examples
<a name="aws-resource-eventsv2-eventbus--examples"></a>

The following examples create Amazon EventBridge event buses.

**Topics**
+ [Create a minimal event bus](#aws-resource-eventsv2-eventbus--examples--Create_a_minimal_event_bus)
+ [Create a fully configured event bus](#aws-resource-eventsv2-eventbus--examples--Create_a_fully_configured_event_bus)

### Create a minimal event bus
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_minimal_event_bus"></a>

The following example creates an event bus with only the required `Name` property.

#### JSON
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_minimal_event_bus--json"></a>

```
{
  "Resources": {
    "OrdersEventBus": {
      "Type": "AWS::EventsV2::EventBus",
      "Properties": {
        "Name": "orders-event-bus"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_minimal_event_bus--yaml"></a>

```
Resources:
  OrdersEventBus:
    Type: AWS::EventsV2::EventBus
    Properties:
      Name: orders-event-bus
```

### Create a fully configured event bus
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_fully_configured_event_bus"></a>

The following example creates an event bus that retains events for 90 days, encrypts events with a customer managed key, and applies two tags.

#### JSON
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_fully_configured_event_bus--json"></a>

```
{
  "Resources": {
    "OrdersEventBus": {
      "Type": "AWS::EventsV2::EventBus",
      "Properties": {
        "Name": "orders-event-bus",
        "Description": "Receives and routes order events",
        "StorageConfiguration": {
          "RetentionPeriodInDays": 90
        },
        "EncryptionConfiguration": {
          "KmsKeyIdentifier": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        },
        "Tags": [
          { "Key": "Team", "Value": "Orders" },
          { "Key": "Environment", "Value": "Production" }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-eventbus--examples--Create_a_fully_configured_event_bus--yaml"></a>

```
Resources:
  OrdersEventBus:
    Type: AWS::EventsV2::EventBus
    Properties:
      Name: orders-event-bus
      Description: Receives and routes order events
      StorageConfiguration:
        RetentionPeriodInDays: 90
      EncryptionConfiguration:
        KmsKeyIdentifier: arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab
      Tags:
        - Key: Team
          Value: Orders
        - Key: Environment
          Value: Production
```
