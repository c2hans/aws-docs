---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateLaunchConfigurationTemplate.html
---

# CreateLaunchConfigurationTemplate
<a name="API_CreateLaunchConfigurationTemplate"></a>

Creates a new Launch Configuration Template.

## Request Syntax
<a name="API_CreateLaunchConfigurationTemplate_RequestSyntax"></a>

```
POST /CreateLaunchConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "copyPrivateIp": {{boolean}},
   "copyTags": {{boolean}},
   "exportBucketArn": "{{string}}",
   "launchDisposition": "{{string}}",
   "launchIntoSourceInstance": {{boolean}},
   "licensing": {
      "osByol": {{boolean}}
   },
   "postLaunchEnabled": {{boolean}},
   "recoveryMode": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateLaunchConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLaunchConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [copyPrivateIp](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-copyPrivateIp"></a>
Copy private IP.
Type: Boolean
Required: No

 ** [copyTags](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** [exportBucketArn](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-exportBucketArn"></a>
S3 bucket ARN to export Source Network templates.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** [launchDisposition](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [launchIntoSourceInstance](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-launchIntoSourceInstance"></a>
DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.
Type: Boolean
Required: No

 ** [licensing](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-licensing"></a>
Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [postLaunchEnabled](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-postLaunchEnabled"></a>
Whether we want to activate post-launch actions.
Type: Boolean
Required: No

 ** [recoveryMode](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`
Required: No

 ** [tags](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-tags"></a>
Request to associate tags during creation of a Launch Configuration Template.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [targetInstanceTypeRightSizingMethod](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-request-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`
Required: No

## Response Syntax
<a name="API_CreateLaunchConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "launchConfigurationTemplate": {
      "arn": "string",
      "copyPrivateIp": boolean,
      "copyTags": boolean,
      "exportBucketArn": "string",
      "launchConfigurationTemplateID": "string",
      "launchDisposition": "string",
      "launchIntoSourceInstance": boolean,
      "licensing": {
         "osByol": boolean
      },
      "postLaunchEnabled": boolean,
      "recoveryMode": "string",
      "tags": {
         "string" : "string"
      },
      "targetInstanceTypeRightSizingMethod": "string"
   }
}
```

## Response Elements
<a name="API_CreateLaunchConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [launchConfigurationTemplate](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="drs-CreateLaunchConfigurationTemplate-response-launchConfigurationTemplate"></a>
Created Launch Configuration Template.
Type: [LaunchConfigurationTemplate](API_LaunchConfigurationTemplate.md) object

## Errors
<a name="API_CreateLaunchConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateLaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/CreateLaunchConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
