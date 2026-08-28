---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AccountDetails.html
---

# AccountDetails
<a name="API_taxSettings_AccountDetails"></a>

 An object with your `accountId` and TRN information.

## Contents
<a name="API_taxSettings_AccountDetails_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-taxSettings_AccountDetails-accountId"></a>
List of unique account identifiers.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** accountMetaData **   <a name="awscostmanagement-Type-taxSettings_AccountDetails-accountMetaData"></a>
 The meta data information associated with the account.
Type: [AccountMetaData](API_taxSettings_AccountMetaData.md) object
Required: No

 ** taxInheritanceDetails **   <a name="awscostmanagement-Type-taxSettings_AccountDetails-taxInheritanceDetails"></a>
 Tax inheritance information associated with the account.
Type: [TaxInheritanceDetails](API_taxSettings_TaxInheritanceDetails.md) object
Required: No

 ** taxRegistration **   <a name="awscostmanagement-Type-taxSettings_AccountDetails-taxRegistration"></a>
Your TRN information. Instead of having full legal address, here TRN information will have jurisdiction details (for example, country code and state/region/province if applicable).
Type: [TaxRegistrationWithJurisdiction](API_taxSettings_TaxRegistrationWithJurisdiction.md) object
Required: No

## See Also
<a name="API_taxSettings_AccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/AccountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/AccountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/AccountDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
