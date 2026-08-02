---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_NetworkAccessConfiguration.html
---

# NetworkAccessConfiguration
<a name="API_NetworkAccessConfiguration"></a>

Describes the network details of a WorkSpaces Pool.

## Contents
<a name="API_NetworkAccessConfiguration_Contents"></a>

 ** EniId **   <a name="WorkSpaces-Type-NetworkAccessConfiguration-EniId"></a>
The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** EniPrivateIpAddress **   <a name="WorkSpaces-Type-NetworkAccessConfiguration-EniPrivateIpAddress"></a>
The private IP address of the elastic network interface that is attached to instances in your VPC.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_NetworkAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/NetworkAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/NetworkAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/NetworkAccessConfiguration)
