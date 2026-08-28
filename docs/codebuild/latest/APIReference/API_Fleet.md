---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Fleet.html
---

# Fleet
<a name="API_Fleet"></a>

A set of dedicated instances for your build environment.

## Contents
<a name="API_Fleet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-Fleet-arn"></a>
The ARN of the compute fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** baseCapacity **   <a name="CodeBuild-Type-Fleet-baseCapacity"></a>
The initial number of machines allocated to the compute ﬂeet, which deﬁnes the number of builds that can run in parallel.
Type: Integer
Required: No

 ** computeConfiguration **   <a name="CodeBuild-Type-Fleet-computeConfiguration"></a>
The compute configuration of the compute fleet. This is only required if `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` or `CUSTOM_INSTANCE_TYPE`.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
Required: No

 ** computeType **   <a name="CodeBuild-Type-Fleet-computeType"></a>
Information about the compute resources the compute fleet uses. Available values include:
+  `ATTRIBUTE_BASED_COMPUTE`: Specify the amount of vCPUs, memory, disk space, and the type of machine.
**Note**
 If you use `ATTRIBUTE_BASED_COMPUTE`, you must define your attributes by using `computeConfiguration`. CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see [Reserved capacity environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types) in the * AWS CodeBuild User Guide*.
+  `CUSTOM_INSTANCE_TYPE`: Specify the instance type for your compute fleet. For a list of supported instance types, see [Supported instance families ](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.instance-types) in the * AWS CodeBuild User Guide*.
+  `BUILD_GENERAL1_SMALL`: Use up to 4 GiB memory and 2 vCPUs for builds.
+  `BUILD_GENERAL1_MEDIUM`: Use up to 8 GiB memory and 4 vCPUs for builds.
+  `BUILD_GENERAL1_LARGE`: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.
+  `BUILD_GENERAL1_XLARGE`: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.
+  `BUILD_GENERAL1_2XLARGE`: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.
+  `BUILD_LAMBDA_1GB`: Use up to 1 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+  `BUILD_LAMBDA_2GB`: Use up to 2 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+  `BUILD_LAMBDA_4GB`: Use up to 4 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+  `BUILD_LAMBDA_8GB`: Use up to 8 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+  `BUILD_LAMBDA_10GB`: Use up to 10 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
 If you use `BUILD_GENERAL1_SMALL`:
+  For environment type `LINUX_CONTAINER`, you can use up to 4 GiB memory and 2 vCPUs for builds.
+  For environment type `LINUX_GPU_CONTAINER`, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.
+  For environment type `ARM_CONTAINER`, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.
 If you use `BUILD_GENERAL1_LARGE`:
+  For environment type `LINUX_CONTAINER`, you can use up to 16 GiB memory and 8 vCPUs for builds.
+  For environment type `LINUX_GPU_CONTAINER`, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
+  For environment type `ARM_CONTAINER`, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.
For more information, see [On-demand environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types) in the * AWS CodeBuild User Guide.*
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | BUILD_LAMBDA_1GB | BUILD_LAMBDA_2GB | BUILD_LAMBDA_4GB | BUILD_LAMBDA_8GB | BUILD_LAMBDA_10GB | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
Required: No

 ** created **   <a name="CodeBuild-Type-Fleet-created"></a>
The time at which the compute fleet was created.
Type: Timestamp
Required: No

 ** environmentType **   <a name="CodeBuild-Type-Fleet-environmentType"></a>
The environment type of the compute fleet.
+ The environment type `ARM_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), EU (Frankfurt), and South America (São Paulo).
+ The environment type `ARM_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_GPU_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), and Asia Pacific (Sydney).
+ The environment type `MAC_ARM` is available for Medium fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), and EU (Frankfurt)
+ The environment type `MAC_ARM` is available for Large fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), and Asia Pacific (Sydney).
+ The environment type `WINDOWS_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `WINDOWS_SERVER_2019_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai) and EU (Ireland).
+ The environment type `WINDOWS_SERVER_2022_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Tokyo), South America (São Paulo) and Asia Pacific (Mumbai).
For more information, see [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the * AWS CodeBuild user guide*.
Type: String
Valid Values: `WINDOWS_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER | WINDOWS_SERVER_2019_CONTAINER | WINDOWS_SERVER_2022_CONTAINER | LINUX_LAMBDA_CONTAINER | ARM_LAMBDA_CONTAINER | LINUX_EC2 | ARM_EC2 | WINDOWS_EC2 | MAC_ARM`
Required: No

 ** fleetServiceRole **   <a name="CodeBuild-Type-Fleet-fleetServiceRole"></a>
The service role associated with the compute fleet. For more information, see [ Allow a user to add a permission policy for a fleet service role](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html) in the * AWS CodeBuild User Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** id **   <a name="CodeBuild-Type-Fleet-id"></a>
The ID of the compute fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** imageId **   <a name="CodeBuild-Type-Fleet-imageId"></a>
The Amazon Machine Image (AMI) of the compute fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** lastModified **   <a name="CodeBuild-Type-Fleet-lastModified"></a>
The time at which the compute fleet was last modified.
Type: Timestamp
Required: No

 ** name **   <a name="CodeBuild-Type-Fleet-name"></a>
The name of the compute fleet.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,127}`
Required: No

 ** overflowBehavior **   <a name="CodeBuild-Type-Fleet-overflowBehavior"></a>
The compute fleet overflow behavior.
+ For overflow behavior `QUEUE`, your overflow builds need to wait on the existing fleet instance to become available.
+ For overflow behavior `ON_DEMAND`, your overflow builds run on CodeBuild on-demand.
**Note**
If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see [Example policy statement to allow CodeBuild access to AWS services required to create a VPC network interface](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface).
Type: String
Valid Values: `QUEUE | ON_DEMAND`
Required: No

 ** proxyConfiguration **   <a name="CodeBuild-Type-Fleet-proxyConfiguration"></a>
The proxy configuration of the compute fleet.
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object
Required: No

 ** scalingConfiguration **   <a name="CodeBuild-Type-Fleet-scalingConfiguration"></a>
The scaling configuration of the compute fleet.
Type: [ScalingConfigurationOutput](API_ScalingConfigurationOutput.md) object
Required: No

 ** status **   <a name="CodeBuild-Type-Fleet-status"></a>
The status of the compute fleet.
Type: [FleetStatus](API_FleetStatus.md) object
Required: No

 ** tags **   <a name="CodeBuild-Type-Fleet-tags"></a>
A list of tag key and value pairs associated with this compute fleet.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** vpcConfig **   <a name="CodeBuild-Type-Fleet-vpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Fleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Fleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Fleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Fleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
