---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberSummary.html
---

# MemberSummary
<a name="API_MemberSummary"></a>

A summary of configuration properties for a member.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_MemberSummary_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-MemberSummary-Arn"></a>
The Amazon Resource Name (ARN) of the member. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-MemberSummary-CreationDate"></a>
The date and time that the member was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-MemberSummary-Description"></a>
An optional description of the member.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-MemberSummary-Id"></a>
The unique identifier of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** IsOwned **   <a name="ManagedBlockchain-Type-MemberSummary-IsOwned"></a>
An indicator of whether the member is owned by your AWS account or a different AWS account.
Type: Boolean
Required: No

 ** Name **   <a name="ManagedBlockchain-Type-MemberSummary-Name"></a>
The name of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-MemberSummary-Status"></a>
The status of the member.
+  `CREATING` - The AWS account is in the process of creating a member.
+  `AVAILABLE` - The member has been created and can participate in the network.
+  `CREATE_FAILED` - The AWS account attempted to create a member and creation failed.
+  `UPDATING` - The member is in the process of being updated.
+  `DELETING` - The member and all associated resources are in the process of being deleted. Either the AWS account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
+  `DELETED` - The member can no longer participate on the network and all associated resources are deleted. Either the AWS account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
+  `INACCESSIBLE_ENCRYPTION_KEY` - The member is impaired and might not function as expected because it cannot access the specified customer managed key in AWS Key Management Service (AWS KMS) for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.

  The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the member resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | UPDATING | DELETING | DELETED | INACCESSIBLE_ENCRYPTION_KEY`
Required: No

## See Also
<a name="API_MemberSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/MemberSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/MemberSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/MemberSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
