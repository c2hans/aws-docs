---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConcentrator.html
---

# CreateVpnConcentrator
<a name="API_CreateVpnConcentrator"></a>

Creates a VPN concentrator that aggregates multiple VPN connections to a transit gateway.

## Request Parameters
<a name="API_CreateVpnConcentrator_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to apply to the VPN concentrator during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TransitGatewayId**
The ID of the transit gateway to attach the VPN concentrator to.
Type: String
Required: No

 **Type**
The type of VPN concentrator to create.
Type: String
Valid Values: `ipsec.1`
Required: Yes

## Response Elements
<a name="API_CreateVpnConcentrator_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpnConcentrator**
Information about the VPN concentrator.
Type: [VpnConcentrator](API_VpnConcentrator.md) object

## Errors
<a name="API_CreateVpnConcentrator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpnConcentrator_Examples"></a>

### Example
<a name="API_CreateVpnConcentrator_Example_1"></a>

This example creates a VPN Concentrator on the Transit Gateway `tgw-0eae06e326d7c27d8`.

#### Sample Request
<a name="API_CreateVpnConcentrator_Example_1_Request"></a>

```
https://ec2.us-east-1.amazonaws.com/?Version=2016-11-15&Action=CreateVpnConcentrator
                   &Type=ipsec.1
                   &TransitGatewayId=tgw-0eae06e326d7c27d8
```

#### Sample Response
<a name="API_CreateVpnConcentrator_Example_1_Response"></a>

```
<CreateVpnConcentratorResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c875a725-2eb7-4deb-ad8f-4445c071460f</requestId>
    <vpnConcentrator>
        <state>pending</state>
        <transitGatewayAttachmentId>tgw-attach-04a445da95a6814cc</transitGatewayAttachmentId>
        <transitGatewayId>tgw-0eae06e326d7c27d8</transitGatewayId>
        <type>ipsec.1</type>
        <vpnConcentratorId>vcn-0767cb7521c5c4945</vpnConcentratorId>
    </vpnConcentrator>
</CreateVpnConcentratorResponse>
```

## See Also
<a name="API_CreateVpnConcentrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpnConcentrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpnConcentrator)
