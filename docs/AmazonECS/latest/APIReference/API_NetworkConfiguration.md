---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

The network configuration for a task or service.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** awsvpcConfiguration **   <a name="ECS-Type-NetworkConfiguration-awsvpcConfiguration"></a>
The VPC subnets and security groups that are associated with a task.
All specified subnets and security groups must be from the same VPC.
Type: [AwsVpcConfiguration](API_AwsVpcConfiguration.md) object
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/NetworkConfiguration)
