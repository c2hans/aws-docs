---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html
---

# ModifyInstanceAttribute
<a name="API_ModifyInstanceAttribute"></a>

Modifies the specified attribute of the specified instance. You can specify only one attribute at a time.

 **Note: **Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the [ModifyNetworkInterfaceAttribute](API_ModifyNetworkInterfaceAttribute.md) action.

To modify some attributes, the instance must be stopped. For more information, see [Modify a stopped instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingAttributesWhileInstanceStopped.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyInstanceAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The name of the attribute to modify.
When changing the instance type: If the original instance type is configured for configurable bandwidth, and the desired instance type doesn't support configurable bandwidth, first set the existing bandwidth configuration to `default` using the [ModifyInstanceNetworkPerformanceOptions](API_ModifyInstanceNetworkPerformanceOptions.md) operation.
Type: String
Valid Values: `disableApiTermination | instanceType | kernel | ramdisk | instanceInitiatedShutdownBehavior | blockDeviceMapping | userData | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport | enaSupport | nvmeSupport | disableApiStop | enclaveOptions`
Required: No

 **BlockDeviceMapping.N**
Modifies the `DeleteOnTermination` attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for `DeleteOnTermination`, the default is `true` and the volume is deleted when the instance is terminated. You can't modify the `DeleteOnTermination` attribute for volumes that are attached to AWS-managed resources.
To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see [Update the block device mapping when launching an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#Using_OverridingAMIBDM) in the *Amazon EC2 User Guide*.
Type: Array of [InstanceBlockDeviceMappingSpecification](API_InstanceBlockDeviceMappingSpecification.md) objects
Required: No

 **DisableApiStop**
Indicates whether an instance is enabled for stop protection. For more information, see [Enable stop protection for your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html).

Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **DisableApiTermination**
Enable or disable termination protection for the instance. If the value is `true`, you can't terminate the instance using the Amazon EC2 console, command line interface, or API. You can't enable termination protection for Spot Instances.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EbsOptimized**
Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnaSupport**
Set to `true` to enable enhanced networking with ENA for the instance.
This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **GroupId.N**
Replaces the security groups of the instance with the specified security groups. You must specify the ID of at least one security group, even if it's just the default security group for the VPC.
Type: Array of strings
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **InstanceInitiatedShutdownBehavior**
Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **InstanceType**
Changes the instance type to the specified value. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*. If the instance type is not valid, the error returned is `InvalidInstanceAttributeValue`.
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **Kernel**
Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html).
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **Ramdisk**
Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html).
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **SourceDestCheck**
Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is `true`, source/destination checks are enabled; otherwise, they are disabled. The default value is `true`. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **SriovNetSupport**
Set to `simple` to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.
There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.
This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **UserData**
Changes the instance's user data to the specified value. User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64-encoding might be performed for you. For more information, see [Work with instance user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html).
Type: [SecureBlobAttributeValue](API_SecureBlobAttributeValue.md) object
Required: No

 **Value**
A new value for the attribute. Use only with the `kernel`, `ramdisk`, `userData`, `disableApiTermination`, or `instanceInitiatedShutdownBehavior` attribute.
Type: String
Required: No

## Response Elements
<a name="API_ModifyInstanceAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyInstanceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyInstanceAttribute_Examples"></a>

### Example 1
<a name="API_ModifyInstanceAttribute_Example_1"></a>

This example changes the `instanceType` attribute of the specified instance. The instance must be in the `stopped` state.

#### Sample Request
<a name="API_ModifyInstanceAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceAttribute
&InstanceId=i-1234567890abcdef0
&InstanceType.Value=m1.small
&AUTHPARAMS
```

### Example 2
<a name="API_ModifyInstanceAttribute_Example_2"></a>

This example changes the `enaSupport` attribute of the specified instance.

#### Sample Request
<a name="API_ModifyInstanceAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceAttribute
&InstanceId=i-1234567890abcdef0
&EnaSupport.Value=true
&AUTHPARAMS
```

### Example 3
<a name="API_ModifyInstanceAttribute_Example_3"></a>

This example changes the `ebsOptimized` attribute of the specified instance.

#### Sample Request
<a name="API_ModifyInstanceAttribute_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceAttribute
&InstanceId=i-1234567890abcdef0
&EbsOptimized.Value=true
&AUTHPARAMS
```

### Example 4
<a name="API_ModifyInstanceAttribute_Example_4"></a>

This example changes the `instanceInitiatedShutdownBehavior` attribute of the specified instance.

#### Sample Request
<a name="API_ModifyInstanceAttribute_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceAttribute
&InstanceId=i-1234567890abcdef0
&InstanceInitiatedShutdownBehavior.Value=terminate
&AUTHPARAMS
```

### Example 5
<a name="API_ModifyInstanceAttribute_Example_5"></a>

This example changes the `disableApiTermination` attribute of the specified instance.

#### Sample Request
<a name="API_ModifyInstanceAttribute_Example_5_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceAttribute
&InstanceId=i-1234567890abcdef0
&DisableApiTermination.Value=true
&AUTHPARAMS
```

## See Also
<a name="API_ModifyInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
