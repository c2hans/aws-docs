---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceSummaries.html
---

# ListInvoiceSummaries
<a name="API_invoicing_ListInvoiceSummaries"></a>

Retrieves your invoice details programmatically, without line item details.

## Request Syntax
<a name="API_invoicing_ListInvoiceSummaries_RequestSyntax"></a>

```
{
   "Filter": {
      "BillingPeriod": {
         "Month": {{number}},
         "Year": {{number}}
      },
      "InvoicingEntity": "{{string}}",
      "ReceiverRole": "{{string}}",
      "TimeInterval": {
         "EndDate": {{number}},
         "StartDate": {{number}}
      }
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Selector": {
      "ResourceType": "{{string}}",
      "Value": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_invoicing_ListInvoiceSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_invoicing_ListInvoiceSummaries_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-request-Filter"></a>
Filters you can use to customize your invoice summary.
Type: [InvoiceSummariesFilter](API_invoicing_InvoiceSummariesFilter.md) object
Required: No

 ** [MaxResults](#API_invoicing_ListInvoiceSummaries_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-request-MaxResults"></a>
The maximum number of invoice summaries a paginated response can contain.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_invoicing_ListInvoiceSummaries_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-request-NextToken"></a>
The token for the next set of results. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S\s]*`
Required: No

 ** [Selector](#API_invoicing_ListInvoiceSummaries_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-request-Selector"></a>
The option to retrieve details for a specific invoice by providing its unique ID. Alternatively, access information for all invoices linked to the account by providing an account ID.
Type: [InvoiceSummariesSelector](API_invoicing_InvoiceSummariesSelector.md) object
Required: Yes

## Response Syntax
<a name="API_invoicing_ListInvoiceSummaries_ResponseSyntax"></a>

```
{
   "InvoiceSummaries": [
      {
         "AccountId": "string",
         "BaseCurrencyAmount": {
            "AmountBreakdown": {
               "Discounts": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "Fees": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "SubTotalAmount": "string",
               "Taxes": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               }
            },
            "CurrencyCode": "string",
            "CurrencyExchangeDetails": {
               "Rate": "string",
               "SourceCurrencyCode": "string",
               "TargetCurrencyCode": "string"
            },
            "TotalAmount": "string",
            "TotalAmountBeforeTax": "string"
         },
         "BillingPeriod": {
            "Month": number,
            "Year": number
         },
         "BillSourceAccounts": [ "string" ],
         "BillSourceAccountsTotalCount": number,
         "BillType": "string",
         "CommercialInvoiceId": "string",
         "DueDate": number,
         "EinvoiceDeliveryStatus": "string",
         "Entity": {
            "BillingEntity": "string",
            "InvoicingEntity": "string"
         },
         "InvoiceFrequency": "string",
         "InvoiceId": "string",
         "InvoiceType": "string",
         "IssuedDate": number,
         "OriginalInvoiceId": "string",
         "PaymentCurrencyAmount": {
            "AmountBreakdown": {
               "Discounts": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "Fees": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "SubTotalAmount": "string",
               "Taxes": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               }
            },
            "CurrencyCode": "string",
            "CurrencyExchangeDetails": {
               "Rate": "string",
               "SourceCurrencyCode": "string",
               "TargetCurrencyCode": "string"
            },
            "TotalAmount": "string",
            "TotalAmountBeforeTax": "string"
         },
         "PurchaseOrderNumber": "string",
         "ReceiverRole": "string",
         "TaxAuthorityStatus": "string",
         "TaxCurrencyAmount": {
            "AmountBreakdown": {
               "Discounts": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "Fees": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               },
               "SubTotalAmount": "string",
               "Taxes": {
                  "Breakdown": [
                     {
                        "Amount": "string",
                        "Description": "string",
                        "Rate": "string"
                     }
                  ],
                  "TotalAmount": "string"
               }
            },
            "CurrencyCode": "string",
            "CurrencyExchangeDetails": {
               "Rate": "string",
               "SourceCurrencyCode": "string",
               "TargetCurrencyCode": "string"
            },
            "TotalAmount": "string",
            "TotalAmountBeforeTax": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_invoicing_ListInvoiceSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvoiceSummaries](#API_invoicing_ListInvoiceSummaries_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-response-InvoiceSummaries"></a>
List of key (summary level) invoice details without line item details.
Type: Array of [InvoiceSummary](API_invoicing_InvoiceSummary.md) objects

 ** [NextToken](#API_invoicing_ListInvoiceSummaries_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListInvoiceSummaries-response-NextToken"></a>
The token to use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S\s]*`

## Errors
<a name="API_invoicing_ListInvoiceSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The processing request failed because of an unknown error, exception, or failure.
 ** retryAfterSeconds **
The processing request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The resource could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
 The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

## See Also
<a name="API_invoicing_ListInvoiceSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/ListInvoiceSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ListInvoiceSummaries)
