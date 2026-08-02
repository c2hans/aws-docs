---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateTemplateSyncConfig.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateTemplateSyncConfig
<a name="API_CreateTemplateSyncConfig"></a>

Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](API_CreateRepository.md).

When a commit is pushed to your linked repository, AWS Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see [Template sync configurations](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateTemplateSyncConfig_RequestSyntax"></a>

```
{
   "branch": "{{string}}",
   "repositoryName": "{{string}}",
   "repositoryProvider": "{{string}}",
   "subdirectory": "{{string}}",
   "templateName": "{{string}}",
   "templateType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTemplateSyncConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branch](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-branch"></a>
The repository branch for your template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [repositoryName](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-repositoryName"></a>
The repository name (for example, `myrepos/myrepo`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** [repositoryProvider](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-repositoryProvider"></a>
The provider type for your repository.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** [subdirectory](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-subdirectory"></a>
A repository subdirectory path to your template bundle directory. When included, AWS Proton limits the template bundle search to this repository directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [templateName](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-templateName"></a>
The name of your registered template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [templateType](#API_CreateTemplateSyncConfig_RequestSyntax) **   <a name="proton-CreateTemplateSyncConfig-request-templateType"></a>
The type of the registered template.
Type: String
Valid Values: `ENVIRONMENT | SERVICE`
Required: Yes

## Response Syntax
<a name="API_CreateTemplateSyncConfig_ResponseSyntax"></a>

```
{
   "templateSyncConfig": {
      "branch": "string",
      "repositoryName": "string",
      "repositoryProvider": "string",
      "subdirectory": "string",
      "templateName": "string",
      "templateType": "string"
   }
}
```

## Response Elements
<a name="API_CreateTemplateSyncConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [templateSyncConfig](#API_CreateTemplateSyncConfig_ResponseSyntax) **   <a name="proton-CreateTemplateSyncConfig-response-templateSyncConfig"></a>
The template sync configuration detail data that's returned by AWS Proton.
Type: [TemplateSyncConfig](API_TemplateSyncConfig.md) object

## Errors
<a name="API_CreateTemplateSyncConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateTemplateSyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateTemplateSyncConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateTemplateSyncConfig)
