---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListAvailableModules.html
---

# ListAvailableModules

Lists the modules that you can attach, newest first by `createdAt`. Results are paginated. Use `nextToken` to get the next page. Before you list MARKETPLACE modules, or list without `subscriptionType`, create a gateway.

## Request Syntax
<a name="API_ListAvailableModules_RequestSyntax"></a>

```
GET /available-modules?maxResults={{maxResults}}&nextToken={{nextToken}}&subscriptionType={{subscriptionType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAvailableModules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAvailableModules_RequestSyntax) **   <a name="rtbfabric-ListAvailableModules-request-uri-maxResults"></a>
The maximum number of results for each page, from 1 to 10. The default is 10.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [nextToken](#API_ListAvailableModules_RequestSyntax) **   <a name="rtbfabric-ListAvailableModules-request-uri-nextToken"></a>
If nextToken is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours; using an expired token fails with ValidationException.

 ** [subscriptionType](#API_ListAvailableModules_RequestSyntax) **   <a name="rtbfabric-ListAvailableModules-request-uri-subscriptionType"></a>
Lists only modules of this type: AWS\_BUILT\_IN for built-in modules, or MARKETPLACE for modules that you subscribe to in AWS Marketplace.
Valid Values: `MARKETPLACE | PRIVATE | AWS_BUILT_IN`

## Request Body
<a name="API_ListAvailableModules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAvailableModules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modules": [
      {
         "marketplaceProductId": "string",
         "moduleArn": "string",
         "moduleId": "string",
         "moduleName": "string",
         "subscriptionStatus": "string",
         "subscriptionType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailableModules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modules](#API_ListAvailableModules_ResponseSyntax) **   <a name="rtbfabric-ListAvailableModules-response-modules"></a>
The modules on this page, newest first.
Type: Array of [AvailableModuleSummary](API_AvailableModuleSummary.md) objects

 ** [nextToken](#API_ListAvailableModules_ResponseSyntax) **   <a name="rtbfabric-ListAvailableModules-response-nextToken"></a>
If nextToken is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours; using an expired token fails with ValidationException.
Type: String

## Errors
<a name="API_ListAvailableModules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListAvailableModules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/ListAvailableModules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ListAvailableModules)
