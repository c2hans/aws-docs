---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingStatisticSummaries.html
---

# GetSamplingStatisticSummaries
<a name="API_GetSamplingStatisticSummaries"></a>

Retrieves information about recent sampling results for all sampling rules.

## Request Syntax
<a name="API_GetSamplingStatisticSummaries_RequestSyntax"></a>

```
POST /SamplingStatisticSummaries HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetSamplingStatisticSummaries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSamplingStatisticSummaries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_GetSamplingStatisticSummaries_RequestSyntax) **   <a name="xray-GetSamplingStatisticSummaries-request-NextToken"></a>
Pagination token.
Type: String
Required: No

## Response Syntax
<a name="API_GetSamplingStatisticSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SamplingStatisticSummaries": [
      {
         "BorrowCount": number,
         "RequestCount": number,
         "RuleName": "string",
         "SampledCount": number,
         "Timestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_GetSamplingStatisticSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSamplingStatisticSummaries_ResponseSyntax) **   <a name="xray-GetSamplingStatisticSummaries-response-NextToken"></a>
Pagination token.
Type: String

 ** [SamplingStatisticSummaries](#API_GetSamplingStatisticSummaries_ResponseSyntax) **   <a name="xray-GetSamplingStatisticSummaries-response-SamplingStatisticSummaries"></a>
Information about the number of requests instrumented for each sampling rule.
Type: Array of [SamplingStatisticSummary](API_SamplingStatisticSummary.md) objects

## Errors
<a name="API_GetSamplingStatisticSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetSamplingStatisticSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetSamplingStatisticSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetSamplingStatisticSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
