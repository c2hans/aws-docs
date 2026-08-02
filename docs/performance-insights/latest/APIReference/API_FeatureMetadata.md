---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_FeatureMetadata.html
---

# FeatureMetadata
<a name="API_FeatureMetadata"></a>

The metadata for a feature. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance.

## Contents
<a name="API_FeatureMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Status **   <a name="performanceinsights-Type-FeatureMetadata-Status"></a>
The status of the feature on the DB instance. Possible values include the following:
+  `ENABLED` - The feature is enabled on the instance.
+  `DISABLED` - The feature is disabled on the instance.
+  `UNSUPPORTED` - The feature isn't supported on the instance.
+  `ENABLED_PENDING_REBOOT` - The feature is enabled on the instance but requires a reboot to take effect.
+  `DISABLED_PENDING_REBOOT` - The feature is disabled on the instance but requires a reboot to take effect.
+  `UNKNOWN` - The feature status couldn't be determined.
Type: String
Valid Values: `ENABLED | DISABLED | UNSUPPORTED | ENABLED_PENDING_REBOOT | DISABLED_PENDING_REBOOT | UNKNOWN`
Required: No

## See Also
<a name="API_FeatureMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/FeatureMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/FeatureMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/FeatureMetadata)
