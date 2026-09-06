---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkInterfaceCountRequest.html
---

# NetworkInterfaceCountRequest
<a name="API_NetworkInterfaceCountRequest"></a>

The minimum and maximum number of network interfaces for instance type selection. This is useful for workloads that require multiple network interfaces.

## Contents
<a name="API_NetworkInterfaceCountRequest_Contents"></a>

 ** max **   <a name="ECS-Type-NetworkInterfaceCountRequest-max"></a>
The maximum number of network interfaces. Instance types that support more network interfaces are excluded from selection.
Type: Integer
Required: No

 ** min **   <a name="ECS-Type-NetworkInterfaceCountRequest-min"></a>
The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection.
Type: Integer
Required: No

## See Also
<a name="API_NetworkInterfaceCountRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/NetworkInterfaceCountRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/NetworkInterfaceCountRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/NetworkInterfaceCountRequest)
