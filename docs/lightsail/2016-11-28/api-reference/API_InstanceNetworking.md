---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceNetworking.html
---

# InstanceNetworking
<a name="API_InstanceNetworking"></a>

Describes monthly data transfer rates and port information for an instance.

## Contents
<a name="API_InstanceNetworking_Contents"></a>

 ** monthlyTransfer **   <a name="Lightsail-Type-InstanceNetworking-monthlyTransfer"></a>
The amount of data in GB allocated for monthly data transfers.
Type: [MonthlyTransfer](API_MonthlyTransfer.md) object
Required: No

 ** ports **   <a name="Lightsail-Type-InstanceNetworking-ports"></a>
An array of key-value pairs containing information about the ports on the instance.
Type: Array of [InstancePortInfo](API_InstancePortInfo.md) objects
Required: No

## See Also
<a name="API_InstanceNetworking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceNetworking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceNetworking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceNetworking)
