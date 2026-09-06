---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_EphemeralStorageConfiguration.html
---

# EphemeralStorageConfiguration
<a name="API_EphemeralStorageConfiguration"></a>

Configuration for ephemeral storage attached to the container task.

## Contents
<a name="API_EphemeralStorageConfiguration_Contents"></a>

 ** storageClass **   <a name="iotsitewise-Type-EphemeralStorageConfiguration-storageClass"></a>
Storage type that determines I/O performance family and level.
Type: String
Valid Values: `STANDARD_1 | STANDARD_2 | THROUGHPUT_1 | THROUGHPUT_2`
Required: Yes

 ** storageSizeInGiB **   <a name="iotsitewise-Type-EphemeralStorageConfiguration-storageSizeInGiB"></a>
Storage volume size in GiB.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16384.
Required: Yes

## See Also
<a name="API_EphemeralStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/EphemeralStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/EphemeralStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/EphemeralStorageConfiguration)
