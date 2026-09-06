---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-asset-assetproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Asset AssetProperty
<a name="aws-properties-iotsitewise-asset-assetproperty"></a>

Contains asset property information.

## Syntax
<a name="aws-properties-iotsitewise-asset-assetproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-asset-assetproperty-syntax.json"></a>

```
{
  "[Alias](#cfn-iotsitewise-asset-assetproperty-alias)" : {{String}},
  "[ExternalId](#cfn-iotsitewise-asset-assetproperty-externalid)" : {{String}},
  "[Id](#cfn-iotsitewise-asset-assetproperty-id)" : {{String}},
  "[LogicalId](#cfn-iotsitewise-asset-assetproperty-logicalid)" : {{String}},
  "[NotificationState](#cfn-iotsitewise-asset-assetproperty-notificationstate)" : {{String}},
  "[Unit](#cfn-iotsitewise-asset-assetproperty-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-asset-assetproperty-syntax.yaml"></a>

```
  [Alias](#cfn-iotsitewise-asset-assetproperty-alias): {{String}}
  [ExternalId](#cfn-iotsitewise-asset-assetproperty-externalid): {{String}}
  [Id](#cfn-iotsitewise-asset-assetproperty-id): {{String}}
  [LogicalId](#cfn-iotsitewise-asset-assetproperty-logicalid): {{String}}
  [NotificationState](#cfn-iotsitewise-asset-assetproperty-notificationstate): {{String}}
  [Unit](#cfn-iotsitewise-asset-assetproperty-unit): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-asset-assetproperty-properties"></a>

`Alias`  <a name="cfn-iotsitewise-asset-assetproperty-alias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-iotsitewise-asset-assetproperty-externalid"></a>
The external ID of the property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotsitewise-asset-assetproperty-id"></a>
The ID of the asset property.
This is a return value and can't be set.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalId`  <a name="cfn-iotsitewise-asset-assetproperty-logicalid"></a>
The `LogicalID` of the asset property.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationState`  <a name="cfn-iotsitewise-asset-assetproperty-notificationstate"></a>
The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see [Interacting with other services](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html) in the *AWS IoT SiteWise User Guide*.
If you omit this parameter, the notification state is set to `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-iotsitewise-asset-assetproperty-unit"></a>
The unit (such as `Newtons` or `RPM`) of the asset property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
