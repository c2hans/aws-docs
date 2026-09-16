---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateClientVpnTargetNetwork.html
---

# AssociateClientVpnTargetNetwork
<a name="API_AssociateClientVpnTargetNetwork"></a>

Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.

If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, the specified subnet must be in the same VPC. To specify a subnet that's in a different VPC, you must first modify the Client VPN endpoint ([ModifyClientVpnEndpoint](API_ModifyClientVpnEndpoint.md)) and change the VPC that's associated with it.

## Request Parameters
<a name="API_AssociateClientVpnTargetNetwork_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone**
The Availability Zone name for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both `SubnetId` and `AvailabilityZone`.
Type: String
Required: No

 **AvailabilityZoneId**
The Availability Zone ID for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both `AvailabilityZone` and `AvailabilityZoneId`.
Type: String
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SubnetId**
The ID of the subnet to associate with the Client VPN endpoint. Required for VPC-based endpoints. For Transit Gateway-based endpoints, use `AvailabilityZone` or `AvailabilityZoneId` instead.
Type: String
Required: No

## Response Elements
<a name="API_AssociateClientVpnTargetNetwork_ResponseElements"></a>

The following elements are returned by the service.

 **associationId**
The unique ID of the target network association.
Type: String

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the target network association.
Type: [AssociationStatus](API_AssociationStatus.md) object

## Errors
<a name="API_AssociateClientVpnTargetNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateClientVpnTargetNetwork_Examples"></a>

### Example
<a name="API_AssociateClientVpnTargetNetwork_Example_1"></a>

This example associates a subnet with a Client VPN endpoint.

#### Sample Request
<a name="API_AssociateClientVpnTargetNetwork_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateClientVpnTargetNetwork
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&SubnetId=subnet-057fa0918fEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateClientVpnTargetNetwork_Example_1_Response"></a>

```
<AssociateClientVpnTargetNetworkResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7d1f819b-7f2a-4f81-aabf-81caeEXAMPLE</requestId>
    <status>
        <code>associating</code>
    </status>
    <associationId>cvpn-assoc-0822b0983cEXAMPLE</associationId>
</AssociateClientVpnTargetNetworkRespons>
```

## See Also
<a name="API_AssociateClientVpnTargetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateClientVpnTargetNetwork)
