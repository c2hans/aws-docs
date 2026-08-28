---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxInheritanceDetails.html
---

# TaxInheritanceDetails
<a name="API_taxSettings_TaxInheritanceDetails"></a>

 Tax inheritance information associated with the account.

## Contents
<a name="API_taxSettings_TaxInheritanceDetails_Contents"></a>

 ** inheritanceObtainedReason **   <a name="awscostmanagement-Type-taxSettings_TaxInheritanceDetails-inheritanceObtainedReason"></a>
 Tax inheritance reason information associated with the account.
Type: String
Pattern: `[\s\S]*`
Required: No

 ** parentEntityId **   <a name="awscostmanagement-Type-taxSettings_TaxInheritanceDetails-parentEntityId"></a>
 Tax inheritance parent account information associated with the account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_taxSettings_TaxInheritanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxInheritanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxInheritanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxInheritanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
