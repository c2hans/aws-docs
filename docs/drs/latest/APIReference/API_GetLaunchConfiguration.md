---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_GetLaunchConfiguration.html
---

# GetLaunchConfiguration
<a name="API_GetLaunchConfiguration"></a>

Gets a LaunchConfiguration, filtered by Source Server IDs.

## Request Syntax
<a name="API_GetLaunchConfiguration_RequestSyntax"></a>

```
POST /GetLaunchConfiguration HTTP/1.1
Content-type: application/json

{
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetLaunchConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLaunchConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceServerID](#API_GetLaunchConfiguration_RequestSyntax) **   <a name="drs-GetLaunchConfiguration-request-sourceServerID"></a>
The ID of the Source Server that we want to retrieve a Launch Configuration for.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_GetLaunchConfiguration_ResponseSyntax"></a>

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
<a name="API_GetLaunchConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [copyPrivateIp](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-copyPrivateIp"></a>
Whether we should copy the Private IP of the Source Server to the Recovery Instance.
Type: Boolean

 ** [copyTags](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-copyTags"></a>
Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-ec2LaunchTemplateID"></a>
The EC2 launch template ID of this launch configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [launchDisposition](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-launchDisposition"></a>
The state of the Recovery Instance in EC2 after the recovery operation.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [launchIntoInstanceProperties](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-launchIntoInstanceProperties"></a>
Launch into existing instance properties.
Type: [LaunchIntoInstanceProperties](API_LaunchIntoInstanceProperties.md) object

 ** [licensing](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-licensing"></a>
The licensing configuration to be used for this launch configuration.
Type: [Licensing](API_Licensing.md) object

 ** [name](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-name"></a>
The name of the launch configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [postLaunchEnabled](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-postLaunchEnabled"></a>
Whether we want to activate post-launch actions for the Source Server.
Type: Boolean

 ** [recoveryMode](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`

 ** [sourceServerID](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-sourceServerID"></a>
The ID of the Source Server for this launch configuration.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [targetInstanceTypeRightSizingMethod](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="drs-GetLaunchConfiguration-response-targetInstanceTypeRightSizingMethod"></a>
Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`

## Errors
<a name="API_GetLaunchConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_GetLaunchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/GetLaunchConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
