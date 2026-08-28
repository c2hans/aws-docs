---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionState.html
---

# EncryptionState
<a name="API_EncryptionState"></a>

A structure that contains the encryption configuration for the policy store and child resources.

This data type is used as a response parameter field for the [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html) operation.

## Contents
<a name="API_EncryptionState_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** default **   <a name="verifiedpermissions-Type-EncryptionState-default"></a>
This is the default encryption state. The policy store is encrypted using an AWS owned key.
Type: Structure
Required: No

 ** kmsEncryptionState **   <a name="verifiedpermissions-Type-EncryptionState-kmsEncryptionState"></a>
The AWS KMS encryption settings currently configured for this policy store to encrypt data with. It contains the customer-managed KMS key, and a user-defined encryption context.
Type: [KmsEncryptionState](API_KmsEncryptionState.md) object
Required: No

## See Also
<a name="API_EncryptionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EncryptionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EncryptionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EncryptionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
