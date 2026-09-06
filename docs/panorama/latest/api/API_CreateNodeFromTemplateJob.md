---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_CreateNodeFromTemplateJob.html
---

# CreateNodeFromTemplateJob
<a name="API_CreateNodeFromTemplateJob"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Creates a camera stream node.

## Request Syntax
<a name="API_CreateNodeFromTemplateJob_RequestSyntax"></a>

```
POST /packages/template-job HTTP/1.1
Content-type: application/json

{
   "JobTags": [
      {
         "ResourceType": "{{string}}",
         "Tags": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "NodeDescription": "{{string}}",
   "NodeName": "{{string}}",
   "OutputPackageName": "{{string}}",
   "OutputPackageVersion": "{{string}}",
   "TemplateParameters": {
      "{{string}}" : "{{string}}"
   },
   "TemplateType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateNodeFromTemplateJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNodeFromTemplateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [JobTags](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-JobTags"></a>
Tags for the job.
Type: Array of [JobResourceTags](API_JobResourceTags.md) objects
Required: No

 ** [NodeDescription](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-NodeDescription"></a>
A description for the node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [NodeName](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-NodeName"></a>
A name for the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [OutputPackageName](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-OutputPackageName"></a>
An output package name for the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [OutputPackageVersion](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-OutputPackageVersion"></a>
An output package version for the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** [TemplateParameters](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-TemplateParameters"></a>
Template parameters for the node.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `.+`
Required: Yes

 ** [TemplateType](#API_CreateNodeFromTemplateJob_RequestSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-request-TemplateType"></a>
The type of node.
Type: String
Valid Values: `RTSP_CAMERA_STREAM`
Required: Yes

## Response Syntax
<a name="API_CreateNodeFromTemplateJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobId": "string"
}
```

## Response Elements
<a name="API_CreateNodeFromTemplateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_CreateNodeFromTemplateJob_ResponseSyntax) **   <a name="panorama-CreateNodeFromTemplateJob-response-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

## Errors
<a name="API_CreateNodeFromTemplateJob_Errors"></a>

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
<a name="API_CreateNodeFromTemplateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/CreateNodeFromTemplateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/CreateNodeFromTemplateJob)
