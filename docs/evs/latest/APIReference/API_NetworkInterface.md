---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

An elastic network interface (ENI) that connects hosts to the VLAN subnets. Amazon EVS provisions two identically configured ENIs in the VMkernel management subnet during host creation. One ENI is active, and the other is in standby mode for automatic switchover during a failure scenario.

## Contents
<a name="API_NetworkInterface_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** networkInterfaceId **   <a name="evs-Type-NetworkInterface-networkInterfaceId"></a>
The unique ID of the elastic network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/NetworkInterface)
