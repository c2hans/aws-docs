---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCards.html
---

# ListModelCards
<a name="API_ListModelCards"></a>

List existing model cards.

## Request Syntax
<a name="API_ListModelCards_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "ModelCardStatus": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelCards_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-CreationTimeAfter"></a>
Only list model cards that were created after the time specified.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-CreationTimeBefore"></a>
Only list model cards that were created before the time specified.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-MaxResults"></a>
The maximum number of model cards to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModelCardStatus](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-ModelCardStatus"></a>
Only list model cards with the specified approval status.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

 ** [NameContains](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-NameContains"></a>
Only list model cards with names that contain the specified string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-NextToken"></a>
If the response to a previous `ListModelCards` request was truncated, the response includes a `NextToken`. To retrieve the next set of model cards, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-SortBy"></a>
Sort model cards by either name or creation time. Sorts by creation time by default.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelCards_RequestSyntax) **   <a name="sagemaker-ListModelCards-request-SortOrder"></a>
Sort model cards by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelCards_ResponseSyntax"></a>

```
{
   "ModelCardSummaries": [
      {
         "CreationTime": number,
         "LastModifiedTime": number,
         "ModelCardArn": "string",
         "ModelCardName": "string",
         "ModelCardStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelCards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardSummaries](#API_ListModelCards_ResponseSyntax) **   <a name="sagemaker-ListModelCards-response-ModelCardSummaries"></a>
The summaries of the listed model cards.
Type: Array of [ModelCardSummary](API_ModelCardSummary.md) objects

 ** [NextToken](#API_ListModelCards_ResponseSyntax) **   <a name="sagemaker-ListModelCards-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of model cards, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelCards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelCards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelCards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelCards)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
