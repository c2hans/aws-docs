---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_CreateJobForDevices.html
---

# CreateJobForDevices
<a name="API_CreateJobForDevices"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Creates a job to run on a device. A job can update a device's software or reboot it.

## Request Syntax
<a name="API_CreateJobForDevices_RequestSyntax"></a>

```
POST /jobs HTTP/1.1
Content-type: application/json

{
   "DeviceIds": [ "{{string}}" ],
   "DeviceJobConfig": {
      "OTAJobConfig": {
         "AllowMajorVersionUpdate": {{boolean}},
         "ImageVersion": "{{string}}"
      }
   },
   "JobType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateJobForDevices_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateJobForDevices_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceIds](#API_CreateJobForDevices_RequestSyntax) **   <a name="panorama-CreateJobForDevices-request-DeviceIds"></a>
ID of target device.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [DeviceJobConfig](#API_CreateJobForDevices_RequestSyntax) **   <a name="panorama-CreateJobForDevices-request-DeviceJobConfig"></a>
Configuration settings for a software update job.
Type: [DeviceJobConfig](API_DeviceJobConfig.md) object
Required: No

 ** [JobType](#API_CreateJobForDevices_RequestSyntax) **   <a name="panorama-CreateJobForDevices-request-JobType"></a>
The type of job to run.
Type: String
Valid Values: `OTA | REBOOT`
Required: Yes

## Response Syntax
<a name="API_CreateJobForDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Jobs": [
      {
         "DeviceId": "string",
         "JobId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateJobForDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Jobs](#API_CreateJobForDevices_ResponseSyntax) **   <a name="panorama-CreateJobForDevices-response-Jobs"></a>
A list of jobs.
Type: Array of [Job](API_Job.md) objects

## Errors
<a name="API_CreateJobForDevices_Errors"></a>

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
<a name="API_CreateJobForDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/CreateJobForDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/CreateJobForDevices)
