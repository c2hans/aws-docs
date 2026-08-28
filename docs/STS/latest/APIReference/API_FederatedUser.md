---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_FederatedUser.html
---

# FederatedUser
<a name="API_FederatedUser"></a>

Identifiers for the federated user that is associated with the credentials.

## Contents
<a name="API_FederatedUser_Contents"></a>

 ** Arn **
The ARN that specifies the federated user that is associated with the credentials. For more information about ARNs and how to use them in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`
Required: Yes

 ** FederatedUserId **
The string that identifies the federated user associated with the credentials, similar to the unique ID of an IAM user.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 193.
Pattern: `[\w+=,.@\:-]*`
Required: Yes

## See Also
<a name="API_FederatedUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/FederatedUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/FederatedUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/FederatedUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Token Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query STS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
