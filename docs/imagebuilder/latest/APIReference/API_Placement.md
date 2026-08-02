---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Placement.html
---

# Placement
<a name="API_Placement"></a>

By default, EC2 instances run on shared tenancy hardware. This means that multiple AWS accounts might share the same physical hardware. When you use dedicated hardware, the physical server that hosts your instances is dedicated to your AWS account. Instance placement settings contain the details for the physical hardware where instances that Image Builder launches during image creation will run.

## Contents
<a name="API_Placement_Contents"></a>

 ** availabilityZone **   <a name="imagebuilder-Type-Placement-availabilityZone"></a>
The Availability Zone where your build and test instances will launch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** hostId **   <a name="imagebuilder-Type-Placement-hostId"></a>
The ID of the Dedicated Host on which build and test instances run. This only applies if `tenancy` is `host`. If you specify the host ID, you must not specify the resource group ARN. If you specify both, Image Builder returns an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** hostResourceGroupArn **   <a name="imagebuilder-Type-Placement-hostResourceGroupArn"></a>
The Amazon Resource Name (ARN) of the host resource group in which to launch build and test instances. This only applies if `tenancy` is `host`. If you specify the resource group ARN, you must not specify the host ID. If you specify both, Image Builder returns an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** tenancy **   <a name="imagebuilder-Type-Placement-tenancy"></a>
The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware. An instance with a tenancy of `host` runs on a Dedicated Host.
If tenancy is set to `host`, then you can optionally specify one target for placement – either host ID or host resource group ARN. If automatic placement is enabled for your host, and you don't specify any placement target, Amazon EC2 will try to find an available host for your build and test instances.
Type: String
Valid Values: `default | dedicated | host`
Required: No

## See Also
<a name="API_Placement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Placement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Placement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Placement)
