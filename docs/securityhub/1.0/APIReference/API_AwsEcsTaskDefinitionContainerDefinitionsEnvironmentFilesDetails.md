---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails"></a>

A file that contain environment variables to pass to a container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails_Contents"></a>

 ** Type **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails-Type"></a>
The type of environment file. The valid value is `s3`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Value **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails-Value"></a>
The ARN of the S3 object that contains the environment variable file.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
