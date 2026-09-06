---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteEnvironmentBlueprintConfiguration.html
---

# DeleteEnvironmentBlueprintConfiguration
<a name="API_DeleteEnvironmentBlueprintConfiguration"></a>

Deletes the blueprint configuration in Amazon DataZone.

## Request Syntax
<a name="API_DeleteEnvironmentBlueprintConfiguration_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/environment-blueprint-configurations/{{environmentBlueprintIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEnvironmentBlueprintConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-DeleteEnvironmentBlueprintConfiguration-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the blueprint configuration is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentBlueprintIdentifier](#API_DeleteEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-DeleteEnvironmentBlueprintConfiguration-request-uri-environmentBlueprintIdentifier"></a>
The ID of the blueprint the configuration of which is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteEnvironmentBlueprintConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEnvironmentBlueprintConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteEnvironmentBlueprintConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteEnvironmentBlueprintConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteEnvironmentBlueprintConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteEnvironmentBlueprintConfiguration)
