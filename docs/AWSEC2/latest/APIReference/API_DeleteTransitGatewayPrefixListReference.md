---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayPrefixListReference.html
---

# DeleteTransitGatewayPrefixListReference
<a name="API_DeleteTransitGatewayPrefixListReference"></a>

Deletes a reference (route) to a prefix list in a specified transit gateway route table.

## Request Parameters
<a name="API_DeleteTransitGatewayPrefixListReference_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrefixListId**
The ID of the prefix list.
Type: String
Required: Yes

 **TransitGatewayRouteTableId**
The ID of the route table.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteTransitGatewayPrefixListReference_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPrefixListReference**
Information about the deleted prefix list reference.
Type: [TransitGatewayPrefixListReference](API_TransitGatewayPrefixListReference.md) object

## Errors
<a name="API_DeleteTransitGatewayPrefixListReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteTransitGatewayPrefixListReference_Examples"></a>

### Example
<a name="API_DeleteTransitGatewayPrefixListReference_Example_1"></a>

This example deletes the specified prefix list reference in the specified transit gateway route table.

#### Sample Request
<a name="API_DeleteTransitGatewayPrefixListReference_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteTransitGatewayPrefixListReference
&TransitGatewayRouteTableId=tgw-rtb-0f98a0a5d09abcabc
&PrefixListId=pl-001122334455aabbc
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteTransitGatewayPrefixListReference_Example_1_Response"></a>

```
<DeleteTransitGatewayPrefixListReferenceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>482823e8-8165-4312-86ee-example</requestId>
    <transitGatewayPrefixListReference>
        <blackhole>false</blackhole>
        <prefixListId>pl-001122334455aabbc</prefixListId>
        <prefixListOwnerId>123456789012</prefixListOwnerId>
        <state>deleting</state>
        <transitGatewayRouteTableId>tgw-rtb-0f98a0a5d09abcabc</transitGatewayRouteTableId>
    </transitGatewayPrefixListReference>
</DeleteTransitGatewayPrefixListReferenceResponse>
```

## See Also
<a name="API_DeleteTransitGatewayPrefixListReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteTransitGatewayPrefixListReference)
