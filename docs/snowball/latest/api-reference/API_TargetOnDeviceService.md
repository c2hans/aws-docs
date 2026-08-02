---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_TargetOnDeviceService.html
---

# TargetOnDeviceService
<a name="API_TargetOnDeviceService"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

An object that represents the service or services on the Snowball Edge device that your transferred data will be exported from or imported into. AWS Snowball Edge supports Amazon S3 and NFS (Network File System).

## Contents
<a name="API_TargetOnDeviceService_Contents"></a>

 ** ServiceName **   <a name="Snowball-Type-TargetOnDeviceService-ServiceName"></a>
Specifies the name of the service on the Snowball Edge device that your transferred data will be exported from or imported into.
Type: String
Valid Values: `NFS_ON_DEVICE_SERVICE | S3_ON_DEVICE_SERVICE`
Required: No

 ** TransferOption **   <a name="Snowball-Type-TargetOnDeviceService-TransferOption"></a>
Specifies whether the data is being imported or exported. You can import or export the data, or use it locally on the device.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: No

## See Also
<a name="API_TargetOnDeviceService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/TargetOnDeviceService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/TargetOnDeviceService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/TargetOnDeviceService)
