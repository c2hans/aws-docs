---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

Represents an individual node within a cluster. Each node runs its own instance of the cluster's protocol-compliant caching software.

## Contents
<a name="API_Node_Contents"></a>

 ** AvailabilityZone **   <a name="MemoryDB-Type-Node-AvailabilityZone"></a>
The Availability Zone in which the node resides
Type: String
Required: No

 ** CreateTime **   <a name="MemoryDB-Type-Node-CreateTime"></a>
The date and time when the node was created.
Type: Timestamp
Required: No

 ** Endpoint **   <a name="MemoryDB-Type-Node-Endpoint"></a>
The hostname for connecting to this node.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Name **   <a name="MemoryDB-Type-Node-Name"></a>
The node identifier. A node name is a numeric identifier (0001, 0002, etc.). The combination of cluster name, shard name and node name uniquely identifies every node used in a customer's Amazon account.
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-Node-Status"></a>
The status of the service update on the node
Type: String
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
