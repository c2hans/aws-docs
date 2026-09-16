---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html
---

# ImportInstance
<a name="API_ImportInstance"></a>

**Note**
We recommend that you use the [`ImportImage`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) API instead. For more information, see [Importing a VM as an image using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html) in the *VM Import/Export User Guide*.

Creates an import instance task using metadata from the specified disk image.

This API action supports only single-volume VMs. To import multi-volume VMs, use [ImportImage](API_ImportImage.md) instead.

For information about the import manifest referenced by this API action, see [VM Import Manifest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).

This API action is not supported by the AWS Command Line Interface (AWS CLI).

## Request Parameters
<a name="API_ImportInstance_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
A description for the instance being imported.
Type: String
Required: No

 **DiskImage.N**
The disk image.
Type: Array of [DiskImage](API_DiskImage.md) objects
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **LaunchSpecification**
The launch specification.
Type: [ImportInstanceLaunchSpecification](API_ImportInstanceLaunchSpecification.md) object
Required: No

 **Platform**
The instance operating system.
Type: String
Valid Values: `Windows`
Required: Yes

## Response Elements
<a name="API_ImportInstance_ResponseElements"></a>

The following elements are returned by the service.

 **conversionTask**
Information about the conversion task.
Type: [ConversionTask](API_ConversionTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ImportInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ImportInstance_Examples"></a>

### Example
<a name="API_ImportInstance_Example_1"></a>

This example creates an import instance task that migrates a Windows Server 2008 SP2 (32-bit) VM into the `us-east-1` Region.

#### Sample Request
<a name="API_ImportInstance_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ImportInstance
&LaunchSpecification.Architecture=x86_64
&LaunchSpecification.InstanceType=m1.xlarge
&DiskImage.1.Image.Format=VMDK
&DiskImage.1.Image.Bytes=1179593728
&DiskImage.1.Image.ImportManifestUrl=https://s3.amazonaws.com/amzn-s3-demo-bucket/​a3a5e1b6-590d-43cc-97c1-15c7325d3f41/​Win_2008_Server_Data_Center_SP2_32-bit.​vmdkmanifest.xml?AWSAccessKeyId=​AKIAIOSFODNN7EXAMPLE&​Expires=1294855591&​Signature=5snej01TlTtL0uR7KExtEXAMPLE%3D
&DiskImage.1.Volume.Size=12
&Platform=Windows
&AUTHPARAMS
```

#### Sample Response
<a name="API_ImportInstance_Example_1_Response"></a>

```
<ImportInstanceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <conversionTask>
    <conversionTaskId>import-i-ffvko9js</conversionTaskId>
    <expirationTime>2010-12-22T12:01Z</expirationTime>
    <importInstance>
       <volumes>
          <item>
             <bytesConverted>0</bytesConverted>
             <availabilityZone>us-east-1a</availabilityZone>
             <image>
                <format>VMDK</format>
                <size>1179593728</size>
                <importManifestUrl>
                 https://s3.amazonaws.com/amzn-s3-demo-bucket/​a3a5e1b6-590d-43cc-97c1-15c7325d3f41/​Win_2008_Server_Data_Center_SP2_32-bit.​vmdkmanifest.xml?AWSAccessKeyId=​AKIAIOSFODNN7EXAMPLE&​Expires=1294855591&​Signature=5snej01TlTtL0uR7KExtEXAMPLE%3D
                </importManifestUrl>
             </image>
             <description/>
             <volume>
                <size>12</size>
                <id>vol-1234567890abcdef0</id>
             </volume>
             <status>active</status>
             <statusMessage/>
          </item>
       </volumes>
       <instanceId>i-1234567890abcdef0</instanceId>
       <description/>
    </importInstance>
  </conversionTask>
</ImportInstanceResponse>
```

## See Also
<a name="API_ImportInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ImportInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportInstance)
