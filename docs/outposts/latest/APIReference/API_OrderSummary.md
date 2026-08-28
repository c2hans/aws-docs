---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_OrderSummary.html
---

# OrderSummary
<a name="API_OrderSummary"></a>

 A summary of line items in your order.

## Contents
<a name="API_OrderSummary_Contents"></a>

 ** LineItemCountsByStatus **   <a name="outposts-Type-OrderSummary-LineItemCountsByStatus"></a>
 The status of all line items in the order.
Type: String to integer map
Valid Keys: `PREPARING | BUILDING | SHIPPED | DELIVERED | INSTALLING | INSTALLED | ERROR | CANCELLED | REPLACED`
Valid Range: Minimum value of 1.
Required: No

 ** OrderFulfilledDate **   <a name="outposts-Type-OrderSummary-OrderFulfilledDate"></a>
 The fulfilment date for the order.
Type: Timestamp
Required: No

 ** OrderId **   <a name="outposts-Type-OrderSummary-OrderId"></a>
 The ID of the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: No

 ** OrderSubmissionDate **   <a name="outposts-Type-OrderSummary-OrderSubmissionDate"></a>
 The submission date for the order.
Type: Timestamp
Required: No

 ** OrderType **   <a name="outposts-Type-OrderSummary-OrderType"></a>
The type of order.
Type: String
Valid Values: `OUTPOST | REPLACEMENT`
Required: No

 ** OutpostId **   <a name="outposts-Type-OrderSummary-OutpostId"></a>
 The ID of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^op-[a-f0-9]{17}$`
Required: No

 ** Status **   <a name="outposts-Type-OrderSummary-Status"></a>
The status of the order.
+  `PREPARING` - Order is received and is being prepared.
+  `IN_PROGRESS` - Order is either being built, shipped, or installed. For more information, see the `LineItem` status.
+  `COMPLETED` - Order is complete.
+  `CANCELLED` - Order is cancelled.
+  `ERROR` - Customer should contact support.
The following statuses are deprecated: `RECEIVED`, `PENDING`, `PROCESSING`, `INSTALLING`, and `FULFILLED`.
Type: String
Valid Values: `RECEIVED | PENDING | PROCESSING | INSTALLING | FULFILLED | CANCELLED | PREPARING | IN_PROGRESS | DELIVERED | COMPLETED | ERROR`
Required: No

## See Also
<a name="API_OrderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/OrderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/OrderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/OrderSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
