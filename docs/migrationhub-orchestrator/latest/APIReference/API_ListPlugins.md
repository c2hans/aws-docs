---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListPlugins.html
---

# ListPlugins
<a name="API_ListPlugins"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

List AWS Migration Hub Orchestrator plugins.

## Request Syntax
<a name="API_ListPlugins_RequestSyntax"></a>

```
GET /plugins?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPlugins_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPlugins_RequestSyntax) **   <a name="migrationhuborchestrator-ListPlugins-request-uri-maxResults"></a>
The maximum number of plugins that can be returned.
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [nextToken](#API_ListPlugins_RequestSyntax) **   <a name="migrationhuborchestrator-ListPlugins-request-uri-nextToken"></a>
The pagination token.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Request Body
<a name="API_ListPlugins_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPlugins_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "plugins": [
      {
         "hostname": "string",
         "ipAddress": "string",
         "pluginId": "string",
         "registeredTime": "string",
         "status": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPlugins_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPlugins_ResponseSyntax) **   <a name="migrationhuborchestrator-ListPlugins-response-nextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

 ** [plugins](#API_ListPlugins_ResponseSyntax) **   <a name="migrationhuborchestrator-ListPlugins-response-plugins"></a>
Migration Hub Orchestrator plugins.
Type: Array of [PluginSummary](API_PluginSummary.md) objects

## Errors
<a name="API_ListPlugins_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListPlugins_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/ListPlugins)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/ListPlugins)
