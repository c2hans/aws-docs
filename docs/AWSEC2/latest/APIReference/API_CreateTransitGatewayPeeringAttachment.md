---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPeeringAttachment.html
---

# CreateTransitGatewayPeeringAttachment
<a name="API_CreateTransitGatewayPeeringAttachment"></a>

Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The peer transit gateway can be in your account or a different AWS account.

After you create the peering attachment, the owner of the accepter transit gateway must accept the attachment request.

## Request Parameters
<a name="API_CreateTransitGatewayPeeringAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Options**
Requests a transit gateway peering attachment.
Type: [CreateTransitGatewayPeeringAttachmentRequestOptions](API_CreateTransitGatewayPeeringAttachmentRequestOptions.md) object
Required: No

 **PeerAccountId**
The ID of the AWS account that owns the peer transit gateway.
Type: String
Required: Yes

 **PeerRegion**
The Region where the peer transit gateway is located.
Type: String
Required: Yes

 **PeerTransitGatewayId**
The ID of the peer transit gateway with which to create the peering attachment.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the transit gateway peering attachment.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TransitGatewayId**
The ID of the transit gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayPeeringAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPeeringAttachment**
The transit gateway peering attachment.
Type: [TransitGatewayPeeringAttachment](API_TransitGatewayPeeringAttachment.md) object

## Errors
<a name="API_CreateTransitGatewayPeeringAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateTransitGatewayPeeringAttachment_Examples"></a>

### Example
<a name="API_CreateTransitGatewayPeeringAttachment_Example_1"></a>

This example creates a transit gateway peering attachment for the specified transit gateways. The accepter (peer) transit gateway is in the `us-west-2` Region.

#### Sample Request
<a name="API_CreateTransitGatewayPeeringAttachment_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateTransitGatewayPeeringAttachment
&TransitGatewayId=tgw-11223344aabbcc112
&PeerTransitGatewayId=tgw-1234567890abc1234
&PeerAccountId=123456789012
&PeerRegion=us-west-2
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTransitGatewayPeeringAttachment_Example_1_Response"></a>

```
<CreateTransitGatewayPeeringAttachmentResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>701859fa-6a57-4e55-858c-e63example</requestId>
    <transitGatewayPeeringAttachment>
        <accepterTgwInfo>
            <ownerId>123456789012</ownerId>
            <region>us-west-2</region>
            <transitGatewayId>tgw-1234567890abc1234</transitGatewayId>
        </accepterTgwInfo>
        <creationTime>2019-11-11T11:36:30.000Z</creationTime>
        <requesterTgwInfo>
            <ownerId>123456789012</ownerId>
            <region>us-east-1</region>
            <transitGatewayId>tgw-11223344aabbcc112</transitGatewayId>
        </requesterTgwInfo>
        <state>initiatingRequest</state>
        <transitGatewayAttachmentId>tgw-attach-0a73702c5c7123123</transitGatewayAttachmentId>
    </transitGatewayPeeringAttachment>
</CreateTransitGatewayPeeringAttachmentResponse>
```

## See Also
<a name="API_CreateTransitGatewayPeeringAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayPeeringAttachment)
