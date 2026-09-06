---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerPortRange.html
---

# ContainerPortRange
<a name="API_ContainerPortRange"></a>

A set of one or more port numbers that can be opened on the container, and the supported network protocol.

 **Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

## Contents
<a name="API_ContainerPortRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FromPort **   <a name="gameliftservers-Type-ContainerPortRange-FromPort"></a>
A starting value for the range of allowed port numbers.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

 ** Protocol **   <a name="gameliftservers-Type-ContainerPortRange-Protocol"></a>
The network protocol that these ports support.
Type: String
Valid Values: `TCP | UDP`
Required: Yes

 ** ToPort **   <a name="gameliftservers-Type-ContainerPortRange-ToPort"></a>
An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

## See Also
<a name="API_ContainerPortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerPortRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerPortRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerPortRange)
