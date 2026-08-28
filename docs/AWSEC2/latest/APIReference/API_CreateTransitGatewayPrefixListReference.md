---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPrefixListReference.html
---

# CreateTransitGatewayPrefixListReference
<a name="API_CreateTransitGatewayPrefixListReference"></a>

Creates a reference (route) to a prefix list in a specified transit gateway route table.

## Request Parameters
<a name="API_CreateTransitGatewayPrefixListReference_RequestParameters"></a>

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
The ID of the prefix list that is used for destination matches.
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
<a name="API_CreateTransitGatewayPrefixListReference_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPrefixListReference**
Information about the prefix list reference.
Type: [TransitGatewayPrefixListReference](API_TransitGatewayPrefixListReference.md) object

## Errors
<a name="API_CreateTransitGatewayPrefixListReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateTransitGatewayPrefixListReference_Examples"></a>

### Example
<a name="API_CreateTransitGatewayPrefixListReference_Example_1"></a>

This example creates a reference to a prefix list in the specified transit gateway route table.

#### Sample Request
<a name="API_CreateTransitGatewayPrefixListReference_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateTransitGatewayPrefixListReference
&TransitGatewayRouteTableId=tgw-rtb-0f98a0a5d09abcabc
&PrefixListId=pl-001122334455aabbc
&TransitGatewayAttachmentId=tgw-attach-01234567abcabcabc
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTransitGatewayPrefixListReference_Example_1_Response"></a>

```
<CreateTransitGatewayPrefixListReferenceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>326fdc31-cd8d-491a-824a-example</requestId>
    <transitGatewayPrefixListReference>
        <blackhole>false</blackhole>
        <prefixListId>pl-001122334455aabbc</prefixListId>
        <prefixListOwnerId>123456789012</prefixListOwnerId>
        <state>pending</state>
        <transitGatewayAttachment>
            <resourceId>vpn-12312312312312312</resourceId>
            <resourceType>vpn</resourceType>
            <transitGatewayAttachmentId>tgw-attach-01234567abcabcabc</transitGatewayAttachmentId>
        </transitGatewayAttachment>
        <transitGatewayRouteTableId>tgw-rtb-0f98a0a5d09abcabc</transitGatewayRouteTableId>
    </transitGatewayPrefixListReference>
</CreateTransitGatewayPrefixListReferenceResponse>
```

## See Also
<a name="API_CreateTransitGatewayPrefixListReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayPrefixListReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
