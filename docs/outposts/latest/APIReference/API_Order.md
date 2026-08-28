---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Order.html
---

# Order
<a name="API_Order"></a>

Information about an order.

## Contents
<a name="API_Order_Contents"></a>

 ** LineItems **   <a name="outposts-Type-Order-LineItems"></a>
The line items for the order
Type: Array of [LineItem](API_LineItem.md) objects
Required: No

 ** OrderFulfilledDate **   <a name="outposts-Type-Order-OrderFulfilledDate"></a>
The fulfillment date of the order.
Type: Timestamp
Required: No

 ** OrderId **   <a name="outposts-Type-Order-OrderId"></a>
The ID of the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: No

 ** OrderSubmissionDate **   <a name="outposts-Type-Order-OrderSubmissionDate"></a>
The submission date for the order.
Type: Timestamp
Required: No

 ** OrderType **   <a name="outposts-Type-Order-OrderType"></a>
The type of order.
Type: String
Valid Values: `OUTPOST | REPLACEMENT`
Required: No

 ** OutpostId **   <a name="outposts-Type-Order-OutpostId"></a>
 The ID of the Outpost in the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^op-[a-f0-9]{17}$`
Required: No

 ** PaymentOption **   <a name="outposts-Type-Order-PaymentOption"></a>
The payment option for the order.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** PaymentTerm **   <a name="outposts-Type-Order-PaymentTerm"></a>
The payment term.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

 ** QuoteIdentifier **   <a name="outposts-Type-Order-QuoteIdentifier"></a>
The ID of the quote associated with the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:quote/)?oq-[a-f0-9]{17}$`
Required: No

 ** QuoteOptionIdentifier **   <a name="outposts-Type-Order-QuoteOptionIdentifier"></a>
The ID of the quote option associated with the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21.
Pattern: `^oqo-[a-f0-9]{17}$`
Required: No

 ** Status **   <a name="outposts-Type-Order-Status"></a>
The status of the order.
+  `PREPARING` - Order is received and being prepared.
+  `IN_PROGRESS` - Order is either being built or shipped. To get more details, see the line item status.
+  `DELIVERED` - Order was delivered to the Outpost site.
+  `COMPLETED` - Order is complete.
+  `CANCELLED` - Order is cancelled.
+  `ERROR` - Customer should contact support.
The following status are deprecated: `RECEIVED`, `PENDING`, `PROCESSING`, `INSTALLING`, and `FULFILLED`.
Type: String
Valid Values: `RECEIVED | PENDING | PROCESSING | INSTALLING | FULFILLED | CANCELLED | PREPARING | IN_PROGRESS | DELIVERED | COMPLETED | ERROR`
Required: No

## See Also
<a name="API_Order_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Order)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Order)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Order)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
