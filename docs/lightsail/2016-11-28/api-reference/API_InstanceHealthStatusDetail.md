---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceHealthStatusDetail.html
---

# InstanceHealthStatusDetail
<a name="API_InstanceHealthStatusDetail"></a>

Describes the instance status.

## Contents
<a name="API_InstanceHealthStatusDetail_Contents"></a>

 ** impairedSince **   <a name="Lightsail-Type-InstanceHealthStatusDetail-impairedSince"></a>
The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.
Type: Timestamp
Required: No

 ** name **   <a name="Lightsail-Type-InstanceHealthStatusDetail-name"></a>
The type of instance status. The only possible value is `reachability`.
Type: String
Valid Values: `reachability`
Required: No

 ** status **   <a name="Lightsail-Type-InstanceHealthStatusDetail-status"></a>
The status.
The following values are possible:
+  `passed` - The check passed.
+  `failed` - The check failed.
+  `initializing` - The check is in progress.
+  `insufficient-data` - There isn't enough data yet to determine the result.
Type: String
Valid Values: `passed | failed | insufficient-data | initializing`
Required: No

## See Also
<a name="API_InstanceHealthStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceHealthStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceHealthStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceHealthStatusDetail)
