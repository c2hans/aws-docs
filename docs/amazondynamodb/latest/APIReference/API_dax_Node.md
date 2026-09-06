---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Node.html
---

# Node
<a name="API_dax_Node"></a>

Represents an individual node within a DAX cluster.

## Contents
<a name="API_dax_Node_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityZone **   <a name="DDB-Type-dax_Node-AvailabilityZone"></a>
The Availability Zone (AZ) in which the node has been deployed.
Type: String
Required: No

 ** Endpoint **   <a name="DDB-Type-dax_Node-Endpoint"></a>
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
Type: [Endpoint](API_dax_Endpoint.md) object
Required: No

 ** NodeCreateTime **   <a name="DDB-Type-dax_Node-NodeCreateTime"></a>
The date and time (in UNIX epoch format) when the node was launched.
Type: Timestamp
Required: No

 ** NodeId **   <a name="DDB-Type-dax_Node-NodeId"></a>
A system-generated identifier for the node.
Type: String
Required: No

 ** NodeStatus **   <a name="DDB-Type-dax_Node-NodeStatus"></a>
The current status of the node. For example: `available`.
Type: String
Required: No

 ** ParameterGroupStatus **   <a name="DDB-Type-dax_Node-ParameterGroupStatus"></a>
The status of the parameter group associated with this node. For example, `in-sync`.
Type: String
Required: No

## See Also
<a name="API_dax_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/Node)
