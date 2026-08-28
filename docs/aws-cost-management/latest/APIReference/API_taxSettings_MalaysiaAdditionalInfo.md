---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_MalaysiaAdditionalInfo.html
---

# MalaysiaAdditionalInfo
<a name="API_taxSettings_MalaysiaAdditionalInfo"></a>

 Additional tax information associated with your TRN in Malaysia.

## Contents
<a name="API_taxSettings_MalaysiaAdditionalInfo_Contents"></a>

 ** businessRegistrationNumber **   <a name="awscostmanagement-Type-taxSettings_MalaysiaAdditionalInfo-businessRegistrationNumber"></a>
The tax registration number (TRN) in Malaysia.
For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid MyKad or NRIC number. For business, you must specify a `businessRegistrationNumber` in `MalaysiaAdditionalInfo` with a TIN type and tax identification number. For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.
For business resellers with service codes, you must specify `businessRegistrationNumber`, `taxInformationNumber`, and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, AWS registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.
Type: String
Pattern: `([0-9]{12}|LL[0-9]{5})`
Required: No

 ** serviceTaxCodes **   <a name="awscostmanagement-Type-taxSettings_MalaysiaAdditionalInfo-serviceTaxCodes"></a>
List of service tax codes for your TRN in Malaysia.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `Consultancy | Digital Service And Electronic Medium | IT Services | Training Or Coaching`
Required: No

 ** taxInformationNumber **   <a name="awscostmanagement-Type-taxSettings_MalaysiaAdditionalInfo-taxInformationNumber"></a>
The tax information number in Malaysia.
For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid MyKad or NRIC number. For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.
For business resellers with service codes, you must specify `businessRegistrationNumber`, `taxInformationNumber`, and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, AWS registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.
Type: String
Pattern: `(IG|C|CS|P|D|F|FA|PT|TA|TC|TN|TR|TP|J|LE)[0-9]{10,13}`
Required: No

## See Also
<a name="API_taxSettings_MalaysiaAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/MalaysiaAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/MalaysiaAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/MalaysiaAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
