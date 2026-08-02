---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeConversionTasks.html
---

# DescribeConversionTasks
<a name="API_DescribeConversionTasks"></a>

Describes the specified conversion tasks or all your conversion tasks. For more information, see the [VM Import/Export User Guide](https://docs.aws.amazon.com/vm-import/latest/userguide/).

For information about the import manifest referenced by this API action, see [VM Import Manifest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).

## Request Parameters
<a name="API_DescribeConversionTasks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ConversionTaskId.N**
The conversion task IDs.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeConversionTasks_ResponseElements"></a>

The following elements are returned by the service.

 **conversionTasks**
Information about the conversion tasks.
Type: Array of [ConversionTask](API_ConversionTask.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeConversionTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeConversionTasks_Examples"></a>

### Example
<a name="API_DescribeConversionTasks_Example_1"></a>

This example describes all your conversion tasks.

#### Sample Request
<a name="API_DescribeConversionTasks_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeConversionTasks
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeConversionTasks_Example_1_Response"></a>

```
<DescribeConversionTasksResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <conversionTasks>
     <item>
        <conversionTask>
           <conversionTaskId>import-i-fh95npoc</conversionTaskId>
           <expirationTime>2010-12-22T12:01Z</expirationTime>
           <importVolume>
              <bytesConverted>1000</bytesConverted>
              <availabilityZone>us-east-1a</availabilityZone>
              <description/>
              <image>
                 <format>VDMK</format>
                 <size>128696320</size>
                 <importManifestUrl>
                  https://s3.amazonaws.com/amzn-s3-demo-bucket/​a3a5e1b6-590d-43cc-97c1-15c7325d3f41/​Win_2008_Server_Data_Center_SP2_32-bit.​vmdkmanifest.xml?AWSAccessKeyId=​AKIAIOSFODNN7EXAMPLE&​Expires=1294855591&​Signature=5snej01TlTtL0uR7KExtEXAMPLE%3D
                 </importManifestUrl>
             </image>
             <volume>
                <size>8</size>
                <id>vol-1234567890abcdef0</id>
             </volume>
           </importVolume>
           <state>active</state>
           <statusMessage/>
        </conversionTask>
     </item>
  </conversionTasks>
</DescribeConversionTasksResponse>
```

## See Also
<a name="API_DescribeConversionTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeConversionTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeConversionTasks)
