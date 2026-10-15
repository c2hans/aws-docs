---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GlobalAuroraUngraceful.html
---

# GlobalAuroraUngraceful
<a name="API_GlobalAuroraUngraceful"></a>

Configuration for an Aurora global database execution block in ungraceful mode.

## Contents
<a name="API_GlobalAuroraUngraceful_Contents"></a>

 ** ungraceful **   <a name="regionswitch-Type-GlobalAuroraUngraceful-ungraceful"></a>
The ungraceful behavior. The only valid value is `failover`, which calls `FailoverGlobalCluster` with `AllowDataLoss` set to `true` and might cause data loss.
Type: String
Valid Values: `failover`
Required: No

## See Also
<a name="API_GlobalAuroraUngraceful_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/GlobalAuroraUngraceful)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/GlobalAuroraUngraceful)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GlobalAuroraUngraceful)
