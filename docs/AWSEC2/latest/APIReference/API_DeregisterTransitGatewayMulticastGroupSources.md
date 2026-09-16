---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterTransitGatewayMulticastGroupSources.html
---

# DeregisterTransitGatewayMulticastGroupSources
<a name="API_DeregisterTransitGatewayMulticastGroupSources"></a>

Deregisters the specified sources (network interfaces) from the transit gateway multicast group.

## Request Parameters
<a name="API_DeregisterTransitGatewayMulticastGroupSources_RequestParameters"></a>

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
The IDs of the group sources' network interfaces.
Type: Array of strings
Required: No

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: No

## Response Elements
<a name="API_DeregisterTransitGatewayMulticastGroupSources_ResponseElements"></a>

The following elements are returned by the service.

 **deregisteredMulticastGroupSources**
Information about the deregistered group sources.
Type: [TransitGatewayMulticastDeregisteredGroupSources](API_TransitGatewayMulticastDeregisteredGroupSources.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeregisterTransitGatewayMulticastGroupSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeregisterTransitGatewayMulticastGroupSources_Examples"></a>

### Example 1
<a name="API_DeregisterTransitGatewayMulticastGroupSources_Example_1"></a>

This example deregisters the network interface as a group source `eni-07f290fc3cEXAMPLE` from the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_DeregisterTransitGatewayMulticastGroupSources_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeregisterTransitGatewayMulticastGroupSources
&TransitGatewayMulticastDomainId=tgw-mcast-domain-0c4905cef7EXAMPLE
&NetworkInterfaceIds=eni-07f290fc3cEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeregisterTransitGatewayMulticastGroupSources_Example_1_Response"></a>

```
<DeregisterTransitGatewayMulticastGroupSourcesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1ca916e8-a4b5-4ff8-9fc3-3052dEXAMPLE</requestId>
    <deregisteredMulticastGroupSources>
        <deregisteredNetworkInterfaceIds>
            <item>eni-07f290fc3cEXAMPLE</item>
        </deregisteredNetworkInterfaceIds>
        <groupIpAddress>224.0.1.0</groupIpAddress>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
    </deregisteredMulticastGroupSources>
</DeregisterTransitGatewayMulticastGroupSourcesResponse>
```

## See Also
<a name="API_DeregisterTransitGatewayMulticastGroupSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupSources)
