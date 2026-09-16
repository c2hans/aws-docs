---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperations.html
---

# ListSolNetworkOperations
<a name="API_ListSolNetworkOperations"></a>

Lists details for a network operation, including when the operation started and the status of the operation.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Request Syntax
<a name="API_ListSolNetworkOperations_RequestSyntax"></a>

```
GET /sol/nslcm/v1/ns_lcm_op_occs?max_results={{maxResults}}&nextpage_opaque_marker={{nextToken}}&nsInstanceId={{nsInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSolNetworkOperations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSolNetworkOperations_RequestSyntax) **   <a name="TNB-ListSolNetworkOperations-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSolNetworkOperations_RequestSyntax) **   <a name="TNB-ListSolNetworkOperations-request-uri-nextToken"></a>
The token for the next page of results.

 ** [nsInstanceId](#API_ListSolNetworkOperations_RequestSyntax) **   <a name="TNB-ListSolNetworkOperations-request-uri-nsInstanceId"></a>
Network instance id filter, to retrieve network operations associated to a network instance.
Pattern: `ni-[a-f0-9]{17}`

## Request Body
<a name="API_ListSolNetworkOperations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSolNetworkOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "networkOperations": [
      {
         "arn": "string",
         "error": {
            "detail": "string",
            "title": "string"
         },
         "id": "string",
         "lcmOperationType": "string",
         "metadata": {
            "createdAt": "string",
            "lastModified": "string",
            "nsdInfoId": "string",
            "vnfInstanceId": "string"
         },
         "nsInstanceId": "string",
         "operationState": "string",
         "updateType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSolNetworkOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkOperations](#API_ListSolNetworkOperations_ResponseSyntax) **   <a name="TNB-ListSolNetworkOperations-response-networkOperations"></a>
Lists network operation occurrences. Lifecycle management operations are deploy, update, or delete operations.
Type: Array of [ListSolNetworkOperationsInfo](API_ListSolNetworkOperationsInfo.md) objects

 ** [nextToken](#API_ListSolNetworkOperations_ResponseSyntax) **   <a name="TNB-ListSolNetworkOperations-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListSolNetworkOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListSolNetworkOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ListSolNetworkOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkOperations)
