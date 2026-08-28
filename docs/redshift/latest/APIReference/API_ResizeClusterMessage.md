---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ResizeClusterMessage.html
---

# ResizeClusterMessage
<a name="API_ResizeClusterMessage"></a>

Describes a resize cluster operation. For example, a scheduled action to run the `ResizeCluster` API operation.

## Contents
<a name="API_ResizeClusterMessage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterIdentifier **
The unique identifier for the cluster to resize.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: Yes

 ** Classic **
A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to `false`, the resize type is elastic.
Type: Boolean
Required: No

 ** ClusterType **
The new cluster type for the specified cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NodeType **
The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NumberOfNodes **
The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.
Type: Integer
Required: No

 ** ReservedNodeId **
The identifier of the reserved node.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TargetReservedNodeOfferingId **
The identifier of the target reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_ResizeClusterMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ResizeClusterMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ResizeClusterMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ResizeClusterMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
