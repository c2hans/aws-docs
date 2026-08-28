---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_OutputDataConfig.html
---

# OutputDataConfig
<a name="API_OutputDataConfig"></a>

The output properties for a detection job.

## Contents
<a name="API_OutputDataConfig_Contents"></a>

 ** S3Bucket **   <a name="comprehendmedical-Type-OutputDataConfig-S3Bucket"></a>
When you use the `OutputDataConfig` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[0-9a-z\.\-_]*(?!\.)$`
Required: Yes

 ** S3Key **   <a name="comprehendmedical-Type-OutputDataConfig-S3Key"></a>
The path to the output data files in the S3 bucket. Comprehend Medical; creates an output directory using the job ID so that the output from one job does not overwrite the output of another.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_OutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/OutputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/OutputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/OutputDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
