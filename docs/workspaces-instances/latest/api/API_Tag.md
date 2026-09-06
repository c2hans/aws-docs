---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Represents a key-value metadata tag.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="workspacesinstances-Type-Tag-Key"></a>
Unique identifier for the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Required: No

 ** Value **   <a name="workspacesinstances-Type-Tag-Value"></a>
Value associated with the tag key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/Tag)
