---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterTransitGatewayMulticastGroupMembers.html
---

# DeregisterTransitGatewayMulticastGroupMembers
<a name="API_DeregisterTransitGatewayMulticastGroupMembers"></a>

Deregisters the specified members (network interfaces) from the transit gateway multicast group.

## Request Parameters
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_RequestParameters"></a>

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
The IDs of the group members' network interfaces.
Type: Array of strings
Required: No

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: No

## Response Elements
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_ResponseElements"></a>

The following elements are returned by the service.

 **deregisteredMulticastGroupMembers**
Information about the deregistered members.
Type: [TransitGatewayMulticastDeregisteredGroupMembers](API_TransitGatewayMulticastDeregisteredGroupMembers.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_Examples"></a>

### Example 1
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_Example_1"></a>

This example deregisters the network interface as a group member `eni-0e246d3269EXAMPLE` from the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeregisterTransitGatewayMulticastGroupMembers
&TransitGatewayMulticastDomainId=tgw-mcast-domain-0c4905cef7EXAMPLE
&NetworkInterfaceIds=eni-0e246d3269EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_Example_1_Response"></a>

```
<DeregisterTransitGatewayMulticastGroupMembersResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>6f4167cd-0870-4858-8872-f1c34EXAMPLE</requestId>
    <registeredMulticastGroupMembers>
        <groupIpAddress>224.0.1.0</groupIpAddress>
        <registeredNetworkInterfaceIds>
            <item>eni-0e246d3269EXAMPLE</item>
        </registeredNetworkInterfaceIds>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
    </registeredMulticastGroupMembers>
</DeregisterTransitGatewayMulticastGroupMembersResponse>
```

## See Also
<a name="API_DeregisterTransitGatewayMulticastGroupMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeregisterTransitGatewayMulticastGroupMembers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
