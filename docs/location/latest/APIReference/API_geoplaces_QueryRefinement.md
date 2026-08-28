---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_QueryRefinement.html
---

# QueryRefinement
<a name="API_geoplaces_QueryRefinement"></a>

Suggestions for refining individual query terms. Suggestions are returned as objects which note the term, suggested replacement, and its index in the query.

## Contents
<a name="API_geoplaces_QueryRefinement_Contents"></a>

 ** EndIndex **   <a name="location-Type-geoplaces_QueryRefinement-EndIndex"></a>
End index of the parsed query.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** OriginalTerm **   <a name="location-Type-geoplaces_QueryRefinement-OriginalTerm"></a>
The sub-string of the original query that is replaced by this query term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** RefinedTerm **   <a name="location-Type-geoplaces_QueryRefinement-RefinedTerm"></a>
The term that will be suggested to the user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** StartIndex **   <a name="location-Type-geoplaces_QueryRefinement-StartIndex"></a>
Start index of the parsed component.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_geoplaces_QueryRefinement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/QueryRefinement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/QueryRefinement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/QueryRefinement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
