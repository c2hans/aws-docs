---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ComponentVersion.html
---

# ComponentVersion
<a name="API_ComponentVersion"></a>

Version information for agent components.

## Contents
<a name="API_ComponentVersion_Contents"></a>

 ** componentType **   <a name="groundstation-Type-ComponentVersion-componentType"></a>
Component type.
Type: String
Pattern: `[a-zA-Z0-9_]{1,64}`
Required: Yes

 ** versions **   <a name="groundstation-Type-ComponentVersion-versions"></a>
List of versions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(0|[1-9]\d*)(\.(0|[1-9]\d*))*`
Required: Yes

## See Also
<a name="API_ComponentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ComponentVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ComponentVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ComponentVersion)
