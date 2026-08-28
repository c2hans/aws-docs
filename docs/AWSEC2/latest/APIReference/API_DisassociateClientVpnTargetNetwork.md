---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateClientVpnTargetNetwork.html
---

# DisassociateClientVpnTargetNetwork
<a name="API_DisassociateClientVpnTargetNetwork"></a>

Disassociates a target network from the specified Client VPN endpoint. When you disassociate the last target network from a Client VPN, the following happens:
+ The route that was automatically added for the VPC is deleted
+ All active client connections are terminated
+ New client connections are disallowed
+ The Client VPN endpoint's status changes to `pending-associate`

## Request Parameters
<a name="API_DisassociateClientVpnTargetNetwork_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The ID of the target network association.
Type: String
Required: Yes

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint from which to disassociate the target network.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DisassociateClientVpnTargetNetwork_ResponseElements"></a>

The following elements are returned by the service.

 **associationId**
The ID of the target network association.
Type: String

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the target network association.
Type: [AssociationStatus](API_AssociationStatus.md) object

## Errors
<a name="API_DisassociateClientVpnTargetNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateClientVpnTargetNetwork_Examples"></a>

### Example
<a name="API_DisassociateClientVpnTargetNetwork_Example_1"></a>

This example disassociates a target network from a Client VPN endpoint.

#### Sample Request
<a name="API_DisassociateClientVpnTargetNetwork_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateClientVpnTargetNetwork
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&AssociationId=cvpn-assoc-0bc4bd8cecEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateClientVpnTargetNetwork_Example_1_Response"></a>

```
<DisassociateClientVpnTargetNetworkResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>61312648-93ec-4a86-a1d1-098c9EXAMPLE</requestId>
    <status>
        <code>disassociating</code>
    </status>
    <associationId>cvpn-assoc-0bc4bd8cecEXAMPLE</associationId>
</DisassociateClientVpnTargetNetworkResponse>
```

## See Also
<a name="API_DisassociateClientVpnTargetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateClientVpnTargetNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
