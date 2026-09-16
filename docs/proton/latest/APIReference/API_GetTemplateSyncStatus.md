---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetTemplateSyncStatus.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetTemplateSyncStatus
<a name="API_GetTemplateSyncStatus"></a>

Get the status of a template sync.

## Request Syntax
<a name="API_GetTemplateSyncStatus_RequestSyntax"></a>

```
{
   "templateName": "{{string}}",
   "templateType": "{{string}}",
   "templateVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTemplateSyncStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [templateName](#API_GetTemplateSyncStatus_RequestSyntax) **   <a name="proton-GetTemplateSyncStatus-request-templateName"></a>
The template name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [templateType](#API_GetTemplateSyncStatus_RequestSyntax) **   <a name="proton-GetTemplateSyncStatus-request-templateType"></a>
The template type.
Type: String
Valid Values: `ENVIRONMENT | SERVICE`
Required: Yes

 ** [templateVersion](#API_GetTemplateSyncStatus_RequestSyntax) **   <a name="proton-GetTemplateSyncStatus-request-templateVersion"></a>
The template major version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

## Response Syntax
<a name="API_GetTemplateSyncStatus_ResponseSyntax"></a>

```
{
   "desiredState": {
      "branch": "string",
      "directory": "string",
      "repositoryName": "string",
      "repositoryProvider": "string",
      "sha": "string"
   },
   "latestSuccessfulSync": {
      "events": [
         {
            "event": "string",
            "externalId": "string",
            "time": number,
            "type": "string"
         }
      ],
      "initialRevision": {
         "branch": "string",
         "directory": "string",
         "repositoryName": "string",
         "repositoryProvider": "string",
         "sha": "string"
      },
      "startedAt": number,
      "status": "string",
      "target": "string",
      "targetRevision": {
         "branch": "string",
         "directory": "string",
         "repositoryName": "string",
         "repositoryProvider": "string",
         "sha": "string"
      }
   },
   "latestSync": {
      "events": [
         {
            "event": "string",
            "externalId": "string",
            "time": number,
            "type": "string"
         }
      ],
      "initialRevision": {
         "branch": "string",
         "directory": "string",
         "repositoryName": "string",
         "repositoryProvider": "string",
         "sha": "string"
      },
      "startedAt": number,
      "status": "string",
      "target": "string",
      "targetRevision": {
         "branch": "string",
         "directory": "string",
         "repositoryName": "string",
         "repositoryProvider": "string",
         "sha": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetTemplateSyncStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [desiredState](#API_GetTemplateSyncStatus_ResponseSyntax) **   <a name="proton-GetTemplateSyncStatus-response-desiredState"></a>
The template sync desired state that's returned by AWS Proton.
Type: [Revision](API_Revision.md) object

 ** [latestSuccessfulSync](#API_GetTemplateSyncStatus_ResponseSyntax) **   <a name="proton-GetTemplateSyncStatus-response-latestSuccessfulSync"></a>
The details of the last successful sync that's returned by AWS Proton.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

 ** [latestSync](#API_GetTemplateSyncStatus_ResponseSyntax) **   <a name="proton-GetTemplateSyncStatus-response-latestSync"></a>
The details of the last sync that's returned by AWS Proton.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

## Errors
<a name="API_GetTemplateSyncStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_GetTemplateSyncStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetTemplateSyncStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetTemplateSyncStatus)
