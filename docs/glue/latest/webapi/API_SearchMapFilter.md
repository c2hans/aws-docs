---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchMapFilter.html
---

# SearchMapFilter
<a name="API_SearchMapFilter"></a>

A filter on a map attribute's key-value pair.

## Contents
<a name="API_SearchMapFilter_Contents"></a>

 ** Attribute **   <a name="Glue-Type-SearchMapFilter-Attribute"></a>
The map attribute name to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Key **   <a name="Glue-Type-SearchMapFilter-Key"></a>
The key within the map attribute to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="Glue-Type-SearchMapFilter-Value"></a>
The value to compare against.
Type: [SearchMapFilterValue](API_SearchMapFilterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_SearchMapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchMapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchMapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchMapFilter)
