---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SparkSubmitJobDriver.html
---

# SparkSubmitJobDriver
<a name="API_SparkSubmitJobDriver"></a>

The information about job driver for Spark submit.

## Contents
<a name="API_SparkSubmitJobDriver_Contents"></a>

 ** entryPoint **   <a name="emroneks-Type-SparkSubmitJobDriver-entryPoint"></a>
The entry point of job application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** entryPointArguments **   <a name="emroneks-Type-SparkSubmitJobDriver-entryPointArguments"></a>
The arguments for job application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `.*\S.*`
Required: No

 ** sparkSubmitParameters **   <a name="emroneks-Type-SparkSubmitJobDriver-sparkSubmitParameters"></a>
The Spark submit parameters that are used for job runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SparkSubmitJobDriver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/SparkSubmitJobDriver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/SparkSubmitJobDriver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/SparkSubmitJobDriver)
