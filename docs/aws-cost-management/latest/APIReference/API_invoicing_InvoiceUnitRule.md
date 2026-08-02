---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceUnitRule.html
---

# InvoiceUnitRule
<a name="API_invoicing_InvoiceUnitRule"></a>

 This is used to categorize the invoice unit. Values are AWS account IDs. Currently, the only supported rule is `LINKED_ACCOUNT`.

## Contents
<a name="API_invoicing_InvoiceUnitRule_Contents"></a>

 ** BillSourceAccounts **   <a name="awscostmanagement-Type-invoicing_InvoiceUnitRule-BillSourceAccounts"></a>
 A list of AWS account IDs that have delegated their billing responsibility to the receiver account through transfer billing. Unlike linked accounts, these bill source accounts can be payer accounts from other organizations that have authorized billing transfer to this account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

 ** LinkedAccounts **   <a name="awscostmanagement-Type-invoicing_InvoiceUnitRule-LinkedAccounts"></a>
The list of `LINKED_ACCOUNT` IDs where charges are included within the invoice unit.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_invoicing_InvoiceUnitRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceUnitRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceUnitRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceUnitRule)
