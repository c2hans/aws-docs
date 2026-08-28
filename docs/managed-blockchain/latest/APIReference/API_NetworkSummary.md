---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkSummary.html
---

# NetworkSummary
<a name="API_NetworkSummary"></a>

A summary of network configuration properties.

## Contents
<a name="API_NetworkSummary_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-NetworkSummary-Arn"></a>
The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-NetworkSummary-CreationDate"></a>
The date and time that the network was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-NetworkSummary-Description"></a>
An optional description of the network.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** Framework **   <a name="ManagedBlockchain-Type-NetworkSummary-Framework"></a>
The blockchain framework that the network uses.
Type: String
Valid Values: `HYPERLEDGER_FABRIC | ETHEREUM`
Required: No

 ** FrameworkVersion **   <a name="ManagedBlockchain-Type-NetworkSummary-FrameworkVersion"></a>
The version of the blockchain framework that the network uses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-NetworkSummary-Id"></a>
The unique identifier of the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Name **   <a name="ManagedBlockchain-Type-NetworkSummary-Name"></a>
The name of the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-NetworkSummary-Status"></a>
The current status of the network.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | DELETING | DELETED`
Required: No

## See Also
<a name="API_NetworkSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/NetworkSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/NetworkSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/NetworkSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
