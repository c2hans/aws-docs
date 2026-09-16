---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListFindingAggregators.html
---

# ListFindingAggregators
<a name="API_ListFindingAggregators"></a>

If cross-Region aggregation is enabled, then `ListFindingAggregators` returns the Amazon Resource Name (ARN) of the finding aggregator. You can run this operation from any AWS Region.

## Request Syntax
<a name="API_ListFindingAggregators_RequestSyntax"></a>

```
GET /findingAggregator/list?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFindingAggregators_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListFindingAggregators_RequestSyntax) **   <a name="securityhub-ListFindingAggregators-request-uri-MaxResults"></a>
The maximum number of results to return. This operation currently only returns a single result.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListFindingAggregators_RequestSyntax) **   <a name="securityhub-ListFindingAggregators-request-uri-NextToken"></a>
The token returned with the previous set of results. Identifies the next set of results to return.

## Request Body
<a name="API_ListFindingAggregators_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFindingAggregators_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FindingAggregators": [
      {
         "FindingAggregatorArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFindingAggregators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FindingAggregators](#API_ListFindingAggregators_ResponseSyntax) **   <a name="securityhub-ListFindingAggregators-response-FindingAggregators"></a>
The list of finding aggregators. This operation currently only returns a single result.
Type: Array of [FindingAggregator](API_FindingAggregator.md) objects

 ** [NextToken](#API_ListFindingAggregators_ResponseSyntax) **   <a name="securityhub-ListFindingAggregators-response-NextToken"></a>
If there are more results, this is the token to provide in the next call to `ListFindingAggregators`.
This operation currently only returns a single result.
Type: String

## Errors
<a name="API_ListFindingAggregators_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListFindingAggregators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListFindingAggregators)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListFindingAggregators)
