---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCardExportJobs.html
---

# ListModelCardExportJobs
<a name="API_ListModelCardExportJobs"></a>

List the export jobs for the Amazon SageMaker Model Card.

## Request Syntax
<a name="API_ListModelCardExportJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "ModelCardExportJobNameContains": "{{string}}",
   "ModelCardName": "{{string}}",
   "ModelCardVersion": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelCardExportJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-MaxResults"></a>
The maximum number of model card export jobs to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModelCardExportJobNameContains](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-ModelCardExportJobNameContains"></a>
Only list model card export jobs with names that contain the specified string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [ModelCardName](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-ModelCardName"></a>
List export jobs for the model card with the specified name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelCardVersion](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-ModelCardVersion"></a>
List export jobs for the model card with the specified version.
Type: Integer
Required: No

 ** [NextToken](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-NextToken"></a>
If the response to a previous `ListModelCardExportJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of model card export jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-SortBy"></a>
Sort model card export jobs by either name or creation time. Sorts by creation time by default.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-SortOrder"></a>
Sort model card export jobs by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListModelCardExportJobs_RequestSyntax) **   <a name="sagemaker-ListModelCardExportJobs-request-StatusEquals"></a>
Only list model card export jobs with the specified status.
Type: String
Valid Values: `InProgress | Completed | Failed`
Required: No

## Response Syntax
<a name="API_ListModelCardExportJobs_ResponseSyntax"></a>

```
{
   "ModelCardExportJobSummaries": [
      {
         "ModelCardExportJobArn": "string",
         "ModelCardExportJobName": "string",
         "ModelCardName": "string",
         "ModelCardVersion": number,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelCardExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardExportJobSummaries](#API_ListModelCardExportJobs_ResponseSyntax) **   <a name="sagemaker-ListModelCardExportJobs-response-ModelCardExportJobSummaries"></a>
The summaries of the listed model card export jobs.
Type: Array of [ModelCardExportJobSummary](API_ModelCardExportJobSummary.md) objects

 ** [NextToken](#API_ListModelCardExportJobs_ResponseSyntax) **   <a name="sagemaker-ListModelCardExportJobs-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of model card export jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelCardExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelCardExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelCardExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelCardExportJobs)
