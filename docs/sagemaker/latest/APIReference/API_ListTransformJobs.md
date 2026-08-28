---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTransformJobs.html
---

# ListTransformJobs
<a name="API_ListTransformJobs"></a>

Lists transform jobs.

## Request Syntax
<a name="API_ListTransformJobs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTransformJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-CreationTimeAfter"></a>
A filter that returns only transform jobs created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-CreationTimeBefore"></a>
A filter that returns only transform jobs created before the specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-LastModifiedTimeAfter"></a>
A filter that returns only transform jobs modified after the specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-LastModifiedTimeBefore"></a>
A filter that returns only transform jobs modified before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-MaxResults"></a>
The maximum number of transform jobs to return in the response. The default value is `10`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-NameContains"></a>
A string in the transform job name. This filter returns only transform jobs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-NextToken"></a>
If the result of the previous `ListTransformJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of transform jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListTransformJobs_RequestSyntax) **   <a name="sagemaker-ListTransformJobs-request-StatusEquals"></a>
A filter that retrieves only transform jobs with a specific status.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## Response Syntax
<a name="API_ListTransformJobs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TransformJobSummaries": [
      {
         "CreationTime": number,
         "FailureReason": "string",
         "LastModifiedTime": number,
         "TransformEndTime": number,
         "TransformJobArn": "string",
         "TransformJobName": "string",
         "TransformJobStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTransformJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTransformJobs_ResponseSyntax) **   <a name="sagemaker-ListTransformJobs-response-NextToken"></a>
If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of transform jobs, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TransformJobSummaries](#API_ListTransformJobs_ResponseSyntax) **   <a name="sagemaker-ListTransformJobs-response-TransformJobSummaries"></a>
An array of `TransformJobSummary` objects.
Type: Array of [TransformJobSummary](API_TransformJobSummary.md) objects

## Errors
<a name="API_ListTransformJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListTransformJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTransformJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTransformJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
