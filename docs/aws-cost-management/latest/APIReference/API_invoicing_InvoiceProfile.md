---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceProfile.html
---

# InvoiceProfile
<a name="API_invoicing_InvoiceProfile"></a>

 Contains high-level information about the invoice receiver.

## Contents
<a name="API_invoicing_InvoiceProfile_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-AccountId"></a>
 The account ID the invoice profile is generated for.
Type: String
Pattern: `\d{12}`
Required: No

 ** Issuer **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-Issuer"></a>
 This specifies the issuing entity of the invoice.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** ReceiverAddress **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-ReceiverAddress"></a>
The address of the receiver that will be printed on the invoice.
Type: [ReceiverAddress](API_invoicing_ReceiverAddress.md) object
Required: No

 ** ReceiverEmail **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-ReceiverEmail"></a>
The email address for the invoice profile receiver.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** ReceiverName **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-ReceiverName"></a>
 The name of the person receiving the invoice profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** TaxRegistrationNumber **   <a name="awscostmanagement-Type-invoicing_InvoiceProfile-TaxRegistrationNumber"></a>
 Your Tax Registration Number (TRN) information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## See Also
<a name="API_invoicing_InvoiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
