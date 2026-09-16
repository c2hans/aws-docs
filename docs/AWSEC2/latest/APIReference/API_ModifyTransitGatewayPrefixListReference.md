---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayPrefixListReference.html
---

# ModifyTransitGatewayPrefixListReference
<a name="API_ModifyTransitGatewayPrefixListReference"></a>

Modifies a reference (route) to a prefix list in a specified transit gateway route table.

## Request Parameters
<a name="API_ModifyTransitGatewayPrefixListReference_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Blackhole**
Indicates whether to drop traffic that matches this route.
Type: Boolean
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrefixListId**
The ID of the prefix list.
Type: String
Required: Yes

 **TransitGatewayAttachmentId**
The ID of the attachment to which traffic is routed.
Type: String
Required: No

 **TransitGatewayRouteTableId**
The ID of the transit gateway route table.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTransitGatewayPrefixListReference_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPrefixListReference**
Information about the prefix list reference.
Type: [TransitGatewayPrefixListReference](API_TransitGatewayPrefixListReference.md) object

## Errors
<a name="API_ModifyTransitGatewayPrefixListReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyTransitGatewayPrefixListReference_Examples"></a>

### Example
<a name="API_ModifyTransitGatewayPrefixListReference_Example_1"></a>

This example modifies the prefix list reference in the specified route table by changing the attachment to which traffic is routed.

#### Sample Request
<a name="API_ModifyTransitGatewayPrefixListReference_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyTransitGatewayPrefixListReference
&TransitGatewayRouteTableId=tgw-rtb-0f98a0a5d09abcabc
&PrefixListId=pl-001122334455aabbc
&TransitGatewayAttachmentId=tgw-attach-11223344aabbcc112
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyTransitGatewayPrefixListReference_Example_1_Response"></a>

```
<ModifyTransitGatewayPrefixListReferenceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>bbd3e523-3e5b-4d3b-b010-example</requestId>
    <transitGatewayPrefixListReference>
        <blackhole>false</blackhole>
        <prefixListId>pl-001122334455aabbc</prefixListId>
        <prefixListOwnerId>123456789012</prefixListOwnerId>
        <state>modifying</state>
        <transitGatewayAttachment>
            <resourceId>tgw-012233aabbcc11223</resourceId>
            <resourceType>peering</resourceType>
            <transitGatewayAttachmentId>tgw-attach-11223344aabbcc112</transitGatewayAttachmentId>
        </transitGatewayAttachment>
        <transitGatewayRouteTableId>tgw-rtb-0f98a0a5d09abcabc</transitGatewayRouteTableId>
    </transitGatewayPrefixListReference>
</ModifyTransitGatewayPrefixListReferenceResponse>
```

## See Also
<a name="API_ModifyTransitGatewayPrefixListReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayPrefixListReference)
