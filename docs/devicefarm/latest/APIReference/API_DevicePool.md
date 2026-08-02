---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DevicePool.html
---

# DevicePool
<a name="API_DevicePool"></a>

Represents a collection of device types.

## Contents
<a name="API_DevicePool_Contents"></a>

 ** arn **   <a name="devicefarm-Type-DevicePool-arn"></a>
The device pool's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** description **   <a name="devicefarm-Type-DevicePool-description"></a>
The device pool's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** maxDevices **   <a name="devicefarm-Type-DevicePool-maxDevices"></a>
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the `rules` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.
Type: Integer
Required: No

 ** name **   <a name="devicefarm-Type-DevicePool-name"></a>
The device pool's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** rules **   <a name="devicefarm-Type-DevicePool-rules"></a>
Information about the device pool's rules.
Type: Array of [Rule](API_Rule.md) objects
Required: No

 ** type **   <a name="devicefarm-Type-DevicePool-type"></a>
The device pool's type.
Allowed values include:
+ CURATED: A device pool that is created and managed by AWS Device Farm.
+ PRIVATE: A device pool that is created and managed by the device pool developer.
Type: String
Valid Values: `CURATED | PRIVATE`
Required: No

## See Also
<a name="API_DevicePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DevicePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DevicePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DevicePool)
