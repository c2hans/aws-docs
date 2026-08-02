---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_IpPermission.html
---

# IpPermission
<a name="API_IpPermission"></a>

A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet. Processes are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges.

For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically opens two port ranges, one for TCP messaging and one for UDP.

## Contents
<a name="API_IpPermission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FromPort **   <a name="gameliftservers-Type-IpPermission-FromPort"></a>
A starting value for a range of allowed port numbers.
For fleets using Linux builds, only ports `22` and `1026-60000` are valid.
For fleets using Windows builds, only ports `1026-60000` are valid.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

 ** IpRange **   <a name="gameliftservers-Type-IpPermission-IpRange"></a>
A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "`000.000.000.000/[subnet mask]`" or optionally the shortened version "`0.0.0.0/[subnet mask]`".
Type: String
Pattern: `[^\s]+`
Required: Yes

 ** Protocol **   <a name="gameliftservers-Type-IpPermission-Protocol"></a>
The network communication protocol used by the fleet.
Type: String
Valid Values: `TCP | UDP`
Required: Yes

 ** ToPort **   <a name="gameliftservers-Type-IpPermission-ToPort"></a>
An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort`.
For fleets using Linux builds, only ports `22` and `1026-60000` are valid.
For fleets using Windows builds, only ports `1026-60000` are valid.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

## See Also
<a name="API_IpPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/IpPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/IpPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/IpPermission)
