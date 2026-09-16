---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstances.html
---

# ListSolFunctionInstances
<a name="API_ListSolFunctionInstances"></a>

Lists network function instances.

A network function instance is a function in a function package .

## Request Syntax
<a name="API_ListSolFunctionInstances_RequestSyntax"></a>

```
GET /sol/vnflcm/v1/vnf_instances?max_results={{maxResults}}&nextpage_opaque_marker={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSolFunctionInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSolFunctionInstances_RequestSyntax) **   <a name="TNB-ListSolFunctionInstances-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSolFunctionInstances_RequestSyntax) **   <a name="TNB-ListSolFunctionInstances-request-uri-nextToken"></a>
The token for the next page of results.

## Request Body
<a name="API_ListSolFunctionInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSolFunctionInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "functionInstances": [
      {
         "arn": "string",
         "id": "string",
         "instantiatedVnfInfo": {
            "vnfState": "string"
         },
         "instantiationState": "string",
         "metadata": {
            "createdAt": "string",
            "lastModified": "string"
         },
         "nsInstanceId": "string",
         "vnfPkgId": "string",
         "vnfPkgName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSolFunctionInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [functionInstances](#API_ListSolFunctionInstances_ResponseSyntax) **   <a name="TNB-ListSolFunctionInstances-response-functionInstances"></a>
Network function instances.
Type: Array of [ListSolFunctionInstanceInfo](API_ListSolFunctionInstanceInfo.md) objects

 ** [nextToken](#API_ListSolFunctionInstances_ResponseSyntax) **   <a name="TNB-ListSolFunctionInstances-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListSolFunctionInstances_Errors"></a>

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
<a name="API_ListSolFunctionInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ListSolFunctionInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolFunctionInstances)
