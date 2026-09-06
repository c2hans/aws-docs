---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListDevicesJobs.html
---

# ListDevicesJobs
<a name="API_ListDevicesJobs"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of jobs.

## Request Syntax
<a name="API_ListDevicesJobs_RequestSyntax"></a>

```
GET /jobs?DeviceId={{DeviceId}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDevicesJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_ListDevicesJobs_RequestSyntax) **   <a name="panorama-ListDevicesJobs-request-uri-DeviceId"></a>
Filter results by the job's target device ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [MaxResults](#API_ListDevicesJobs_RequestSyntax) **   <a name="panorama-ListDevicesJobs-request-uri-MaxResults"></a>
The maximum number of device jobs to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NextToken](#API_ListDevicesJobs_RequestSyntax) **   <a name="panorama-ListDevicesJobs-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Request Body
<a name="API_ListDevicesJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDevicesJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeviceJobs": [
      {
         "CreatedTime": number,
         "DeviceId": "string",
         "DeviceName": "string",
         "JobId": "string",
         "JobType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDevicesJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceJobs](#API_ListDevicesJobs_ResponseSyntax) **   <a name="panorama-ListDevicesJobs-response-DeviceJobs"></a>
A list of jobs.
Type: Array of [DeviceJob](API_DeviceJob.md) objects

 ** [NextToken](#API_ListDevicesJobs_ResponseSyntax) **   <a name="panorama-ListDevicesJobs-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Errors
<a name="API_ListDevicesJobs_Errors"></a>

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
<a name="API_ListDevicesJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListDevicesJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListDevicesJobs)
