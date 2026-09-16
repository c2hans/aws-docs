---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteVpcEndpoint.html
---

# DeleteVpcEndpoint
<a name="API_DeleteVpcEndpoint"></a>

Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

## Request Syntax
<a name="API_DeleteVpcEndpoint_RequestSyntax"></a>

```
DELETE /2021-01-01/opensearch/vpcEndpoints/{{VpcEndpointId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteVpcEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VpcEndpointId](#API_DeleteVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-DeleteVpcEndpoint-request-uri-VpcEndpointId"></a>
The unique identifier of the endpoint.
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: Yes

## Request Body
<a name="API_DeleteVpcEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteVpcEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VpcEndpointSummary": {
      "DomainArn": "string",
      "Status": "string",
      "VpcEndpointId": "string",
      "VpcEndpointOwner": "string"
   }
}
```

## Response Elements
<a name="API_DeleteVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpointSummary](#API_DeleteVpcEndpoint_ResponseSyntax) **   <a name="opensearchservice-DeleteVpcEndpoint-response-VpcEndpointSummary"></a>
Information about the deleted endpoint, including its current status (`DELETING` or `DELETE_FAILED`).
Type: [VpcEndpointSummary](API_VpcEndpointSummary.md) object

## Errors
<a name="API_DeleteVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

## See Also
<a name="API_DeleteVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeleteVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeleteVpcEndpoint)
