---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchableContactAttributes.html
---

# SearchableContactAttributes
<a name="API_SearchableContactAttributes"></a>

A structure that defines search criteria based on user-defined contact attributes that are configured for contact search.

## Contents
<a name="API_SearchableContactAttributes_Contents"></a>

 ** Criteria **   <a name="connect-Type-SearchableContactAttributes-Criteria"></a>
The list of criteria based on user-defined contact attributes that are configured for contact search.
Type: Array of [SearchableContactAttributesCriteria](API_SearchableContactAttributesCriteria.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: Yes

 ** MatchType **   <a name="connect-Type-SearchableContactAttributes-MatchType"></a>
The match type combining search criteria using multiple searchable contact attributes.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: No

## See Also
<a name="API_SearchableContactAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchableContactAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchableContactAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchableContactAttributes)
