---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeSummary.html
---

# NodeSummary
<a name="API_NodeSummary"></a>

A summary of configuration properties for a node.

## Contents
<a name="API_NodeSummary_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-NodeSummary-Arn"></a>
The Amazon Resource Name (ARN) of the node. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** AvailabilityZone **   <a name="ManagedBlockchain-Type-NodeSummary-AvailabilityZone"></a>
The Availability Zone in which the node exists.
Type: String
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-NodeSummary-CreationDate"></a>
The date and time that the node was created.
Type: Timestamp
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-NodeSummary-Id"></a>
The unique identifier of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** InstanceType **   <a name="ManagedBlockchain-Type-NodeSummary-InstanceType"></a>
The EC2 instance type for the node.
Type: String
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-NodeSummary-Status"></a>
The status of the node.
Type: String
Valid Values: `CREATING | AVAILABLE | UNHEALTHY | CREATE_FAILED | UPDATING | DELETING | DELETED | FAILED | INACCESSIBLE_ENCRYPTION_KEY`
Required: No

## See Also
<a name="API_NodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/NodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/NodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/NodeSummary)
