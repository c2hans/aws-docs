---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceExperiments.html
---

# ListInferenceExperiments
<a name="API_ListInferenceExperiments"></a>

Returns the list of all inference experiments.

## Request Syntax
<a name="API_ListInferenceExperiments_RequestSyntax"></a>

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
   "StatusEquals": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceExperiments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-CreationTimeAfter"></a>
Selects inference experiments which were created after this timestamp.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-CreationTimeBefore"></a>
Selects inference experiments which were created before this timestamp.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-LastModifiedTimeAfter"></a>
Selects inference experiments which were last modified after this timestamp.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-LastModifiedTimeBefore"></a>
Selects inference experiments which were last modified before this timestamp.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-MaxResults"></a>
The maximum number of results to select.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-NameContains"></a>
Selects inference experiments whose names contain this name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-NextToken"></a>
 The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-SortBy"></a>
The column by which to sort the listed inference experiments.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-SortOrder"></a>
The direction of sorting (ascending or descending).
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-StatusEquals"></a>
 Selects inference experiments which are in this status. For the possible statuses, see [DescribeInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html).
Type: String
Valid Values: `Creating | Created | Updating | Running | Starting | Stopping | Completed | Cancelled`
Required: No

 ** [Type](#API_ListInferenceExperiments_RequestSyntax) **   <a name="sagemaker-ListInferenceExperiments-request-Type"></a>
 Selects inference experiments of this type. For the possible types of inference experiments, see [CreateInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html).
Type: String
Valid Values: `ShadowMode`
Required: No

## Response Syntax
<a name="API_ListInferenceExperiments_ResponseSyntax"></a>

```
{
   "InferenceExperiments": [
      {
         "CompletionTime": number,
         "CreationTime": number,
         "Description": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "RoleArn": "string",
         "Schedule": {
            "EndTime": number,
            "StartTime": number
         },
         "Status": "string",
         "StatusReason": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceExperiments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExperiments](#API_ListInferenceExperiments_ResponseSyntax) **   <a name="sagemaker-ListInferenceExperiments-response-InferenceExperiments"></a>
List of inference experiments.
Type: Array of [InferenceExperimentSummary](API_InferenceExperimentSummary.md) objects

 ** [NextToken](#API_ListInferenceExperiments_ResponseSyntax) **   <a name="sagemaker-ListInferenceExperiments-response-NextToken"></a>
The token to use when calling the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListInferenceExperiments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListInferenceExperiments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListInferenceExperiments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListInferenceExperiments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
