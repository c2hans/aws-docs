---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReservedNodesOffering.html
---

# ReservedNodesOffering
<a name="API_ReservedNodesOffering"></a>

The offering type of this node.

## Contents
<a name="API_ReservedNodesOffering_Contents"></a>

 ** Duration **   <a name="MemoryDB-Type-ReservedNodesOffering-Duration"></a>
The duration of the reservation in seconds.
Type: Integer
Required: No

 ** FixedPrice **   <a name="MemoryDB-Type-ReservedNodesOffering-FixedPrice"></a>
The fixed price charged for this reserved node.
Type: Double
Required: No

 ** NodeType **   <a name="MemoryDB-Type-ReservedNodesOffering-NodeType"></a>
The node type for the reserved nodes. For more information, see [Supported node types](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported).
Type: String
Required: No

 ** OfferingType **   <a name="MemoryDB-Type-ReservedNodesOffering-OfferingType"></a>
The offering type of this reserved node.
Type: String
Required: No

 ** RecurringCharges **   <a name="MemoryDB-Type-ReservedNodesOffering-RecurringCharges"></a>
The recurring price charged to run this reserved node.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservedNodesOfferingId **   <a name="MemoryDB-Type-ReservedNodesOffering-ReservedNodesOfferingId"></a>
The offering identifier.
Type: String
Required: No

## See Also
<a name="API_ReservedNodesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ReservedNodesOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ReservedNodesOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ReservedNodesOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
