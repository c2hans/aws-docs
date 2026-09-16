---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFpgaImage.html
---

# CreateFpgaImage
<a name="API_CreateFpgaImage"></a>

Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).

The create operation is asynchronous. To verify that the AFI was successfully created and is ready for use, check the output logs.

An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on multiple FPGA-accelerated instances. For more information, see the [AWS FPGA Hardware Development Kit](https://github.com/aws/aws-fpga/).

## Request Parameters
<a name="API_CreateFpgaImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the AFI.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InputStorageLocation**
The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.
Type: [StorageLocation](API_StorageLocation.md) object
Required: Yes

 **LogsStorageLocation**
The location in Amazon S3 for the output logs.
Type: [StorageLocation](API_StorageLocation.md) object
Required: No

 **Name**
A name for the AFI.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the FPGA image during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateFpgaImage_ResponseElements"></a>

The following elements are returned by the service.

 **fpgaImageGlobalId**
The global FPGA image identifier (AGFI ID).
Type: String

 **fpgaImageId**
The FPGA image identifier (AFI ID).
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateFpgaImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateFpgaImage_Examples"></a>

### Example
<a name="API_CreateFpgaImage_Example_1"></a>

This example creates an AFI from the specified tarball in the specified bucket.

#### Sample Request
<a name="API_CreateFpgaImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateFpgaImage
&Name=my-afi
&Description=test-afi
&InputStorageLocation.Bucket=my-fpga-bucket
&InputStorageLocation.Key=dcp/17_12_22-103226.Developer_CL.tar
&LogsStorageLocation.Bucket=my-fpga-bucket
&LogsStorageLocation.Key=logs
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateFpgaImage_Example_1_Response"></a>

```
<CreateFpgaImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d97baa5e-d3dd-4ead-9586-c68example</requestId>
    <fpgaImageId>afi-0d123e123bfc85abc</fpgaImageId>
    <fpgaImageGlobalId>agfi-123cb27b5e84a0abc</fpgaImageGlobalId>
</CreateFpgaImageResponse>
```

## See Also
<a name="API_CreateFpgaImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateFpgaImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateFpgaImage)
