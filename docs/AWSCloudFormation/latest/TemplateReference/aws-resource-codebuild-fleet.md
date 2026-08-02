---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-fleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet
<a name="aws-resource-codebuild-fleet"></a>

The `AWS::CodeBuild::Fleet` resource configures a compute fleet, a set of dedicated instances for your build environment.

## Syntax
<a name="aws-resource-codebuild-fleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-fleet-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::Fleet",
  "Properties" : {
      "[BaseCapacity](#cfn-codebuild-fleet-basecapacity)" : {{Integer}},
      "[ComputeConfiguration](#cfn-codebuild-fleet-computeconfiguration)" : {{ComputeConfiguration}},
      "[ComputeType](#cfn-codebuild-fleet-computetype)" : {{String}},
      "[EnvironmentType](#cfn-codebuild-fleet-environmenttype)" : {{String}},
      "[FleetProxyConfiguration](#cfn-codebuild-fleet-fleetproxyconfiguration)" : {{ProxyConfiguration}},
      "[FleetServiceRole](#cfn-codebuild-fleet-fleetservicerole)" : {{String}},
      "[FleetVpcConfig](#cfn-codebuild-fleet-fleetvpcconfig)" : {{VpcConfig}},
      "[ImageId](#cfn-codebuild-fleet-imageid)" : {{String}},
      "[Name](#cfn-codebuild-fleet-name)" : {{String}},
      "[OverflowBehavior](#cfn-codebuild-fleet-overflowbehavior)" : {{String}},
      "[ScalingConfiguration](#cfn-codebuild-fleet-scalingconfiguration)" : {{ScalingConfigurationInput}},
      "[Tags](#cfn-codebuild-fleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-fleet-syntax.yaml"></a>

```
Type: AWS::CodeBuild::Fleet
Properties:
  [BaseCapacity](#cfn-codebuild-fleet-basecapacity): {{Integer}}
  [ComputeConfiguration](#cfn-codebuild-fleet-computeconfiguration): {{
    ComputeConfiguration}}
  [ComputeType](#cfn-codebuild-fleet-computetype): {{String}}
  [EnvironmentType](#cfn-codebuild-fleet-environmenttype): {{String}}
  [FleetProxyConfiguration](#cfn-codebuild-fleet-fleetproxyconfiguration): {{
    ProxyConfiguration}}
  [FleetServiceRole](#cfn-codebuild-fleet-fleetservicerole): {{String}}
  [FleetVpcConfig](#cfn-codebuild-fleet-fleetvpcconfig): {{
    VpcConfig}}
  [ImageId](#cfn-codebuild-fleet-imageid): {{String}}
  [Name](#cfn-codebuild-fleet-name): {{String}}
  [OverflowBehavior](#cfn-codebuild-fleet-overflowbehavior): {{String}}
  [ScalingConfiguration](#cfn-codebuild-fleet-scalingconfiguration): {{
    ScalingConfigurationInput}}
  [Tags](#cfn-codebuild-fleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-codebuild-fleet-properties"></a>

`BaseCapacity`  <a name="cfn-codebuild-fleet-basecapacity"></a>
The initial number of machines allocated to the compute ﬂeet, which deﬁnes the number of builds that can run in parallel.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeConfiguration`  <a name="cfn-codebuild-fleet-computeconfiguration"></a>
The compute configuration of the compute fleet. This is only required if `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` or `CUSTOM_INSTANCE_TYPE`.
*Required*: No
*Type*: [ComputeConfiguration](aws-properties-codebuild-fleet-computeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeType`  <a name="cfn-codebuild-fleet-computetype"></a>
Information about the compute resources the compute fleet uses. Available values include:
+ `ATTRIBUTE_BASED_COMPUTE`: Specify the amount of vCPUs, memory, disk space, and the type of machine.
**Note**
 If you use `ATTRIBUTE_BASED_COMPUTE`, you must define your attributes by using `computeConfiguration`. AWS CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see [Reserved capacity environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types) in the *AWS CodeBuild User Guide*.
+ `BUILD_GENERAL1_SMALL`: Use up to 4 GiB memory and 2 vCPUs for builds.
+ `BUILD_GENERAL1_MEDIUM`: Use up to 8 GiB memory and 4 vCPUs for builds.
+ `BUILD_GENERAL1_LARGE`: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.
+ `BUILD_GENERAL1_XLARGE`: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.
+ `BUILD_GENERAL1_2XLARGE`: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.
+ `BUILD_LAMBDA_1GB`: Use up to 1 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+ `BUILD_LAMBDA_2GB`: Use up to 2 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+ `BUILD_LAMBDA_4GB`: Use up to 4 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+ `BUILD_LAMBDA_8GB`: Use up to 8 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
+ `BUILD_LAMBDA_10GB`: Use up to 10 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER`.
 If you use `BUILD_GENERAL1_SMALL`:
+  For environment type `LINUX_CONTAINER`, you can use up to 4 GiB memory and 2 vCPUs for builds.
+  For environment type `LINUX_GPU_CONTAINER`, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.
+  For environment type `ARM_CONTAINER`, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.
 If you use `BUILD_GENERAL1_LARGE`:
+  For environment type `LINUX_CONTAINER`, you can use up to 16 GiB memory and 8 vCPUs for builds.
+  For environment type `LINUX_GPU_CONTAINER`, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
+  For environment type `ARM_CONTAINER`, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.
For more information, see [On-demand environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types) in the *AWS CodeBuild User Guide.*
*Required*: No
*Type*: String
*Allowed values*: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentType`  <a name="cfn-codebuild-fleet-environmenttype"></a>
The environment type of the compute fleet.
+ The environment type `ARM_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), EU (Frankfurt), and South America (São Paulo).
+ The environment type `ARM_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `LINUX_GPU_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), and Asia Pacific (Sydney).
+ The environment type `MAC_ARM` is available only in regions US East (Ohio), US East (N. Virginia), US West (Oregon), Europe (Frankfurt), and Asia Pacific (Sydney).
+ The environment type `WINDOWS_EC2` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).
+ The environment type `WINDOWS_SERVER_2019_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai) and EU (Ireland).
+ The environment type `WINDOWS_SERVER_2022_CONTAINER` is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Tokyo), South America (São Paulo) and Asia Pacific (Mumbai).
For more information, see [Build environment compute types](https://docs.aws.amazon.com//codebuild/latest/userguide/build-env-ref-compute-types.html) in the *AWS CodeBuild user guide*.
*Required*: No
*Type*: String
*Allowed values*: `WINDOWS_SERVER_2019_CONTAINER | WINDOWS_SERVER_2022_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER | MAC_ARM | LINUX_EC2 | ARM_EC2 | WINDOWS_EC2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FleetProxyConfiguration`  <a name="cfn-codebuild-fleet-fleetproxyconfiguration"></a>
Information about the proxy configurations that apply network access control to your reserved capacity instances.
*Required*: No
*Type*: [ProxyConfiguration](aws-properties-codebuild-fleet-proxyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FleetServiceRole`  <a name="cfn-codebuild-fleet-fleetservicerole"></a>
The service role associated with the compute fleet. For more information, see [ Allow a user to add a permission policy for a fleet service role](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html) in the *AWS CodeBuild User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^(?:arn:)[a-zA-Z+-=,._:/@]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FleetVpcConfig`  <a name="cfn-codebuild-fleet-fleetvpcconfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
*Required*: No
*Type*: [VpcConfig](aws-properties-codebuild-fleet-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageId`  <a name="cfn-codebuild-fleet-imageid"></a>
The Amazon Machine Image (AMI) of the compute fleet.
*Required*: No
*Type*: String
*Pattern*: `^((aws/codebuild/([A-Za-z0-9._-]+|ami/[A-Za-z0-9._-]+):[A-Za-z0-9._-]+)|ami-[a-z0-9]{1,1020})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codebuild-fleet-name"></a>
The name of the compute fleet.
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverflowBehavior`  <a name="cfn-codebuild-fleet-overflowbehavior"></a>
The compute fleet overflow behavior.
+ For overflow behavior `QUEUE`, your overflow builds need to wait on the existing fleet instance to become available.
+ For overflow behavior `ON_DEMAND`, your overflow builds run on CodeBuild on-demand.
**Note**
If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see [Example policy statement to allow CodeBuild access to AWS services required to create a VPC network interface](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface).
*Required*: No
*Type*: String
*Allowed values*: `QUEUE | ON_DEMAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfiguration`  <a name="cfn-codebuild-fleet-scalingconfiguration"></a>
The scaling configuration of the compute fleet.
*Required*: No
*Type*: [ScalingConfigurationInput](aws-properties-codebuild-fleet-scalingconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-codebuild-fleet-tags"></a>
A list of tag key and value pairs associated with this compute fleet.
These tags are available for use by AWS services that support AWS CodeBuild compute fleet tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-codebuild-fleet-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codebuild-fleet-return-values"></a>

### Ref
<a name="aws-resource-codebuild-fleet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the AWS CodeBuild compute fleet.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codebuild-fleet-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codebuild-fleet-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the compute fleet.
