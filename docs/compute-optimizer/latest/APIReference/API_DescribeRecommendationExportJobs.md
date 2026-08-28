---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DescribeRecommendationExportJobs.html
---

# DescribeRecommendationExportJobs
<a name="API_DescribeRecommendationExportJobs"></a>

Describes recommendation export jobs created in the last seven days.

Use the [ExportAutoScalingGroupRecommendations](API_ExportAutoScalingGroupRecommendations.md) or [ExportEC2InstanceRecommendations](API_ExportEC2InstanceRecommendations.md) actions to request an export of your recommendations. Then use the [DescribeRecommendationExportJobs](#API_DescribeRecommendationExportJobs) action to view your export jobs.

## Request Syntax
<a name="API_DescribeRecommendationExportJobs_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "jobIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRecommendationExportJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeRecommendationExportJobs_RequestSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of export jobs.
Type: Array of [JobFilter](API_JobFilter.md) objects
Required: No

 ** [jobIds](#API_DescribeRecommendationExportJobs_RequestSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-request-jobIds"></a>
The identification numbers of the export jobs to return.
An export job ID is returned when you create an export using the [ExportAutoScalingGroupRecommendations](API_ExportAutoScalingGroupRecommendations.md) or [ExportEC2InstanceRecommendations](API_ExportEC2InstanceRecommendations.md) actions.
All export jobs created in the last seven days are returned if this parameter is omitted.
Type: Array of strings
Required: No

 ** [maxResults](#API_DescribeRecommendationExportJobs_RequestSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-request-maxResults"></a>
The maximum number of export jobs to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeRecommendationExportJobs_RequestSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-request-nextToken"></a>
The token to advance to the next page of export jobs.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeRecommendationExportJobs_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recommendationExportJobs": [
      {
         "creationTimestamp": number,
         "destination": {
            "s3": {
               "bucket": "string",
               "key": "string",
               "metadataKey": "string"
            }
         },
         "failureReason": "string",
         "jobId": "string",
         "lastUpdatedTimestamp": number,
         "resourceType": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRecommendationExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeRecommendationExportJobs_ResponseSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-response-nextToken"></a>
The token to use to advance to the next page of export jobs.
This value is null when there are no more pages of export jobs to return.
Type: String

 ** [recommendationExportJobs](#API_DescribeRecommendationExportJobs_ResponseSyntax) **   <a name="computeoptimizer-DescribeRecommendationExportJobs-response-recommendationExportJobs"></a>
An array of objects that describe recommendation export jobs.
Type: Array of [RecommendationExportJob](API_RecommendationExportJob.md) objects

## Errors
<a name="API_DescribeRecommendationExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** OptInRequiredException **
The account is not opted in to AWS Compute Optimizer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRecommendationExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/DescribeRecommendationExportJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
