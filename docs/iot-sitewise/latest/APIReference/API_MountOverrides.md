---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_MountOverrides.html
---

# MountOverrides
<a name="API_MountOverrides"></a>

Runtime mount overrides applied to a single pipeline execution. Overrides are transient — they do not modify the stored task configuration.

## Contents
<a name="API_MountOverrides_Contents"></a>

 ** computeNodes **   <a name="iotsitewise-Type-MountOverrides-computeNodes"></a>
The mount overrides for each compute node, keyed by compute node name.
Type: String to array of [Mount](API_Mount.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[a-zA-Z0-9_-]+`
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_MountOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/MountOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/MountOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/MountOverrides)
