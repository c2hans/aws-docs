---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StartThingRegistrationTask.html
---

# StartThingRegistrationTask
<a name="API_StartThingRegistrationTask"></a>

Creates a bulk thing provisioning task.

Requires permission to access the [StartThingRegistrationTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_StartThingRegistrationTask_RequestSyntax"></a>

```
POST /thing-registration-tasks HTTP/1.1
Content-type: application/json

{
   "inputFileBucket": "{{string}}",
   "inputFileKey": "{{string}}",
   "roleArn": "{{string}}",
   "templateBody": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartThingRegistrationTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartThingRegistrationTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [inputFileBucket](#API_StartThingRegistrationTask_RequestSyntax) **   <a name="iot-StartThingRegistrationTask-request-inputFileBucket"></a>
The S3 bucket that contains the input file.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

 ** [inputFileKey](#API_StartThingRegistrationTask_RequestSyntax) **   <a name="iot-StartThingRegistrationTask-request-inputFileKey"></a>
The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9!_.*'()-\/]+`
Required: Yes

 ** [roleArn](#API_StartThingRegistrationTask_RequestSyntax) **   <a name="iot-StartThingRegistrationTask-request-roleArn"></a>
The IAM role ARN that grants permission the input file.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [templateBody](#API_StartThingRegistrationTask_RequestSyntax) **   <a name="iot-StartThingRegistrationTask-request-templateBody"></a>
The provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_StartThingRegistrationTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskId": "string"
}
```

## Response Elements
<a name="API_StartThingRegistrationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_StartThingRegistrationTask_ResponseSyntax) **   <a name="iot-StartThingRegistrationTask-response-taskId"></a>
The bulk thing provisioning task ID.
Type: String
Length Constraints: Maximum length of 40.

## Errors
<a name="API_StartThingRegistrationTask_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_StartThingRegistrationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/StartThingRegistrationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StartThingRegistrationTask)
