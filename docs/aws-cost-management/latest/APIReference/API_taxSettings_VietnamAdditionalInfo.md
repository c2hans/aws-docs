---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_VietnamAdditionalInfo.html
---

# VietnamAdditionalInfo
<a name="API_taxSettings_VietnamAdditionalInfo"></a>

Additional tax information to specify for a TRN in Vietnam.

## Contents
<a name="API_taxSettings_VietnamAdditionalInfo_Contents"></a>

 ** electronicTransactionCodeNumber **   <a name="awscostmanagement-Type-taxSettings_VietnamAdditionalInfo-electronicTransactionCodeNumber"></a>
The electronic transaction code number on the tax return document. This field must be provided for successful API operation.
Type: String
Pattern: `\d{17}`
Required: No

 ** enterpriseIdentificationNumber **   <a name="awscostmanagement-Type-taxSettings_VietnamAdditionalInfo-enterpriseIdentificationNumber"></a>
The enterprise identification number for tax registration. This field must be provided for successful API operation.
Type: String
Pattern: `(\d{10}|(\d{10}-\d{3}))`
Required: No

 ** paymentVoucherNumber **   <a name="awscostmanagement-Type-taxSettings_VietnamAdditionalInfo-paymentVoucherNumber"></a>
The payment voucher number on the tax return payment document. This field must be provided for successful API operation.
Type: String
Pattern: `(\d{17}|[A-Za-z]{3}\d{13}|(?=[^A-Za-z]*[A-Za-z][^A-Za-z]*$)[0-9A-Za-z]{17})`
Required: No

 ** paymentVoucherNumberDate **   <a name="awscostmanagement-Type-taxSettings_VietnamAdditionalInfo-paymentVoucherNumberDate"></a>
The date on the tax return payment document. This field must be provided for successful API operation.
Type: String
Pattern: `(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))`
Required: No

## See Also
<a name="API_taxSettings_VietnamAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/VietnamAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/VietnamAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/VietnamAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
