---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationStatusReason.html
---

# TaxRegistrationStatusReason
<a name="API_taxSettings_TaxRegistrationStatusReason"></a>

The reason that a tax registration was rejected.

## Contents
<a name="API_taxSettings_TaxRegistrationStatusReason_Contents"></a>

 ** code **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationStatusReason-code"></a>
A code that identifies the rejection reason (for example, `NIT_MISMATCH` or `ENCRYPTED_PDF`). If the reason isn't recognized, the value is `OTHER`. New codes might be added in the future.
Type: String
Pattern: `[\s\S]*`
Required: No

 ** message **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationStatusReason-message"></a>
A description of the rejection reason in English.
Type: String
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_taxSettings_TaxRegistrationStatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxRegistrationStatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxRegistrationStatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxRegistrationStatusReason)
