---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DockerServer.html
---

# DockerServer
<a name="API_DockerServer"></a>

Contains docker server information.

## Contents
<a name="API_DockerServer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** computeType **   <a name="CodeBuild-Type-DockerServer-computeType"></a>
Information about the compute resources the docker server uses. Available values include:
+  `BUILD_GENERAL1_SMALL`: Use up to 4 GiB memory and 2 vCPUs for your docker server.
+  `BUILD_GENERAL1_MEDIUM`: Use up to 8 GiB memory and 4 vCPUs for your docker server.
+  `BUILD_GENERAL1_LARGE`: Use up to 16 GiB memory and 8 vCPUs for your docker server.
+  `BUILD_GENERAL1_XLARGE`: Use up to 64 GiB memory and 32 vCPUs for your docker server.
+  `BUILD_GENERAL1_2XLARGE`: Use up to 128 GiB memory and 64 vCPUs for your docker server.
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | BUILD_LAMBDA_1GB | BUILD_LAMBDA_2GB | BUILD_LAMBDA_4GB | BUILD_LAMBDA_8GB | BUILD_LAMBDA_10GB | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
Required: Yes

 ** securityGroupIds **   <a name="CodeBuild-Type-DockerServer-securityGroupIds"></a>
A list of one or more security groups IDs.
Security groups configured for Docker servers should allow ingress network traffic from the VPC configured in the project. They should allow ingress on port 9876.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: No

 ** status **   <a name="CodeBuild-Type-DockerServer-status"></a>
A DockerServerStatus object to use for this docker server.
Note that `status` is only an output and cannot be passed in as an input.
Type: [DockerServerStatus](API_DockerServerStatus.md) object
Required: No

## See Also
<a name="API_DockerServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DockerServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DockerServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DockerServer)
