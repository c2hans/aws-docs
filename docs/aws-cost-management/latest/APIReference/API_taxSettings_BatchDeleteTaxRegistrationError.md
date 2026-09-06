---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchDeleteTaxRegistrationError.html
---

# BatchDeleteTaxRegistrationError
<a name="API_taxSettings_BatchDeleteTaxRegistrationError"></a>

 The error object for representing failures in the `BatchDeleteTaxRegistration` operation.

## Contents
<a name="API_taxSettings_BatchDeleteTaxRegistrationError_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-taxSettings_BatchDeleteTaxRegistrationError-accountId"></a>
 The unique account identifier for the account whose tax registration couldn't be deleted during the `BatchDeleteTaxRegistration` operation.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** message **   <a name="awscostmanagement-Type-taxSettings_BatchDeleteTaxRegistrationError-message"></a>
 The error message for an individual failure in the `BatchDeleteTaxRegistration` operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: Yes

 ** code **   <a name="awscostmanagement-Type-taxSettings_BatchDeleteTaxRegistrationError-code"></a>
 The error code for an individual failure in BatchDeleteTaxRegistration operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_taxSettings_BatchDeleteTaxRegistrationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/BatchDeleteTaxRegistrationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/BatchDeleteTaxRegistrationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/BatchDeleteTaxRegistrationError)
