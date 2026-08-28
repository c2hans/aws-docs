---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_IdentityCenterDetails.html
---

# IdentityCenterDetails
<a name="API_IdentityCenterDetails"></a>

Contains detailed information about the IAM Identity Center configuration for an application.

## Contents
<a name="API_IdentityCenterDetails_Contents"></a>

 ** instanceArn **   <a name="accountaccess-Type-IdentityCenterDetails-instanceArn"></a>
The ARN of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[a-z0-9-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** applicationArn **   <a name="accountaccess-Type-IdentityCenterDetails-applicationArn"></a>
The ARN of the IAM Identity Center application created for this account access manager application. This property is not required or supported as input. It can be read after creation.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[a-z0-9-]+:sso::[0-9]{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

## See Also
<a name="API_IdentityCenterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/IdentityCenterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/IdentityCenterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/IdentityCenterDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
