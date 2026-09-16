---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodesOfferings.html
---

# DescribeReservedNodesOfferings
<a name="API_DescribeReservedNodesOfferings"></a>

Lists available reserved node offerings.

## Request Syntax
<a name="API_DescribeReservedNodesOfferings_RequestSyntax"></a>

```
{
   "Duration": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "NodeType": "{{string}}",
   "OfferingType": "{{string}}",
   "ReservedNodesOfferingId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReservedNodesOfferings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Duration](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-Duration"></a>
Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.
Type: String
Required: No

 ** [MaxResults](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-NextToken"></a>
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.
Type: String
Required: No

 ** [NodeType](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-NodeType"></a>
The node type for the reserved nodes. For more information, see [Supported node types](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported).
Type: String
Required: No

 ** [OfferingType](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-OfferingType"></a>
The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "All Upfront"\|"Partial Upfront"\| "No Upfront"
Type: String
Required: No

 ** [ReservedNodesOfferingId](#API_DescribeReservedNodesOfferings_RequestSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-request-ReservedNodesOfferingId"></a>
The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeReservedNodesOfferings_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ReservedNodesOfferings": [
      {
         "Duration": number,
         "FixedPrice": number,
         "NodeType": "string",
         "OfferingType": "string",
         "RecurringCharges": [
            {
               "RecurringChargeAmount": number,
               "RecurringChargeFrequency": "string"
            }
         ],
         "ReservedNodesOfferingId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReservedNodesOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeReservedNodesOfferings_ResponseSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-response-NextToken"></a>
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.
Type: String

 ** [ReservedNodesOfferings](#API_DescribeReservedNodesOfferings_ResponseSyntax) **   <a name="MemoryDB-DescribeReservedNodesOfferings-response-ReservedNodesOfferings"></a>
Lists available reserved node offerings.
Type: Array of [ReservedNodesOffering](API_ReservedNodesOffering.md) objects

## Errors
<a name="API_DescribeReservedNodesOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ReservedNodesOfferingNotFoundFault **
The requested node offering does not exist.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeReservedNodesOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeReservedNodesOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeReservedNodesOfferings)
