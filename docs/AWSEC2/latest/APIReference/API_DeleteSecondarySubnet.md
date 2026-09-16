---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecondarySubnet.html
---

# DeleteSecondarySubnet
<a name="API_DeleteSecondarySubnet"></a>

Deletes a secondary subnet. A secondary subnet must not contain any secondary interfaces prior to deletion.

## Request Parameters
<a name="API_DeleteSecondarySubnet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SecondarySubnetId**
The ID of the secondary subnet to delete.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteSecondarySubnet_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String

 **requestId**
The ID of the request.
Type: String

 **secondarySubnet**
Information about the secondary subnet being deleted.
Type: [SecondarySubnet](API_SecondarySubnet.md) object

## Errors
<a name="API_DeleteSecondarySubnet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteSecondarySubnet_Examples"></a>

### Example
<a name="API_DeleteSecondarySubnet_Example_1"></a>

This example deletes a secondary subnet.

#### Sample Request
<a name="API_DeleteSecondarySubnet_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteSecondarySubnet
   &SecondarySubnetId=ss-0123456789abcdef0
   &ClientToken=550e8400-e29b-41d4-a716-446655440000
   &AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteSecondarySubnet_Example_1_Response"></a>

```
<DeleteSecondarySubnetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <secondarySubnet>
      <secondarySubnetId>ss-0123456789abcdef0</secondarySubnetId>
      <secondarySubnetArn>arn:aws:ec2:us-east-2:123456789012:secondary-subnet/ss-0123456789abcdef0</secondarySubnetArn>
      <secondaryNetworkId>sn-0123456789abcdef0</secondaryNetworkId>
      <secondaryNetworkType>rdma</secondaryNetworkType>
      <ownerId>123456789012</ownerId>
      <availabilityZoneId>use2-az1</availabilityZoneId>
      <availabilityZone>us-east-2a</availabilityZone>
      <ipv4CidrBlockAssociations>
         <item>
            <associationId>ss-cidr-assoc-56789901234abcdef0</associationId>
            <cidrBlock>10.0.0.0/24</cidrBlock>
            <state>disassociating</state>
         </item>
      </ipv4CidrBlockAssociations>
      <state>delete-in-progress</state>
      <tagSet>
         <item>
            <key>Name</key>
            <value>Prod Secondary Subnet</value>
         </item>
      </tagSet>
   </secondarySubnet>
   <clientToken>550e8400-e29b-41d4-a716-446655440000</clientToken>
</DeleteSecondarySubnetResponse>
```

## See Also
<a name="API_DeleteSecondarySubnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteSecondarySubnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteSecondarySubnet)
