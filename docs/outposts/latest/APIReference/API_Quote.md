---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Quote.html
---

# Quote
<a name="API_Quote"></a>

Information about a quote for an Outpost. A quote provides pricing and configuration options based on the requested capacity.

## Contents
<a name="API_Quote_Contents"></a>

 ** AccountId **   <a name="outposts-Type-Quote-AccountId"></a>
The ID of the account that owns the quote.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CountryCode **   <a name="outposts-Type-Quote-CountryCode"></a>
The country code for the Outpost site location.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: No

 ** CreatedDate **   <a name="outposts-Type-Quote-CreatedDate"></a>
The date the quote was created.
Type: Timestamp
Required: No

 ** Description **   <a name="outposts-Type-Quote-Description"></a>
The description of the quote.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^[\S \n]*$`
Required: No

 ** ExpirationDate **   <a name="outposts-Type-Quote-ExpirationDate"></a>
The date the quote expires.
Type: Timestamp
Required: No

 ** OrderingRequirements **   <a name="outposts-Type-Quote-OrderingRequirements"></a>
The requirements that must be met before an order can be submitted for the quote.
Type: Array of [OrderingRequirement](API_OrderingRequirement.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** OutpostArn **   <a name="outposts-Type-Quote-OutpostArn"></a>
The ARN of the Outpost associated with the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** QuoteId **   <a name="outposts-Type-Quote-QuoteId"></a>
The ID of the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^oq-[a-f0-9]{17}$`
Required: No

 ** QuoteOptions **   <a name="outposts-Type-Quote-QuoteOptions"></a>
The configuration and pricing options for the quote. Each option includes capacity details, physical specifications, and pricing information.
Type: Array of [QuoteOption](API_QuoteOption.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** QuoteStatus **   <a name="outposts-Type-Quote-QuoteStatus"></a>
The status of the quote.
+  `CREATED` - The quote has been created and is available for review.
+  `ORDER_SUBMITTED` - An order has been submitted for the quote.
+  `EXPIRED` - The quote has expired and can no longer be used to submit an order.
Type: String
Valid Values: `CREATED | ORDER_SUBMITTED | EXPIRED`
Required: No

 ** RequestedCapacities **   <a name="outposts-Type-Quote-RequestedCapacities"></a>
The capacity requirements specified in the quote request.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** RequestedConstraints **   <a name="outposts-Type-Quote-RequestedConstraints"></a>
The physical constraints specified in the quote request.
Type: Array of [QuoteConstraint](API_QuoteConstraint.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** RequestedPaymentOptions **   <a name="outposts-Type-Quote-RequestedPaymentOptions"></a>
The payment options specified in the quote request.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** RequestedPaymentTerms **   <a name="outposts-Type-Quote-RequestedPaymentTerms"></a>
The payment terms specified in the quote request.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

 ** StatusMessage **   <a name="outposts-Type-Quote-StatusMessage"></a>
A message about the status of the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\S \n]+$`
Required: No

 ** SubmittedOrderId **   <a name="outposts-Type-Quote-SubmittedOrderId"></a>
The ID of the order submitted for the quote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^oo-[a-f0-9]{17}$`
Required: No

## See Also
<a name="API_Quote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Quote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Quote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Quote)
