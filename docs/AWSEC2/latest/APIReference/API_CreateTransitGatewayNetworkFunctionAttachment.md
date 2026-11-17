---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayNetworkFunctionAttachment.html
---

# CreateTransitGatewayNetworkFunctionAttachment
<a name="API_CreateTransitGatewayNetworkFunctionAttachment"></a>

Creates a network function attachment that connects the specified transit gateway to a Gateway Load Balancer endpoint service. Traffic that you route to the attachment is sent to the network function appliances behind the endpoint service. To use this operation, you must be the owner of the transit gateway.

You can create one network function attachment for each combination of transit gateway and endpoint service. The attachment remains in the `pendingAcceptance` state until the endpoint service owner accepts the endpoint connection.

## Request Parameters
<a name="API_CreateTransitGatewayNetworkFunctionAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone.N**
The names of the Availability Zones for the attachment. You must specify at least one Availability Zone, using this parameter, `AvailabilityZoneIds`, or both. Each Availability Zone must be supported by both the transit gateway and the endpoint service.
Type: Array of strings
Required: No

 **AvailabilityZoneId.N**
The IDs of the Availability Zones for the attachment. You must specify at least one Availability Zone, using this parameter, `AvailabilityZones`, or both. Each Availability Zone must be supported by both the transit gateway and the endpoint service.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ServiceName**
The name of the Gateway Load Balancer endpoint service.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the network function attachment.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TransitGatewayId**
The ID of the transit gateway. The transit gateway must be in the `available` state.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayNetworkFunctionAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayNetworkFunctionAttachment**
Information about the network function attachment.
Type: [TransitGatewayNetworkFunctionAttachment](API_TransitGatewayNetworkFunctionAttachment.md) object

## Errors
<a name="API_CreateTransitGatewayNetworkFunctionAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTransitGatewayNetworkFunctionAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayNetworkFunctionAttachment)
