---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CustomEntityConfig.html
---

# CustomEntityConfig
<a name="API_CustomEntityConfig"></a>

The configuration for defining custom patterns to be redacted from logs and error messages. This is for the CUSTOM config under entitiesToRedact. Both CustomEntityConfig and entitiesToRedact need to be present or not present.

## Contents
<a name="API_CustomEntityConfig_Contents"></a>

 ** customDataIdentifiers **   <a name="API-Type-CustomEntityConfig-customDataIdentifiers"></a>
Defines data identifiers for the custom entity configuration. Provide this only if CUSTOM redaction is configured.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9\_\#\=\@/\;\,\-\ \^\$\?\[\]\{\}\|\\\*\+\.\(\)]+`
Required: Yes

## See Also
<a name="API_CustomEntityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CustomEntityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CustomEntityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CustomEntityConfig)
