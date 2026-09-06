---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceUnit.html
---

# InvoiceUnit
<a name="API_invoicing_InvoiceUnit"></a>

An invoice unit is a set of mutually exclusive accounts that correspond to your business entity. Invoice units allow you separate AWS account costs and configures your invoice for each business entity going forward.

## Contents
<a name="API_invoicing_InvoiceUnit_Contents"></a>

 ** Description **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-Description"></a>
The assigned description for an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\S\s]*`
Required: No

 ** InvoiceReceiver **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-InvoiceReceiver"></a>
The account that receives invoices related to the invoice unit.
Type: String
Pattern: `\d{12}`
Required: No

 ** InvoiceUnitArn **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-InvoiceUnitArn"></a>
ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** LastModified **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-LastModified"></a>
 The last time the invoice unit was updated. This is important to determine the version of invoice unit configuration used to create the invoices. Any invoice created after this modified time will use this invoice unit configuration.
Type: Timestamp
Required: No

 ** Name **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-Name"></a>
 A unique name that is distinctive within your AWS.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`
Required: No

 ** Rule **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-Rule"></a>
 An `InvoiceUnitRule` object used the categorize invoice units.
Type: [InvoiceUnitRule](API_invoicing_InvoiceUnitRule.md) object
Required: No

 ** TaxInheritanceDisabled **   <a name="awscostmanagement-Type-invoicing_InvoiceUnit-TaxInheritanceDisabled"></a>
Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
Type: Boolean
Required: No

## See Also
<a name="API_invoicing_InvoiceUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceUnit)
