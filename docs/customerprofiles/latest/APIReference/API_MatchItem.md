---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchItem.html
---

# MatchItem
<a name="API_connect-customer-profiles_MatchItem"></a>

The Match group object.

## Contents
<a name="API_connect-customer-profiles_MatchItem_Contents"></a>

 ** ConfidenceScore **   <a name="connect-Type-connect-customer-profiles_MatchItem-ConfidenceScore"></a>
A number between 0 and 1, where a higher score means higher similarity. Examining match confidence scores lets you distinguish between groups of similar records in which the system is highly confident (which you may decide to merge), groups of similar records about which the system is uncertain (which you may decide to have reviewed by a human), and groups of similar records that the system deems to be unlikely (which you may decide to reject). Given confidence scores vary as per the data input, it should not be used an absolute measure of matching quality.
Type: Double
Required: No

 ** MatchId **   <a name="connect-Type-connect-customer-profiles_MatchItem-MatchId"></a>
The unique identifiers for this group of profiles that match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ProfileIds **   <a name="connect-Type-connect-customer-profiles_MatchItem-ProfileIds"></a>
A list of identifiers for profiles that match.
Type: Array of strings
Pattern: `[a-f0-9]{32}`
Required: No

## See Also
<a name="API_connect-customer-profiles_MatchItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/MatchItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/MatchItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/MatchItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
