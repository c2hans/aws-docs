---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterTransitGatewayMulticastGroupMembers.html
---

# RegisterTransitGatewayMulticastGroupMembers
<a name="API_RegisterTransitGatewayMulticastGroupMembers"></a>

Registers members (network interfaces) with the transit gateway multicast group. A member is a network interface associated with a supported EC2 instance that receives multicast traffic. For more information, see [Multicast on transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html) in the * AWS Transit Gateways Guide*.

After you add the members, use [SearchTransitGatewayMulticastGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayMulticastGroups.html) to verify that the members were added to the transit gateway multicast group.

## Request Parameters
<a name="API_RegisterTransitGatewayMulticastGroupMembers_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupIpAddress**
The IP address assigned to the transit gateway multicast group.
Type: String
Required: No

 **NetworkInterfaceIds.N**
The group members' network interface IDs to register with the transit gateway multicast group.
Type: Array of strings
Required: Yes

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: Yes

## Response Elements
<a name="API_RegisterTransitGatewayMulticastGroupMembers_ResponseElements"></a>

The following elements are returned by the service.

 **registeredMulticastGroupMembers**
Information about the registered transit gateway multicast group members.
Type: [TransitGatewayMulticastRegisteredGroupMembers](API_TransitGatewayMulticastRegisteredGroupMembers.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_RegisterTransitGatewayMulticastGroupMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RegisterTransitGatewayMulticastGroupMembers_Examples"></a>

### Example 1
<a name="API_RegisterTransitGatewayMulticastGroupMembers_Example_1"></a>

This example registers the network interface as a group member `eni-0e246d3269EXAMPLE` with the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_RegisterTransitGatewayMulticastGroupMembers_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RegisterTransitGatewayMulticastGroupMembers
&TransitGatewayMulticastDomainId=tgw-mcast-domain-0c4905cef7EXAMPLE
&NetworkInterfaceIds=eni-0e246d3269EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_RegisterTransitGatewayMulticastGroupMembers_Example_1_Response"></a>

```
<RegisterTransitGatewayMulticastGroupMembersResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>6f4167cd-0870-4858-8872-f1c34EXAMPLE</requestId>
    <registeredMulticastGroupMembers>
        <groupIpAddress>224.0.1.0</groupIpAddress>
        <registeredNetworkInterfaceIds>
            <item>eni-0e246d3269EXAMPLE</item>
        </registeredNetworkInterfaceIds>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
    </registeredMulticastGroupMembers>
</RegisterTransitGatewayMulticastGroupMembersResponse>
```

## See Also
<a name="API_RegisterTransitGatewayMulticastGroupMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RegisterTransitGatewayMulticastGroupMembers)
