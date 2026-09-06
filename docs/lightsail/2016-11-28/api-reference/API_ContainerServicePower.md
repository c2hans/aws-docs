---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServicePower.html
---

# ContainerServicePower
<a name="API_ContainerServicePower"></a>

Describes the powers that can be specified for an Amazon Lightsail container service.

The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.

## Contents
<a name="API_ContainerServicePower_Contents"></a>

 ** cpuCount **   <a name="Lightsail-Type-ContainerServicePower-cpuCount"></a>
The number of vCPUs included in the power.
Type: Float
Required: No

 ** isActive **   <a name="Lightsail-Type-ContainerServicePower-isActive"></a>
A Boolean value indicating whether the power is active and can be specified for container services.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-ContainerServicePower-name"></a>
The friendly name of the power (`nano`).
Type: String
Required: No

 ** powerId **   <a name="Lightsail-Type-ContainerServicePower-powerId"></a>
The ID of the power (`nano-1`).
Type: String
Required: No

 ** price **   <a name="Lightsail-Type-ContainerServicePower-price"></a>
The monthly price of the power in USD.
Type: Float
Required: No

 ** ramSizeInGb **   <a name="Lightsail-Type-ContainerServicePower-ramSizeInGb"></a>
The amount of RAM (in GB) of the power.
Type: Float
Required: No

## See Also
<a name="API_ContainerServicePower_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServicePower)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServicePower)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServicePower)
