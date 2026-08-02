---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_AccountSettings.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# AccountSettings
<a name="API_AccountSettings"></a>

 AWS Proton settings that are used for multiple services in the AWS account.

## Contents
<a name="API_AccountSettings_Contents"></a>

 ** pipelineCodebuildRoleArn **   <a name="proton-Type-AccountSettings-pipelineCodebuildRoleArn"></a>
The Amazon Resource Name (ARN) of the service role that AWS Proton uses for provisioning pipelines. AWS Proton assumes this role for CodeBuild-based provisioning.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*(^$)|(^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$).*`
Required: No

 ** pipelineProvisioningRepository **   <a name="proton-Type-AccountSettings-pipelineProvisioningRepository"></a>
The linked repository for pipeline provisioning. Required if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](API_CreateRepository.md).
Type: [RepositoryBranch](API_RepositoryBranch.md) object
Required: No

 ** pipelineServiceRoleArn **   <a name="proton-Type-AccountSettings-pipelineServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by AWS Proton for AWS-managed provisioning, and by customer-owned automation for self-managed provisioning.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*(^$)|(^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$).*`
Required: No

## See Also
<a name="API_AccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/AccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/AccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/AccountSettings)
