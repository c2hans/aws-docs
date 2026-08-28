---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_OpenZFSReadCacheConfiguration.html
---

# OpenZFSReadCacheConfiguration
<a name="API_OpenZFSReadCacheConfiguration"></a>

 The configuration for the optional provisioned SSD read cache on Amazon FSx for OpenZFS file systems that use the Intelligent-Tiering storage class.

## Contents
<a name="API_OpenZFSReadCacheConfiguration_Contents"></a>

 ** SizeGiB **   <a name="FSx-Type-OpenZFSReadCacheConfiguration-SizeGiB"></a>
 Required if `SizingMode` is set to `USER_PROVISIONED`. Specifies the size of the file system's SSD read cache, in gibibytes (GiB).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** SizingMode **   <a name="FSx-Type-OpenZFSReadCacheConfiguration-SizingMode"></a>
 Specifies how the provisioned SSD read cache is sized, as follows:
+ Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
+ Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
+ Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.
Type: String
Valid Values: `NO_CACHE | USER_PROVISIONED | PROPORTIONAL_TO_THROUGHPUT_CAPACITY`
Required: No

## See Also
<a name="API_OpenZFSReadCacheConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSReadCacheConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSReadCacheConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSReadCacheConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
