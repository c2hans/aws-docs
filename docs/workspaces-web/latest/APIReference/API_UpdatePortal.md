---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_UpdatePortal.html
---

# UpdatePortal
<a name="API_UpdatePortal"></a>

Updates a web portal.

## Request Syntax
<a name="API_UpdatePortal_RequestSyntax"></a>

```
PUT /portals/{{portalArn+}} HTTP/1.1
Content-type: application/json

{
   "authenticationType": "{{string}}",
   "displayName": "{{string}}",
   "instanceType": "{{string}}",
   "maxConcurrentSessions": {{number}},
   "portalCustomDomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePortal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [portalArn](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-uri-portalArn"></a>
The ARN of the web portal.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

## Request Body
<a name="API_UpdatePortal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authenticationType](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-authenticationType"></a>
The type of authentication integration points used when signing into the web portal. Defaults to `Standard`.
 `Standard` web portals are authenticated directly through your identity provider. You need to call `CreateIdentityProvider` to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.
 `IAM Identity Center` web portals are authenticated through AWS IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.
Type: String
Valid Values: `Standard | IAM_Identity_Center`
Required: No

 ** [displayName](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-displayName"></a>
The name of the web portal. This is not visible to users who log into the web portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`
Required: No

 ** [instanceType](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-instanceType"></a>
The type and resources of the underlying instance.
Type: String
Valid Values: `standard.regular | standard.large | standard.xlarge`
Required: No

 ** [maxConcurrentSessions](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-maxConcurrentSessions"></a>
The maximum number of concurrent sessions for the portal.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [portalCustomDomain](#API_UpdatePortal_RequestSyntax) **   <a name="workspacesweb-UpdatePortal-request-portalCustomDomain"></a>
The custom domain of the web portal that users access in order to start streaming sessions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(|[a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+)`
Required: No

## Response Syntax
<a name="API_UpdatePortal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "portal": {
      "additionalEncryptionContext": {
         "string" : "string"
      },
      "authenticationType": "string",
      "browserSettingsArn": "string",
      "browserType": "string",
      "creationDate": number,
      "customerManagedKey": "string",
      "dataProtectionSettingsArn": "string",
      "displayName": "string",
      "instanceType": "string",
      "ipAccessSettingsArn": "string",
      "maxConcurrentSessions": number,
      "networkSettingsArn": "string",
      "portalArn": "string",
      "portalCustomDomain": "string",
      "portalEndpoint": "string",
      "portalStatus": "string",
      "rendererType": "string",
      "sessionLoggerArn": "string",
      "statusReason": "string",
      "trustStoreArn": "string",
      "userAccessLoggingSettingsArn": "string",
      "userSettingsArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePortal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [portal](#API_UpdatePortal_ResponseSyntax) **   <a name="workspacesweb-UpdatePortal-response-portal"></a>
The web portal.
Type: [Portal](API_Portal.md) object

## Errors
<a name="API_UpdatePortal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict.
 ** resourceId **
Identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** quotaCode **
The originating quota.
 ** resourceId **
Identifier of the resource affected.
 ** resourceType **
 Type of the resource affected.
 ** serviceCode **
The originating service.
HTTP Status Code: 402

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
<a name="API_UpdatePortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/UpdatePortal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/UpdatePortal)
