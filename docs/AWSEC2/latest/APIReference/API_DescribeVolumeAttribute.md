---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeAttribute.html
---

# DescribeVolumeAttribute
<a name="API_DescribeVolumeAttribute"></a>

Describes the specified attribute of the specified volume. You can specify only one attribute at a time.

For more information about EBS volumes, see [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_DescribeVolumeAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The attribute of the volume. This parameter is required.
Type: String
Valid Values: `autoEnableIO | productCodes`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VolumeId**
The ID of the volume.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeVolumeAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **autoEnableIO**
The state of `autoEnableIO` attribute.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **productCodes**
A list of product codes.
Type: Array of [ProductCode](API_ProductCode.md) objects

 **requestId**
The ID of the request.
Type: String

 **volumeId**
The ID of the volume.
Type: String

## Errors
<a name="API_DescribeVolumeAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVolumeAttribute_Examples"></a>

### Example
<a name="API_DescribeVolumeAttribute_Example_1"></a>

This example describes the `autoEnableIO` attribute of the volume vol-1234567890abcdef0.

#### Sample Request
<a name="API_DescribeVolumeAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumeAttribute
&Attribute=autoEnableIO
&VolumeId=vol-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVolumeAttribute_Example_1_Response"></a>

```
<DescribeVolumeAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
  <volumeId>vol-1234567890abcdef0</volumeId>
  <autoEnableIO>
    <value>false</value>
  </autoEnableIO>
</DescribeVolumeAttributeResponse>
```

### Example
<a name="API_DescribeVolumeAttribute_Example_2"></a>

This example describes the `productCodes` attribute of the volume vol-1234567890abcdef0.

#### Sample Request
<a name="API_DescribeVolumeAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumeAttribute
&Attribute=productCodes
&VolumeId=vol-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVolumeAttribute_Example_2_Response"></a>

```
<DescribeVolumeAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
  <volumeId>vol-1234567890abcdef0</volumeId>
  <productCodes>
      <item>
          <productCode>a1b2c3d4e5f6g7h8i9j10k11</productCode>
          <type>marketplace</type>
        </item>
  </productCodes>
</DescribeVolumeAttributeResponse>
```

## See Also
<a name="API_DescribeVolumeAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVolumeAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVolumeAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
