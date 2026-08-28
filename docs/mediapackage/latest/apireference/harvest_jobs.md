---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/harvest_jobs.html
---

# Harvest\_jobs
<a name="harvest_jobs"></a>

HarvestJobs provide details about the video on demand (VOD) assets that you want to harvest, or extract, from live content streams.

## URI
<a name="harvest_jobs-url"></a>

`/harvest_jobs`

## HTTP methods
<a name="harvest_jobs-http-methods"></a>

### GET
<a name="harvest_jobsget"></a>

**Operation ID:** `ListHarvestJobs`

 Lists harvestJobs that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| includeStatus | String | False | Limits results to harvestJobs with the given status. Valid values are `IN_PROGRESS`, `SUCCEEDED`, and `FAILED`.  |
| nextToken | String | False | Pagination token from the GET list request. Use the token to fetch the next page of results. |
| maxResults | String | False | Upper bound on number of records to return. |
| includeChannelId | String | False | Limits results to harvestJobs associated with the given channel ID.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | HarvestJobList |  `200 OK response` <br />The list of harvestJobs is returned successfully.  |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="harvest_jobspost"></a>

**Operation ID:** `CreateHarvestJob`

Creates a harvestJob to extract a video on demand (VOD) clip from the live stream.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | HarvestJob |  `200 OK response` <br />The harvestJob is created successfully.  |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="harvest_jobsoptions"></a>

Enable CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="harvest_jobs-schemas"></a>

### Request bodies
<a name="harvest_jobs-request-examples"></a>

#### POST schema
<a name="harvest_jobs-request-body-post-example"></a>

```
{
  "s3Destination": {
    "bucketName": "string",
    "manifestKey": "string",
    "roleArn": "string"
  },
  "startTime": "string",
  "endTime": "string",
  "id": "string",
  "originEndpointId": "string"
}
```

### Response bodies
<a name="harvest_jobs-response-examples"></a>

#### HarvestJobList schema
<a name="harvest_jobs-response-body-harvestjoblist-example"></a>

```
{
  "harvestJobs": [
    {
      "createdAt": "string",
      "s3Destination": {
        "bucketName": "string",
        "manifestKey": "string",
        "roleArn": "string"
      },
      "startTime": "string",
      "endTime": "string",
      "id": "string",
      "originEndpointId": "string",
      "arn": "string",
      "channelId": "string",
      "status": enum
    }
  ],
  "nextToken": "string"
}
```

#### HarvestJob schema
<a name="harvest_jobs-response-body-harvestjob-example"></a>

```
{
  "createdAt": "string",
  "s3Destination": {
    "bucketName": "string",
    "manifestKey": "string",
    "roleArn": "string"
  },
  "startTime": "string",
  "endTime": "string",
  "id": "string",
  "originEndpointId": "string",
  "arn": "string",
  "channelId": "string",
  "status": enum
}
```

## Properties
<a name="harvest_jobs-properties"></a>

### HarvestJob
<a name="harvest_jobs-model-harvestjob"></a>

HarvestJob configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) that MediaPackage assigns to the harvestJob.  |
| channelId | string | False | The ID of the channel that the HarvestJob harvests from.  |
| createdAt | string | False | The time that you submitted the HarvestJob.  |
| endTime | string | False | The end time of the window for the live-to-VOD asset.  |
| id | string | False | Unique identifier for this harvestJob. The identifier can't be changed after the harvestJob is created.  |
| originEndpointId | string | False | The endpoint that MediaPackage harvests the live-to-VOD asset from.  |
| s3Destination | [S3Destination](#harvest_jobs-model-s3destination) | False | Parameters that define how MediaPackage accesses and saves the harvested asset to your Amazon S3 bucket.  |
| startTime | string | False | The start time of the window for the live-to-VOD asset.  |
| status | string<br />Values: `IN_PROGRESS \| SUCCEEDED \| FAILED` | False | The current status of the harvestJob.<br />We recommend that you configure a CloudWatch Event to notify you as harvestJobs complete or fail. For any failures, the CloudWatch Event explains why the harvestJob failed. For more information about CloudWatch Events, see [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch Events](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-cloudwatch-events.html). |

### HarvestJobCreateParameters
<a name="harvest_jobs-model-harvestjobcreateparameters"></a>

HarvestJob configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endTime | string | True | The end time of the window for the live-to-VOD asset. The length of the asset can't exceed the startover window on the endpoint. If the startover window is five hours, the asset's end time can't be more than five hours from the asset's start time.  |
| id | string | True | Unique identifier for this harvestJob. The identifier can't be changed after the harvestJob is created.  |
| originEndpointId | string | True | The endpoint that MediaPackage harvests the live-to-VOD asset from.  |
| s3Destination | [S3Destination](#harvest_jobs-model-s3destination) | True | Parameters that define how MediaPackage accesses and saves the harvested asset to your Amazon S3 bucket.  |
| startTime | string | True | The start time of the window for the live-to-VOD asset. This time must be at the same time or after the live event started, and must be within the startover window on the endpoint. If the endpoint has a startover window of five hours and the asset's start time is six hours ago, the harvestJob fails.  |

### HarvestJobList
<a name="harvest_jobs-model-harvestjoblist"></a>

Lists harvestJobs that match a set of filters that you define.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| harvestJobs | Array of type [HarvestJob](#harvest_jobs-model-harvestjob) | False | List of harvestJobs that you created on this account. MediaPackage runs each harvestJob only once. After that, MediaPackage keeps a record of the job on your account for 90 days, for reference purposes only.  |
| nextToken | string | False | Pagination token from the GET list request. Use the token to fetch the next page of results.  |

### S3Destination
<a name="harvest_jobs-model-s3destination"></a>

Defines how and where MediaPackage saves the live-to-VOD asset after it's been harvested from the live stream.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string | True | The name of the Amazon S3 bucket where MediaPackage stores the live-to-VOD asset.  |
| manifestKey | string | True | The path within the S3 bucket where MediaPackage stores the parent manifest of the harvested asset.  |
| roleArn | string | True | The Amazon Resource Name (ARN) for the IAM role that provides MediaPackage access to read and write to the Amazon S3 bucket where the harvested live-to-VOD asset is stored. For more information about this role, see [Allowing AWS Elemental MediaPackage to Access Amazon S3](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-create-trust-rel.html).  |

## See also
<a name="harvest_jobs-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListHarvestJobs
<a name="ListHarvestJobs-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/ListHarvestJobs)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/ListHarvestJobs)

### CreateHarvestJob
<a name="CreateHarvestJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/CreateHarvestJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/CreateHarvestJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
