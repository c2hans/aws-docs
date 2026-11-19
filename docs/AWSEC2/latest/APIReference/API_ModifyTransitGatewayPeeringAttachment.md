---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayPeeringAttachment.html
---

# ModifyTransitGatewayPeeringAttachment

Modifies the options for a transit gateway peering attachment. The peering attachment must be in the `available` state.

You can allow multipath resilience for your side of an inter-Region transit gateway peering attachment between supported Regions. Multipath resilience isn't supported for transit gateway peering attachments in the same Region. It takes effect only when both the requester and the accepter allow it. To modify the requester side, send the request in the Region of the requester transit gateway. To modify the accepter side, send the request in the Region of the accepter transit gateway. To check whether multipath resilience is in effect, use [DescribeTransitGatewayPeeringAttachments](API_DescribeTransitGatewayPeeringAttachments.md) and check `multipathResilienceStatus`.

## Request Parameters
<a name="API_ModifyTransitGatewayPeeringAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Options**
The options to modify for the transit gateway peering attachment.
Type: [ModifyTransitGatewayPeeringAttachmentRequestOptions](API_ModifyTransitGatewayPeeringAttachmentRequestOptions.md) object
Required: No

 **TransitGatewayAttachmentId**
The ID of the transit gateway peering attachment.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTransitGatewayPeeringAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPeeringAttachment**
Information about the transit gateway peering attachment.
Type: [TransitGatewayPeeringAttachment](API_TransitGatewayPeeringAttachment.md) object

## Errors
<a name="API_ModifyTransitGatewayPeeringAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyTransitGatewayPeeringAttachment_Examples"></a>

### Example – Allow multipath resilience
<a name="API_ModifyTransitGatewayPeeringAttachment_Example_1"></a>

The following example request allows multipath resilience for the requester side of the specified transit gateway peering attachment. Because the accepter doesn't allow multipath resilience yet, the response shows a `multipathResilienceStatus` of `pending`:

#### Sample Request
<a name="API_ModifyTransitGatewayPeeringAttachment_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyTransitGatewayPeeringAttachment
&TransitGatewayAttachmentId=tgw-attach-1234567890abcdef0
&Options.AllowMultipathResilience=true
&Options.MultipathResilienceMode=always-on
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyTransitGatewayPeeringAttachment_Example_1_Response"></a>

```
<ModifyTransitGatewayPeeringAttachmentResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4e9b2c7d-1a3f-4b8e-9c5d-2f6a8e1bexample</requestId>
    <transitGatewayPeeringAttachment>
        <accepterTgwInfo>
            <ownerId>123456789012</ownerId>
            <region>us-west-2</region>
            <transitGatewayId>tgw-1234567890abc1234</transitGatewayId>
        </accepterTgwInfo>
        <creationTime>2026-11-10T11:36:30.000Z</creationTime>
        <options>
            <requesterAllowMultipathResilience>true</requesterAllowMultipathResilience>
            <requesterMultipathResilienceMode>always-on</requesterMultipathResilienceMode>
            <accepterAllowMultipathResilience>false</accepterAllowMultipathResilience>
            <multipathResilienceStatus>pending</multipathResilienceStatus>
        </options>
        <requesterTgwInfo>
            <ownerId>123456789012</ownerId>
            <region>us-east-1</region>
            <transitGatewayId>tgw-11223344aabbcc112</transitGatewayId>
        </requesterTgwInfo>
        <state>available</state>
        <transitGatewayAttachmentId>tgw-attach-1234567890abcdef0</transitGatewayAttachmentId>
    </transitGatewayPeeringAttachment>
</ModifyTransitGatewayPeeringAttachmentResponse>
```

## See Also
<a name="API_ModifyTransitGatewayPeeringAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayPeeringAttachment)
