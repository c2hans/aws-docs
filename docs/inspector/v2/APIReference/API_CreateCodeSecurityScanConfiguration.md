---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityScanConfiguration.html
---

# CreateCodeSecurityScanConfiguration
<a name="API_CreateCodeSecurityScanConfiguration"></a>

Creates a scan configuration for code security scanning.

## Request Syntax
<a name="API_CreateCodeSecurityScanConfiguration_RequestSyntax"></a>

```
POST /codesecurity/scan-configuration/create HTTP/1.1
Content-type: application/json

{
   "configuration": {
      "continuousIntegrationScanConfiguration": {
         "supportedEvents": [ "{{string}}" ]
      },
      "periodicScanConfiguration": {
         "frequency": "{{string}}",
         "frequencyExpression": "{{string}}"
      },
      "ruleSetCategories": [ "{{string}}" ]
   },
   "level": "{{string}}",
   "name": "{{string}}",
   "scopeSettings": {
      "projectSelectionScope": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCodeSecurityScanConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCodeSecurityScanConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_CreateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-request-configuration"></a>
The configuration settings for the code security scan.
Type: [CodeSecurityScanConfiguration](API_CodeSecurityScanConfiguration.md) object
Required: Yes

 ** [level](#API_CreateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-request-level"></a>
The security level for the scan configuration.
Type: String
Valid Values: `ORGANIZATION | ACCOUNT`
Required: Yes

 ** [name](#API_CreateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-request-name"></a>
The name of the scan configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[a-zA-Z0-9-_$:.]*`
Required: Yes

 ** [scopeSettings](#API_CreateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-request-scopeSettings"></a>
The scope settings that define which repositories will be scanned. Include this parameter to create a default scan configuration. Otherwise Amazon Inspector creates a general scan configuration.
A default scan configuration automatically applies to all existing and future projects imported into Amazon Inspector. Use the `BatchAssociateCodeSecurityScanConfiguration` operation to associate a general scan configuration with projects.
Type: [ScopeSettings](API_ScopeSettings.md) object
Required: No

 ** [tags](#API_CreateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-request-tags"></a>
The tags to apply to the scan configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCodeSecurityScanConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scanConfigurationArn": "string"
}
```

## Response Elements
<a name="API_CreateCodeSecurityScanConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scanConfigurationArn](#API_CreateCodeSecurityScanConfiguration_ResponseSyntax) **   <a name="inspector2-CreateCodeSecurityScanConfiguration-response-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the created scan configuration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`

## Errors
<a name="API_CreateCodeSecurityScanConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
 ** resourceId **
The ID of the resource that exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateCodeSecurityScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateCodeSecurityScanConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
