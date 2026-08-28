---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementInvoiceLineItems.html
---

# ListAgreementInvoiceLineItems
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems"></a>

Allows sellers (proposers) to retrieve aggregated billing data from AWS Marketplace agreements using flexible grouping. Supports invoice-level aggregation with filtering by billing period, invoice type, and issued date.

**Note**
The `groupBy` parameter is required and supports only `INVOICE_ID` as a value. The `agreementId` parameter is required.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax"></a>

```
{
   "afterIssuedTime": {{number}},
   "agreementId": "{{string}}",
   "beforeIssuedTime": {{number}},
   "groupBy": "{{string}}",
   "invoiceBillingPeriod": {
      "month": {{number}},
      "year": {{number}}
   },
   "invoiceId": "{{string}}",
   "invoiceType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [groupBy](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-groupBy"></a>
Specifies a grouping strategy for line items. Currently supports `INVOICE_ID`.
Type: String
Valid Values: `INVOICE_ID`
Required: Yes

 ** [afterIssuedTime](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-afterIssuedTime"></a>
An optional filter for invoices issued after the specified timestamp.
Type: Timestamp
Required: No

 ** [beforeIssuedTime](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-beforeIssuedTime"></a>
An optional filter for invoices issued before the specified timestamp.
Type: Timestamp
Required: No

 ** [invoiceBillingPeriod](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-invoiceBillingPeriod"></a>
An optional filter for the billing period associated with the invoice.
Type: [InvoiceBillingPeriod](API_marketplace-agreements_InvoiceBillingPeriod.md) object
Required: No

 ** [invoiceId](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-invoiceId"></a>
An optional filter to retrieve invoice information for a specific invoice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [invoiceType](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-invoiceType"></a>
An optional filter for the type of invoice. Valid values are `INVOICE` and `CREDIT_MEMO`.
Type: String
Valid Values: `INVOICE | CREDIT_MEMO`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementInvoiceLineItems_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_ResponseSyntax"></a>

```
{
   "agreementInvoiceLineItemGroupSummaries": [
      {
         "agreementId": "string",
         "invoiceBillingPeriod": {
            "month": number,
            "year": number
         },
         "invoiceId": "string",
         "invoiceType": "string",
         "invoicingEntity": {
            "branchName": "string",
            "legalName": "string"
         },
         "issuedTime": number,
         "pricingCurrencyAmount": {
            "amount": "string",
            "currencyCode": "string",
            "maxAdjustmentAmount": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementInvoiceLineItemGroupSummaries](#API_marketplace-agreements_ListAgreementInvoiceLineItems_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-response-agreementInvoiceLineItemGroupSummaries"></a>
A list of grouped billing data objects.
Type: Array of [AgreementInvoiceLineItemGroupSummary](API_marketplace-agreements_AgreementInvoiceLineItemGroupSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementInvoiceLineItems_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementInvoiceLineItems-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error during processing of request.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier for the resource.
 ** resourceType **
The type of resource.
HTTP Status Code: 400

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fields **
The fields associated with the error.
 ** message **
Description of the error.
 ** reason **
The reason associated with the error.
 ** requestId **
The unique identifier associated with the error.
HTTP Status Code: 400

## Examples
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_Example_1"></a>

This example illustrates one usage of ListAgreementInvoiceLineItems.

```
{
    "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
    "groupBy": "INVOICE_ID"
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_Example_2"></a>

This example illustrates one usage of ListAgreementInvoiceLineItems.

```
{
    "agreementInvoiceLineItemGroupSummaries": [
        {
            "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
            "invoiceId": "E2E20250105a108cfae",
            "pricingCurrencyAmount": {
                "amount": "1080.00",
                "maxAdjustmentAmount": "1000.00",
                "currencyCode": "USD"
            },
            "invoiceBillingPeriod": {
                "month": 1,
                "year": 2025
            },
            "issuedTime": 1736103549,
            "invoiceType": "INVOICE",
            "invoicingEntity": {
                "legalName": "Amazon Web Services, Inc."
            }
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementInvoiceLineItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementInvoiceLineItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
