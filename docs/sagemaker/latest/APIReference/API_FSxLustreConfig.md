---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FSxLustreConfig.html
---

# FSxLustreConfig
<a name="API_FSxLustreConfig"></a>

Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.

## Contents
<a name="API_FSxLustreConfig_Contents"></a>

 ** PerUnitStorageThroughput **   <a name="sagemaker-Type-FSxLustreConfig-PerUnitStorageThroughput"></a>
The throughput capacity of the Amazon FSx for Lustre file system, measured in MB/s per TiB of storage.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 1000.
Required: Yes

 ** SizeInGiB **   <a name="sagemaker-Type-FSxLustreConfig-SizeInGiB"></a>
The storage capacity of the Amazon FSx for Lustre file system, specified in gibibytes (GiB).
Type: Integer
Valid Range: Minimum value of 1200. Maximum value of 100800.
Required: Yes

## See Also
<a name="API_FSxLustreConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FSxLustreConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FSxLustreConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FSxLustreConfig)
