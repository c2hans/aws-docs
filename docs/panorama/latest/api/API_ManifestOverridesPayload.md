---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ManifestOverridesPayload.html
---

# ManifestOverridesPayload
<a name="API_ManifestOverridesPayload"></a>

Parameter overrides for an application instance. This is a JSON document that has a single key (`PayloadData`) where the value is an escaped string representation of the overrides document.

## Contents
<a name="API_ManifestOverridesPayload_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PayloadData **   <a name="panorama-Type-ManifestOverridesPayload-PayloadData"></a>
The overrides document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

## See Also
<a name="API_ManifestOverridesPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ManifestOverridesPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ManifestOverridesPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ManifestOverridesPayload)
