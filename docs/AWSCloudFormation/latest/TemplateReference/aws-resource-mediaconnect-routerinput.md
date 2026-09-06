---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-routerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput
<a name="aws-resource-mediaconnect-routerinput"></a>

The `AWS::MediaConnect::RouterInput` resource defines a connection point in the MediaConnect router that can receive content from your source endpoint. You can configure a router input with either a Regional routing scope or a global routing scope.

## Syntax
<a name="aws-resource-mediaconnect-routerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-routerinput-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::RouterInput",
  "Properties" : {
      "[AvailabilityZone](#cfn-mediaconnect-routerinput-availabilityzone)" : {{String}},
      "[Configuration](#cfn-mediaconnect-routerinput-configuration)" : {{RouterInputConfiguration}},
      "[ContentQualityAnalysisConfiguration](#cfn-mediaconnect-routerinput-contentqualityanalysisconfiguration)" : {{RouterContentQualityAnalysisConfiguration}},
      "[MaintenanceConfiguration](#cfn-mediaconnect-routerinput-maintenanceconfiguration)" : {{MaintenanceConfiguration}},
      "[MaximumBitrate](#cfn-mediaconnect-routerinput-maximumbitrate)" : {{Integer}},
      "[Name](#cfn-mediaconnect-routerinput-name)" : {{String}},
      "[RegionName](#cfn-mediaconnect-routerinput-regionname)" : {{String}},
      "[RoutingScope](#cfn-mediaconnect-routerinput-routingscope)" : {{String}},
      "[Tags](#cfn-mediaconnect-routerinput-tags)" : {{[ Tag, ... ]}},
      "[Tier](#cfn-mediaconnect-routerinput-tier)" : {{String}},
      "[TransitEncryption](#cfn-mediaconnect-routerinput-transitencryption)" : {{RouterInputTransitEncryption}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-routerinput-syntax.yaml"></a>

```
Type: AWS::MediaConnect::RouterInput
Properties:
  [AvailabilityZone](#cfn-mediaconnect-routerinput-availabilityzone): {{String}}
  [Configuration](#cfn-mediaconnect-routerinput-configuration): {{
    RouterInputConfiguration}}
  [ContentQualityAnalysisConfiguration](#cfn-mediaconnect-routerinput-contentqualityanalysisconfiguration): {{
    RouterContentQualityAnalysisConfiguration}}
  [MaintenanceConfiguration](#cfn-mediaconnect-routerinput-maintenanceconfiguration): {{
    MaintenanceConfiguration}}
  [MaximumBitrate](#cfn-mediaconnect-routerinput-maximumbitrate): {{Integer}}
  [Name](#cfn-mediaconnect-routerinput-name): {{String}}
  [RegionName](#cfn-mediaconnect-routerinput-regionname): {{String}}
  [RoutingScope](#cfn-mediaconnect-routerinput-routingscope): {{String}}
  [Tags](#cfn-mediaconnect-routerinput-tags): {{
    - Tag}}
  [Tier](#cfn-mediaconnect-routerinput-tier): {{String}}
  [TransitEncryption](#cfn-mediaconnect-routerinput-transitencryption): {{
    RouterInputTransitEncryption}}
```

## Properties
<a name="aws-resource-mediaconnect-routerinput-properties"></a>

`AvailabilityZone`  <a name="cfn-mediaconnect-routerinput-availabilityzone"></a>
The Availability Zone of the router input.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-mediaconnect-routerinput-configuration"></a>
The configuration settings for a router input.
*Required*: Yes
*Type*: [RouterInputConfiguration](aws-properties-mediaconnect-routerinput-routerinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentQualityAnalysisConfiguration`  <a name="cfn-mediaconnect-routerinput-contentqualityanalysisconfiguration"></a>
The content quality analysis configuration for the router input.
*Required*: No
*Type*: [RouterContentQualityAnalysisConfiguration](aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceConfiguration`  <a name="cfn-mediaconnect-routerinput-maintenanceconfiguration"></a>
The maintenance configuration settings applied to this router input.
*Required*: No
*Type*: [MaintenanceConfiguration](aws-properties-mediaconnect-routerinput-maintenanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBitrate`  <a name="cfn-mediaconnect-routerinput-maximumbitrate"></a>
The maximum bitrate for the router input.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-routerinput-name"></a>
The name of the router input.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-mediaconnect-routerinput-regionname"></a>
The AWS Region where the router input is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoutingScope`  <a name="cfn-mediaconnect-routerinput-routingscope"></a>
Indicates whether the router input is configured for Regional or global routing.
*Required*: Yes
*Type*: String
*Allowed values*: `REGIONAL | GLOBAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-routerinput-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-routerinput-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-mediaconnect-routerinput-tier"></a>
The tier level of the router input.
*Required*: Yes
*Type*: String
*Allowed values*: `INPUT_100 | INPUT_50 | INPUT_20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitEncryption`  <a name="cfn-mediaconnect-routerinput-transitencryption"></a>
 Encryption information.
*Required*: No
*Type*: [RouterInputTransitEncryption](aws-properties-mediaconnect-routerinput-routerinputtransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-routerinput-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-routerinput-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the router input ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-west-2:111122223333:routerInput:86f52099b545" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-routerinput-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-routerinput-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the router input.

`ContentQualityAnalysisType`  <a name="ContentQualityAnalysisType-fn::getatt"></a>
The type of content quality analysis applied to the router input.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the router input was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the router input.

`InputType`  <a name="InputType-fn::getatt"></a>
The type of the router input.

`IpAddress`  <a name="IpAddress-fn::getatt"></a>
The IP address of the router input.

`MaintenanceType`  <a name="MaintenanceType-fn::getatt"></a>
The type of maintenance configuration applied to this router input.

`RoutedOutputs`  <a name="RoutedOutputs-fn::getatt"></a>
The number of router outputs associated with the router input.

`State`  <a name="State-fn::getatt"></a>
The current state of the router input.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the router input was last updated.
