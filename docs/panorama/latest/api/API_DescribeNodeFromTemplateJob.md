---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNodeFromTemplateJob.html
---

# DescribeNodeFromTemplateJob
<a name="API_DescribeNodeFromTemplateJob"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a job to create a camera stream node.

## Request Syntax
<a name="API_DescribeNodeFromTemplateJob_RequestSyntax"></a>

```
GET /packages/template-job/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeNodeFromTemplateJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_DescribeNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-request-uri-JobId"></a>
The job's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_DescribeNodeFromTemplateJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeNodeFromTemplateJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTime": number,
   "JobId": "string",
   "JobTags": [
      {
         "ResourceType": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "LastUpdatedTime": number,
   "NodeDescription": "string",
   "NodeName": "string",
   "OutputPackageName": "string",
   "OutputPackageVersion": "string",
   "Status": "string",
   "StatusMessage": "string",
   "TemplateParameters": {
      "string" : "string"
   },
   "TemplateType": "string"
}
```

## Response Elements
<a name="API_DescribeNodeFromTemplateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTime](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-CreatedTime"></a>
When the job was created.
Type: Timestamp

 ** [JobId](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [JobTags](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-JobTags"></a>
The job's tags.
Type: Array of [JobResourceTags](API_JobResourceTags.md) objects

 ** [LastUpdatedTime](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-LastUpdatedTime"></a>
When the job was updated.
Type: Timestamp

 ** [NodeDescription](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-NodeDescription"></a>
The node's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [NodeName](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-NodeName"></a>
The node's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [OutputPackageName](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-OutputPackageName"></a>
The job's output package name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [OutputPackageVersion](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-OutputPackageVersion"></a>
The job's output package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`

 ** [Status](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-Status"></a>
The job's status.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`

 ** [StatusMessage](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-StatusMessage"></a>
The job's status message.
Type: String

 ** [TemplateParameters](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-TemplateParameters"></a>
The job's template parameters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `.+`

 ** [TemplateType](#API_DescribeNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-DescribeNodeFromTemplateJob-response-TemplateType"></a>
The job's template type.
Type: String
Valid Values: `RTSP_CAMERA_STREAM`

## Errors
<a name="API_DescribeNodeFromTemplateJob_Errors"></a>

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
<a name="API_DescribeNodeFromTemplateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribeNodeFromTemplateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribeNodeFromTemplateJob)
