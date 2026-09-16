---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegration.html
---

# UpdateDataIntegration
<a name="API_connect-app-integrations_UpdateDataIntegration"></a>

Updates the description of a DataIntegration.

**Note**
You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html) API.

## Request Syntax
<a name="API_connect-app-integrations_UpdateDataIntegration_RequestSyntax"></a>

```
PATCH /dataIntegrations/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_UpdateDataIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_connect-app-integrations_UpdateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegration-request-uri-Identifier"></a>
A unique identifier for the DataIntegration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_UpdateDataIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-app-integrations_UpdateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegration-request-Description"></a>
A description of the DataIntegration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** [Name](#API_connect-app-integrations_UpdateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegration-request-Name"></a>
The name of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## Response Syntax
<a name="API_connect-app-integrations_UpdateDataIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_UpdateDataIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_UpdateDataIntegration_Errors"></a>

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
<a name="API_connect-app-integrations_UpdateDataIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/UpdateDataIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/UpdateDataIntegration)
