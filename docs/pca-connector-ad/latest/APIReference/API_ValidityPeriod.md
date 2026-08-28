---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ValidityPeriod.html
---

# ValidityPeriod
<a name="API_ValidityPeriod"></a>

Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in hours, days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

## Contents
<a name="API_ValidityPeriod_Contents"></a>

 ** Period **   <a name="PcaConnectorAd-Type-ValidityPeriod-Period"></a>
The numeric value for the validity period.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 8766000.
Required: Yes

 ** PeriodType **   <a name="PcaConnectorAd-Type-ValidityPeriod-PeriodType"></a>
The unit of time. You can select hours, days, weeks, months, and years.
Type: String
Valid Values: `HOURS | DAYS | WEEKS | MONTHS | YEARS`
Required: Yes

## See Also
<a name="API_ValidityPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/ValidityPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/ValidityPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/ValidityPeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
