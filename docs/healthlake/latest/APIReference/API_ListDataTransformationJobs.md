---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationJobs.html
---

# ListDataTransformationJobs
<a name="API_ListDataTransformationJobs"></a>

Lists data transformation jobs for your AWS account. Results can be filtered by status, job name, and submit time window. Results are paginated. Use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListDataTransformationJobs_RequestSyntax"></a>

```
{
   "JobName": "{{string}}",
   "JobStatus": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubmittedAfter": {{number}},
   "SubmittedBefore": {{number}}
}
```

## Request Parameters
<a name="API_ListDataTransformationJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-JobName"></a>
Filters the results to include only jobs with the specified name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-%@]*`
Required: No

 ** [JobStatus](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-JobStatus"></a>
Filters the results to include only jobs with the specified status.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: No

 ** [MaxResults](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-MaxResults"></a>
The maximum number of jobs to return per page. If you don't specify a value, the service returns up to 100 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-NextToken"></a>
The pagination token from a previous response. Pass this value to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [SubmittedAfter](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-SubmittedAfter"></a>
Filters the results to include only jobs submitted at or after this timestamp.
Type: Timestamp
Required: No

 ** [SubmittedBefore](#API_ListDataTransformationJobs_RequestSyntax) **   <a name="HealthLake-ListDataTransformationJobs-request-SubmittedBefore"></a>
Filters the results to include only jobs submitted at or before this timestamp.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListDataTransformationJobs_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "EndTime": number,
         "JobId": "string",
         "JobName": "string",
         "JobStatus": "string",
         "SourceFormat": "string",
         "SubmitTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataTransformationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDataTransformationJobs_ResponseSyntax) **   <a name="HealthLake-ListDataTransformationJobs-response-Items"></a>
The list of data transformation job summaries.
Type: Array of [TransformationJobSummary](API_TransformationJobSummary.md) objects

 ** [NextToken](#API_ListDataTransformationJobs_ResponseSyntax) **   <a name="HealthLake-ListDataTransformationJobs-response-NextToken"></a>
The pagination token to use in the next request. If this value is `null`, there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDataTransformationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListDataTransformationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListDataTransformationJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ListDataTransformationJobs)
