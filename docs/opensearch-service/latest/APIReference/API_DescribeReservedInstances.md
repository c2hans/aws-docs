---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstances.html
---

# DescribeReservedInstances
<a name="API_DescribeReservedInstances"></a>

Describes the Amazon OpenSearch Service instances that you have reserved in a given Region. For more information, see [Reserved Instances in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html).

## Request Syntax
<a name="API_DescribeReservedInstances_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/reservedInstances?maxResults={{MaxResults}}&nextToken={{NextToken}}&reservationId={{ReservedInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeReservedInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_DescribeReservedInstances_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstances-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_DescribeReservedInstances_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstances-request-uri-NextToken"></a>
If your initial `DescribeReservedInstances` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `DescribeReservedInstances` operations, which returns results in the next page.

 ** [ReservedInstanceId](#API_DescribeReservedInstances_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstances-request-uri-ReservedInstanceId"></a>
The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

## Request Body
<a name="API_DescribeReservedInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeReservedInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ReservedInstances": [
      {
         "BillingSubscriptionId": number,
         "CurrencyCode": "string",
         "Duration": number,
         "FixedPrice": number,
         "InstanceCount": number,
         "InstanceType": "string",
         "PaymentOption": "string",
         "RecurringCharges": [
            {
               "RecurringChargeAmount": number,
               "RecurringChargeFrequency": "string"
            }
         ],
         "ReservationName": "string",
         "ReservedInstanceId": "string",
         "ReservedInstanceOfferingId": "string",
         "StartTime": number,
         "State": "string",
         "UsagePrice": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReservedInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeReservedInstances_ResponseSyntax) **   <a name="opensearchservice-DescribeReservedInstances-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [ReservedInstances](#API_DescribeReservedInstances_ResponseSyntax) **   <a name="opensearchservice-DescribeReservedInstances-response-ReservedInstances"></a>
List of Reserved Instances in the current Region.
Type: Array of [ReservedInstance](API_ReservedInstance.md) objects

## Errors
<a name="API_DescribeReservedInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReservedInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeReservedInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeReservedInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
