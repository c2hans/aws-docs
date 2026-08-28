---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_IdentityCenterConfiguration.html
---

# IdentityCenterConfiguration
<a name="API_IdentityCenterConfiguration"></a>

The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.

## Contents
<a name="API_IdentityCenterConfiguration_Contents"></a>

 ** identityCenterApplicationArn **   <a name="emrserverless-Type-IdentityCenterConfiguration-identityCenterApplicationArn"></a>
The ARN of the EMR Serverless created IAM Identity Center Application that provides trusted-identity propagation.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** identityCenterInstanceArn **   <a name="emrserverless-Type-IdentityCenterConfiguration-identityCenterInstanceArn"></a>
The ARN of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** userBackgroundSessionsEnabled **   <a name="emrserverless-Type-IdentityCenterConfiguration-userBackgroundSessionsEnabled"></a>
Enables user background sessions for this application so Livy sessions can continue running after users log out of their interactive notebook or their Identity Center sessions expire.
Type: Boolean
Required: No

## See Also
<a name="API_IdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/IdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/IdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/IdentityCenterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
