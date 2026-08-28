---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetEnvironmentTemplateVersion
<a name="API_GetEnvironmentTemplateVersion"></a>

Get detailed data for a major or minor version of an environment template.

## Request Syntax
<a name="API_GetEnvironmentTemplateVersion_RequestSyntax"></a>

```
{
   "majorVersion": "{{string}}",
   "minorVersion": "{{string}}",
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEnvironmentTemplateVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [majorVersion](#API_GetEnvironmentTemplateVersion_RequestSyntax) **   <a name="proton-GetEnvironmentTemplateVersion-request-majorVersion"></a>
To get environment template major version detail data, include `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [minorVersion](#API_GetEnvironmentTemplateVersion_RequestSyntax) **   <a name="proton-GetEnvironmentTemplateVersion-request-minorVersion"></a>
To get environment template minor version detail data, include `minorVersion`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [templateName](#API_GetEnvironmentTemplateVersion_RequestSyntax) **   <a name="proton-GetEnvironmentTemplateVersion-request-templateName"></a>
The name of the environment template a version of which you want to get detailed data for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_GetEnvironmentTemplateVersion_ResponseSyntax"></a>

```
{
   "environmentTemplateVersion": {
      "arn": "string",
      "createdAt": number,
      "description": "string",
      "lastModifiedAt": number,
      "majorVersion": "string",
      "minorVersion": "string",
      "recommendedMinorVersion": "string",
      "schema": "string",
      "status": "string",
      "statusMessage": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_GetEnvironmentTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentTemplateVersion](#API_GetEnvironmentTemplateVersion_ResponseSyntax) **   <a name="proton-GetEnvironmentTemplateVersion-response-environmentTemplateVersion"></a>
The detailed data of the requested environment template version.
Type: [EnvironmentTemplateVersion](API_EnvironmentTemplateVersion.md) object

## Errors
<a name="API_GetEnvironmentTemplateVersion_Errors"></a>

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
<a name="API_GetEnvironmentTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetEnvironmentTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetEnvironmentTemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
