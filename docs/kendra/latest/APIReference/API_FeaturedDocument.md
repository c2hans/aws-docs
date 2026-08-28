---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedDocument.html
---

# FeaturedDocument
<a name="API_FeaturedDocument"></a>

A featured document. This document is displayed at the top of the search results page, placed above all other results for certain queries. If there's an exact match of a query, then the document is featured in the search results.

## Contents
<a name="API_FeaturedDocument_Contents"></a>

 ** Id **   <a name="kendra-Type-FeaturedDocument-Id"></a>
The identifier of the document to feature in the search results. You can use the [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) API to search for specific documents with their document IDs included in the result items, or you can use the console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_FeaturedDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/FeaturedDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/FeaturedDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/FeaturedDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
