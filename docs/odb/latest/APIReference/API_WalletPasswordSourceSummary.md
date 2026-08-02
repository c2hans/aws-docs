---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_WalletPasswordSourceSummary.html
---

# WalletPasswordSourceSummary
<a name="API_WalletPasswordSourceSummary"></a>

A summary of the password source configuration for an Autonomous Database wallet.

## Contents
<a name="API_WalletPasswordSourceSummary_Contents"></a>

 ** passwordSource **   <a name="odb-Type-WalletPasswordSourceSummary-passwordSource"></a>
The source of the password for the Autonomous Database wallet.
Type: String
Valid Values: `CUSTOMER_MANAGED_AWS_SECRET | API_REQUEST_PARAMETER`
Required: No

 ** passwordSourceConfiguration **   <a name="odb-Type-WalletPasswordSourceSummary-passwordSourceConfiguration"></a>
The configuration of the password source for the Autonomous Database wallet.
Type: [WalletPasswordSourceConfiguration](API_WalletPasswordSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_WalletPasswordSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/WalletPasswordSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/WalletPasswordSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/WalletPasswordSourceSummary)
