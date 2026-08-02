---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_QuoteSummary.html
---

# QuoteSummary
<a name="API_QuoteSummary"></a>

Summary information about a quote.

## Contents
<a name="API_QuoteSummary_Contents"></a>

 ** AccountId **   <a name="outposts-Type-QuoteSummary-AccountId"></a>
The ID of the account that owns the quote.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CountryCode **   <a name="outposts-Type-QuoteSummary-CountryCode"></a>
The country code for the Outpost site location.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: No

 ** CreatedDate **   <a name="outposts-Type-QuoteSummary-CreatedDate"></a>
The date the quote was created.
Type: Timestamp
Required: No

 ** Description **   <a name="outposts-Type-QuoteSummary-Description"></a>
The description of the quote.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^[\S \n]*$`
Required: No

 ** ExpirationDate **   <a name="outposts-Type-QuoteSummary-ExpirationDate"></a>
The date the quote expires.
Type: Timestamp
Required: No

 ** OutpostArn **   <a name="outposts-Type-QuoteSummary-OutpostArn"></a>
The ARN of the Outpost associated with the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** QuoteId **   <a name="outposts-Type-QuoteSummary-QuoteId"></a>
The ID of the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^oq-[a-f0-9]{17}$`
Required: No

 ** QuoteOptions **   <a name="outposts-Type-QuoteSummary-QuoteOptions"></a>
The configuration and pricing options for the quote.
Type: Array of [QuoteOption](API_QuoteOption.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** QuoteStatus **   <a name="outposts-Type-QuoteSummary-QuoteStatus"></a>
The status of the quote.
Type: String
Valid Values: `CREATED | ORDER_SUBMITTED | EXPIRED`
Required: No

 ** RequestedCapacities **   <a name="outposts-Type-QuoteSummary-RequestedCapacities"></a>
The capacity requirements specified in the quote request.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** RequestedConstraints **   <a name="outposts-Type-QuoteSummary-RequestedConstraints"></a>
The physical constraints specified in the quote request.
Type: Array of [QuoteConstraint](API_QuoteConstraint.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** RequestedPaymentOptions **   <a name="outposts-Type-QuoteSummary-RequestedPaymentOptions"></a>
The payment options specified in the quote request.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** RequestedPaymentTerms **   <a name="outposts-Type-QuoteSummary-RequestedPaymentTerms"></a>
The payment terms specified in the quote request.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

 ** StatusMessage **   <a name="outposts-Type-QuoteSummary-StatusMessage"></a>
A message about the status of the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\S \n]+$`
Required: No

 ** SubmittedOrderId **   <a name="outposts-Type-QuoteSummary-SubmittedOrderId"></a>
The ID of the order submitted for the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^oo-[a-f0-9]{17}$`
Required: No

## See Also
<a name="API_QuoteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/QuoteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/QuoteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/QuoteSummary)
