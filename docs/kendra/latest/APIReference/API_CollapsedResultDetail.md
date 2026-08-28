---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_CollapsedResultDetail.html
---

# CollapsedResultDetail
<a name="API_CollapsedResultDetail"></a>

Provides details about a collapsed group of search results.

## Contents
<a name="API_CollapsedResultDetail_Contents"></a>

 ** DocumentAttribute **   <a name="kendra-Type-CollapsedResultDetail-DocumentAttribute"></a>
The value of the document attribute that results are collapsed on.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: Yes

 ** ExpandedResults **   <a name="kendra-Type-CollapsedResultDetail-ExpandedResults"></a>
A list of results in the collapsed group.
Type: Array of [ExpandedResultItem](API_ExpandedResultItem.md) objects
Required: No

## See Also
<a name="API_CollapsedResultDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/CollapsedResultDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/CollapsedResultDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/CollapsedResultDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
