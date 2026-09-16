---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorSession.html
---

# ModifyTrafficMirrorSession
<a name="API_ModifyTrafficMirrorSession"></a>

Modifies a Traffic Mirror session.

## Request Parameters
<a name="API_ModifyTrafficMirrorSession_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
The description to assign to the Traffic Mirror session.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PacketLength**
The number of bytes in each packet to mirror. These are bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet.
For sessions with Network Load Balancer (NLB) traffic mirror targets, the default `PacketLength` will be set to 8500. Valid values are 1-8500. Setting a `PacketLength` greater than 8500 will result in an error response.
Type: Integer
Required: No

 **RemoveField.N**
The properties that you want to remove from the Traffic Mirror session.
When you remove a property from a Traffic Mirror session, the property is set to the default.
Type: Array of strings
Valid Values: `packet-length | description | virtual-network-id`
Required: No

 **SessionNumber**
The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.
Valid values are 1-32766.
Type: Integer
Required: No

 **TrafficMirrorFilterId**
The ID of the Traffic Mirror filter.
Type: String
Required: No

 **TrafficMirrorSessionId**
The ID of the Traffic Mirror session.
Type: String
Required: Yes

 **TrafficMirrorTargetId**
The Traffic Mirror target. The target must be in the same VPC as the source, or have a VPC peering connection with the source.
Type: String
Required: No

 **VirtualNetworkId**
The virtual network ID of the Traffic Mirror session.
Type: Integer
Required: No

## Response Elements
<a name="API_ModifyTrafficMirrorSession_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **trafficMirrorSession**
Information about the Traffic Mirror session.
Type: [TrafficMirrorSession](API_TrafficMirrorSession.md) object

## Errors
<a name="API_ModifyTrafficMirrorSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyTrafficMirrorSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTrafficMirrorSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTrafficMirrorSession)
