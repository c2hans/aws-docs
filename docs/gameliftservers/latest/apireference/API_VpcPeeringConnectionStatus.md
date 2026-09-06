---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_VpcPeeringConnectionStatus.html
---

# VpcPeeringConnectionStatus
<a name="API_VpcPeeringConnectionStatus"></a>

Represents status information for a VPC peering connection. Status codes and messages are provided from EC2 (see [VpcPeeringConnectionStateReason](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnectionStateReason.html)). Connection status information is also communicated as a fleet event.

## Contents
<a name="API_VpcPeeringConnectionStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="gameliftservers-Type-VpcPeeringConnectionStatus-Code"></a>
Code indicating the status of a VPC peering connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Message **   <a name="gameliftservers-Type-VpcPeeringConnectionStatus-Message"></a>
Additional messaging associated with the connection status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VpcPeeringConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/VpcPeeringConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/VpcPeeringConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/VpcPeeringConnectionStatus)
