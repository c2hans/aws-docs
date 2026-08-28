---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstanceMetadataServiceConfiguration.html
---

# InstanceMetadataServiceConfiguration
<a name="API_InstanceMetadataServiceConfiguration"></a>

Information on the IMDS configuration of the notebook instance

## Contents
<a name="API_InstanceMetadataServiceConfiguration_Contents"></a>

 ** MinimumInstanceMetadataServiceVersion **   <a name="sagemaker-Type-InstanceMetadataServiceConfiguration-MinimumInstanceMetadataServiceVersion"></a>
Indicates the minimum IMDS version that the notebook instance supports. When passed as part of `CreateNotebookInstance`, if no value is selected, then it defaults to IMDSv1. This means that both IMDSv1 and IMDSv2 are supported. If passed as part of `UpdateNotebookInstance`, there is no default.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1.
Pattern: `1|2`
Required: Yes

## See Also
<a name="API_InstanceMetadataServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstanceMetadataServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstanceMetadataServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstanceMetadataServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
