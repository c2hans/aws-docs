---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html
---

# ListTrials
<a name="API_ListTrials"></a>

Lists the trials in your account. Specify an experiment name to limit the list to the trials that are part of that experiment. Specify a trial component name to limit the list to the trials that associated with that trial component. The list can be filtered to show only trials that were created in a specific time range. The list can be sorted by trial name or creation time.

## Request Syntax
<a name="API_ListTrials_RequestSyntax"></a>

```
{
   "ExperimentName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "TrialComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExperimentName](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-ExperimentName"></a>
A filter that returns only trials that are part of the specified experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [MaxResults](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-MaxResults"></a>
The maximum number of trials to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-NextToken"></a>
If the previous call to `ListTrials` didn't return the full set of trials, the call returns a token for getting the next set of trials.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [TrialComponentName](#API_ListTrials_RequestSyntax) **   <a name="sagemaker-ListTrials-request-TrialComponentName"></a>
A filter that returns only trials that are associated with the specified trial component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## Response Syntax
<a name="API_ListTrials_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrialSummaries": [
      {
         "DisplayName": "string",
         "TrialArn": "string",
         "TrialName": "string",
         "TrialSource": {
            "SourceArn": "string",
            "SourceType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTrials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrials_ResponseSyntax) **   <a name="sagemaker-ListTrials-response-NextToken"></a>
A token for getting the next set of trials, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrialSummaries](#API_ListTrials_ResponseSyntax) **   <a name="sagemaker-ListTrials-response-TrialSummaries"></a>
A list of the summaries of your trials.
Type: Array of [TrialSummary](API_TrialSummary.md) objects

## Errors
<a name="API_ListTrials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListTrials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTrials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTrials)
