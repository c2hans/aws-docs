---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobsqueries.html
---

# JobsQueries
<a name="jobsqueries"></a>

## URI
<a name="jobsqueries-url"></a>

`/2017-08-29/jobsQueries`

## HTTP methods
<a name="jobsqueries-http-methods"></a>

### POST
<a name="jobsqueriespost"></a>

**Operation ID:** `StartJobsQuery`

Start an asynchronous jobs query using the provided filters. To receive the list of jobs that match your query, call the GetJobsQueryResults API using the query ID returned by this API.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | StartJobsQueryResponse | 201 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="jobsqueriesoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="jobsqueries-schemas"></a>

### Request bodies
<a name="jobsqueries-request-examples"></a>

#### POST schema
<a name="jobsqueries-request-body-post-example"></a>

```
{
  "nextToken": "string",
  "order": enum,
  "maxResults": integer,
  "filterList": [
    {
      "key": enum,
      "values": [
        "string"
      ]
    }
  ]
}
```

### Response bodies
<a name="jobsqueries-response-examples"></a>

#### StartJobsQueryResponse schema
<a name="jobsqueries-response-body-startjobsqueryresponse-example"></a>

```
{
  "id": "string"
}
```

#### ExceptionBody schema
<a name="jobsqueries-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="jobsqueries-properties"></a>

### ExceptionBody
<a name="jobsqueries-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### JobsQueryFilter
<a name="jobsqueries-model-jobsqueryfilter"></a>

Provide one or more JobsQueryFilter objects, each containing a Key with an associated Values array. Note that MediaConvert queries jobs using OR logic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | [JobsQueryFilterKey](#jobsqueries-model-jobsqueryfilterkey) | False | Specify job details to filter for while performing a jobs query. You specify these filters as part of a key-value pair within the JobsQueryFilter array. The following list describes which keys are available and their possible values: \* queue - Your Queue's name or ARN. \* status - Your job's status. (SUBMITTED \| PROGRESSING \| COMPLETE \| CANCELED \| ERROR) \* fileInput - Your input file URL, or partial input file name. \* jobEngineVersionRequested - The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format. \* jobEngineVersionUsed - The Job engine version that your job used. This may differ from the version that you requested. Valid versions are in a YYYY-MM-DD format. \* audioCodec - Your output's audio codec. (AAC \| MP2 \| MP3 \| WAV \| AIFF \| AC3\| EAC3 \| EAC3\_ATMOS \| VORBIS \| OPUS \| PASSTHROUGH \| FLAC) \* videoCodec - Your output's video codec. (AV1 \| AVC\_INTRA \| FRAME\_CAPTURE \| H\_264 \| H\_265 \| MPEG2 \| PASSTHROUGH \| PRORES \| UNCOMPRESSED \| VC3 \| VP8 \| VP9 \| XAVC) |
| values | Array of type string<br />MaxLength: 100 | False | A list of values associated with a JobsQueryFilterKey. |

### JobsQueryFilterKey
<a name="jobsqueries-model-jobsqueryfilterkey"></a>

Specify job details to filter for while performing a jobs query. You specify these filters as part of a key-value pair within the JobsQueryFilter array. The following list describes which keys are available and their possible values: \* queue - Your Queue's name or ARN. \* status - Your job's status. (SUBMITTED \| PROGRESSING \| COMPLETE \| CANCELED \| ERROR) \* fileInput - Your input file URL, or partial input file name. \* jobEngineVersionRequested - The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format. \* jobEngineVersionUsed - The Job engine version that your job used. This may differ from the version that you requested. Valid versions are in a YYYY-MM-DD format. \* audioCodec - Your output's audio codec. (AAC \| MP2 \| MP3 \| WAV \| AIFF \| AC3\| EAC3 \| EAC3\_ATMOS \| VORBIS \| OPUS \| PASSTHROUGH \| FLAC) \* videoCodec - Your output's video codec. (AV1 \| AVC\_INTRA \| FRAME\_CAPTURE \| H\_264 \| H\_265 \| MPEG2 \| PASSTHROUGH \| PRORES \| UNCOMPRESSED \| VC3 \| VP8 \| VP9 \| XAVC)
+ `queue`
+ `status`
+ `fileInput`
+ `jobEngineVersionRequested`
+ `jobEngineVersionUsed`
+ `audioCodec`
+ `videoCodec`

### Order
<a name="jobsqueries-model-order"></a>

Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
+ `ASCENDING`
+ `DESCENDING`

### StartJobsQueryRequest
<a name="jobsqueries-model-startjobsqueryrequest"></a>

Start an asynchronous jobs query using the provided filters. To receive the list of jobs that match your query, call the GetJobsQueryResults API using the query ID returned by this API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| filterList | Array of type [JobsQueryFilter](#jobsqueries-model-jobsqueryfilter) | False | Optional. Provide an array of JobsQueryFilters for your StartJobsQuery request. |
| maxResults | integer<br />Format: int32<br />Minimum: 1<br />Maximum: 20 | False | Optional. Number of jobs, up to twenty, that will be included in the jobs query. |
| nextToken | string | False | Use this string to request the next batch of jobs matched by a jobs query. |
| order | [Order](#jobsqueries-model-order) | False | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. |

### StartJobsQueryResponse
<a name="jobsqueries-model-startjobsqueryresponse"></a>

Successful requests return an ID that corresponds to an asynchronous jobs query.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The ID of the jobs query. |

## See also
<a name="jobsqueries-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StartJobsQuery
<a name="StartJobsQuery-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/StartJobsQuery)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/StartJobsQuery)
