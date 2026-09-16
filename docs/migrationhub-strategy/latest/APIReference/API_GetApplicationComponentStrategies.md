---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentStrategies.html
---

# GetApplicationComponentStrategies
<a name="API_GetApplicationComponentStrategies"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves a list of all the recommended strategies and tools for an application component running on a server.

## Request Syntax
<a name="API_GetApplicationComponentStrategies_RequestSyntax"></a>

```
GET /get-applicationcomponent-strategies/{{applicationComponentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplicationComponentStrategies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationComponentId](#API_GetApplicationComponentStrategies_RequestSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentStrategies-request-uri-applicationComponentId"></a>
 The ID of the application component. The ID is unique within an AWS account.
Length Constraints: Minimum length of 0. Maximum length of 44.
Pattern: `.*[0-9a-zA-Z-]+.*`
Required: Yes

## Request Body
<a name="API_GetApplicationComponentStrategies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplicationComponentStrategies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationComponentStrategies": [
      {
         "isPreferred": boolean,
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
<a name="API_GetApplicationComponentStrategies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationComponentStrategies](#API_GetApplicationComponentStrategies_ResponseSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentStrategies-response-applicationComponentStrategies"></a>
 A list of application component strategy recommendations.
Type: Array of [ApplicationComponentStrategy](API_ApplicationComponentStrategy.md) objects

## Errors
<a name="API_GetApplicationComponentStrategies_Errors"></a>

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

## See Also
<a name="API_GetApplicationComponentStrategies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetApplicationComponentStrategies)
