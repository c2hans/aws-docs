---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ListResourceEvaluations.html
---

# ListResourceEvaluations
<a name="API_ListResourceEvaluations"></a>

Returns a list of proactive resource evaluations.

## Request Syntax
<a name="API_ListResourceEvaluations_RequestSyntax"></a>

```
{
   "Filters": {
      "EvaluationContextIdentifier": "{{string}}",
      "EvaluationMode": "{{string}}",
      "TimeWindow": {
         "EndTime": {{number}},
         "StartTime": {{number}}
      }
   },
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceEvaluations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListResourceEvaluations_RequestSyntax) **   <a name="config-ListResourceEvaluations-request-Filters"></a>
Returns a `ResourceEvaluationFilters` object.
Type: [ResourceEvaluationFilters](API_ResourceEvaluationFilters.md) object
Required: No

 ** [Limit](#API_ListResourceEvaluations_RequestSyntax) **   <a name="config-ListResourceEvaluations-request-Limit"></a>
The maximum number of evaluations returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResourceEvaluations_RequestSyntax) **   <a name="config-ListResourceEvaluations-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_ListResourceEvaluations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceEvaluations": [
      {
         "EvaluationMode": "string",
         "EvaluationStartTimestamp": number,
         "ResourceEvaluationId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceEvaluations_ResponseSyntax) **   <a name="config-ListResourceEvaluations-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [ResourceEvaluations](#API_ListResourceEvaluations_ResponseSyntax) **   <a name="config-ListResourceEvaluations-response-ResourceEvaluations"></a>
Returns a `ResourceEvaluations` object.
Type: Array of [ResourceEvaluation](API_ResourceEvaluation.md) objects

## Errors
<a name="API_ListResourceEvaluations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** InvalidTimeRangeException **
The specified time range is not valid. The earlier time is not chronologically before the later time.
HTTP Status Code: 400

## See Also
<a name="API_ListResourceEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/ListResourceEvaluations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ListResourceEvaluations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
