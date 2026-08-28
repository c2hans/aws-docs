---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails"></a>

A secret to pass to the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails_Contents"></a>

 ** Name **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails-Name"></a>
The name of the secret.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ValueFrom **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails-ValueFrom"></a>
The secret to expose to the container. The value is either the full ARN of the Secrets Manager secret or the full ARN of the parameter in the Systems Manager Parameter Store.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
