---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SparkSubmit.html
---

# SparkSubmit
<a name="API_SparkSubmit"></a>

The configurations for the Spark submit job driver.

## Contents
<a name="API_SparkSubmit_Contents"></a>

 ** entryPoint **   <a name="emrserverless-Type-SparkSubmit-entryPoint"></a>
The entry point for the Spark submit job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.*\S.*`
Required: Yes

 ** entryPointArguments **   <a name="emrserverless-Type-SparkSubmit-entryPointArguments"></a>
The arguments for the Spark submit job run.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1024 items.
Length Constraints: Minimum length of 0.
Required: No

 ** sparkSubmitParameters **   <a name="emrserverless-Type-SparkSubmit-sparkSubmitParameters"></a>
The parameters for the Spark submit job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SparkSubmit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/SparkSubmit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/SparkSubmit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/SparkSubmit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
