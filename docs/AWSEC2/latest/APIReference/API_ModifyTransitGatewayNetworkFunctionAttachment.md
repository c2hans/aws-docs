---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayNetworkFunctionAttachment.html
---

# ModifyTransitGatewayNetworkFunctionAttachment
<a name="API_ModifyTransitGatewayNetworkFunctionAttachment"></a>

Adds Availability Zones to or removes Availability Zones from the specified network function attachment. The attachment must be in the `available` state. You must specify at least one Availability Zone to add or remove, and the attachment must keep at least one Availability Zone.

Adding an Availability Zone provisions a new Gateway Load Balancer endpoint in that Availability Zone. If the endpoint service doesn't automatically accept connection requests, the endpoint service owner must accept the endpoint connection for each Availability Zone that you add.

## Request Parameters
<a name="API_ModifyTransitGatewayNetworkFunctionAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddAvailabilityZone.N**
The names of the Availability Zones to add to the attachment. You can't add and remove the same Availability Zone in a single request.
Type: Array of strings
Required: No

 **AddAvailabilityZoneId.N**
The IDs of the Availability Zones to add to the attachment. You can't add and remove the same Availability Zone in a single request.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RemoveAvailabilityZone.N**
The names of the Availability Zones to remove from the attachment. Each Availability Zone must be currently in the attachment.
Type: Array of strings
Required: No

 **RemoveAvailabilityZoneId.N**
The IDs of the Availability Zones to remove from the attachment. Each Availability Zone must be currently in the attachment.
Type: Array of strings
Required: No

 **TransitGatewayAttachmentId**
The ID of the network function attachment.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTransitGatewayNetworkFunctionAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayNetworkFunctionAttachment**
Information about the network function attachment.
Type: [TransitGatewayNetworkFunctionAttachment](API_TransitGatewayNetworkFunctionAttachment.md) object

## Errors
<a name="API_ModifyTransitGatewayNetworkFunctionAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyTransitGatewayNetworkFunctionAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayNetworkFunctionAttachment)
