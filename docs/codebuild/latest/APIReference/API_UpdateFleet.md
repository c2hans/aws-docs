---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateFleet.html
---

# UpdateFleet
<a name="API_UpdateFleet"></a>

Updates a compute fleet.

## Request Syntax
<a name="API_UpdateFleet_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "baseCapacity": {{number}},
   "computeConfiguration": {
      "disk": {{number}},
      "instanceType": "{{string}}",
      "machineType": "{{string}}",
      "memory": {{number}},
      "vCpu": {{number}}
   },
   "computeType": "{{string}}",
   "environmentType": "{{string}}",
   "fleetServiceRole": "{{string}}",
   "imageId": "{{string}}",
   "overflowBehavior": "{{string}}",
   "proxyConfiguration": {
      "defaultBehavior": "{{string}}",
      "orderedProxyRules": [
         {
            "effect": "{{string}}",
            "entities": [ "{{string}}" ],
            "type": "{{string}}"
         }
      ]
   },
   "scalingConfiguration": {
      "maxCapacity": {{number}},
      "scalingType": "{{string}}",
      "targetTrackingScalingConfigs": [
         {
            "metricType": "{{string}}",
            "targetValue": {{number}}
         }
      ]
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "vpcConfig": {
      "securityGroupIds": [ "{{string}}" ],
      "subnets": [ "{{string}}" ],
      "vpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [arn](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-arn"></a>
The ARN of the compute fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [baseCapacity](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-baseCapacity"></a>
The initial number of machines allocated to the compute ﬂeet, which deﬁnes the number of builds that can run in parallel.
Type: Integer
Required: No

 ** [computeConfiguration](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-computeConfiguration"></a>
The compute configuration of the compute fleet. This is only required if `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` or `CUSTOM_INSTANCE_TYPE`.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
Required: No

 ** [computeType](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-computeType"></a>
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

 ** [environmentType](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-environmentType"></a>
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

 ** [fleetServiceRole](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-fleetServiceRole"></a>
The service role associated with the compute fleet. For more information, see [ Allow a user to add a permission policy for a fleet service role](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html) in the * AWS CodeBuild User Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [imageId](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-imageId"></a>
The Amazon Machine Image (AMI) of the compute fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [overflowBehavior](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-overflowBehavior"></a>
The compute fleet overflow behavior.
+ For overflow behavior `QUEUE`, your overflow builds need to wait on the existing fleet instance to become available.
+ For overflow behavior `ON_DEMAND`, your overflow builds run on CodeBuild on-demand.
**Note**
If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see [Example policy statement to allow CodeBuild access to AWS services required to create a VPC network interface](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface).
Type: String
Valid Values: `QUEUE | ON_DEMAND`
Required: No

 ** [proxyConfiguration](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-proxyConfiguration"></a>
The proxy configuration of the compute fleet.
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object
Required: No

 ** [scalingConfiguration](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-scalingConfiguration"></a>
The scaling configuration of the compute fleet.
Type: [ScalingConfigurationInput](API_ScalingConfigurationInput.md) object
Required: No

 ** [tags](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-tags"></a>
A list of tag key and value pairs associated with this compute fleet.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [vpcConfig](#API_UpdateFleet_RequestSyntax) **   <a name="CodeBuild-UpdateFleet-request-vpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateFleet_ResponseSyntax"></a>

```
{
   "fleet": {
      "arn": "string",
      "baseCapacity": number,
      "computeConfiguration": {
         "disk": number,
         "instanceType": "string",
         "machineType": "string",
         "memory": number,
         "vCpu": number
      },
      "computeType": "string",
      "created": number,
      "environmentType": "string",
      "fleetServiceRole": "string",
      "id": "string",
      "imageId": "string",
      "lastModified": number,
      "name": "string",
      "overflowBehavior": "string",
      "proxyConfiguration": {
         "defaultBehavior": "string",
         "orderedProxyRules": [
            {
               "effect": "string",
               "entities": [ "string" ],
               "type": "string"
            }
         ]
      },
      "scalingConfiguration": {
         "desiredCapacity": number,
         "maxCapacity": number,
         "scalingType": "string",
         "targetTrackingScalingConfigs": [
            {
               "metricType": "string",
               "targetValue": number
            }
         ]
      },
      "status": {
         "context": "string",
         "message": "string",
         "statusCode": "string"
      },
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fleet](#API_UpdateFleet_ResponseSyntax) **   <a name="CodeBuild-UpdateFleet-response-fleet"></a>
A `Fleet` object.
Type: [Fleet](API_Fleet.md) object

## Errors
<a name="API_UpdateFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountLimitExceededException **
An AWS service limit was exceeded for the calling AWS account.
HTTP Status Code: 400

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/UpdateFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/UpdateFleet)
