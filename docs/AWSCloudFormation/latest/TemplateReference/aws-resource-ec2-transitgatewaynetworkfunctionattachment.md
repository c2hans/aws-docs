---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaynetworkfunctionattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayNetworkFunctionAttachment
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment"></a>

<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-description"></a>The `AWS::EC2::TransitGatewayNetworkFunctionAttachment` resource Property description not available. for EC2.

## Syntax
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayNetworkFunctionAttachment",
  "Properties" : {
      "[AvailabilityZoneIds](#cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzoneids)" : {{[ String, ... ]}},
      "[AvailabilityZones](#cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzones)" : {{[ String, ... ]}},
      "[ServiceName](#cfn-ec2-transitgatewaynetworkfunctionattachment-servicename)" : {{String}},
      "[Tags](#cfn-ec2-transitgatewaynetworkfunctionattachment-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-transitgatewaynetworkfunctionattachment-transitgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayNetworkFunctionAttachment
Properties:
  [AvailabilityZoneIds](#cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzoneids): {{
    - String}}
  [AvailabilityZones](#cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzones): {{
    - String}}
  [ServiceName](#cfn-ec2-transitgatewaynetworkfunctionattachment-servicename): {{String}}
  [Tags](#cfn-ec2-transitgatewaynetworkfunctionattachment-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-transitgatewaynetworkfunctionattachment-transitgatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-properties"></a>

`AvailabilityZoneIds`  <a name="cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzoneids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZones`  <a name="cfn-ec2-transitgatewaynetworkfunctionattachment-availabilityzones"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-ec2-transitgatewaynetworkfunctionattachment-servicename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-transitgatewaynetworkfunctionattachment-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewaynetworkfunctionattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-transitgatewaynetworkfunctionattachment-transitgatewayid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaynetworkfunctionattachment-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`ResourceId`  <a name="ResourceId-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

`TransitGatewayAttachmentId`  <a name="TransitGatewayAttachmentId-fn::getatt"></a>
Property description not available.
