---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ImageConfigurationInput.html
---

# ImageConfigurationInput
<a name="API_ImageConfigurationInput"></a>

The image configuration.

## Contents
<a name="API_ImageConfigurationInput_Contents"></a>

 ** applicationLevelDigestResolution **   <a name="emrserverless-Type-ImageConfigurationInput-applicationLevelDigestResolution"></a>
Boolean value indicating if the digest resolution is application level or workload level. If true, a custom image URI is resolved at application start time and all workloads submitted will use that image digest. If false, the custom image URI is resolved at the workload submission time.
Type: Boolean
Required: No

 ** imageUri **   <a name="emrserverless-Type-ImageConfigurationInput-imageUri"></a>
The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+).([a-z0-9._-]+)\/((?:[a-z0-9]+(?:[-._][a-z0-9]+)*/)*[a-z0-9]+(?:[-._][a-z0-9]+)*)(?::([a-zA-Z0-9_]+[a-zA-Z0-9-._]*)|@(sha256:[0-9a-f]{64}))`
Required: No

## See Also
<a name="API_ImageConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ImageConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ImageConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ImageConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
