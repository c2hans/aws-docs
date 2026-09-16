---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDeviceJob.html
---

# DescribeDeviceJob
<a name="API_DescribeDeviceJob"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a device job.

## Request Syntax
<a name="API_DescribeDeviceJob_RequestSyntax"></a>

```
GET /jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDeviceJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_DescribeDeviceJob_RequestSyntax) **   <a name="panorama-DescribeDeviceJob-request-uri-JobId"></a>
The job's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_DescribeDeviceJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDeviceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTime": number,
   "DeviceArn": "string",
   "DeviceId": "string",
   "DeviceName": "string",
   "DeviceType": "string",
   "ImageVersion": "string",
   "JobId": "string",
   "JobType": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeDeviceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTime](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-CreatedTime"></a>
When the job was created.
Type: Timestamp

 ** [DeviceArn](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-DeviceArn"></a>
The device's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [DeviceId](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-DeviceId"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [DeviceName](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-DeviceName"></a>
The device's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [DeviceType](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-DeviceType"></a>
The device's type.
Type: String
Valid Values: `PANORAMA_APPLIANCE_DEVELOPER_KIT | PANORAMA_APPLIANCE`

 ** [ImageVersion](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-ImageVersion"></a>
For an OTA job, the target version of the device software.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`

 ** [JobId](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [JobType](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-JobType"></a>
The job's type.
Type: String
Valid Values: `OTA | REBOOT`

 ** [Status](#API_DescribeDeviceJob_ResponseSyntax) **   <a name="panorama-DescribeDeviceJob-response-Status"></a>
The job's status.
Type: String
Valid Values: `PENDING | IN_PROGRESS | VERIFYING | REBOOTING | DOWNLOADING | COMPLETED | FAILED`

## Errors
<a name="API_DescribeDeviceJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 404

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDeviceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribeDeviceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribeDeviceJob)
