---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_RetentionProperties.html
---

# RetentionProperties
<a name="API_RetentionProperties"></a>

Retention properties contain the duration for which your time-series data must be stored in the magnetic store and the memory store.

## Contents
<a name="API_RetentionProperties_Contents"></a>

 ** MagneticStoreRetentionPeriodInDays **   <a name="timestream-Type-RetentionProperties-MagneticStoreRetentionPeriodInDays"></a>
The duration for which data must be stored in the magnetic store.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 73000.
Required: Yes

 ** MemoryStoreRetentionPeriodInHours **   <a name="timestream-Type-RetentionProperties-MemoryStoreRetentionPeriodInHours"></a>
The duration for which data must be stored in the memory store.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 8766.
Required: Yes

## See Also
<a name="API_RetentionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/RetentionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/RetentionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/RetentionProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
