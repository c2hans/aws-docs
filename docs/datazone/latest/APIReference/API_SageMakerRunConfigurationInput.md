---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SageMakerRunConfigurationInput.html
---

# SageMakerRunConfigurationInput
<a name="API_SageMakerRunConfigurationInput"></a>

The Amazon SageMaker run configuration.

## Contents
<a name="API_SageMakerRunConfigurationInput_Contents"></a>

 ** trackingAssets **   <a name="datazone-Type-SageMakerRunConfigurationInput-trackingAssets"></a>
The tracking assets of the Amazon SageMaker run.
Type: String to array of strings map
Map Entries: Maximum number of 1 item.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Pattern: `arn:aws[^:]*:sagemaker:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:[\w+=,.@-]{1,128}/[\w+=,.@-]{1,256}`
Required: Yes

## See Also
<a name="API_SageMakerRunConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SageMakerRunConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SageMakerRunConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SageMakerRunConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
