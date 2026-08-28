---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-import.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Segment Import Jobs
<a name="apps-application-id-segments-segment-id-jobs-import"></a>

The Segment Import Jobs resource represents jobs that create user segments by importing endpoint definitions. A *segment* designates which users receive messages from a campaign or journey.

You can use this resource to retrieve information about the import jobs for a segment. This includes checking the status of an in-progress import job and accessing the history of your import jobs.

## URI
<a name="apps-application-id-segments-segment-id-jobs-import-url"></a>

`/v1/apps/{{application-id}}/segments/{{segment-id}}/jobs/import`

## HTTP methods
<a name="apps-application-id-segments-segment-id-jobs-import-http-methods"></a>

### GET
<a name="apps-application-id-segments-segment-id-jobs-importget"></a>

**Operation ID:** `GetSegmentImportJobs`

Retrieves information about the status and settings of the import jobs for a segment.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{segment-id}} | String | True | The unique identifier for the segment. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| token | String | False | The `NextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ImportJobsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-segments-segment-id-jobs-importoptions"></a>

Retrieves information about the communication requirements and options that are available for the Segment Import Jobs resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{segment-id}} | String | True | The unique identifier for the segment. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-segments-segment-id-jobs-import-schemas"></a>

### Response bodies
<a name="apps-application-id-segments-segment-id-jobs-import-response-examples"></a>

#### ImportJobsResponse schema
<a name="apps-application-id-segments-segment-id-jobs-import-response-body-importjobsresponse-example"></a>

```
{
  "Item": [
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
        "S3Url": "string",
        "RoleArn": "string",
        "ExternalId": "string",
        "Format": enum,
        "RegisterEndpoints": boolean,
        "DefineSegment": boolean,
        "SegmentName": "string",
        "SegmentId": "string"
      }
    }
  ],
  "NextToken": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-segments-segment-id-jobs-import-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-segments-segment-id-jobs-import-properties"></a>

### ImportJobResource
<a name="apps-application-id-segments-segment-id-jobs-import-model-importjobresource"></a>

Provides information about the resource settings for a job that imports endpoint definitions from one or more files. The files can be stored in an Amazon Simple Storage Service (Amazon S3) bucket or uploaded directly from a computer by using the Amazon Pinpoint console.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DefineSegment | boolean | False | Specifies whether the import job creates a segment that contains the endpoints, when the endpoint definitions are imported. |
| ExternalId | string | False | (Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint. |
| Format | string<br />Values: `CSV \| JSON` | True | The format of the files that contain the endpoint definitions to import. Valid values are: `CSV`, for comma-separated values format; and, `JSON`, for newline-delimited JSON format.<br />If the files are stored in an Amazon S3 location and that location contains multiple files that use different formats, Amazon Pinpoint imports data only from the files that use the specified format. |
| RegisterEndpoints | boolean | False | Specifies whether the import job registers the endpoints with Amazon Pinpoint, when the endpoint definitions are imported. |
| RoleArn | string | True | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from. |
| S3Url | string | True | The URL of the Amazon Simple Storage Service (Amazon S3) bucket that contains the endpoint definitions to import. This location can be a folder or a single file. If the location is a folder, Amazon Pinpoint imports endpoint definitions from the files in this location, including any subfolders that the folder contains.<br />The URL should be in the following format: `s3://{{bucket-name}}/{{folder-name}}/{{file-name}}.` The location can end with the key for an individual object or a prefix that qualifies multiple objects. |
| SegmentId | string | False | The identifier for the segment that the import job updates or adds endpoint definitions to, if the import job updates an existing segment. |
| SegmentName | string | False | The custom name for the segment that's created by the import job, if the value of the `DefineSegment` property is `true`.A segment must have a name otherwise it will not appear in the Amazon Pinpoint console. |

### ImportJobResponse
<a name="apps-application-id-segments-segment-id-jobs-import-model-importjobresponse"></a>

Provides information about the status and settings of a job that imports endpoint definitions from one or more files. The files can be stored in an Amazon Simple Storage Service (Amazon S3) bucket or uploaded directly from a computer by using the Amazon Pinpoint console.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that's associated with the import job. |
| CompletedPieces | integer | False | The number of pieces that were processed successfully (completed) by the import job, as of the time of the request. |
| CompletionDate | string | False | The date, in ISO 8601 format, when the import job was completed. |
| CreationDate | string | True | The date, in ISO 8601 format, when the import job was created. |
| Definition | [ImportJobResource](#apps-application-id-segments-segment-id-jobs-import-model-importjobresource) | True | The resource settings that apply to the import job. |
| FailedPieces | integer | False | The number of pieces that weren't processed successfully (failed) by the import job, as of the time of the request. |
| Failures | Array of type string | False | An array of entries, one for each of the first 100 entries that weren't processed successfully (failed) by the import job, if any. |
| Id | string | True | The unique identifier for the import job. |
| JobStatus | string<br />Values: `CREATED \| PREPARING_FOR_INITIALIZATION \| INITIALIZING \| PROCESSING \| PENDING_JOB \| COMPLETING \| COMPLETED \| CANCELLING \| CANCELLED \| FAILING \| FAILED` | True | The status of the import job. The job status is `FAILED` if Amazon Pinpoint wasn't able to process one or more pieces in the job. |
| TotalFailures | integer | False | The total number of endpoint definitions that weren't processed successfully (failed) by the import job, typically because an error, such as a syntax error, occurred. |
| TotalPieces | integer | False | The total number of pieces that must be processed to complete the import job. Each piece consists of an approximately equal portion of the endpoint definitions that are part of the import job. |
| TotalProcessed | integer | False | The total number of endpoint definitions that were processed by the import job. |
| Type | string | True | The job type. This value is `IMPORT` for import jobs. |

### ImportJobsResponse
<a name="apps-application-id-segments-segment-id-jobs-import-model-importjobsresponse"></a>

Provides information about the status and settings of all the import jobs that are associated with an application or segment. An import job is a job that imports endpoint definitions from one or more files.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [ImportJobResponse](#apps-application-id-segments-segment-id-jobs-import-model-importjobresponse) | True | An array of responses, one for each import job that's associated with the application (Import Jobs resource) or segment (Segment Import Jobs resource). |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### MessageBody
<a name="apps-application-id-segments-segment-id-jobs-import-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-segments-segment-id-jobs-import-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSegmentImportJobs
<a name="GetSegmentImportJobs-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetSegmentImportJobs)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetSegmentImportJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
