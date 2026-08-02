---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpoints.html
---

# ListVpcEndpoints
<a name="API_ListVpcEndpoints"></a>

Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current AWS account and Region.

## Request Syntax
<a name="API_ListVpcEndpoints_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/vpcEndpoints?nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVpcEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListVpcEndpoints_RequestSyntax) **   <a name="opensearchservice-ListVpcEndpoints-request-uri-NextToken"></a>
If your initial `ListVpcEndpoints` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListVpcEndpoints` operations, which returns results in the next page.

## Request Body
<a name="API_ListVpcEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVpcEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "VpcEndpointSummaryList": [
      {
         "DomainArn": "string",
         "Status": "string",
         "VpcEndpointId": "string",
         "VpcEndpointOwner": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVpcEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVpcEndpoints_ResponseSyntax) **   <a name="opensearchservice-ListVpcEndpoints-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [VpcEndpointSummaryList](#API_ListVpcEndpoints_ResponseSyntax) **   <a name="opensearchservice-ListVpcEndpoints-response-VpcEndpointSummaryList"></a>
Information about each endpoint.
Type: Array of [VpcEndpointSummary](API_VpcEndpointSummary.md) objects

## Errors
<a name="API_ListVpcEndpoints_Errors"></a>

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

## See Also
<a name="API_ListVpcEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListVpcEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListVpcEndpoints)
