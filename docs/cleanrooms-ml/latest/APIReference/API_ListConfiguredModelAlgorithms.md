---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListConfiguredModelAlgorithms.html
---

# ListConfiguredModelAlgorithms
<a name="API_ListConfiguredModelAlgorithms"></a>

Returns a list of configured model algorithms.

## Request Syntax
<a name="API_ListConfiguredModelAlgorithms_RequestSyntax"></a>

```
GET /configured-model-algorithms?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConfiguredModelAlgorithms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListConfiguredModelAlgorithms_RequestSyntax) **   <a name="API-ListConfiguredModelAlgorithms-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListConfiguredModelAlgorithms_RequestSyntax) **   <a name="API-ListConfiguredModelAlgorithms-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Request Body
<a name="API_ListConfiguredModelAlgorithms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConfiguredModelAlgorithms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredModelAlgorithms": [
      {
         "configuredModelAlgorithmArn": "string",
         "createTime": "string",
         "description": "string",
         "name": "string",
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConfiguredModelAlgorithms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredModelAlgorithms](#API_ListConfiguredModelAlgorithms_ResponseSyntax) **   <a name="API-ListConfiguredModelAlgorithms-response-configuredModelAlgorithms"></a>
The list of configured model algorithms.
Type: Array of [ConfiguredModelAlgorithmSummary](API_ConfiguredModelAlgorithmSummary.md) objects

 ** [nextToken](#API_ListConfiguredModelAlgorithms_ResponseSyntax) **   <a name="API-ListConfiguredModelAlgorithms-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_ListConfiguredModelAlgorithms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListConfiguredModelAlgorithms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListConfiguredModelAlgorithms)
