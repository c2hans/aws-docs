---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-routeroutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput
<a name="aws-resource-mediaconnect-routeroutput"></a>

The `AWS::MediaConnect::RouterOutput` resource defines a connection point in the MediaConnect router that can send content to your destination endpoint. You can configure a router output with either a Regional routing scope or a global routing scope.

## Syntax
<a name="aws-resource-mediaconnect-routeroutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-routeroutput-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::RouterOutput",
  "Properties" : {
      "[AvailabilityZone](#cfn-mediaconnect-routeroutput-availabilityzone)" : {{String}},
      "[Configuration](#cfn-mediaconnect-routeroutput-configuration)" : {{RouterOutputConfiguration}},
      "[MaintenanceConfiguration](#cfn-mediaconnect-routeroutput-maintenanceconfiguration)" : {{MaintenanceConfiguration}},
      "[MaximumBitrate](#cfn-mediaconnect-routeroutput-maximumbitrate)" : {{Integer}},
      "[Name](#cfn-mediaconnect-routeroutput-name)" : {{String}},
      "[RegionName](#cfn-mediaconnect-routeroutput-regionname)" : {{String}},
      "[RoutingScope](#cfn-mediaconnect-routeroutput-routingscope)" : {{String}},
      "[Tags](#cfn-mediaconnect-routeroutput-tags)" : {{[ Tag, ... ]}},
      "[Tier](#cfn-mediaconnect-routeroutput-tier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-routeroutput-syntax.yaml"></a>

```
Type: AWS::MediaConnect::RouterOutput
Properties:
  [AvailabilityZone](#cfn-mediaconnect-routeroutput-availabilityzone): {{String}}
  [Configuration](#cfn-mediaconnect-routeroutput-configuration): {{
    RouterOutputConfiguration}}
  [MaintenanceConfiguration](#cfn-mediaconnect-routeroutput-maintenanceconfiguration): {{
    MaintenanceConfiguration}}
  [MaximumBitrate](#cfn-mediaconnect-routeroutput-maximumbitrate): {{Integer}}
  [Name](#cfn-mediaconnect-routeroutput-name): {{String}}
  [RegionName](#cfn-mediaconnect-routeroutput-regionname): {{String}}
  [RoutingScope](#cfn-mediaconnect-routeroutput-routingscope): {{String}}
  [Tags](#cfn-mediaconnect-routeroutput-tags): {{
    - Tag}}
  [Tier](#cfn-mediaconnect-routeroutput-tier): {{String}}
```

## Properties
<a name="aws-resource-mediaconnect-routeroutput-properties"></a>

`AvailabilityZone`  <a name="cfn-mediaconnect-routeroutput-availabilityzone"></a>
The Availability Zone of the router output.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-mediaconnect-routeroutput-configuration"></a>
The configuration settings for a router output.
*Required*: Yes
*Type*: [RouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceConfiguration`  <a name="cfn-mediaconnect-routeroutput-maintenanceconfiguration"></a>
The maintenance configuration settings applied to this router output.
*Required*: No
*Type*: [MaintenanceConfiguration](aws-properties-mediaconnect-routeroutput-maintenanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBitrate`  <a name="cfn-mediaconnect-routeroutput-maximumbitrate"></a>
The maximum bitrate for the router output.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-routeroutput-name"></a>
The name of the router output.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-mediaconnect-routeroutput-regionname"></a>
The AWS Region where the router output is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoutingScope`  <a name="cfn-mediaconnect-routeroutput-routingscope"></a>
Indicates whether the router output is configured for Regional or global routing.
*Required*: Yes
*Type*: String
*Allowed values*: `REGIONAL | GLOBAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-routeroutput-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-routeroutput-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-mediaconnect-routeroutput-tier"></a>
The tier level of the router output.
*Required*: Yes
*Type*: String
*Allowed values*: `OUTPUT_100 | OUTPUT_50 | OUTPUT_20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-routeroutput-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-routeroutput-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the router output ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-west-2:111122223333:routerOutput:56eb95d755a1" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-routeroutput-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-routeroutput-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the router output.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the router output was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the router output.

`IpAddress`  <a name="IpAddress-fn::getatt"></a>
The IP address of the router output.

`MaintenanceType`  <a name="MaintenanceType-fn::getatt"></a>
The type of maintenance configuration applied to this router output.

`OutputType`  <a name="OutputType-fn::getatt"></a>
The type of the router output.

`RoutedState`  <a name="RoutedState-fn::getatt"></a>
The current state of the association between the router output and its input.

`State`  <a name="State-fn::getatt"></a>
The overall state of the router output.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the router output was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
