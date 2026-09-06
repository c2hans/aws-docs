---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobDriver.html
---

# JobDriver
<a name="API_JobDriver"></a>

The driver that the job runs on.

## Contents
<a name="API_JobDriver_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hive **   <a name="emrserverless-Type-JobDriver-hive"></a>
The job driver parameters specified for Hive.
Type: [Hive](API_Hive.md) object
Required: No

 ** sparkSubmit **   <a name="emrserverless-Type-JobDriver-sparkSubmit"></a>
The job driver parameters specified for Spark.
Type: [SparkSubmit](API_SparkSubmit.md) object
Required: No

## See Also
<a name="API_JobDriver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/JobDriver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/JobDriver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/JobDriver)
