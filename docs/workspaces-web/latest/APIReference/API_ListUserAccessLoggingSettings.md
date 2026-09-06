---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ListUserAccessLoggingSettings.html
---

# ListUserAccessLoggingSettings
<a name="API_ListUserAccessLoggingSettings"></a>

Retrieves a list of user access logging settings.

## Request Syntax
<a name="API_ListUserAccessLoggingSettings_RequestSyntax"></a>

```
GET /userAccessLoggingSettings?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListUserAccessLoggingSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListUserAccessLoggingSettings_RequestSyntax) **   <a name="workspacesweb-ListUserAccessLoggingSettings-request-uri-maxResults"></a>
The maximum number of results to be included in the next page.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_ListUserAccessLoggingSettings_RequestSyntax) **   <a name="workspacesweb-ListUserAccessLoggingSettings-request-uri-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

## Request Body
<a name="API_ListUserAccessLoggingSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListUserAccessLoggingSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "userAccessLoggingSettings": [
      {
         "kinesisStreamArn": "string",
         "userAccessLoggingSettingsArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUserAccessLoggingSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUserAccessLoggingSettings_ResponseSyntax) **   <a name="workspacesweb-ListUserAccessLoggingSettings-response-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [userAccessLoggingSettings](#API_ListUserAccessLoggingSettings_ResponseSyntax) **   <a name="workspacesweb-ListUserAccessLoggingSettings-response-userAccessLoggingSettings"></a>
The user access logging settings.
Type: Array of [UserAccessLoggingSettingsSummary](API_UserAccessLoggingSettingsSummary.md) objects

## Errors
<a name="API_ListUserAccessLoggingSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
There is an internal server error.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ThrottlingException **
There is a throttling error.
 ** quotaCode **
The originating quota.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
 ** serviceCode **
The originating service.
HTTP Status Code: 429

 ** ValidationException **
There is a validation error.
 ** fieldList **
The field that caused the error.
 ** reason **
Reason the request failed validation
HTTP Status Code: 400

## See Also
<a name="API_ListUserAccessLoggingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ListUserAccessLoggingSettings)
