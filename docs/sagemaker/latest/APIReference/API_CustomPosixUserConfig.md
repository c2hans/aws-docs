---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CustomPosixUserConfig.html
---

# CustomPosixUserConfig
<a name="API_CustomPosixUserConfig"></a>

Details about the POSIX identity that is used for file system operations.

## Contents
<a name="API_CustomPosixUserConfig_Contents"></a>

 ** Gid **   <a name="sagemaker-Type-CustomPosixUserConfig-Gid"></a>
The POSIX group ID.
Type: Long
Valid Range: Minimum value of 1001. Maximum value of 4000000.
Required: Yes

 ** Uid **   <a name="sagemaker-Type-CustomPosixUserConfig-Uid"></a>
The POSIX user ID.
Type: Long
Valid Range: Minimum value of 10000. Maximum value of 4000000.
Required: Yes

## See Also
<a name="API_CustomPosixUserConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CustomPosixUserConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CustomPosixUserConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CustomPosixUserConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
