---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_KmsAccess.html
---

# KmsAccess
<a name="API_KmsAccess"></a>

Configuration for AWS Key Management Service (KMS) access from the ODB network.

## Contents
<a name="API_KmsAccess_Contents"></a>

 ** domainName **   <a name="odb-Type-KmsAccess-domainName"></a>
The domain name for AWS Key Management Service (KMS) access configuration.
Type: String
Required: No

 ** ipv4Addresses **   <a name="odb-Type-KmsAccess-ipv4Addresses"></a>
The IPv4 addresses allowed for AWS Key Management Service (KMS) access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** kmsPolicyDocument **   <a name="odb-Type-KmsAccess-kmsPolicyDocument"></a>
The AWS Key Management Service (KMS) policy document that defines permissions for key usage.
Type: String
Required: No

 ** status **   <a name="odb-Type-KmsAccess-status"></a>
The current status of the AWS Key Management Service (KMS) access configuration.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: No

## See Also
<a name="API_KmsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/KmsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/KmsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/KmsAccess)
