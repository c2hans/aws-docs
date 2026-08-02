---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkRunConfiguration.html
---

# FlinkRunConfiguration
<a name="API_FlinkRunConfiguration"></a>

Describes the starting parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_FlinkRunConfiguration_Contents"></a>

 ** AllowNonRestoredState **   <a name="APIReference-Type-FlinkRunConfiguration-AllowNonRestoredState"></a>
When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see [ Allowing Non-Restored State](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/savepoints/#allowing-non-restored-state) in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/).
This value defaults to `false`. If you update your application without specifying this parameter, `AllowNonRestoredState` will be set to `false`, even if it was previously set to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_FlinkRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/FlinkRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/FlinkRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/FlinkRunConfiguration)
