---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListDataQualityStatisticAnnotations.html
---

# ListDataQualityStatisticAnnotations
<a name="API_ListDataQualityStatisticAnnotations"></a>

Retrieve annotations for a data quality statistic.

## Request Syntax
<a name="API_ListDataQualityStatisticAnnotations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProfileId": "{{string}}",
   "StatisticId": "{{string}}",
   "TimestampFilter": {
      "RecordedAfter": {{number}},
      "RecordedBefore": {{number}}
   }
}
```

## Request Parameters
<a name="API_ListDataQualityStatisticAnnotations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDataQualityStatisticAnnotations_RequestSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-request-MaxResults"></a>
The maximum number of results to return in this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataQualityStatisticAnnotations_RequestSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-request-NextToken"></a>
A pagination token to retrieve the next set of results.
Type: String
Required: No

 ** [ProfileId](#API_ListDataQualityStatisticAnnotations_RequestSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-request-ProfileId"></a>
The Profile ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [StatisticId](#API_ListDataQualityStatisticAnnotations_RequestSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-request-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TimestampFilter](#API_ListDataQualityStatisticAnnotations_RequestSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-request-TimestampFilter"></a>
A timestamp filter.
Type: [TimestampFilter](API_TimestampFilter.md) object
Required: No

## Response Syntax
<a name="API_ListDataQualityStatisticAnnotations_ResponseSyntax"></a>

```
{
   "Annotations": [
      {
         "InclusionAnnotation": {
            "LastModifiedOn": number,
            "Value": "string"
         },
         "ProfileId": "string",
         "StatisticId": "string",
         "StatisticRecordedOn": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataQualityStatisticAnnotations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Annotations](#API_ListDataQualityStatisticAnnotations_ResponseSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-response-Annotations"></a>
A list of `StatisticAnnotation` applied to the Statistic
Type: Array of [StatisticAnnotation](API_StatisticAnnotation.md) objects

 ** [NextToken](#API_ListDataQualityStatisticAnnotations_ResponseSyntax) **   <a name="Glue-ListDataQualityStatisticAnnotations-response-NextToken"></a>
A pagination token to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListDataQualityStatisticAnnotations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListDataQualityStatisticAnnotations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListDataQualityStatisticAnnotations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListDataQualityStatisticAnnotations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
