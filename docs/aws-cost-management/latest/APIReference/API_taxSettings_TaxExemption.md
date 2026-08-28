---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxExemption.html
---

# TaxExemption
<a name="API_taxSettings_TaxExemption"></a>

The tax exemption.

## Contents
<a name="API_taxSettings_TaxExemption_Contents"></a>

 ** authority **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-authority"></a>
The address domain associate with tax exemption.
Type: [Authority](API_taxSettings_Authority.md) object
Required: Yes

 ** taxExemptionType **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-taxExemptionType"></a>
The tax exemption type.
Type: [TaxExemptionType](API_taxSettings_TaxExemptionType.md) object
Required: Yes

 ** effectiveDate **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-effectiveDate"></a>
The tax exemption effective date.
Type: Timestamp
Required: No

 ** expirationDate **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-expirationDate"></a>
The tax exemption expiration date.
Type: Timestamp
Required: No

 ** status **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-status"></a>
The tax exemption status.
Type: String
Valid Values: `None | Valid | Expired | Pending`
Required: No

 ** systemEffectiveDate **   <a name="awscostmanagement-Type-taxSettings_TaxExemption-systemEffectiveDate"></a>
The tax exemption recording time in the `TaxSettings` system.
Type: Timestamp
Required: No

## See Also
<a name="API_taxSettings_TaxExemption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxExemption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxExemption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxExemption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
