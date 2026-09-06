---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceImageInstanceTypeSpecification.html
---

# ReplaceImageInstanceTypeSpecification
<a name="API_ReplaceImageInstanceTypeSpecification"></a>

Replaces or removes the instance type specification for an AMI. The instance type specification defines which instance types are compatible with the AMI.

When you launch an instance using [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html), Amazon EC2 validates the requested instance type against the AMI's instance type specification. If the instance type is not compatible, the request fails with an `InvalidParameterCombination` error.

You can specify supported instance types, unsupported instance types, or both. The evaluation logic is as follows:
+ No specification set – all instance types are allowed.
+ Only `UnsupportedInstanceTypes` set – All instance types are allowed except those that match the unsupported list.
+  `SupportedInstanceTypes` set – The instance type must match the supported list and must not match the unsupported list.

Instance type entries support wildcard patterns using `*` (for example, `t3.*` matches all t3 sizes).

To remove an existing instance type specification, omit the `InstanceTypeSpecification` parameter or set it to `null`.

To set the instance type specification, you must be the AMI owner. You cannot set an instance type specification on an AMI that is listed in AWS Marketplace, and you cannot list an AMI in AWS Marketplace if it has an instance type specification set.

## Request Parameters
<a name="API_ReplaceImageInstanceTypeSpecification_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

 **InstanceTypeSpecification**
The instance type specification to set on the AMI. Omit this parameter to remove the existing instance type specification.
Type: [InstanceTypeSpecificationRequest](API_InstanceTypeSpecificationRequest.md) object
Required: No

## Response Elements
<a name="API_ReplaceImageInstanceTypeSpecification_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **returnValue**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ReplaceImageInstanceTypeSpecification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReplaceImageInstanceTypeSpecification_Examples"></a>

### Example: Set the instance type specification
<a name="API_ReplaceImageInstanceTypeSpecification_Example_1"></a>

This example request sets the instance type specification for the specified AMI so that all `t3` instance types are supported, except for `t3.nano`, which is unsupported.

#### Sample Request
<a name="API_ReplaceImageInstanceTypeSpecification_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReplaceImageInstanceTypeSpecification
&ImageId=ami-1234567890abcdef0
&InstanceTypeSpecification.SupportedInstanceType.1=t3.*
&InstanceTypeSpecification.UnsupportedInstanceType.1=t3.nano
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReplaceImageInstanceTypeSpecification_Example_1_Response"></a>

```
<ReplaceImageInstanceTypeSpecificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <returnValue>true</returnValue>
</ReplaceImageInstanceTypeSpecificationResponse>
```

### Example: Remove the instance type specification
<a name="API_ReplaceImageInstanceTypeSpecification_Example_2"></a>

This example request removes the existing instance type specification from the AMI by omitting the `InstanceTypeSpecification` parameter, which makes all instance types compatible with the AMI again.

#### Sample Request
<a name="API_ReplaceImageInstanceTypeSpecification_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReplaceImageInstanceTypeSpecification
&ImageId=ami-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReplaceImageInstanceTypeSpecification_Example_2_Response"></a>

```
<ReplaceImageInstanceTypeSpecificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <returnValue>true</returnValue>
</ReplaceImageInstanceTypeSpecificationResponse>
```

## See Also
<a name="API_ReplaceImageInstanceTypeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReplaceImageInstanceTypeSpecification)
