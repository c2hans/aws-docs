---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export-job-id.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Export Job
<a name="apps-application-id-jobs-export-job-id"></a>

The Export Job resource represents a job that exports endpoint definitions to a file. The file can be added directly to an Amazon Simple Storage Service (Amazon S3) bucket by using the Amazon Pinpoint API or downloaded directly to a computer by using the Amazon Pinpoint console.

An *endpoint* uniquely identifies a mobile device, email address, or phone number that can receive a message. By using export jobs, you can export information about all the endpoints that are associated with an application, or you can export information about the subset of endpoints that belong to a segment.

You can use the Export Job resource to retrieve information about the status and settings of a specific export job for an application. To create an export job for an application or to retrieve information about all the export jobs for an application, use the [Export Jobs](apps-application-id-jobs-export.md) resource.

## URI
<a name="apps-application-id-jobs-export-job-id-url"></a>

`/v1/apps/{{application-id}}/jobs/export/{{job-id}}`

## HTTP methods
<a name="apps-application-id-jobs-export-job-id-http-methods"></a>

### GET
<a name="apps-application-id-jobs-export-job-idget"></a>

**Operation ID:** `GetExportJob`

Retrieves information about the status and settings of a specific export job for an application.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{job-id}} | String | True | The unique identifier for the job. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ExportJobResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-jobs-export-job-idoptions"></a>

Retrieves information about the communication requirements and options that are available for the Export Job resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{job-id}} | String | True | The unique identifier for the job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-jobs-export-job-id-schemas"></a>

### Response bodies
<a name="apps-application-id-jobs-export-job-id-response-examples"></a>

#### ExportJobResponse schema
<a name="apps-application-id-jobs-export-job-id-response-body-exportjobresponse-example"></a>

```
{
  "ApplicationId": "string",
  "Id": "string",
  "JobStatus": enum,
  "CompletedPieces": integer,
  "FailedPieces": integer,
  "TotalPieces": integer,
  "CreationDate": "string",
  "CompletionDate": "string",
  "Type": "string",
  "TotalFailures": integer,
  "TotalProcessed": integer,
  "Failures": [
    "string"
  ],
  "Definition": {
    "SegmentId": "string",
    "SegmentVersion": integer,
    "S3UrlPrefix": "string",
    "RoleArn": "string"
  }
}
```

#### MessageBody schema
<a name="apps-application-id-jobs-export-job-id-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-jobs-export-job-id-properties"></a>

### ExportJobResource
<a name="apps-application-id-jobs-export-job-id-model-exportjobresource"></a>

Provides information about the resource settings for a job that exports endpoint definitions to a file. The file can be added directly to an Amazon Simple Storage Service (Amazon S3) bucket by using the Amazon Pinpoint API or downloaded directly to a computer by using the Amazon Pinpoint console.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| RoleArn | string | True | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorized Amazon Pinpoint to access the Amazon S3 location where the endpoint definitions were exported to. |
| S3UrlPrefix | string | True | The URL of the location in an Amazon Simple Storage Service (Amazon S3) bucket where the endpoint definitions were exported to. This location is typically a folder that contains multiple files. The URL should be in the following format: `s3://{{bucket-name}}/{{folder-name}}/`. |
| SegmentId | string | False | The identifier for the segment that the endpoint definitions were exported from. If this value isn't present, Amazon Pinpoint exported definitions for all the endpoints that are associated with the application. |
| SegmentVersion | integer | False | The version of the segment that the endpoint definitions were exported from. |

### ExportJobResponse
<a name="apps-application-id-jobs-export-job-id-model-exportjobresponse"></a>

Provides information about the status and settings of a job that exports endpoint definitions to a file. The file can be added directly to an Amazon Simple Storage Service (Amazon S3) bucket by using the Amazon Pinpoint API or downloaded directly to a computer by using the Amazon Pinpoint console.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that's associated with the export job. |
| CompletedPieces | integer | False | The number of pieces that were processed successfully (completed) by the export job, as of the time of the request. |
| CompletionDate | string | False | The date, in ISO 8601 format, when the export job was completed. |
| CreationDate | string | True | The date, in ISO 8601 format, when the export job was created. |
| Definition | [ExportJobResource](#apps-application-id-jobs-export-job-id-model-exportjobresource) | True | The resource settings that apply to the export job. |
| FailedPieces | integer | False | The number of pieces that weren't processed successfully (failed) by the export job, as of the time of the request. |
| Failures | Array of type string | False | An array of entries, one for each of the first 100 entries that weren't processed successfully (failed) by the export job, if any. |
| Id | string | True | The unique identifier for the export job. |
| JobStatus | string<br />Values: `CREATED \| PREPARING_FOR_INITIALIZATION \| INITIALIZING \| PROCESSING \| PENDING_JOB \| COMPLETING \| COMPLETED \| CANCELLING \| CANCELLED \| FAILING \| FAILED` | True | The status of the export job. The job status is `FAILED` if Amazon Pinpoint wasn't able to process one or more pieces in the job. |
| TotalFailures | integer | False | The total number of endpoint definitions that weren't processed successfully (failed) by the export job, typically because an error, such as a syntax error, occurred. |
| TotalPieces | integer | False | The total number of pieces that must be processed to complete the export job. Each piece consists of an approximately equal portion of the endpoint definitions that are part of the export job. |
| TotalProcessed | integer | False | The total number of endpoint definitions that were processed by the export job. |
| Type | string | True | The job type. This value is `EXPORT` for export jobs. |

### MessageBody
<a name="apps-application-id-jobs-export-job-id-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-jobs-export-job-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetExportJob
<a name="GetExportJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetExportJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetExportJob)
