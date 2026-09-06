---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HostProperties.html
---

# HostProperties
<a name="API_HostProperties"></a>

Describes the properties of a Dedicated Host.

## Contents
<a name="API_HostProperties_Contents"></a>

 ** cores **
The number of cores on the Dedicated Host.
Type: Integer
Required: No

 ** instanceFamily **
The instance family supported by the Dedicated Host. For example, `m5`.
Type: String
Required: No

 ** instanceType **
The instance type supported by the Dedicated Host. For example, `m5.large`. If the host supports multiple instance types, no **instanceType** is returned.
Type: String
Required: No

 ** sockets **
The number of sockets on the Dedicated Host.
Type: Integer
Required: No

 ** totalVCpus **
The total number of vCPUs on the Dedicated Host.
Type: Integer
Required: No

## See Also
<a name="API_HostProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HostProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HostProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HostProperties)
