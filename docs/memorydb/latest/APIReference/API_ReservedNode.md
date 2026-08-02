---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReservedNode.html
---

# ReservedNode
<a name="API_ReservedNode"></a>

Represents the output of a `PurchaseReservedNodesOffering` operation.

## Contents
<a name="API_ReservedNode_Contents"></a>

 ** ARN **   <a name="MemoryDB-Type-ReservedNode-ARN"></a>
The Amazon Resource Name (ARN) of the reserved node.
Type: String
Required: No

 ** Duration **   <a name="MemoryDB-Type-ReservedNode-Duration"></a>
The duration of the reservation in seconds.
Type: Integer
Required: No

 ** FixedPrice **   <a name="MemoryDB-Type-ReservedNode-FixedPrice"></a>
The fixed price charged for this reserved node.
Type: Double
Required: No

 ** NodeCount **   <a name="MemoryDB-Type-ReservedNode-NodeCount"></a>
The number of nodes that have been reserved.
Type: Integer
Required: No

 ** NodeType **   <a name="MemoryDB-Type-ReservedNode-NodeType"></a>
The node type for the reserved nodes.
Type: String
Required: No

 ** OfferingType **   <a name="MemoryDB-Type-ReservedNode-OfferingType"></a>
The offering type of this reserved node.
Type: String
Required: No

 ** RecurringCharges **   <a name="MemoryDB-Type-ReservedNode-RecurringCharges"></a>
The recurring price charged to run this reserved node.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservationId **   <a name="MemoryDB-Type-ReservedNode-ReservationId"></a>
A customer-specified identifier to track this reservation.
Type: String
Required: No

 ** ReservedNodesOfferingId **   <a name="MemoryDB-Type-ReservedNode-ReservedNodesOfferingId"></a>
The ID of the reserved node offering to purchase.
Type: String
Required: No

 ** StartTime **   <a name="MemoryDB-Type-ReservedNode-StartTime"></a>
The time the reservation started.
Type: Timestamp
Required: No

 ** State **   <a name="MemoryDB-Type-ReservedNode-State"></a>
The state of the reserved node.
Type: String
Required: No

## See Also
<a name="API_ReservedNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ReservedNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ReservedNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ReservedNode)
