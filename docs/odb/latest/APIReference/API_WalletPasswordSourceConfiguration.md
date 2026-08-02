---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_WalletPasswordSourceConfiguration.html
---

# WalletPasswordSourceConfiguration
<a name="API_WalletPasswordSourceConfiguration"></a>

The configuration of the wallet password source. This is a union, so only one of the following members can be specified.

## Contents
<a name="API_WalletPasswordSourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customerManagedAwsSecret **   <a name="odb-Type-WalletPasswordSourceConfiguration-customerManagedAwsSecret"></a>
The configuration for a customer-managed AWS Secrets Manager secret used as the wallet password source.
Type: [CustomerManagedAwsSecretConfiguration](API_CustomerManagedAwsSecretConfiguration.md) object
Required: No

## See Also
<a name="API_WalletPasswordSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/WalletPasswordSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/WalletPasswordSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/WalletPasswordSourceConfiguration)
