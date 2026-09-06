---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfiguration.html
---

# UpdateLaunchConfiguration
<a name="API_UpdateLaunchConfiguration"></a>

Updates a LaunchConfiguration by Source Server ID.

## Request Syntax
<a name="API_UpdateLaunchConfiguration_RequestSyntax"></a>

```
POST /UpdateLaunchConfiguration HTTP/1.1
Content-type: application/json

{
   "copyPrivateIp": {{boolean}},
   "copyTags": {{boolean}},
   "launchDisposition": "{{string}}",
   "launchIntoInstanceProperties": {
      "launchIntoEC2InstanceID": "{{string}}"
   },
   "licensing": {
      "osByol": {{boolean}}
   },
   "name": "{{string}}",
   "postLaunchEnabled": {{boolean}},
   "recoveryMode": "{{string}}",
   "sourceServerID": "{{string}}",
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLaunchConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLaunchConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [copyPrivateIp](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-copyPrivateIp"></a>
Whether we should copy the Private IP of the Source Server to the Recovery Instance.
Type: Boolean
Required: No

 ** [copyTags](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-copyTags"></a>
Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.
Type: Boolean
Required: No

 ** [launchDisposition](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-launchDisposition"></a>
The state of the Recovery Instance in EC2 after the recovery operation.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [launchIntoInstanceProperties](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-launchIntoInstanceProperties"></a>
Launch into existing instance properties.
Type: [LaunchIntoInstanceProperties](API_LaunchIntoInstanceProperties.md) object
Required: No

 ** [licensing](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-licensing"></a>
The licensing configuration to be used for this launch configuration.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [name](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-name"></a>
The name of the launch configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [postLaunchEnabled](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-postLaunchEnabled"></a>
Whether we want to enable post-launch actions for the Source Server.
Type: Boolean
Required: No

 ** [recoveryMode](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`
Required: No

 ** [sourceServerID](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-sourceServerID"></a>
The ID of the Source Server that we want to retrieve a Launch Configuration for.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="drs-UpdateLaunchConfiguration-request-targetInstanceTypeRightSizingMethod"></a>
Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`
Required: No

## Response Syntax
<a name="API_UpdateLaunchConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "copyPrivateIp": boolean,
   "copyTags": boolean,
   "ec2LaunchTemplateID": "string",
   "launchDisposition": "string",
   "launchIntoInstanceProperties": {
      "launchIntoEC2InstanceID": "string"
   },
   "licensing": {
      "osByol": boolean
   },
   "name": "string",
   "postLaunchEnabled": boolean,
   "recoveryMode": "string",
   "sourceServerID": "string",
   "targetInstanceTypeRightSizingMethod": "string"
}
```

## Response Elements
<a name="API_UpdateLaunchConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [copyPrivateIp](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-copyPrivateIp"></a>
Whether we should copy the Private IP of the Source Server to the Recovery Instance.
Type: Boolean

 ** [copyTags](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-copyTags"></a>
Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-ec2LaunchTemplateID"></a>
The EC2 launch template ID of this launch configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [launchDisposition](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-launchDisposition"></a>
The state of the Recovery Instance in EC2 after the recovery operation.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [launchIntoInstanceProperties](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-launchIntoInstanceProperties"></a>
Launch into existing instance properties.
Type: [LaunchIntoInstanceProperties](API_LaunchIntoInstanceProperties.md) object

 ** [licensing](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-licensing"></a>
The licensing configuration to be used for this launch configuration.
Type: [Licensing](API_Licensing.md) object

 ** [name](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-name"></a>
The name of the launch configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [postLaunchEnabled](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-postLaunchEnabled"></a>
Whether we want to activate post-launch actions for the Source Server.
Type: Boolean

 ** [recoveryMode](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`

 ** [sourceServerID](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-sourceServerID"></a>
The ID of the Source Server for this launch configuration.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="drs-UpdateLaunchConfiguration-response-targetInstanceTypeRightSizingMethod"></a>
Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`

## Errors
<a name="API_UpdateLaunchConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

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
<a name="API_UpdateLaunchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateLaunchConfiguration)
