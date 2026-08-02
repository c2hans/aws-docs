---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ListConformancePackComplianceScores.html
---

# ListConformancePackComplianceScores
<a name="API_ListConformancePackComplianceScores"></a>

Returns a list of conformance pack compliance scores. A compliance score is the percentage of the number of compliant rule-resource combinations in a conformance pack compared to the number of total possible rule-resource combinations in the conformance pack. This metric provides you with a high-level view of the compliance state of your conformance packs. You can use it to identify, investigate, and understand the level of compliance in your conformance packs.

**Note**
Conformance packs with no evaluation results will have a compliance score of `INSUFFICIENT_DATA`.

## Request Syntax
<a name="API_ListConformancePackComplianceScores_RequestSyntax"></a>

```
{
   "Filters": {
      "ConformancePackNames": [ "{{string}}" ]
   },
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConformancePackComplianceScores_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListConformancePackComplianceScores_RequestSyntax) **   <a name="config-ListConformancePackComplianceScores-request-Filters"></a>
Filters the results based on the `ConformancePackComplianceScoresFilters`.
Type: [ConformancePackComplianceScoresFilters](API_ConformancePackComplianceScoresFilters.md) object
Required: No

 ** [Limit](#API_ListConformancePackComplianceScores_RequestSyntax) **   <a name="config-ListConformancePackComplianceScores-request-Limit"></a>
The maximum number of conformance pack compliance scores returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListConformancePackComplianceScores_RequestSyntax) **   <a name="config-ListConformancePackComplianceScores-request-NextToken"></a>
The `nextToken` string in a prior request that you can use to get the paginated response for the next set of conformance pack compliance scores.
Type: String
Required: No

 ** [SortBy](#API_ListConformancePackComplianceScores_RequestSyntax) **   <a name="config-ListConformancePackComplianceScores-request-SortBy"></a>
Sorts your conformance pack compliance scores in either ascending or descending order, depending on `SortOrder`.
By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Enter `SCORE`, to sort conformance pack compliance scores by the numerical value of the compliance score.
Type: String
Valid Values: `SCORE`
Required: No

 ** [SortOrder](#API_ListConformancePackComplianceScores_RequestSyntax) **   <a name="config-ListConformancePackComplianceScores-request-SortOrder"></a>
Determines the order in which conformance pack compliance scores are sorted. Either in ascending or descending order.
By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Conformance pack compliance scores are sorted in reverse alphabetical order if you enter `DESCENDING`.
You can sort conformance pack compliance scores by the numerical value of the compliance score by entering `SCORE` in the `SortBy` action. When compliance scores are sorted by `SCORE`, conformance packs with a compliance score of `INSUFFICIENT_DATA` will be last when sorting by ascending order and first when sorting by descending order.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListConformancePackComplianceScores_ResponseSyntax"></a>

```
{
   "ConformancePackComplianceScores": [
      {
         "ConformancePackName": "string",
         "LastUpdatedTime": number,
         "Score": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConformancePackComplianceScores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackComplianceScores](#API_ListConformancePackComplianceScores_ResponseSyntax) **   <a name="config-ListConformancePackComplianceScores-response-ConformancePackComplianceScores"></a>
A list of `ConformancePackComplianceScore` objects.
Type: Array of [ConformancePackComplianceScore](API_ConformancePackComplianceScore.md) objects

 ** [NextToken](#API_ListConformancePackComplianceScores_ResponseSyntax) **   <a name="config-ListConformancePackComplianceScores-response-NextToken"></a>
The `nextToken` string that you can use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_ListConformancePackComplianceScores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListConformancePackComplianceScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/ListConformancePackComplianceScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ListConformancePackComplianceScores)
