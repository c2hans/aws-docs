---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayPrefixListReferences.html
---

# GetTransitGatewayPrefixListReferences
<a name="API_GetTransitGatewayPrefixListReferences"></a>

Gets information about the prefix list references in a specified transit gateway route table.

## Request Parameters
<a name="API_GetTransitGatewayPrefixListReferences_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `attachment.resource-id` - The ID of the resource for the attachment.
+  `attachment.resource-type` - The type of resource for the attachment. Valid values are `vpc` \| `vpn` \| `direct-connect-gateway` \| `peering`.
+  `attachment.transit-gateway-attachment-id` - The ID of the attachment.
+  `is-blackhole` - Whether traffic matching the route is blocked (`true` \| `false`).
+  `prefix-list-id` - The ID of the prefix list.
+  `prefix-list-owner-id` - The ID of the owner of the prefix list.
+  `state` - The state of the prefix list reference (`pending` \| `available` \| `modifying` \| `deleting`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **TransitGatewayRouteTableId**
The ID of the transit gateway route table.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTransitGatewayPrefixListReferences_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPrefixListReferenceSet**
Information about the prefix list references.
Type: Array of [TransitGatewayPrefixListReference](API_TransitGatewayPrefixListReference.md) objects

## Errors
<a name="API_GetTransitGatewayPrefixListReferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetTransitGatewayPrefixListReferences_Examples"></a>

### Example
<a name="API_GetTransitGatewayPrefixListReferences_Example_1"></a>

This example gets the prefix list references for the specified transit gateway route table.

#### Sample Request
<a name="API_GetTransitGatewayPrefixListReferences_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetTransitGatewayPrefixListReferences
&TransitGatewayRouteTableId=tgw-rtb-0f98a0a5d09abcabc
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetTransitGatewayPrefixListReferences_Example_1_Response"></a>

```
<GetTransitGatewayPrefixListReferencesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>b194523f-807a-4a41-920a-example</requestId>
    <transitGatewayPrefixListReferenceSet>
        <item>
            <blackhole>false</blackhole>
            <prefixListId>pl-001122334455aabbc</prefixListId>
            <prefixListOwnerId>123456789012</prefixListOwnerId>
            <state>available</state>
            <transitGatewayAttachment>
                <resourceId>vpn-12312312312312312</resourceId>
                <resourceType>vpn</resourceType>
                <transitGatewayAttachmentId>tgw-attach-01234567abcabcabc</transitGatewayAttachmentId>
            </transitGatewayAttachment>
            <transitGatewayRouteTableId>tgw-rtb-0f98a0a5d09abcabc</transitGatewayRouteTableId>
        </item>
    </transitGatewayPrefixListReferenceSet>
</GetTransitGatewayPrefixListReferencesResponse>
```

## See Also
<a name="API_GetTransitGatewayPrefixListReferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetTransitGatewayPrefixListReferences)
