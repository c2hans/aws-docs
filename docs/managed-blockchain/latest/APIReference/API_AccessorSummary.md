---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_AccessorSummary.html
---

# AccessorSummary
<a name="API_AccessorSummary"></a>

A summary of accessor properties.

## Contents
<a name="API_AccessorSummary_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-AccessorSummary-Arn"></a>
The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-AccessorSummary-CreationDate"></a>
The creation date and time of the accessor.
Type: Timestamp
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-AccessorSummary-Id"></a>
The unique identifier of the accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NetworkType **   <a name="ManagedBlockchain-Type-AccessorSummary-NetworkType"></a>
The blockchain network that the Accessor token is created for.
Type: String
Valid Values: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-AccessorSummary-Status"></a>
The current status of the accessor.
Type: String
Valid Values: `AVAILABLE | PENDING_DELETION | DELETED`
Required: No

 ** Type **   <a name="ManagedBlockchain-Type-AccessorSummary-Type"></a>
The type of the accessor.
Currently accessor type is restricted to `BILLING_TOKEN`.
Type: String
Valid Values: `BILLING_TOKEN`
Required: No

## See Also
<a name="API_AccessorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/AccessorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/AccessorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/AccessorSummary)
