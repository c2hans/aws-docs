---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_VersionInfo.html
---

# VersionInfo
<a name="API_VersionInfo"></a>

The Docker and Amazon ECS container agent version information about a container instance.

## Contents
<a name="API_VersionInfo_Contents"></a>

 ** agentHash **   <a name="ECS-Type-VersionInfo-agentHash"></a>
The Git commit hash for the Amazon ECS container agent build on the [amazon-ecs-agent ](https://github.com/aws/amazon-ecs-agent) GitHub repository.
Type: String
Required: No

 ** agentVersion **   <a name="ECS-Type-VersionInfo-agentVersion"></a>
The version number of the Amazon ECS container agent.
Type: String
Required: No

 ** dockerVersion **   <a name="ECS-Type-VersionInfo-dockerVersion"></a>
The Docker version that's running on the container instance.
Type: String
Required: No

## See Also
<a name="API_VersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/VersionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/VersionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/VersionInfo)
