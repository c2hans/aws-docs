---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyReservedInstances.html
---

# ModifyReservedInstances
<a name="API_ModifyReservedInstances"></a>

Modifies the configuration of your Reserved Instances, such as the Availability Zone, instance count, or instance type. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type.

For more information, see [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyReservedInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **ReservedInstancesConfigurationSetItemType.N**
The configuration settings for the Reserved Instances to modify.
Type: Array of [ReservedInstancesConfiguration](API_ReservedInstancesConfiguration.md) objects
Required: Yes

 **ReservedInstancesId.N**
The IDs of the Reserved Instances to modify.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_ModifyReservedInstances_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesModificationId**
The ID for the modification.
Type: String

## Errors
<a name="API_ModifyReservedInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyReservedInstances_Examples"></a>

### Example
<a name="API_ModifyReservedInstances_Example_1"></a>

This example illustrates one usage of ModifyReservedInstances.

#### Sample Request
<a name="API_ModifyReservedInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyReservedInstances
&ClientToken=myClientToken
&ReservedInstancesConfigurationSetItemType.1.AvailabilityZone=us-east-1a
&ReservedInstancesConfigurationSetItemType.1.InstanceCount=1
&ReservedInstancesConfigurationSetItemType.1.Platform=EC2-VPC
&ReservedInstancesConfigurationSetItemType.1.InstanceType=m1.small
&ReservedInstancesId.1=d16f7a91-4d0f-4f19-9d7f-a74d26b1ccfa
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyReservedInstances_Example_1_Response"></a>

```
<ModifyReservedInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>bef729b6-0731-4489-8881-2258746ae163</requestId>
<reservedInstancesModificationId>rimod-3aae219d-3d63-47a9-a7e9-e764example</reservedInstancesModificationId>
</ModifyReservedInstancesResponse>
```

## See Also
<a name="API_ModifyReservedInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyReservedInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyReservedInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
