---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateS3LogConfigurationInput.html
---

# ExperimentTemplateS3LogConfigurationInput
<a name="API_ExperimentTemplateS3LogConfigurationInput"></a>

Specifies the configuration for experiment logging to Amazon S3.

## Contents
<a name="API_ExperimentTemplateS3LogConfigurationInput_Contents"></a>

 ** bucketName **   <a name="fis-Type-ExperimentTemplateS3LogConfigurationInput-bucketName"></a>
The name of the destination bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[\S]+`
Required: Yes

 ** prefix **   <a name="fis-Type-ExperimentTemplateS3LogConfigurationInput-prefix"></a>
The bucket prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 700.
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_ExperimentTemplateS3LogConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateS3LogConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateS3LogConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateS3LogConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
