---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchPutTaxRegistrationError.html
---

# BatchPutTaxRegistrationError
<a name="API_taxSettings_BatchPutTaxRegistrationError"></a>

 The error object for representing failures in the `BatchPutTaxRegistration` operation.

## Contents
<a name="API_taxSettings_BatchPutTaxRegistrationError_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-taxSettings_BatchPutTaxRegistrationError-accountId"></a>
 The unique account identifier for the account that the tax registration couldn't be added, or updated during the `BatchPutTaxRegistration` operation.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** message **   <a name="awscostmanagement-Type-taxSettings_BatchPutTaxRegistrationError-message"></a>
 The error message for an individual failure in the `BatchPutTaxRegistration` operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: Yes

 ** code **   <a name="awscostmanagement-Type-taxSettings_BatchPutTaxRegistrationError-code"></a>
 The error code for an individual failure in the `BatchPutTaxRegistration` operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_taxSettings_BatchPutTaxRegistrationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/BatchPutTaxRegistrationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/BatchPutTaxRegistrationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/BatchPutTaxRegistrationError)
