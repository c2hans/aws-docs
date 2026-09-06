---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteVpcEndpoint.html
---

# DeleteVpcEndpoint
<a name="API_DeleteVpcEndpoint"></a>

Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

## Request Syntax
<a name="API_DeleteVpcEndpoint_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteVpcEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-DeleteVpcEndpoint-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [id](#API_DeleteVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-DeleteVpcEndpoint-request-id"></a>
The VPC endpoint identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: Yes

## Response Syntax
<a name="API_DeleteVpcEndpoint_ResponseSyntax"></a>

```
{
   "deleteVpcEndpointDetail": {
      "id": "string",
      "name": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deleteVpcEndpointDetail](#API_DeleteVpcEndpoint_ResponseSyntax) **   <a name="opensearchserverless-DeleteVpcEndpoint-response-deleteVpcEndpointDetail"></a>
Details about the deleted endpoint.
Type: [DeleteVpcEndpointDetail](API_DeleteVpcEndpointDetail.md) object

## Errors
<a name="API_DeleteVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_DeleteVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteVpcEndpoint)
