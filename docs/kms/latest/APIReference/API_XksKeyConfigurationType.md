---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_XksKeyConfigurationType.html
---

# XksKeyConfigurationType
<a name="API_XksKeyConfigurationType"></a>

Information about the [external key ](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key)that is associated with a KMS key in an external key store.

This element appears in a [CreateKey](API_CreateKey.md) or [DescribeKey](API_DescribeKey.md) response only for a KMS key in an external key store.

The *external key* is a symmetric encryption key that is hosted by an external key manager outside of AWS. When you use the KMS key in an external key store in a cryptographic operation, the cryptographic operation is performed in the external key manager using the specified external key. For more information, see [External key](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key) in the * AWS Key Management Service Developer Guide*.

## Contents
<a name="API_XksKeyConfigurationType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="KMS-Type-XksKeyConfigurationType-Id"></a>
The ID of the external key in its external key manager. This is the ID that the external key store proxy uses to identify the external key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_.]+$`
Required: No

## See Also
<a name="API_XksKeyConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/XksKeyConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/XksKeyConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/XksKeyConfigurationType)
