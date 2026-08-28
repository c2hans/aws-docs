---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DatasetSource.html
---

# DatasetSource
<a name="API_DatasetSource"></a>

 Specifies a dataset source for a channel.

## Contents
<a name="API_DatasetSource_Contents"></a>

 ** DatasetArn **   <a name="sagemaker-Type-DatasetSource-DatasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub-content\/)[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/DataSet\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}(\/\d{1,4}.\d{1,4}.\d{1,4})?`
Required: Yes

## See Also
<a name="API_DatasetSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DatasetSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DatasetSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DatasetSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
