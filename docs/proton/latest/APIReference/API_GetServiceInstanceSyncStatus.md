---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceInstanceSyncStatus.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetServiceInstanceSyncStatus
<a name="API_GetServiceInstanceSyncStatus"></a>

Get the status of the synced service instance.

## Request Syntax
<a name="API_GetServiceInstanceSyncStatus_RequestSyntax"></a>

```
{
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetServiceInstanceSyncStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceInstanceName](#API_GetServiceInstanceSyncStatus_RequestSyntax) **   <a name="proton-GetServiceInstanceSyncStatus-request-serviceInstanceName"></a>
The name of the service instance that you want the sync status input for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceName](#API_GetServiceInstanceSyncStatus_RequestSyntax) **   <a name="proton-GetServiceInstanceSyncStatus-request-serviceName"></a>
The name of the service that the service instance belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_GetServiceInstanceSyncStatus_ResponseSyntax"></a>

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
<a name="API_GetServiceInstanceSyncStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [desiredState](#API_GetServiceInstanceSyncStatus_ResponseSyntax) **   <a name="proton-GetServiceInstanceSyncStatus-response-desiredState"></a>
The service instance sync desired state that's returned by AWS Proton
Type: [Revision](API_Revision.md) object

 ** [latestSuccessfulSync](#API_GetServiceInstanceSyncStatus_ResponseSyntax) **   <a name="proton-GetServiceInstanceSyncStatus-response-latestSuccessfulSync"></a>
The detailed data of the latest successful sync with the service instance.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

 ** [latestSync](#API_GetServiceInstanceSyncStatus_ResponseSyntax) **   <a name="proton-GetServiceInstanceSyncStatus-response-latestSync"></a>
The detailed data of the latest sync with the service instance.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

## Errors
<a name="API_GetServiceInstanceSyncStatus_Errors"></a>

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
<a name="API_GetServiceInstanceSyncStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetServiceInstanceSyncStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetServiceInstanceSyncStatus)
