---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingRegistrationTask.html
---

# DescribeThingRegistrationTask
<a name="API_DescribeThingRegistrationTask"></a>

Describes a bulk thing provisioning task.

Requires permission to access the [DescribeThingRegistrationTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeThingRegistrationTask_RequestSyntax"></a>

```
GET /thing-registration-tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeThingRegistrationTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_DescribeThingRegistrationTask_RequestSyntax) **   <a name="iot-DescribeThingRegistrationTask-request-uri-taskId"></a>
The task ID.
Length Constraints: Maximum length of 40.
Required: Yes

## Request Body
<a name="API_DescribeThingRegistrationTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeThingRegistrationTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "failureCount": number,
   "inputFileBucket": "string",
   "inputFileKey": "string",
   "lastModifiedDate": number,
   "message": "string",
   "percentageProgress": number,
   "roleArn": "string",
   "status": "string",
   "successCount": number,
   "taskId": "string",
   "templateBody": "string"
}
```

## Response Elements
<a name="API_DescribeThingRegistrationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-creationDate"></a>
The task creation date.
Type: Timestamp

 ** [failureCount](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-failureCount"></a>
The number of things that failed to be provisioned.
Type: Integer

 ** [inputFileBucket](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-inputFileBucket"></a>
The S3 bucket that contains the input file.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9._-]+`

 ** [inputFileKey](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-inputFileKey"></a>
The input file key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9!_.*'()-\/]+`

 ** [lastModifiedDate](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-lastModifiedDate"></a>
The date when the task was last modified.
Type: Timestamp

 ** [message](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-message"></a>
The message.
Type: String
Length Constraints: Maximum length of 2048.

 ** [percentageProgress](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-percentageProgress"></a>
The progress of the bulk provisioning task expressed as a percentage.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [roleArn](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-roleArn"></a>
The role ARN that grants access to the input file bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [status](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-status"></a>
The status of the bulk thing provisioning task.
Type: String
Valid Values: `InProgress | Completed | Failed | Cancelled | Cancelling`

 ** [successCount](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-successCount"></a>
The number of things successfully provisioned.
Type: Integer

 ** [taskId](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-taskId"></a>
The task ID.
Type: String
Length Constraints: Maximum length of 40.

 ** [templateBody](#API_DescribeThingRegistrationTask_ResponseSyntax) **   <a name="iot-DescribeThingRegistrationTask-response-templateBody"></a>
The task's template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`

## Errors
<a name="API_DescribeThingRegistrationTask_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

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
<a name="API_DescribeThingRegistrationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeThingRegistrationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeThingRegistrationTask)
