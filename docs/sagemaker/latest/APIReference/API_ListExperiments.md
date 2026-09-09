---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListExperiments.html
---

# ListExperiments
<a name="API_ListExperiments"></a>

Lists all the experiments in your account. The list can be filtered to show only experiments that were created in a specific time range. The list can be sorted by experiment name or creation time.

## Request Syntax
<a name="API_ListExperiments_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListExperiments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListExperiments_RequestSyntax) **   <a name="sagemaker-ListExperiments-request-MaxResults"></a>
The maximum number of experiments to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListExperiments_RequestSyntax) **   <a name="sagemaker-ListExperiments-request-NextToken"></a>
If the previous call to `ListExperiments` didn't return the full set of experiments, the call returns a token for getting the next set of experiments.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListExperiments_RequestSyntax) **   <a name="sagemaker-ListExperiments-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListExperiments_RequestSyntax) **   <a name="sagemaker-ListExperiments-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListExperiments_ResponseSyntax"></a>

```
{
   "ExperimentSummaries": [
      {
         "DisplayName": "string",
         "ExperimentArn": "string",
         "ExperimentName": "string",
         "ExperimentSource": {
            "SourceArn": "string",
            "SourceType": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExperiments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExperimentSummaries](#API_ListExperiments_ResponseSyntax) **   <a name="sagemaker-ListExperiments-response-ExperimentSummaries"></a>
A list of the summaries of your experiments.
Type: Array of [ExperimentSummary](API_ExperimentSummary.md) objects

 ** [NextToken](#API_ListExperiments_ResponseSyntax) **   <a name="sagemaker-ListExperiments-response-NextToken"></a>
A token for getting the next set of experiments, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListExperiments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListExperiments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListExperiments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListExperiments)
