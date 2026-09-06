---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_Checksum.html
---

# Checksum
<a name="API_Checksum"></a>

A checksum structure used to verify data integrity.

## Contents
<a name="API_Checksum_Contents"></a>

 ** encryptionAlgorithm **   <a name="mgn-Type-Checksum-encryptionAlgorithm"></a>
The encryption algorithm used to generate the checksum.
Type: String
Valid Values: `SHA256`
Required: No

 ** hash **   <a name="mgn-Type-Checksum-hash"></a>
The hash value of the checksum.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[A-Za-z0-9+/=]{32}`
Required: No

## See Also
<a name="API_Checksum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/Checksum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/Checksum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/Checksum)
