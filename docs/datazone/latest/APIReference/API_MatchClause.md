---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_MatchClause.html
---

# MatchClause
<a name="API_MatchClause"></a>

A clause to match a query pattern

## Contents
<a name="API_MatchClause_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** entityPattern **   <a name="datazone-Type-MatchClause-entityPattern"></a>
The pattern describing the entities for the query to traverse.
Type: [EntityPattern](API_EntityPattern.md) object
Required: No

 ** relationPattern **   <a name="datazone-Type-MatchClause-relationPattern"></a>
The pattern describing the query's relational traversal.
Type: [RelationPattern](API_RelationPattern.md) object
Required: No

## See Also
<a name="API_MatchClause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/MatchClause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/MatchClause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/MatchClause)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
