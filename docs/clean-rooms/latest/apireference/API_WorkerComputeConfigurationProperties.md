---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_WorkerComputeConfigurationProperties.html
---

# WorkerComputeConfigurationProperties
<a name="API_WorkerComputeConfigurationProperties"></a>

The configuration properties that define the compute environment settings for workers in AWS Clean Rooms. These properties enable customization of the underlying compute environment to optimize performance for your specific workloads.

## Contents
<a name="API_WorkerComputeConfigurationProperties_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** spark **   <a name="API-Type-WorkerComputeConfigurationProperties-spark"></a>
The Spark configuration properties for SQL and PySpark workloads. This map contains key-value pairs that configure Apache Spark settings to optimize performance for your data processing jobs. You can specify up to 50 Spark properties, with each key being 1-200 characters and each value being 0-500 characters. These properties allow you to adjust compute capacity for large datasets and complex workloads.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 200.
Value Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_WorkerComputeConfigurationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/WorkerComputeConfigurationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/WorkerComputeConfigurationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/WorkerComputeConfigurationProperties)
