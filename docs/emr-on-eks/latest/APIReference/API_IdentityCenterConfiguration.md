---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_IdentityCenterConfiguration.html
---

# IdentityCenterConfiguration
<a name="API_IdentityCenterConfiguration"></a>

Contains the IAM Identity Center settings for a security configuration, including instance ARN, application assignment requirements, and application ARN.

## Contents
<a name="API_IdentityCenterConfiguration_Contents"></a>

 ** emrIdentityCenterApplicationARN **   <a name="emroneks-Type-IdentityCenterConfiguration-emrIdentityCenterApplicationARN"></a>
The Amazon Resource Name (ARN) of the Amazon EMR Identity Center application.
Type: String
Pattern: `^arn:(aws[a-zA-Z0-9-]*):sso:::application/ssoins-[0-9a-zA-Z/\\-_]+/apl-[0-9a-zA-Z/\\-_]+`
Required: No

 ** enableIdentityCenter **   <a name="emroneks-Type-IdentityCenterConfiguration-enableIdentityCenter"></a>
Specifies whether Identity Center is enabled for the security configuration.
Type: Boolean
Required: No

 ** identityCenterApplicationAssignmentRequired **   <a name="emroneks-Type-IdentityCenterConfiguration-identityCenterApplicationAssignmentRequired"></a>
Specifies whether user assignment is required for the Identity Center application.
Type: Boolean
Required: No

 ** identityCenterInstanceARN **   <a name="emroneks-Type-IdentityCenterConfiguration-identityCenterInstanceARN"></a>
The Amazon Resource Name (ARN) of the Identity Center instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):sso:::instance/ssoins-[0-9a-zA-Z/\\-_]+`
Required: No

## See Also
<a name="API_IdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/IdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/IdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/IdentityCenterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
