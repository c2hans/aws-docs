---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListEnrichmentJobs.html
---

# ListEnrichmentJobs
<a name="API_ListEnrichmentJobs"></a>

Lists enrichment jobs within a workspace with optional filtering and pagination. Results are ordered by createdAt timestamp descending (newest first).

 **Filtering**

Combine filters to narrow results:
+  **datasetId**: Filter by dataset
+  **propertyAlias** OR **timeSeriesId**: Filter by time series (specify one, not both)
+  **status**: Filter by job status (e.g., RUNNING to find active jobs)
+  **jobType**: Filter by enrichment type (currently only EVENT\_DETECTION)
+  **startDate** and **endDate**: Filter by job creation time range

 **Important Constraints**
+ You must specify either propertyAlias OR timeSeriesId, but not both
+ Attempting to specify both results in an InvalidRequestException
+ Date filters use ISO 8601 format
+ startDate is exclusive, endDate is inclusive

 **Pagination**

The operation returns up to maxResults jobs per page (default 50). If more results exist, the response includes a nextToken. Submit this token in a subsequent request to retrieve the next page.

 **Common Use Cases**
+ Find all running jobs: Filter by status=RUNNING
+ List recent jobs for a dataset: Filter by datasetId with optional date range
+ Monitor jobs for a specific sensor: Filter by propertyAlias or timeSeriesId
+ Track all event detection jobs: Filter by jobType=EVENT\_DETECTION

 **Performance**

Performance is optimal when filtering by supported fields (datasetId, propertyAlias, timeSeriesId, status, jobType).

## Request Syntax
<a name="API_ListEnrichmentJobs_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/enrichment-jobs?datasetId={{datasetId}}&endDate={{endDate}}&jobType={{jobType}}&maxResults={{maxResults}}&nextToken={{nextToken}}&propertyAlias={{propertyAlias}}&startDate={{startDate}}&status={{status}}&timeSeriesId={{timeSeriesId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnrichmentJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-datasetId"></a>
Filter jobs by dataset ID. Returns only jobs analyzing data from the specified dataset.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [endDate](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-endDate"></a>
The inclusive end of the date range for filtering jobs by creation time. Jobs created on or before this timestamp are included. Use ISO 8601 format (e.g., 2024-01-31T23:59:59Z).

 ** [jobType](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-jobType"></a>
Filter by enrichment job type. Currently only EVENT\_DETECTION is supported. Use this filter to future-proof queries when additional job types are added.
Valid Values: `EVENT_DETECTION`

 ** [maxResults](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-maxResults"></a>
Maximum number of jobs to return per page. Defaults to 50 if not specified. Use smaller values for faster responses, larger values to reduce API calls.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-nextToken"></a>
Pagination token from a previous ListEnrichmentJobs response. Include this token to retrieve the next page of results. Omit for the first request.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [propertyAlias](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-propertyAlias"></a>
Filter by property alias (human-readable sensor name). Specify either propertyAlias or timeSeriesId, but not both. Returns only jobs analyzing the specified property alias.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [startDate](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-startDate"></a>
The exclusive start of the date range for filtering jobs by creation time. Jobs created after this timestamp are included. Use ISO 8601 format (e.g., 2024-01-01T00:00:00Z).

 ** [status](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-status"></a>
Filter by job status. Returns only jobs in the specified status. Use RUNNING to find active jobs, or FAILED to identify jobs requiring attention.
Valid Values: `PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED`

 ** [timeSeriesId](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-timeSeriesId"></a>
Filter by time series ID (system identifier). Specify either timeSeriesId or propertyAlias, but not both. Returns only jobs analyzing the specified time series.
Length Constraints: Minimum length of 36. Maximum length of 73.

 ** [workspaceName](#API_ListEnrichmentJobs_RequestSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-request-uri-workspaceName"></a>
The name of the IoT SiteWise workspace to list enrichment jobs from.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_ListEnrichmentJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnrichmentJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "createdAt": number,
         "datasetId": "string",
         "jobId": "string",
         "jobType": "string",
         "propertyAlias": "string",
         "status": "string",
         "timeSeriesId": "string",
         "updatedAt": number,
         "workspaceName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnrichmentJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListEnrichmentJobs_ResponseSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-response-jobs"></a>
Array of job summaries matching the filter criteria, ordered by creation time descending (newest first). Each summary includes key identifiers (jobId, datasetId, propertyAlias/timeSeriesId) and status information without the full job configuration. Use DescribeEnrichmentJob to retrieve complete details.
Type: Array of [EnrichmentJobSummary](API_EnrichmentJobSummary.md) objects

 ** [nextToken](#API_ListEnrichmentJobs_ResponseSyntax) **   <a name="iotsitewise-ListEnrichmentJobs-response-nextToken"></a>
Pagination token to retrieve the next page of results. If present, more jobs exist that match the filter criteria. Include this token in a subsequent ListEnrichmentJobs request to retrieve the next page. If absent, you have retrieved all matching jobs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListEnrichmentJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListEnrichmentJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListEnrichmentJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListEnrichmentJobs)
