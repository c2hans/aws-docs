---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceHealthStatus.html
---

# InstanceHealthStatus
<a name="API_InstanceHealthStatus"></a>

Describes the status of an Amazon Lightsail instance.

## Contents
<a name="API_InstanceHealthStatus_Contents"></a>

 ** details **   <a name="Lightsail-Type-InstanceHealthStatus-details"></a>
The system instance health or instance health.
Type: Array of [InstanceHealthStatusDetail](API_InstanceHealthStatusDetail.md) objects
Required: No

 ** status **   <a name="Lightsail-Type-InstanceHealthStatus-status"></a>
The status.
The following values are possible:
+  `ok` - All checks are passing. The instance is reachable.
+  `impaired` - One or more checks have failed.
+  `initializing` - The instance was recently started, and the checks are in progress.
+  `insufficient-data` - There isn't enough data yet to determine the result.
+  `not-applicable` - The check doesn't apply because the instance isn't running.
Type: String
Valid Values: `ok | impaired | initializing | insufficient-data | not-applicable`
Required: No

## See Also
<a name="API_InstanceHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceHealthStatus)
