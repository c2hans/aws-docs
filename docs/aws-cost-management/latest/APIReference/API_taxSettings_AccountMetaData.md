---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AccountMetaData.html
---

# AccountMetaData
<a name="API_taxSettings_AccountMetaData"></a>

 The meta data information associated with the account.

## Contents
<a name="API_taxSettings_AccountMetaData_Contents"></a>

 ** accountName **   <a name="awscostmanagement-Type-taxSettings_AccountMetaData-accountName"></a>
 The AWS accounts name.
Type: String
Pattern: `[\s\S]*`
Required: No

 ** address **   <a name="awscostmanagement-Type-taxSettings_AccountMetaData-address"></a>
 The details of the address associated with the TRN information.
Type: [Address](API_taxSettings_Address.md) object
Required: No

 ** addressRoleMap **   <a name="awscostmanagement-Type-taxSettings_AccountMetaData-addressRoleMap"></a>
 Address roles associated with the account containing country code information.
Type: String to [Jurisdiction](API_taxSettings_Jurisdiction.md) object map
Valid Keys: `TaxAddress | BillingAddress | ContactAddress`
Required: No

 ** addressType **   <a name="awscostmanagement-Type-taxSettings_AccountMetaData-addressType"></a>
 The type of address associated with the legal profile.
Type: String
Valid Values: `TaxAddress | BillingAddress | ContactAddress`
Required: No

 ** seller **   <a name="awscostmanagement-Type-taxSettings_AccountMetaData-seller"></a>
 Seller information associated with the account.
Type: String
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_taxSettings_AccountMetaData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/AccountMetaData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/AccountMetaData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/AccountMetaData)
