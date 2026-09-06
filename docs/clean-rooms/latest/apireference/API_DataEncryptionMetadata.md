---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DataEncryptionMetadata.html
---

# DataEncryptionMetadata
<a name="API_DataEncryptionMetadata"></a>

The settings for client-side encryption for cryptographic computing.

## Contents
<a name="API_DataEncryptionMetadata_Contents"></a>

 ** allowCleartext **   <a name="API-Type-DataEncryptionMetadata-allowCleartext"></a>
Indicates whether encrypted tables can contain cleartext data (`TRUE`) or are to cryptographically process every column (`FALSE`).
Type: Boolean
Required: Yes

 ** allowDuplicates **   <a name="API-Type-DataEncryptionMetadata-allowDuplicates"></a>
Indicates whether Fingerprint columns can contain duplicate entries (`TRUE`) or are to contain only non-repeated values (`FALSE`).
Type: Boolean
Required: Yes

 ** allowJoinsOnColumnsWithDifferentNames **   <a name="API-Type-DataEncryptionMetadata-allowJoinsOnColumnsWithDifferentNames"></a>
Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (`TRUE`) or can only be joined on Fingerprint columns of the same name (`FALSE`).
Type: Boolean
Required: Yes

 ** preserveNulls **   <a name="API-Type-DataEncryptionMetadata-preserveNulls"></a>
Indicates whether NULL values are to be copied as NULL to encrypted tables (`TRUE`) or cryptographically processed (`FALSE`).
Type: Boolean
Required: Yes

## See Also
<a name="API_DataEncryptionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DataEncryptionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DataEncryptionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DataEncryptionMetadata)
