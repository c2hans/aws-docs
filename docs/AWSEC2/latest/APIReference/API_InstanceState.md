---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceState.html
---

# InstanceState
<a name="API_InstanceState"></a>

Describes the current state of an instance.

## Contents
<a name="API_InstanceState_Contents"></a>

 ** code **
The state of the instance as a 16-bit unsigned integer.
The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.
The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.
The valid values for instance-state-code will all be in the range of the low byte and they are:
+  `0` : `pending`
+  `16` : `running`
+  `32` : `shutting-down`
+  `48` : `terminated`
+  `64` : `stopping`
+  `80` : `stopped`
You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.
Type: Integer
Required: No

 ** name **
The current state of the instance.
Type: String
Valid Values: `pending | running | shutting-down | terminated | stopping | stopped`
Required: No

## See Also
<a name="API_InstanceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceState)
