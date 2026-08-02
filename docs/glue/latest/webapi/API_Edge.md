---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Edge.html
---

# Edge
<a name="API_Edge"></a>

An edge represents a directed connection between two AWS Glue components that are part of the workflow the edge belongs to.

## Contents
<a name="API_Edge_Contents"></a>

 ** DestinationId **   <a name="Glue-Type-Edge-DestinationId"></a>
The unique of the node within the workflow where the edge ends.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SourceId **   <a name="Glue-Type-Edge-SourceId"></a>
The unique of the node within the workflow where the edge starts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Edge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Edge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Edge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Edge)
