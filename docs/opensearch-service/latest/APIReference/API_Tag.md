---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A tag (key-value pair) for an Amazon OpenSearch Service resource.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="opensearchservice-Type-Tag-Key"></a>
The tag key. Tag keys must be unique for the domain to which they are attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*`
Required: Yes

 ** Value **   <a name="opensearchservice-Type-Tag-Value"></a>
The value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/Tag)
