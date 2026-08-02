---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Filters.html
---

# Filters
<a name="API_invoicing_Filters"></a>

An optional input to the list API. If multiple filters are specified, the returned list will be a configuration that match all of the provided filters. Supported filter types are `InvoiceReceivers`, `Names`, and `Accounts`.

## Contents
<a name="API_invoicing_Filters_Contents"></a>

 ** Accounts **   <a name="awscostmanagement-Type-invoicing_Filters-Accounts"></a>
 You can specify a list of AWS account IDs inside filters to return invoice units that match only the specified accounts. If multiple accounts are provided, the result is an `OR` condition (match any) of the specified accounts. The specified account IDs are matched with either the receiver or the linked accounts in the rules.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

 ** BillSourceAccounts **   <a name="awscostmanagement-Type-invoicing_Filters-BillSourceAccounts"></a>
 A list of AWS account IDs used to filter invoice units. These are payer accounts from other AWS Organizations that have delegated their billing responsibility to the receiver account through the billing transfer feature.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

 ** InvoiceReceivers **   <a name="awscostmanagement-Type-invoicing_Filters-InvoiceReceivers"></a>
 You can specify a list of AWS account IDs inside filters to return invoice units that match only the specified accounts. If multiple accounts are provided, the result is an `OR` condition (match any) of the specified accounts. This filter only matches the specified accounts on the invoice receivers of the invoice units.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

 ** Names **   <a name="awscostmanagement-Type-invoicing_Filters-Names"></a>
 An optional input to the list API. You can specify a list of invoice unit names inside filters to return invoice units that match only the specified invoice unit names. If multiple names are provided, the result is an `OR` condition (match any) of the specified invoice unit names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`
Required: No

## See Also
<a name="API_invoicing_Filters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/Filters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/Filters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/Filters)
