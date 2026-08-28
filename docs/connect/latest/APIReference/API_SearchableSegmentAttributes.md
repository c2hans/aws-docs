---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchableSegmentAttributes.html
---

# SearchableSegmentAttributes
<a name="API_SearchableSegmentAttributes"></a>

The search criteria based on searchable segment attributes of a contact

## Contents
<a name="API_SearchableSegmentAttributes_Contents"></a>

 ** Criteria **   <a name="connect-Type-SearchableSegmentAttributes-Criteria"></a>
The list of criteria based on searchable segment attributes.
Type: Array of [SearchableSegmentAttributesCriteria](API_SearchableSegmentAttributesCriteria.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: Yes

 ** MatchType **   <a name="connect-Type-SearchableSegmentAttributes-MatchType"></a>
The match type combining search criteria using multiple searchable segment attributes.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: No

## See Also
<a name="API_SearchableSegmentAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchableSegmentAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchableSegmentAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchableSegmentAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
