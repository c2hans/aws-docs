---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_UpdateSessionLogger.html
---

# UpdateSessionLogger
<a name="API_UpdateSessionLogger"></a>

Updates the details of a session logger.

## Request Syntax
<a name="API_UpdateSessionLogger_RequestSyntax"></a>

```
POST /sessionLoggers/{{sessionLoggerArn+}} HTTP/1.1
Content-type: application/json

{
   "displayName": "{{string}}",
   "eventFilter": { ... },
   "logConfiguration": {
      "s3": {
         "bucket": "{{string}}",
         "bucketOwner": "{{string}}",
         "folderStructure": "{{string}}",
         "keyPrefix": "{{string}}",
         "logFileFormat": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateSessionLogger_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionLoggerArn](#API_UpdateSessionLogger_RequestSyntax) **   <a name="workspacesweb-UpdateSessionLogger-request-uri-sessionLoggerArn"></a>
The ARN of the session logger to update.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

## Request Body
<a name="API_UpdateSessionLogger_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [displayName](#API_UpdateSessionLogger_RequestSyntax) **   <a name="workspacesweb-UpdateSessionLogger-request-displayName"></a>
The updated display name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[ _\-\d\w]+`
Required: No

 ** [eventFilter](#API_UpdateSessionLogger_RequestSyntax) **   <a name="workspacesweb-UpdateSessionLogger-request-eventFilter"></a>
The updated eventFilter.
Type: [EventFilter](API_EventFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [logConfiguration](#API_UpdateSessionLogger_RequestSyntax) **   <a name="workspacesweb-UpdateSessionLogger-request-logConfiguration"></a>
The updated logConfiguration.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateSessionLogger_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sessionLogger": {
      "additionalEncryptionContext": {
         "string" : "string"
      },
      "associatedPortalArns": [ "string" ],
      "creationDate": number,
      "customerManagedKey": "string",
      "displayName": "string",
      "eventFilter": { ... },
      "logConfiguration": {
         "s3": {
            "bucket": "string",
            "bucketOwner": "string",
            "folderStructure": "string",
            "keyPrefix": "string",
            "logFileFormat": "string"
         }
      },
      "sessionLoggerArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSessionLogger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sessionLogger](#API_UpdateSessionLogger_ResponseSyntax) **   <a name="workspacesweb-UpdateSessionLogger-response-sessionLogger"></a>
The updated details of the session logger.
Type: [SessionLogger](API_SessionLogger.md) object

## Errors
<a name="API_UpdateSessionLogger_Errors"></a>

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
<a name="API_UpdateSessionLogger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/UpdateSessionLogger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/UpdateSessionLogger)
