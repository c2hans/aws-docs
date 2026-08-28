---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SouthKoreaAdditionalInfo.html
---

# SouthKoreaAdditionalInfo
<a name="API_taxSettings_SouthKoreaAdditionalInfo"></a>

Additional tax information associated with your TRN in South Korea.

## Contents
<a name="API_taxSettings_SouthKoreaAdditionalInfo_Contents"></a>

 ** businessRepresentativeName **   <a name="awscostmanagement-Type-taxSettings_SouthKoreaAdditionalInfo-businessRepresentativeName"></a>
The business legal name based on the most recently uploaded tax registration certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*`
Required: Yes

 ** itemOfBusiness **   <a name="awscostmanagement-Type-taxSettings_SouthKoreaAdditionalInfo-itemOfBusiness"></a>
Item of business based on the most recently uploaded tax registration certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*`
Required: Yes

 ** lineOfBusiness **   <a name="awscostmanagement-Type-taxSettings_SouthKoreaAdditionalInfo-lineOfBusiness"></a>
Line of business based on the most recently uploaded tax registration certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*`
Required: Yes

## See Also
<a name="API_taxSettings_SouthKoreaAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/SouthKoreaAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/SouthKoreaAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/SouthKoreaAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
