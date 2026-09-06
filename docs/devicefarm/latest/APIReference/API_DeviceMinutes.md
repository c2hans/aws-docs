---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceMinutes.html
---

# DeviceMinutes
<a name="API_DeviceMinutes"></a>

Represents the total (metered or unmetered) minutes used by the resource to run tests. Contains the sum of minutes consumed by all children.

## Contents
<a name="API_DeviceMinutes_Contents"></a>

 ** metered **   <a name="devicefarm-Type-DeviceMinutes-metered"></a>
When specified, represents only the sum of metered minutes used by the resource to run tests.
Type: Double
Required: No

 ** total **   <a name="devicefarm-Type-DeviceMinutes-total"></a>
When specified, represents the total minutes used by the resource to run tests.
Type: Double
Required: No

 ** unmetered **   <a name="devicefarm-Type-DeviceMinutes-unmetered"></a>
When specified, represents only the sum of unmetered minutes used by the resource to run tests.
Type: Double
Required: No

## See Also
<a name="API_DeviceMinutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceMinutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceMinutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceMinutes)
