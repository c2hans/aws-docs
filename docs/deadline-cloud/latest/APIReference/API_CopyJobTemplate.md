---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CopyJobTemplate.html
---

# CopyJobTemplate
<a name="API_CopyJobTemplate"></a>

Copies a job template to an Amazon S3 bucket.

## Request Syntax
<a name="API_CopyJobTemplate_RequestSyntax"></a>

```
POST /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/jobs/{{jobId}}/template HTTP/1.1
Content-type: application/json

{
   "targetS3Location": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CopyJobTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_CopyJobTemplate_RequestSyntax) **   <a name="deadlinecloud-CopyJobTemplate-request-uri-farmId"></a>
The farm ID to copy.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [jobId](#API_CopyJobTemplate_RequestSyntax) **   <a name="deadlinecloud-CopyJobTemplate-request-uri-jobId"></a>
The job ID to copy.
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_CopyJobTemplate_RequestSyntax) **   <a name="deadlinecloud-CopyJobTemplate-request-uri-queueId"></a>
The queue ID to copy.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_CopyJobTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetS3Location](#API_CopyJobTemplate_RequestSyntax) **   <a name="deadlinecloud-CopyJobTemplate-request-targetS3Location"></a>
The Amazon S3 bucket name and key where you would like to add a copy of the job template.
Type: [S3Location](API_S3Location.md) object
Required: Yes

## Response Syntax
<a name="API_CopyJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "templateType": "string"
}
```

## Response Elements
<a name="API_CopyJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [templateType](#API_CopyJobTemplate_ResponseSyntax) **   <a name="deadlinecloud-CopyJobTemplate-response-templateType"></a>
The format of the job template, either `JSON` or `YAML`.
Type: String
Valid Values: `JSON | YAML`

## Errors
<a name="API_CopyJobTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CopyJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CopyJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CopyJobTemplate)
