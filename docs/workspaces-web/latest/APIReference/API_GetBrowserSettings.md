---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_GetBrowserSettings.html
---

# GetBrowserSettings
<a name="API_GetBrowserSettings"></a>

Gets browser settings.

## Request Syntax
<a name="API_GetBrowserSettings_RequestSyntax"></a>

```
GET /browserSettings/{{browserSettingsArn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBrowserSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserSettingsArn](#API_GetBrowserSettings_RequestSyntax) **   <a name="workspacesweb-GetBrowserSettings-request-uri-browserSettingsArn"></a>
The ARN of the browser settings.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

## Request Body
<a name="API_GetBrowserSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBrowserSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserSettings": {
      "additionalEncryptionContext": {
         "string" : "string"
      },
      "associatedPortalArns": [ "string" ],
      "browserPolicy": "string",
      "browserSettingsArn": "string",
      "customerManagedKey": "string",
      "webContentFilteringPolicy": {
         "allowedUrls": [ "string" ],
         "blockedCategories": [ "string" ],
         "blockedUrls": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_GetBrowserSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserSettings](#API_GetBrowserSettings_ResponseSyntax) **   <a name="workspacesweb-GetBrowserSettings-response-browserSettings"></a>
The browser settings.
Type: [BrowserSettings](API_BrowserSettings.md) object

## Errors
<a name="API_GetBrowserSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
There is an internal server error.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource cannot be found.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

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
<a name="API_GetBrowserSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/GetBrowserSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/GetBrowserSettings)
