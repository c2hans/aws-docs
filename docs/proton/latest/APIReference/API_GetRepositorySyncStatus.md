---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetRepositorySyncStatus.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetRepositorySyncStatus
<a name="API_GetRepositorySyncStatus"></a>

Get the sync status of a repository used for AWS Proton template sync. For more information about template sync, see .

**Note**
A repository sync status isn't tied to the AWS Proton Repository resource (or any other AWS Proton resource). Therefore, tags on an AWS Proton Repository resource have no effect on this action. Specifically, you can't use these tags to control access to this action using Attribute-based access control (ABAC).
For more information about ABAC, see [ABAC](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_GetRepositorySyncStatus_RequestSyntax"></a>

```
{
   "branch": "{{string}}",
   "repositoryName": "{{string}}",
   "repositoryProvider": "{{string}}",
   "syncType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRepositorySyncStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branch](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="proton-GetRepositorySyncStatus-request-branch"></a>
The repository branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [repositoryName](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="proton-GetRepositorySyncStatus-request-repositoryName"></a>
The repository name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** [repositoryProvider](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="proton-GetRepositorySyncStatus-request-repositoryProvider"></a>
The repository provider.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** [syncType](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="proton-GetRepositorySyncStatus-request-syncType"></a>
The repository sync type.
Type: String
Valid Values: `TEMPLATE_SYNC | SERVICE_SYNC`
Required: Yes

## Response Syntax
<a name="API_GetRepositorySyncStatus_ResponseSyntax"></a>

```
{
   "latestSync": {
      "events": [
         {
            "event": "string",
            "externalId": "string",
            "time": number,
            "type": "string"
         }
      ],
      "startedAt": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetRepositorySyncStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [latestSync](#API_GetRepositorySyncStatus_ResponseSyntax) **   <a name="proton-GetRepositorySyncStatus-response-latestSync"></a>
The repository sync status detail data that's returned by AWS Proton.
Type: [RepositorySyncAttempt](API_RepositorySyncAttempt.md) object

## Errors
<a name="API_GetRepositorySyncStatus_Errors"></a>

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
<a name="API_GetRepositorySyncStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetRepositorySyncStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetRepositorySyncStatus)
