---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ResourceUri.html
---

# ResourceUri
<a name="API_ResourceUri"></a>

The URIs for function resources.

## Contents
<a name="API_ResourceUri_Contents"></a>

 ** ResourceType **   <a name="Glue-Type-ResourceUri-ResourceType"></a>
The type of the resource.
Type: String
Valid Values: `JAR | FILE | ARCHIVE`
Required: No

 ** Uri **   <a name="Glue-Type-ResourceUri-Uri"></a>
The URI for accessing the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ResourceUri_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ResourceUri)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ResourceUri)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ResourceUri)
