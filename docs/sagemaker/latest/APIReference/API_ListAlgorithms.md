---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAlgorithms.html
---

# ListAlgorithms
<a name="API_ListAlgorithms"></a>

Lists the machine learning algorithms that have been created.

## Request Syntax
<a name="API_ListAlgorithms_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAlgorithms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-CreationTimeAfter"></a>
A filter that returns only algorithms created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-CreationTimeBefore"></a>
A filter that returns only algorithms created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-MaxResults"></a>
The maximum number of algorithms to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-NameContains"></a>
A string in the algorithm name. This filter returns only algorithms whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-NextToken"></a>
If the response to a previous `ListAlgorithms` request was truncated, the response includes a `NextToken`. To retrieve the next set of algorithms, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-SortBy"></a>
The parameter by which to sort the results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListAlgorithms_RequestSyntax) **   <a name="sagemaker-ListAlgorithms-request-SortOrder"></a>
The sort order for the results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListAlgorithms_ResponseSyntax"></a>

```
{
   "AlgorithmSummaryList": [
      {
         "AlgorithmArn": "string",
         "AlgorithmDescription": "string",
         "AlgorithmName": "string",
         "AlgorithmStatus": "string",
         "CreationTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAlgorithms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlgorithmSummaryList](#API_ListAlgorithms_ResponseSyntax) **   <a name="sagemaker-ListAlgorithms-response-AlgorithmSummaryList"></a>
>An array of `AlgorithmSummary` objects, each of which lists an algorithm.
Type: Array of [AlgorithmSummary](API_AlgorithmSummary.md) objects

 ** [NextToken](#API_ListAlgorithms_ResponseSyntax) **   <a name="sagemaker-ListAlgorithms-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListAlgorithms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAlgorithms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAlgorithms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAlgorithms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
