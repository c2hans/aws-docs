---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/harvest_jobs-id.html
---

# Harvest\_jobs id
<a name="harvest_jobs-id"></a>

HarvestJobs provide details about the video on demand (VOD) assets that you harvested, or extracted, from live content streams.

## URI
<a name="harvest_jobs-id-url"></a>

`/harvest_jobs/{{id}}`

## HTTP methods
<a name="harvest_jobs-id-http-methods"></a>

### GET
<a name="harvest_jobs-idget"></a>

**Operation ID:** `DescribeHarvestJob`

Provides details about a harvestJob.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you are working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | HarvestJob |  `200 OK response` <br />HarvestJob details are returned successfully.  |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="harvest_jobs-idoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you are working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="harvest_jobs-id-schemas"></a>

### Response bodies
<a name="harvest_jobs-id-response-examples"></a>

#### HarvestJob schema
<a name="harvest_jobs-id-response-body-harvestjob-example"></a>

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
<a name="harvest_jobs-id-properties"></a>

### HarvestJob
<a name="harvest_jobs-id-model-harvestjob"></a>

HarvestJob configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) that MediaPackage assigns to the harvestJob.  |
| channelId | string | False | The ID of the channel that the HarvestJob harvests from.  |
| createdAt | string | False | The time that you submitted the HarvestJob.  |
| endTime | string | False | The end time of the window for the live-to-VOD asset.  |
| id | string | False | Unique identifier for this harvestJob. The identifier can't be changed after the harvestJob is created.  |
| originEndpointId | string | False | The endpoint that MediaPackage harvests the live-to-VOD asset from.  |
| s3Destination | [S3Destination](#harvest_jobs-id-model-s3destination) | False | Parameters that define how MediaPackage accesses and saves the harvested asset to your Amazon S3 bucket.  |
| startTime | string | False | The start time of the window for the live-to-VOD asset.  |
| status | string<br />Values: `IN_PROGRESS \| SUCCEEDED \| FAILED` | False | The current status of the harvestJob.<br />We recommend that you configure a CloudWatch Event to notify you as harvestJobs complete or fail. For any failures, the CloudWatch Event explains why the harvestJob failed. For more information about CloudWatch Events, see [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch Events](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-cloudwatch-events.html). |

### S3Destination
<a name="harvest_jobs-id-model-s3destination"></a>

Defines how and where MediaPackage saves the live-to-VOD asset after it's been harvested from the live stream.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string | True | The name of the Amazon S3 bucket where MediaPackage stores the live-to-VOD asset.  |
| manifestKey | string | True | The path within the S3 bucket where MediaPackage stores the parent manifest of the harvested asset.  |
| roleArn | string | True | The Amazon Resource Name (ARN) for the IAM role that provides MediaPackage access to read and write to the Amazon S3 bucket where the harvested live-to-VOD asset is stored. For more information about this role, see [Allowing AWS Elemental MediaPackage to Access Amazon S3](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-create-trust-rel.html).  |

## See also
<a name="harvest_jobs-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeHarvestJob
<a name="DescribeHarvestJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/DescribeHarvestJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/DescribeHarvestJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
