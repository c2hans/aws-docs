---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTagBackfillHistory.html
---

# ListCostAllocationTagBackfillHistory
<a name="API_ListCostAllocationTagBackfillHistory"></a>

 Retrieves a list of your historical cost allocation tag backfill requests.

## Request Syntax
<a name="API_ListCostAllocationTagBackfillHistory_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCostAllocationTagBackfillHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCostAllocationTagBackfillHistory_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTagBackfillHistory-request-MaxResults"></a>
 The maximum number of objects that are returned for this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCostAllocationTagBackfillHistory_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTagBackfillHistory-request-NextToken"></a>
 The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_ListCostAllocationTagBackfillHistory_ResponseSyntax"></a>

```
{
   "BackfillRequests": [
      {
         "BackfillFrom": "string",
         "BackfillStatus": "string",
         "CompletedAt": "string",
         "LastUpdatedAt": "string",
         "RequestedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCostAllocationTagBackfillHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackfillRequests](#API_ListCostAllocationTagBackfillHistory_ResponseSyntax) **   <a name="awscostmanagement-ListCostAllocationTagBackfillHistory-response-BackfillRequests"></a>
 The list of historical cost allocation tag backfill requests.
Type: Array of [CostAllocationTagBackfillRequest](API_CostAllocationTagBackfillRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [NextToken](#API_ListCostAllocationTagBackfillHistory_ResponseSyntax) **   <a name="awscostmanagement-ListCostAllocationTagBackfillHistory-response-NextToken"></a>
 The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListCostAllocationTagBackfillHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_ListCostAllocationTagBackfillHistory_Examples"></a>

The following are sample requests and responses of the `ListCostAllocationTagBackfillHistory` operations.

### Example 1: List the latest cost allocation tag backfill request
<a name="API_ListCostAllocationTagBackfillHistory_Example_1"></a>

This example illustrates one usage of ListCostAllocationTagBackfillHistory.

#### Sample Request
<a name="API_ListCostAllocationTagBackfillHistory_Example_1_Request"></a>

```
{
    "MaxResults": 1
}
```

#### Sample Response
<a name="API_ListCostAllocationTagBackfillHistory_Example_1_Response"></a>

```
{
    "BackfillRequests": [
        {
            "BackfillFrom":"2024-02-01T00:00:00Z",
            "BackfillStatus":"PROCESSING",
            "RequestedAt":"2024-03-01T09:16:23Z",
            "LastUpdatedAt":"2024-03-01T09:16:23Z"
        }
    ],
    "NextToken": null
}
```

## See Also
<a name="API_ListCostAllocationTagBackfillHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListCostAllocationTagBackfillHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListCostAllocationTagBackfillHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
