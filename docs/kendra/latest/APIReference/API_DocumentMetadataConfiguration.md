---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentMetadataConfiguration.html
---

# DocumentMetadataConfiguration
<a name="API_DocumentMetadataConfiguration"></a>

Specifies the properties, such as relevance tuning and searchability, of an index field.

## Contents
<a name="API_DocumentMetadataConfiguration_Contents"></a>

 ** Name **   <a name="kendra-Type-DocumentMetadataConfiguration-Name"></a>
The name of the index field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: Yes

 ** Type **   <a name="kendra-Type-DocumentMetadataConfiguration-Type"></a>
The data type of the index field.
Type: String
Valid Values: `STRING_VALUE | STRING_LIST_VALUE | LONG_VALUE | DATE_VALUE`
Required: Yes

 ** Relevance **   <a name="kendra-Type-DocumentMetadataConfiguration-Relevance"></a>
Provides tuning parameters to determine how the field affects the search results.
Type: [Relevance](API_Relevance.md) object
Required: No

 ** Search **   <a name="kendra-Type-DocumentMetadataConfiguration-Search"></a>
Provides information about how the field is used during a search.
Type: [Search](API_Search.md) object
Required: No

## See Also
<a name="API_DocumentMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DocumentMetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DocumentMetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DocumentMetadataConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
