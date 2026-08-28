---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CodeRepositoryDetails.html
---

# CodeRepositoryDetails
<a name="API_CodeRepositoryDetails"></a>

 Details about an external code repository with which you can connect your AWS resources. The connection is established through Amazon Inspector.

## Contents
<a name="API_CodeRepositoryDetails_Contents"></a>

 ** CodeSecurityIntegrationArn **   <a name="securityhub-Type-CodeRepositoryDetails-CodeSecurityIntegrationArn"></a>
 The Amazon Resource Name (ARN) of the code security integration associated with the repository.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProjectName **   <a name="securityhub-Type-CodeRepositoryDetails-ProjectName"></a>
 The name of the project in the code repository.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProviderType **   <a name="securityhub-Type-CodeRepositoryDetails-ProviderType"></a>
 The type of repository provider.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_CodeRepositoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CodeRepositoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CodeRepositoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CodeRepositoryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
