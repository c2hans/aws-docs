---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ManifestPayload.html
---

# ManifestPayload
<a name="API_ManifestPayload"></a>

A application verion's manifest file. This is a JSON document that has a single key (`PayloadData`) where the value is an escaped string representation of the application manifest (`graph.json`). This file is located in the `graphs` folder in your application source.

## Contents
<a name="API_ManifestPayload_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PayloadData **   <a name="panorama-Type-ManifestPayload-PayloadData"></a>
The application manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Pattern: `.+`
Required: No

## See Also
<a name="API_ManifestPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ManifestPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ManifestPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ManifestPayload)
