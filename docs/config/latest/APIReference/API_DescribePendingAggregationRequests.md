---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribePendingAggregationRequests.html
---

# DescribePendingAggregationRequests
<a name="API_DescribePendingAggregationRequests"></a>

Returns a list of all pending aggregation requests.

## Request Syntax
<a name="API_DescribePendingAggregationRequests_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePendingAggregationRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribePendingAggregationRequests_RequestSyntax) **   <a name="config-DescribePendingAggregationRequests-request-Limit"></a>
The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [NextToken](#API_DescribePendingAggregationRequests_RequestSyntax) **   <a name="config-DescribePendingAggregationRequests-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribePendingAggregationRequests_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PendingAggregationRequests": [
      {
         "RequesterAccountId": "string",
         "RequesterAwsRegion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribePendingAggregationRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribePendingAggregationRequests_ResponseSyntax) **   <a name="config-DescribePendingAggregationRequests-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [PendingAggregationRequests](#API_DescribePendingAggregationRequests_ResponseSyntax) **   <a name="config-DescribePendingAggregationRequests-response-PendingAggregationRequests"></a>
Returns a PendingAggregationRequests object.
Type: Array of [PendingAggregationRequest](API_PendingAggregationRequest.md) objects

## Errors
<a name="API_DescribePendingAggregationRequests_Errors"></a>

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
<a name="API_DescribePendingAggregationRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribePendingAggregationRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribePendingAggregationRequests)
