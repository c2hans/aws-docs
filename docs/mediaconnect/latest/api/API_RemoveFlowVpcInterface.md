---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowVpcInterface.html
---

# RemoveFlowVpcInterface
<a name="API_RemoveFlowVpcInterface"></a>

 Removes a VPC Interface from an existing flow. This request can be made only on a VPC interface that does not have a Source or Output associated with it. If the VPC interface is referenced by a Source or Output, you must first delete or update the Source or Output to no longer reference the VPC interface.

## Request Syntax
<a name="API_RemoveFlowVpcInterface_RequestSyntax"></a>

```
DELETE /v1/flows/{{flowArn}}/vpcInterfaces/{{vpcInterfaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveFlowVpcInterface_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_RemoveFlowVpcInterface_RequestSyntax) **   <a name="mediaconnect-RemoveFlowVpcInterface-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to remove a VPC interface from.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

 ** [vpcInterfaceName](#API_RemoveFlowVpcInterface_RequestSyntax) **   <a name="mediaconnect-RemoveFlowVpcInterface-request-uri-vpcInterfaceName"></a>
 The name of the VPC interface that you want to remove.
Required: Yes

## Request Body
<a name="API_RemoveFlowVpcInterface_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveFlowVpcInterface_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowArn": "string",
   "nonDeletedNetworkInterfaceIds": [ "string" ],
   "vpcInterfaceName": "string"
}
```

## Response Elements
<a name="API_RemoveFlowVpcInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_RemoveFlowVpcInterface_ResponseSyntax) **   <a name="mediaconnect-RemoveFlowVpcInterface-response-flowArn"></a>
 The ARN of the flow that is associated with the VPC interface you removed.
Type: String

 ** [nonDeletedNetworkInterfaceIds](#API_RemoveFlowVpcInterface_ResponseSyntax) **   <a name="mediaconnect-RemoveFlowVpcInterface-response-nonDeletedNetworkInterfaceIds"></a>
 IDs of network interfaces associated with the removed VPC interface that MediaConnect was unable to remove.
Type: Array of strings

 ** [vpcInterfaceName](#API_RemoveFlowVpcInterface_ResponseSyntax) **   <a name="mediaconnect-RemoveFlowVpcInterface-response-vpcInterfaceName"></a>
 The name of the VPC interface that was removed.
Type: String

## Errors
<a name="API_RemoveFlowVpcInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_RemoveFlowVpcInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/RemoveFlowVpcInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RemoveFlowVpcInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
