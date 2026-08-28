---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_OrderingRequirement.html
---

# OrderingRequirement
<a name="API_OrderingRequirement"></a>

A requirement that must be met before an order can be submitted for a quote.

## Contents
<a name="API_OrderingRequirement_Contents"></a>

 ** OrderingRequirementType **   <a name="outposts-Type-OrderingRequirement-OrderingRequirementType"></a>
The type of ordering requirement. Indicates which check failed or passed.
+  `OUTPOST_ACTIVE_CHECK_ERROR` - The Outpost must be in an active state.
+  `MAXIMUM_ALLOWED_ORDERS_CHECK_ERROR` - The maximum number of allowed orders has been reached.
+  `VALID_ZIP_CODE_CHECK_ERROR` - The site address must have a valid zip code.
+  `RACK_PHYSICAL_PROPERTIES_CHECK_ERROR` - The rack physical properties do not meet requirements.
+  `OPERATING_ADDRESS_EXISTENCE_CHECK_ERROR` - The site must have an operating address.
+  `SHIPPING_ADDRESS_EXISTENCE_CHECK_ERROR` - The site must have a shipping address.
+  `COUNTRY_CODE_MISMATCH_CHECK_ERROR` - The country code on the quote does not match the Outpost site country.
+  `OUTPOST_GENERATION_MISMATCH_ERROR` - The Outpost generation does not match the requested configuration.
+  `OUTPOST_ID_MISSING_ON_QUOTE_ERROR` - The quote must be associated with an Outpost before submitting an order.
+  `ENTERPRISE_SUPPORT_ERROR` - Enterprise Support is required.
+  `SHIPPING_ADDRESS_MISSING_CONTACT_NAME_ERROR` - The shipping address must have a contact name.
+  `SHIPPING_ADDRESS_MISSING_CONTACT_NUMBER_ERROR` - The shipping address must have a contact phone number.
+  `SHIPPING_ADDRESS_MISSING_CONTACT_INFO_ERROR` - The shipping address must have contact information.
+  `OUTPOST_STATE_CHANGED_ERROR` - The Outpost state has changed since the quote was created.
+  `OUTPOST_NOT_FOUND_ERROR` - The Outpost associated with the quote was not found.
+  `OUTPOST_RENEWAL_REQUIRED_ERROR` - The Outpost requires a renewal before a new order can be submitted.
+  `UNSUPPORTED` - The requirement type is not recognized.
Type: String
Valid Values: `OUTPOST_ACTIVE_CHECK_ERROR | MAXIMUM_ALLOWED_ORDERS_CHECK_ERROR | VALID_ZIP_CODE_CHECK_ERROR | RACK_PHYSICAL_PROPERTIES_CHECK_ERROR | OPERATING_ADDRESS_EXISTENCE_CHECK_ERROR | SHIPPING_ADDRESS_EXISTENCE_CHECK_ERROR | COUNTRY_CODE_MISMATCH_CHECK_ERROR | OUTPOST_GENERATION_MISMATCH_ERROR | UNSUPPORTED | OUTPOST_ID_MISSING_ON_QUOTE_ERROR | ENTERPRISE_SUPPORT_ERROR | SHIPPING_ADDRESS_MISSING_CONTACT_NAME_ERROR | SHIPPING_ADDRESS_MISSING_CONTACT_NUMBER_ERROR | SHIPPING_ADDRESS_MISSING_CONTACT_INFO_ERROR | OUTPOST_STATE_CHANGED_ERROR | OUTPOST_NOT_FOUND_ERROR | OUTPOST_RENEWAL_REQUIRED_ERROR`
Required: No

 ** Status **   <a name="outposts-Type-OrderingRequirement-Status"></a>
The status of the ordering requirement. Valid values are `PASS`, `FAIL`, and `EXEMPT`.
Type: String
Valid Values: `PASS | FAIL | EXEMPT`
Required: No

 ** StatusMessage **   <a name="outposts-Type-OrderingRequirement-StatusMessage"></a>
A message about the ordering requirement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_OrderingRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/OrderingRequirement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/OrderingRequirement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/OrderingRequirement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
