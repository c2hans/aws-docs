---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerStrategies.html
---

# GetServerStrategies
<a name="API_GetServerStrategies"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves recommended strategies and tools for the specified server.

## Request Syntax
<a name="API_GetServerStrategies_RequestSyntax"></a>

```
GET /get-server-strategies/{{serverId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServerStrategies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serverId](#API_GetServerStrategies_RequestSyntax) **   <a name="migrationhubstrategy-GetServerStrategies-request-uri-serverId"></a>
 The ID of the server.
Length Constraints: Minimum length of 1. Maximum length of 27.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetServerStrategies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServerStrategies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serverStrategies": [
      {
         "isPreferred": boolean,
         "numberOfApplicationComponents": number,
         "recommendation": {
            "strategy": "string",
            "targetDestination": "string",
            "transformationTool": {
               "description": "string",
               "name": "string",
               "tranformationToolInstallationLink": "string"
            }
         },
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetServerStrategies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serverStrategies](#API_GetServerStrategies_ResponseSyntax) **   <a name="migrationhubstrategy-GetServerStrategies-response-serverStrategies"></a>
 A list of strategy recommendations for the server.
Type: Array of [ServerStrategy](API_ServerStrategy.md) objects

## Errors
<a name="API_GetServerStrategies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_GetServerStrategies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetServerStrategies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetServerStrategies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
