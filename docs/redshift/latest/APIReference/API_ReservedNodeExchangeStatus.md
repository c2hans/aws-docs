---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ReservedNodeExchangeStatus.html
---

# ReservedNodeExchangeStatus
<a name="API_ReservedNodeExchangeStatus"></a>

Reserved-node status details, such as the source reserved-node identifier, the target reserved-node identifier, the node type, the node count, and other details.

## Contents
<a name="API_ReservedNodeExchangeStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RequestTime **
A date and time that indicate when the reserved-node exchange was requested.
Type: Timestamp
Required: No

 ** ReservedNodeExchangeRequestId **
The identifier of the reserved-node exchange request.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceReservedNodeCount **
The source reserved-node count in the cluster.
Type: Integer
Required: No

 ** SourceReservedNodeId **
The identifier of the source reserved node.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceReservedNodeType **
The source reserved-node type, for example ra3.4xlarge.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Status **
The status of the reserved-node exchange request. Statuses include in-progress and requested.
Type: String
Valid Values: `REQUESTED | PENDING | IN_PROGRESS | RETRYING | SUCCEEDED | FAILED`
Required: No

 ** TargetReservedNodeCount **
The count of target reserved nodes in the cluster.
Type: Integer
Required: No

 ** TargetReservedNodeOfferingId **
The identifier of the target reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TargetReservedNodeType **
The node type of the target reserved node, for example ra3.4xlarge.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_ReservedNodeExchangeStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ReservedNodeExchangeStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ReservedNodeExchangeStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ReservedNodeExchangeStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
