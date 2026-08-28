---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_VerificationDetails.html
---

# VerificationDetails
<a name="API_taxSettings_VerificationDetails"></a>

Required information to verify your TRN.

## Contents
<a name="API_taxSettings_VerificationDetails_Contents"></a>

 ** dateOfBirth **   <a name="awscostmanagement-Type-taxSettings_VerificationDetails-dateOfBirth"></a>
Date of birth to verify your submitted TRN. Use the `YYYY-MM-DD` format.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))`
Required: No

 ** taxRegistrationDocuments **   <a name="awscostmanagement-Type-taxSettings_VerificationDetails-taxRegistrationDocuments"></a>
The tax registration document, which is required for specific countries such as Bangladesh, Kenya, South Korea and Spain.
Type: Array of [TaxRegistrationDocument](API_taxSettings_TaxRegistrationDocument.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_taxSettings_VerificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/VerificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/VerificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/VerificationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
