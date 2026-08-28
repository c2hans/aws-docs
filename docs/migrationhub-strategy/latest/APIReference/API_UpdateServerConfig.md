---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateServerConfig.html
---

# UpdateServerConfig
<a name="API_UpdateServerConfig"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Updates the configuration of the specified server.

## Request Syntax
<a name="API_UpdateServerConfig_RequestSyntax"></a>

```
POST /update-server-config/ HTTP/1.1
Content-type: application/json

{
   "serverId": "{{string}}",
   "strategyOption": {
      "isPreferred": {{boolean}},
      "strategy": "{{string}}",
      "targetDestination": "{{string}}",
      "toolName": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateServerConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServerConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [serverId](#API_UpdateServerConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateServerConfig-request-serverId"></a>
 The ID of the server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 27.
Pattern: `.*\S.*`
Required: Yes

 ** [strategyOption](#API_UpdateServerConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateServerConfig-request-strategyOption"></a>
 The preferred strategy options for the application component. See the response from [GetServerStrategies](API_GetServerStrategies.md).
Type: [StrategyOption](API_StrategyOption.md) object
Required: No

## Response Syntax
<a name="API_UpdateServerConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateServerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateServerConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateServerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/UpdateServerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/UpdateServerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
