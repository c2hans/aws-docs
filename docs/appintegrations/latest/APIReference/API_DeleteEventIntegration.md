---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteEventIntegration.html
---

# DeleteEventIntegration
<a name="API_connect-app-integrations_DeleteEventIntegration"></a>

Deletes the specified existing event integration. If the event integration is associated with clients, the request is rejected.

## Request Syntax
<a name="API_connect-app-integrations_DeleteEventIntegration_RequestSyntax"></a>

```
DELETE /eventIntegrations/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_DeleteEventIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_connect-app-integrations_DeleteEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_DeleteEventIntegration-request-uri-Name"></a>
The name of the event integration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_DeleteEventIntegration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_DeleteEventIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_DeleteEventIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_DeleteEventIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_DeleteEventIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/DeleteEventIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/DeleteEventIntegration)
