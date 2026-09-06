---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodes.html
---

# DescribeReservedNodes
<a name="API_DescribeReservedNodes"></a>

Returns information about reserved nodes for this account, or about a specified reserved node.

## Request Syntax
<a name="API_DescribeReservedNodes_RequestSyntax"></a>

```
{
   "Duration": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "NodeType": "{{string}}",
   "OfferingType": "{{string}}",
   "ReservationId": "{{string}}",
   "ReservedNodesOfferingId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReservedNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Duration](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-Duration"></a>
The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.
Type: String
Required: No

 ** [MaxResults](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-NextToken"></a>
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.
Type: String
Required: No

 ** [NodeType](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-NodeType"></a>
The node type filter value. Use this parameter to show only those reservations matching the specified node type. For more information, see [Supported node types](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported).
Type: String
Required: No

 ** [OfferingType](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-OfferingType"></a>
The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "All Upfront"\|"Partial Upfront"\| "No Upfront"
Type: String
Required: No

 ** [ReservationId](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-ReservationId"></a>
The reserved node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.
Type: String
Required: No

 ** [ReservedNodesOfferingId](#API_DescribeReservedNodes_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodes-request-ReservedNodesOfferingId"></a>
The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeReservedNodes_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ReservedNodes": [
      {
         "ARN": "string",
         "Duration": number,
         "FixedPrice": number,
         "NodeCount": number,
         "NodeType": "string",
         "OfferingType": "string",
         "RecurringCharges": [
            {
               "RecurringChargeAmount": number,
               "RecurringChargeFrequency": "string"
            }
         ],
         "ReservationId": "string",
         "ReservedNodesOfferingId": "string",
         "StartTime": number,
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReservedNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeReservedNodes_ResponseSyntax) **   <a name="MemoryDB-DescribeReservedNodes-response-NextToken"></a>
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.
Type: String

 ** [ReservedNodes](#API_DescribeReservedNodes_ResponseSyntax) **   <a name="MemoryDB-DescribeReservedNodes-response-ReservedNodes"></a>
Returns information about reserved nodes for this account, or about a specified reserved node.
Type: Array of [ReservedNode](API_ReservedNode.md) objects

## Errors
<a name="API_DescribeReservedNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ReservedNodeNotFoundFault **
The requested node does not exist.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeReservedNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeReservedNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeReservedNodes)
