---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OffsetConfiguration.html
---

# OffsetConfiguration
<a name="API_OffsetConfiguration"></a>

Offset-based pagination configuration that defines how to handle pagination using numeric offsets and limits.

## Contents
<a name="API_OffsetConfiguration_Contents"></a>

 ** LimitParameter **   <a name="Glue-Type-OffsetConfiguration-LimitParameter"></a>
The parameter name used to specify the maximum number of results to return per page.
Type: [ExtractedParameter](API_ExtractedParameter.md) object
Required: Yes

 ** OffsetParameter **   <a name="Glue-Type-OffsetConfiguration-OffsetParameter"></a>
The parameter name used to specify the starting position or offset for retrieving results.
Type: [ExtractedParameter](API_ExtractedParameter.md) object
Required: Yes

## See Also
<a name="API_OffsetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OffsetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OffsetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OffsetConfiguration)
