---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MovingAddressStatus.html
---

# MovingAddressStatus
<a name="API_MovingAddressStatus"></a>

**Note**
This action is deprecated.

Describes the status of a moving Elastic IP address.

## Contents
<a name="API_MovingAddressStatus_Contents"></a>

 ** moveStatus **
The status of the Elastic IP address that's being moved or restored.
Type: String
Valid Values: `movingToVpc | restoringToClassic`
Required: No

 ** publicIp **
The Elastic IP address.
Type: String
Required: No

## See Also
<a name="API_MovingAddressStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MovingAddressStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MovingAddressStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MovingAddressStatus)
