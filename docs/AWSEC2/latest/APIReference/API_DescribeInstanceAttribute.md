---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceAttribute.html
---

# DescribeInstanceAttribute
<a name="API_DescribeInstanceAttribute"></a>

Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Available attributes include SQL license exemption configuration for instances registered with the SQL LE service.

## Request Parameters
<a name="API_DescribeInstanceAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The instance attribute.
Note that the `enaSupport` attribute is not supported.
Type: String
Valid Values: `instanceType | kernel | ramdisk | userData | disableApiTermination | instanceInitiatedShutdownBehavior | rootDeviceName | blockDeviceMapping | productCodes | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport | enaSupport | enclaveOptions | disableApiStop`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeInstanceAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **blockDeviceMapping**
The block device mapping of the instance.
Type: Array of [InstanceBlockDeviceMapping](API_InstanceBlockDeviceMapping.md) objects

 **disableApiStop**
Indicates whether stop protection is enabled for the instance.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **disableApiTermination**
Indicates whether termination protection is enabled. If the value is `true`, you can't terminate the instance using the Amazon EC2 console, command line tools, or API.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **ebsOptimized**
Indicates whether the instance is optimized for Amazon EBS I/O.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **enaSupport**
Indicates whether enhanced networking with ENA is enabled.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **enclaveOptions**
Indicates whether the instance is enabled for AWS Nitro Enclaves.
Type: [EnclaveOptions](API_EnclaveOptions.md) object

 **groupSet**
The security groups associated with the instance.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects

 **instanceId**
The ID of the instance.
Type: String

 **instanceInitiatedShutdownBehavior**
Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
Type: [AttributeValue](API_AttributeValue.md) object

 **instanceType**
The instance type.
Type: [AttributeValue](API_AttributeValue.md) object

 **kernel**
The kernel ID.
Type: [AttributeValue](API_AttributeValue.md) object

 **productCodes**
The product codes.
Type: Array of [ProductCode](API_ProductCode.md) objects

 **ramdisk**
The RAM disk ID.
Type: [AttributeValue](API_AttributeValue.md) object

 **requestId**
The ID of the request.
Type: String

 **rootDeviceName**
The device name of the root device volume (for example, `/dev/sda1`).
Type: [AttributeValue](API_AttributeValue.md) object

 **sourceDestCheck**
Indicates whether source/destination checks are enabled.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **sriovNetSupport**
Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
Type: [AttributeValue](API_AttributeValue.md) object

 **userData**
The user data.
Type: [AttributeValue](API_AttributeValue.md) object

## Errors
<a name="API_DescribeInstanceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeInstanceAttribute_Examples"></a>

### Example 1
<a name="API_DescribeInstanceAttribute_Example_1"></a>

This example lists the instance type of the specified instance.

#### Sample Request
<a name="API_DescribeInstanceAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeInstanceAttribute
&InstanceId=i-1234567890abcdef0
&Attribute=instanceType
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceAttribute_Example_1_Response"></a>

```
<DescribeInstanceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <instanceType>
    <value>t1.micro</value>
  </instanceType>
</DescribeInstanceAttributeResponse>
```

### Example 2
<a name="API_DescribeInstanceAttribute_Example_2"></a>

This example lists the current value of the `InstanceInitiatedShutdownBehavior` attribute for the specified instance.

#### Sample Request
<a name="API_DescribeInstanceAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeInstanceAttribute
&InstanceId=i-1234567890abcdef0
&Attribute=instanceInitiatedShutdownBehavior
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceAttribute_Example_2_Response"></a>

```
<DescribeInstanceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <instanceInitiatedShutdownBehavior>
    <value>stop</value>
  </instanceInitiatedShutdownBehavior>
</DescribeInstanceAttributeResponse>
```

### Example 3
<a name="API_DescribeInstanceAttribute_Example_3"></a>

This example lists the current value of the `DisableApiTermination` attribute for the specified instance.

#### Sample Request
<a name="API_DescribeInstanceAttribute_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeInstanceAttribute
&InstanceId=i-1234567890abcdef0
&Attribute=disableApiTermination
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceAttribute_Example_3_Response"></a>

```
<DescribeInstanceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <disableApiTermination>
    <value>false</value>
  </disableApiTermination>
</DescribeInstanceAttributeResponse>
```

## See Also
<a name="API_DescribeInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceAttribute)
