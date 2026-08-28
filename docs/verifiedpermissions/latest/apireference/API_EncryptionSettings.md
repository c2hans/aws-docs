---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionSettings.html
---

# EncryptionSettings
<a name="API_EncryptionSettings"></a>

A structure that contains the encryption configuration for the policy store and child resources.

This data type is used as a request parameter in the [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html) operation.

## Contents
<a name="API_EncryptionSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** default **   <a name="verifiedpermissions-Type-EncryptionSettings-default"></a>
This is the default encryption setting. The policy store uses an AWS owned key for encrypting data.
Type: Structure
Required: No

 ** kmsEncryptionSettings **   <a name="verifiedpermissions-Type-EncryptionSettings-kmsEncryptionSettings"></a>
The AWS KMS encryption settings for this policy store to encrypt data with. It will contain the customer-managed KMS key, and a user-defined encryption context.
Type: [KmsEncryptionSettings](API_KmsEncryptionSettings.md) object
Required: No

## See Also
<a name="API_EncryptionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EncryptionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EncryptionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EncryptionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
