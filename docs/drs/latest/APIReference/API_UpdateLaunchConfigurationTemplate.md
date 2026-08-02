---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfigurationTemplate.html
---

# UpdateLaunchConfigurationTemplate
<a name="API_UpdateLaunchConfigurationTemplate"></a>

Updates an existing Launch Configuration Template by ID.

## Request Syntax
<a name="API_UpdateLaunchConfigurationTemplate_RequestSyntax"></a>

```
POST /UpdateLaunchConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "copyPrivateIp": {{boolean}},
   "copyTags": {{boolean}},
   "exportBucketArn": "{{string}}",
   "launchConfigurationTemplateID": "{{string}}",
   "launchDisposition": "{{string}}",
   "launchIntoSourceInstance": {{boolean}},
   "licensing": {
      "osByol": {{boolean}}
   },
   "postLaunchEnabled": {{boolean}},
   "recoveryMode": "{{string}}",
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLaunchConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLaunchConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [copyPrivateIp](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-copyPrivateIp"></a>
Copy private IP.
Type: Boolean
Required: No

 ** [copyTags](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** [exportBucketArn](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-exportBucketArn"></a>
S3 bucket ARN to export Source Network templates.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** [launchConfigurationTemplateID](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-launchConfigurationTemplateID"></a>
Launch Configuration Template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [launchDisposition](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [launchIntoSourceInstance](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-launchIntoSourceInstance"></a>
DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.
Type: Boolean
Required: No

 ** [licensing](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-licensing"></a>
Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [postLaunchEnabled](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-postLaunchEnabled"></a>
Whether we want to activate post-launch actions.
Type: Boolean
Required: No

 ** [recoveryMode](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`
Required: No

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-request-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`
Required: No

## Response Syntax
<a name="API_UpdateLaunchConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateLaunchConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [launchConfigurationTemplate](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateLaunchConfigurationTemplate-response-launchConfigurationTemplate"></a>
Updated Launch Configuration Template.
Type: [LaunchConfigurationTemplate](API_LaunchConfigurationTemplate.md) object

## Errors
<a name="API_UpdateLaunchConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

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
<a name="API_UpdateLaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateLaunchConfigurationTemplate)
