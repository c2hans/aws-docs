---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_PurchaseReservedNodesOffering.html
---

# PurchaseReservedNodesOffering
<a name="API_PurchaseReservedNodesOffering"></a>

Allows you to purchase a reserved node offering. Reserved nodes are not eligible for cancellation and are non-refundable.

## Request Syntax
<a name="API_PurchaseReservedNodesOffering_RequestSyntax"></a>

```
{
   "NodeCount": {{number}},
   "ReservationId": "{{string}}",
   "ReservedNodesOfferingId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PurchaseReservedNodesOffering_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NodeCount](#API_PurchaseReservedNodesOffering_RequestSyntax) **   <a name="MemoryDB-PurchaseReservedNodesOffering-request-NodeCount"></a>
The number of node instances to reserve.
Type: Integer
Required: No

 ** [ReservationId](#API_PurchaseReservedNodesOffering_RequestSyntax) **   <a name="MemoryDB-PurchaseReservedNodesOffering-request-ReservationId"></a>
A customer-specified identifier to track this reservation.
Type: String
Required: No

 ** [ReservedNodesOfferingId](#API_PurchaseReservedNodesOffering_RequestSyntax) **   <a name="MemoryDB-PurchaseReservedNodesOffering-request-ReservedNodesOfferingId"></a>
The ID of the reserved node offering to purchase.
Type: String
Required: Yes

 ** [Tags](#API_PurchaseReservedNodesOffering_RequestSyntax) **   <a name="MemoryDB-PurchaseReservedNodesOffering-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_PurchaseReservedNodesOffering_ResponseSyntax"></a>

```
{
   "ReservedNode": {
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
}
```

## Response Elements
<a name="API_PurchaseReservedNodesOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReservedNode](#API_PurchaseReservedNodesOffering_ResponseSyntax) **   <a name="MemoryDB-PurchaseReservedNodesOffering-response-ReservedNode"></a>
Represents the output of a `PurchaseReservedNodesOffering` operation.
Type: [ReservedNode](API_ReservedNode.md) object

## Errors
<a name="API_PurchaseReservedNodesOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ReservedNodeAlreadyExistsFault **
You already have a reservation with the given identifier.
HTTP Status Code: 400

 ** ReservedNodeQuotaExceededFault **
The request cannot be processed because it would exceed the user's node quota.
HTTP Status Code: 400

 ** ReservedNodesOfferingNotFoundFault **
The requested node offering does not exist.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_PurchaseReservedNodesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/PurchaseReservedNodesOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/PurchaseReservedNodesOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
