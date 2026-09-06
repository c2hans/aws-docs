---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_InstanceState.html
---

# InstanceState
<a name="API_devicemanagement_InstanceState"></a>

The description of the current state of an instance.

## Contents
<a name="API_devicemanagement_InstanceState_Contents"></a>

 ** code **   <a name="Snowball-Type-devicemanagement_InstanceState-code"></a>
The state of the instance as a 16-bit unsigned integer.
The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.
The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.
The valid values for the instance state code are all in the range of the low byte. These values are:
+  `0` : `pending`
+  `16` : `running`
+  `32` : `shutting-down`
+  `48` : `terminated`
+  `64` : `stopping`
+  `80` : `stopped`
You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.
Type: Integer
Required: No

 ** name **   <a name="Snowball-Type-devicemanagement_InstanceState-name"></a>
The current state of the instance.
Type: String
Valid Values: `PENDING | RUNNING | SHUTTING_DOWN | TERMINATED | STOPPING | STOPPED`
Required: No

## See Also
<a name="API_devicemanagement_InstanceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/InstanceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/InstanceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/InstanceState)
